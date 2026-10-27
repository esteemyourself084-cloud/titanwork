// End-to-end checks for Arabingo. usage: node e2e.js <index.html>
const { chromium } = require('playwright');
const fs = require('fs');
const html = process.argv[2];
const src = fs.readFileSync(html, 'utf8');
const SEED = JSON.parse(src.match(/^var SEED=(.*);$/m)[1]);
const QA = {}, EN = {}, PL = {};
SEED.forEach(u => {
  u.qs.forEach(q => { QA[q.q] = q.a; });
  if (u.conv) u.conv.qs.forEach(q => { QA[q.q] = q.a; });
  u.rules.forEach(r => r.ex.forEach(e => { (EN[e.en] = EN[e.en] || []).push(e.ar); }));
  u.words.forEach(w => { (EN[w.en] = EN[w.en] || []).push(w.ar); if (w.pl) PL[w.ar] = w.pl; });
});
function answerFor(q, opts) {
  if (QA[q] && opts.includes(QA[q])) return QA[q];
  let m = q.match(/^(?:Which word means|How do you say) “(.*)”\?$/);
  if (m && EN[m[1]]) { const hit = opts.find(o => EN[m[1]].includes(o)); if (hit) return hit; }
  m = q.match(/^What is the plural of (.*)\?$/);
  if (m && PL[m[1]] && opts.includes(PL[m[1]])) return PL[m[1]];
  return null;
}
const results = [];
function check(name, ok, info) { results.push((ok ? 'PASS ' : 'FAIL ') + name + (info ? ' — ' + info : '')); }
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1100, height: 900 } });
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
  await p.goto('file://' + html);
  await p.waitForTimeout(300);
  const prog = () => p.evaluate(() => JSON.parse(localStorage.getItem('arabingo.progress.v3') || 'null'));

  // 1. complete a unit with a conversation, answering everything correctly
  async function doUnit(id, wrongAt) {
    await p.evaluate(h => { location.hash = h; }, '#unit-' + id);
    await p.waitForTimeout(250);
    for (let i = 0; i < 8; i++) {
      const quiz = await p.$('.qbody, .cvwrap');
      if (quiz) break;
      const qc = await p.$('.qcb:not([disabled])');
      if (qc) { await qc.click(); await p.waitForTimeout(80); }
      await p.click('[data-act=next]'); await p.waitForTimeout(150);
    }
    let n = 0, unknown = 0;
    for (let guard = 0; guard < 40; guard++) {
      if (await p.$('.result')) break;
      if (await p.$('.cvwrap')) {
        const qs = await p.$$eval('.cvq', cs => cs.map(c => ({ q: c.querySelector('h3').textContent, o: [...c.querySelectorAll('.opt .t')].map(t => t.textContent) })));
        for (let i = 0; i < qs.length; i++) {
          const a = answerFor(qs[i].q, qs[i].o); if (!a) unknown++;
          const k = a ? qs[i].o.indexOf(a) : 0;
          await p.click(`[data-act=cvpick][data-q="${i}"][data-i="${k}"]`);
          await p.waitForTimeout(60);
        }
        await p.click('[data-act=cvsubmit]'); await p.waitForTimeout(400);
        await p.click('[data-act=cvcont]'); await p.waitForTimeout(300);
        continue;
      }
      const q = await p.$eval('.qbody .q', e => e.textContent).catch(() => null);
      if (!q) { await p.waitForTimeout(200); continue; }
      const opts = await p.$$eval('.qbody .opt .t', ts => ts.map(t => t.textContent));
      let a = answerFor(q, opts); if (!a) unknown++;
      let k = a ? opts.indexOf(a) : 0;
      if (wrongAt === n) k = (k + 1) % opts.length;
      await p.click(`[data-act=pick][data-i="${k}"]`); await p.waitForTimeout(60);
      await p.click('[data-act=qcheck]'); await p.waitForTimeout(120);
      await p.click('[data-act=cont]'); await p.waitForTimeout(150);
      n++;
    }
    const txt = await p.$eval('.result', e => e.textContent).catch(() => '');
    return { n, unknown, txt };
  }
  let r = await doUnit('1-1-1');
  check('unit 1-1-1 passes with right answers', /Unit complete/.test(r.txt) && /100%/.test(r.txt), `questions=${r.n} unknown=${r.unknown}`);
  let pr = await prog();
  check('progress saved for 1-1-1', pr && pr.done['1-1-1'] && pr.done['1-1-1'].score === 100);
  check('next-unit button offered', !!(await p.$('.result a[href="#unit-1-1-2"]')));

  r = await doUnit('1-2-7', 2);
  pr = await prog();
  check('unit with conversation passes with one mistake', /Unit complete/.test(r.txt) && /90%/.test(r.txt), `questions=${r.n} unknown=${r.unknown} result=${r.txt.slice(0, 60)}`);
  check('wrong answer saved to mistakes', pr.miss.length === 1, 'miss=' + pr.miss.length);

  // 2. mistakes practice clears the mistake when answered correctly
  await p.evaluate(() => { location.hash = '#quiz'; }); await p.waitForTimeout(250);
  await p.click('[data-act=mxstart]'); await p.waitForTimeout(300);
  const mq = await p.$eval('.qbody .q', e => e.textContent);
  const mo = await p.$$eval('.qbody .opt .t', ts => ts.map(t => t.textContent));
  const ma = answerFor(mq, mo);
  await p.click(`[data-act=pick][data-i="${mo.indexOf(ma)}"]`); await p.click('[data-act=qcheck]'); await p.waitForTimeout(150);
  pr = await prog();
  check('mistake practice clears a fixed mistake', pr.miss.length === 0, 'miss=' + pr.miss.length);

  // 3. level test runs 30 questions
  await p.evaluate(() => { location.hash = '#quiz'; }); await p.waitForTimeout(250);
  await p.click('.lmk[data-l="1"]',{force:true}); await p.waitForTimeout(200);
  await p.click('[data-act=leveltest]'); await p.waitForTimeout(300);
  const lt = await p.$eval('.qkind', e => e.textContent);
  check('level test has 30 questions', /of 30/.test(lt), lt);

  // 4. reading: answer all questions, earn XP once
  await p.evaluate(() => { location.hash = '#read-1-2-7'; }); await p.waitForTimeout(300);
  const xp0 = (await prog()).xp;
  const rq = await p.$$eval('.cvq', cs => cs.map(c => ({ q: c.querySelector('h3').textContent, o: [...c.querySelectorAll('.opt .t')].map(t => t.textContent) })));
  for (let i = 0; i < rq.length; i++) {
    const a = answerFor(rq[i].q, rq[i].o);
    await p.click(`[data-act=rpick][data-q="${i}"][data-i="${a ? rq[i].o.indexOf(a) : 0}"]`); await p.waitForTimeout(40);
  }
  await p.click('[data-act=rcheck]'); await p.waitForTimeout(300);
  pr = await prog();
  check('reading passage scored and saved', pr.read['1-2-7'] && pr.read['1-2-7'].score === rq.length, JSON.stringify(pr.read['1-2-7']));
  check('reading gives XP', pr.xp - xp0 === rq.length * 5, `+${pr.xp - xp0}`);
  const tapped = await p.evaluate(() => { const w = document.querySelector('.rconvo .w'); w.click(); return !!document.querySelector('.wsheet'); });
  check('tapping a word opens the meaning sheet', tapped);

  // 5. arena: win against the scorpion with the right answers
  await p.evaluate(() => { location.hash = '#arena'; }); await p.waitForTimeout(250);
  await p.click('[data-act=arenastart][data-t="0"]'); await p.waitForTimeout(300);
  for (let i = 0; i < 30; i++) {
    if (await p.$('.aend')) break;
    const q = await p.$eval('.aq .qq', e => e.textContent).catch(() => null);
    if (!q) { await p.waitForTimeout(300); continue; }
    const o = await p.$$eval('.aq .opt .t', ts => ts.map(t => t.textContent));
    const a = answerFor(q, o);
    await p.click(`[data-act=arenapick][data-i="${a ? o.indexOf(a) : 0}"]`);
    await p.waitForTimeout(1550);
  }
  const won = await p.$eval('.aend', e => e.textContent).catch(() => '');
  pr = await prog();
  check('arena fight can be won', /Victory/.test(won), won.slice(0, 50));
  check('beating an enemy is remembered', pr.shop && pr.shop.beat && pr.shop.beat[0] === 1);

  // 6a. progress saved while Levels 10-17 were shown as Stage 2 moves to Stage 1
  await p.evaluate(() => { localStorage.setItem('arabingo.progress.v3', JSON.stringify({ v: 3, xp: 5, streak: 0, last: '', done: { '2-3-4': { score: 90, stars: 2 }, 'lt-2-1': { score: 80 }, 'st-2': { score: 1 } }, miss: [], read: { '2-1-2': { score: 3, total: 4 } } })); location.reload(); });
  await p.waitForTimeout(1200);
  pr = await prog();
  check('stage 2 progress moved to stage 1', pr && pr.v === 4 && pr.done['1-12-4'] && pr.done['lt-1-10'] && !pr.done['st-2'] && pr.read['1-10-2'], pr ? Object.keys(pr.done).join(',') : 'none');

  // 6. old progress (before the split) moves onto the new units
  await p.evaluate(() => { localStorage.removeItem('arabingo.progress.v3'); localStorage.setItem('arabingo.progress.v2', JSON.stringify({ xp: 77, streak: 1, last: '', done: { '1-1-4': { score: 92, stars: 2 }, '1-3-10': { score: 88, stars: 1 }, 'lt-1-2': { score: 90, stars: 2 } } })); location.reload(); });
  await p.waitForTimeout(600);
  await p.evaluate(() => { location.hash = '#home'; }); await p.waitForTimeout(200);
  await p.evaluate(() => { location.hash = '#words'; }); await p.waitForTimeout(200);
  pr = await prog();
  const want = ['1-2-5', '1-2-6', '1-2-7', '1-8-11', '1-9-11', 'lt-1-5', 'lt-1-6', 'lt-1-7'];
  check('old progress migrated', pr && pr.v === 4 && want.every(k => pr.done[k]) && !pr.done['1-1-4'] && pr.xp === 77, pr ? Object.keys(pr.done).join(',') : 'none');

  // 7. every unit page and the main pages render without errors
  const ids = SEED.map(u => u.id);
  for (const id of ids) { await p.evaluate(h => { location.hash = h; }, '#unit-' + id); await p.waitForTimeout(15); }
  for (const h of ['#home', '#reading', '#words', '#quiz', '#shop', '#arena']) { await p.evaluate(x => { location.hash = x; }, h); await p.waitForTimeout(120); }
  check('all ' + ids.length + ' unit pages and main pages render', errs.length === 0, errs.slice(0, 3).join(' | '));
  console.log(results.join('\n'));
  await b.close();
})();
