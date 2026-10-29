# Learn page: example cards in a grid (question-and-reply pairs as a two-bubble dialogue), the explanation in
# its own panel, and drag-to-box matching questions mixed into every test. Applied after build_fight.py.
import sys
f=sys.argv[1];s=open(f,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a));s=s.replace(a,b)

CSS=r'''
/* lesson topic page: the explanation panel and the example cards */
.lexp{position:relative;margin:6px 0 4px;padding:14px 16px 6px 50px;border-radius:16px;background:var(--soft);border:1px solid var(--line)}
.lexp::before{content:"💡";position:absolute;left:14px;top:12px;font-size:22px}
.lexp p:last-child,.lexp ul:last-child{margin-bottom:.4em}
.xg{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));grid-auto-flow:row dense;align-items:start;gap:12px;margin-top:18px}
.xc{position:relative;display:flex;flex-direction:column;gap:2px;min-width:0;padding:14px 16px 12px;border-radius:16px;background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--brand);box-shadow:0 4px 14px rgba(15,30,58,.06)}
.xc .xs{position:absolute;top:10px;inset-inline-start:10px;display:flex;gap:4px}
.xc .xa{font:400 32px/1.6 var(--f-ar);color:var(--ink);text-align:right;direction:rtl;margin:0 0 0 44px}
.xpair .xc .xa{margin-top:18px}
.xc .xt{font-style:italic;color:var(--ink2);font-size:14px}
.xc .xe{font-weight:700;font-size:15px;color:var(--ink)}
.xc .xn{margin:8px -16px -12px;padding:8px 16px 10px;border-top:1px dashed var(--line);background:var(--surface2);border-radius:0 0 16px 16px;font-size:13px;color:var(--ink2)}
.xc .xn .ar{font-size:18px;color:var(--brand)}
.xpair{grid-column:span 2;display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px;border-radius:18px;background:linear-gradient(135deg,var(--soft),transparent);border:1px solid var(--line)}
.xpair .xc{border-top:0;border-inline-start:4px solid var(--brand)}
.xpair .xc.rep{border-inline-start-color:var(--gold);margin-top:22px}
.xc .xw{position:absolute;top:14px;inset-inline-end:14px;padding:2px 8px;border-radius:99px;background:var(--soft);font:800 10px var(--f-body);letter-spacing:.1em;text-transform:uppercase;color:var(--brand)}
.xc.rep .xw{color:var(--gold-ink,#7A5A00)}
@media (max-width:640px){.xg{grid-template-columns:1fr}.xpair{grid-template-columns:1fr;grid-column:auto}.xpair .xc.rep{margin-top:0;margin-inline-start:28px}.xc .xa{font-size:28px}}
/* drag-to-box matching questions */
.mq{display:flex;flex-direction:column;gap:14px}
.mtray{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;min-height:64px;padding:12px;border-radius:16px;border:2px dashed var(--line);background:var(--surface2)}
.mtray:empty::after{content:"All placed. Press Check.";color:var(--ink2);font-weight:600;align-self:center}
.mchip{display:inline-flex;align-items:center;justify-content:center;min-width:90px;padding:8px 16px;border-radius:12px;border:2px solid var(--brand);border-bottom-width:4px;background:var(--surface);color:var(--ink);font:700 16px var(--f-body);cursor:grab;touch-action:none;user-select:none;-webkit-user-select:none;transition:transform .1s,box-shadow .1s}
.mchip.ar{font:400 26px/1.4 var(--f-ar)}
.mchip:hover{transform:translateY(-2px)}
.mchip.held{background:var(--soft);box-shadow:0 0 0 3px var(--gold);transform:translateY(-3px)}
.mchip.ghost{position:fixed;z-index:200;pointer-events:none;cursor:grabbing;box-shadow:0 14px 28px rgba(0,0,0,.25);transform:rotate(-3deg) scale(1.06)}
.mchip.away{opacity:.3}
.mboxes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.mbox{display:flex;flex-direction:column;gap:8px;padding:10px 12px 12px;border-radius:16px;border:2px solid var(--line);background:var(--surface);min-width:0;cursor:pointer}
.mbox .ml{font-weight:700;color:var(--ink2);font-size:15px}
.mbox .ml.ar{font:400 26px/1.4 var(--f-ar);color:var(--ink);text-align:right}
.mbox .md{display:flex;align-items:center;justify-content:center;min-height:56px;border-radius:12px;border:2px dashed var(--line);background:var(--surface2);color:var(--ink2);font-size:13px}
.mbox.over .md,.mbox.want .md{border-color:var(--gold);background:var(--soft)}
.mbox .md .mchip{margin:2px}
.mbox.right{border-color:var(--good);background:var(--good-bg)}
.mbox.wrong{border-color:var(--bad);background:var(--bad-bg)}
.mbox .mfix{font-size:13px;color:var(--good);font-weight:700}
.mbox .mfix .ar{font-size:20px}
.mhint{text-align:center;color:var(--ink2);font-size:13px;margin:0}
@media (max-width:520px){.mq{gap:10px}.mtray{gap:6px;padding:8px;min-height:52px}.mboxes{gap:8px}.mbox{padding:8px;gap:6px}.mbox .ml{font-size:13px}.mbox .ml.ar{font-size:21px}.mbox .md{min-height:46px}.mchip{min-width:0;padding:4px 10px;font-size:14px}.mchip.ar{font-size:21px}.mhint{display:none}}
'''
rep('@media (max-width:520px){.nav{gap:2px}',CSS+'@media (max-width:520px){.nav{gap:2px}')

# 1. example cards: a reply joins the example before it as a dialogue
old=s[s.index('function exHtml(list){'):s.index('\n}\n',s.index('function exHtml(list){'))+3]
new='''function exHtml(list){
  if(!list.length)return '';
  function card(e,who){
    return '<div class="xc'+(who==='b'?' rep':'')+'"><span class="xs">'+(CAN_SAY?sayBtns(e.ar):'')+'</span>'+(who?'<span class="xw">'+(who==='a'?'Ask':'Reply')+'</span>':'')+
      '<p class="xa">'+esc(e.ar)+'</p>'+(e.tr?'<span class="xt">'+esc(e.tr)+'</span>':'')+'<span class="xe">'+esc(e.en)+'</span>'+(e.note?'<p class="xn">'+arWrap(esc(e.note))+'</p>':'')+'</div>';
  }
  var h='';
  for(var i=0;i<list.length;i++){
    var e=list[i],nx=list[i+1];
    if(nx&&nx.re&&!e.re){h+='<div class="xpair">'+card(e,'a')+card(nx,'b')+'</div>';i++}
    else h+=card(e,e.re?'b':'');
  }
  return '<div class="xg">'+h+'</div>';
}
'''
s=s.replace(old,new)
# 2. the explanation sits in its own panel
rep("""'</h2><div class="prose">'+fmtBody(r.body)+'</div>'+exHtml(r.ex)""","""'</h2><div class="prose lexp">'+fmtBody(r.body)+'</div>'+exHtml(r.ex)""")

# 3. matching questions: two in a ten-question test, built from the unit's own words and examples
rep("""  items.forEach(function(q){q.t=timeFor(q)});
  S.seenQ[u.id]=reuse?used:seen.concat(used);""","""  addMatches(u,items);
  items.forEach(function(q){q.t=q.type==='match'?45:timeFor(q)});
  S.seenQ[u.id]=reuse?used:seen.concat(used);""")
rep("""
/* ---------- views: shell ---------- */""","""
/* Drag-to-box questions: four words and four meanings. A test of four or more questions gets one, and a test of
   eight or more gets two (one asking for the Arabic, one for the meaning), so a test is not one kind of question. */
function addMatches(u,items){
  if(items.length<4)return;
  var seen={},seenE={},pairs=[];
  function add(ar,en){ar=String(ar||'').trim();en=String(en||'').trim();if(!ar||!en||ar.length>24||en.length>30||seen[ar]||seenE[en.toLowerCase()])return;seen[ar]=1;seenE[en.toLowerCase()]=1;pairs.push({ar:ar,en:en})}
  u.words.forEach(function(w){add(w.ar,w.en)});
  u.rules.forEach(function(r){r.ex.forEach(function(e){add(e.ar,e.en)})});
  pairs=shuffle(pairs);
  var n=Math.min(items.length>=8?2:1,Math.floor(pairs.length/4));
  for(var k=0;k<n;k++){
    var ps=pairs.slice(k*4,k*4+4),dir=k%2;
    var mq={type:'match',dir:dir,q:dir?'Drag each meaning into the box with its Arabic':'Drag each Arabic word into the box with its meaning',big:'',pairs:ps,
      chips:shuffle([0,1,2,3]),place:[-1,-1,-1,-1],held:-1,o:['✓','✗'],a:'✓'};
    var at=Math.min(items.length-1,1+k*4+Math.floor(Math.random()*3));
    items.splice(at,1,mq);
  }
}
function matchOk(q){return q.place.every(function(c,i){return c===i})}
function matchHtml(q,p){
  var done=p!=null,chipAr=!q.dir;
  function chip(c,inBox){var t=chipAr?q.pairs[c].ar:q.pairs[c].en;return '<span class="mchip'+(chipAr?' ar':'')+(q.held===c?' held':'')+'" data-mc="'+c+'"'+(done?'':' role="button" tabindex="0" aria-label="'+esc(t)+(inBox?' (placed)':'')+'"')+'>'+esc(t)+'</span>'}
  var placed={};q.place.forEach(function(c){if(c>=0)placed[c]=1});
  var h='<div class="mq">';
  if(!done)h+='<div class="mtray" id="mTray">'+q.chips.filter(function(c){return !placed[c]}).map(function(c){return chip(c)}).join('')+'</div>';
  h+='<div class="mboxes">'+q.pairs.map(function(pr,i){
    var c=q.place[i],cls='mbox'+(done?(c===i?' right':' wrong'):'')+(!done&&q.held>=0&&c<0?' want':'');
    return '<div class="'+cls+'" data-mb="'+i+'"><span class="ml'+(q.dir?' ar':'')+'">'+esc(q.dir?pr.ar:pr.en)+'</span><div class="md">'+(c>=0?chip(c,true):'Drop here')+'</div>'+
      (done&&c!==i?'<span class="mfix">✓ '+(chipAr?'<span class="ar">'+esc(pr.ar)+'</span>':esc(pr.en))+'</span>':'')+'</div>'}).join('')+'</div>';
  if(!done)h+='<p class="mhint">Drag a card into a box, or tap a card and then a box. Tap a placed card to take it back.</p>';
  return h+'</div>';
}
function matchPut(q,c,b){
  if(c<0)return;
  var from=q.place.indexOf(c);if(from>=0)q.place[from]=-1;
  if(b>=0){var prev=q.place[b];if(prev>=0&&from>=0)q.place[from]=prev;q.place[b]=c}
  q.held=-1;
}
function matchRefresh(){
  var L=S.lesson,q=L&&L.quiz&&L.quiz[L.qi];if(!q||q.type!=='match')return;
  L.sel=q.place.every(function(c){return c>=0})?0:null;
  var y=window.scrollY;renderLesson(getUnit(L.id));try{window.scrollTo(0,y)}catch(e){}
}
function matchQ(){var L=S.lesson,q=L&&L.quiz&&L.quiz[L.qi];return q&&q.type==='match'&&L.picked==null&&!L.fin?q:null}
/* tap a card, then a box; or drag a card (mouse or touch) and drop it on a box or back on the tray */
(function(){
  var drag=null,moved=false;
  document.addEventListener('pointerdown',function(ev){
    var q=matchQ();if(!q)return;var ch=ev.target.closest&&ev.target.closest('.mchip[data-mc]');if(!ch||ch.classList.contains('ghost'))return;
    ev.preventDefault();drag={c:+ch.dataset.mc,el:ch,x:ev.clientX,y:ev.clientY,g:null};moved=false;
  });
  document.addEventListener('pointermove',function(ev){
    if(!drag)return;var dx=ev.clientX-drag.x,dy=ev.clientY-drag.y;
    if(!drag.g&&Math.abs(dx)+Math.abs(dy)<7)return;
    if(!drag.g){var r=drag.el.getBoundingClientRect();drag.g=drag.el.cloneNode(true);drag.g.classList.add('ghost');drag.g.style.width=r.width+'px';drag.ox=drag.x-r.left;drag.oy=drag.y-r.top;document.body.appendChild(drag.g);drag.el.classList.add('away');moved=true}
    drag.g.style.left=(ev.clientX-drag.ox)+'px';drag.g.style.top=(ev.clientY-drag.oy)+'px';
    [].forEach.call(document.querySelectorAll('.mbox.over'),function(b){b.classList.remove('over')});
    var t=document.elementFromPoint(ev.clientX,ev.clientY),bx=t&&t.closest&&t.closest('.mbox');if(bx)bx.classList.add('over');
  });
  function end(ev){
    if(!drag)return;var d=drag;drag=null;var q=matchQ();
    if(d.g){d.g.remove();if(!q)return;var t=document.elementFromPoint(ev.clientX,ev.clientY),bx=t&&t.closest&&t.closest('.mbox'),tray=t&&t.closest&&t.closest('#mTray');
      if(bx)matchPut(q,d.c,+bx.dataset.mb);else if(tray)matchPut(q,d.c,-1);matchRefresh();return}
    if(!q)return;
    /* a tap: on a placed card it goes back to the tray; on a tray card it is picked up */
    var inBox=d.el.closest('.mbox');
    if(inBox&&q.held<0){matchPut(q,d.c,-1)}else q.held=q.held===d.c?-1:d.c;
    matchRefresh();
  }
  document.addEventListener('pointerup',end);
  document.addEventListener('pointercancel',function(){if(drag&&drag.g)drag.g.remove();drag=null;matchRefresh()});
  document.addEventListener('click',function(ev){
    var q=matchQ();if(!q||moved)return;var bx=ev.target.closest&&ev.target.closest('.mbox');if(!bx||ev.target.closest('.mchip'))return;
    if(q.held>=0){matchPut(q,q.held,+bx.dataset.mb);matchRefresh()}
  });
  document.addEventListener('keydown',function(ev){
    var q=matchQ();if(!q||(ev.key!=='Enter'&&ev.key!==' '))return;var ch=ev.target.closest&&ev.target.closest('.mchip[data-mc]');if(!ch)return;
    ev.preventDefault();ev.stopPropagation();var c=+ch.dataset.mc;
    if(ch.closest('.mbox'))matchPut(q,c,-1);else{var free=q.place.indexOf(-1);matchPut(q,c,free)}matchRefresh();
  },true);
})();

/* ---------- views: shell ---------- */""")
# 4. the test screen shows the boxes instead of the option buttons
rep("""  h+='<h2 class="q">'+esc(q.q)+'</h2><div class="opts">'+q.o.map(function(o,i){""","""  if(q.type==='match')h+='<h2 class="q">'+esc(q.q)+'</h2>'+matchHtml(q,p)+'</div>';
  else h+='<h2 class="q">'+esc(q.q)+'</h2><div class="opts">'+q.o.map(function(o,i){""")
rep("""(ok?'':'<span>Correct answer:</span><em class="'+(isArOnly(q.a)?'ar':'')+'">'+esc(q.a)+'</em>')""","""(ok?'':q.type==='match'?'<span>The right answers are shown in green.</span>':'<span>Correct answer:</span><em class="'+(isArOnly(q.a)?'ar':'')+'">'+esc(q.a)+'</em>')""")
rep("""var q=L.quiz[L.qi];L.picked=L.sel;""","""var q=L.quiz[L.qi];if(q.type==='match')L.sel=matchOk(q)?0:1;L.picked=L.sel;""")
rep("""if(L.picked==null&&/^[1-9]$/.test(ev.key)&&+ev.key<=q.o.length)""","""if(L.picked==null&&q.type!=='match'&&/^[1-9]$/.test(ev.key)&&+ev.key<=q.o.length)""")
rep("""function noteMiss(q){
  if(!q||!q.a)return;""","""function noteMiss(q){
  if(!q||!q.a||q.type==='match')return;""")
open(f,'w',encoding='utf-8').write(s);print('learn ok')
