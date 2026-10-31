/* ================= arena: a real-time fight ================= */
/* You fight from behind your champion. The creature winds up before it strikes: dodge (left or right) at the
   last moment and it is left open for a counter; block takes a swipe for a little damage, but a red slam can
   only be dodged. Light attacks are quick, heavy attacks break a guard and stop a wind-up, and the special
   fills as you land hits and dodges. Best of three rounds, 60 seconds each. */
var AR_S=null;
function arenaStop(){if(AR_S){AR_S.dead=1;cancelAnimationFrame(AR_S.raf);(AR_S.tm||[]).forEach(clearTimeout);AR_S=null}}
function arT(fn,ms){var A=AR_S;if(!A)return;var id=setTimeout(function(){if(AR_S===A)fn()},ms);(A.tm=A.tm||[]).push(id);return id}
function foeOpen(i){var s=shopState();return REVIEW||i===0||!!s.beatK[ENEMIES[i-1].k]}
function stars(n){var h='';for(var i=0;i<5;i++)h+='<i class="'+(i<n?'on':'')+'">★</i>';return '<span class="dif" aria-label="Difficulty '+n+' of 5">'+h+'</span>'}
function foeStars(i){return Math.min(5,Math.ceil((i+1)/3))}
function foeReward(i,g){return Math.round((30+25*(i+1))*g.xp)}
/* damage a creature does with one swipe, before armour */
function foeHit(e){return Math.round(e.hit*1.25)}
var FT={light:{dur:300,hits:[140],mul:.5},heavy:{dur:640,hits:[380],mul:1.3},special:{dur:1050,hits:[260,520,780],mul:1}};
var FOE_SPECIAL={fire:['Burning blade','#FF7A1A'],poison:['Poison','#7CFC5A'],ice:['Lightning flash','#9BE6FF'],gold:['Golden strike','#FFD94A'],holy:['Twin strike','#FFF3B0']};
function arenaLobby(){
  ensureDefs();
  var q=eqItems(),s=shopState(),g=gearStats();
  var h='<section class="arena"><div class="shophero"><span class="eyebrow">Arena · السَّاحَةُ</span><h2>Battle Arena</h2><p class="muted">A real fight, best of three rounds. Watch the creature wind up, then dodge at the last moment and hit back while it is open. Upgrade your gear in the shop to hit harder and take less damage.</p></div>';
  h+='<div class="abanner">'+fieldSvg(q.field,'abg')+fieldFx(q.field)+'<div class="champ">'+rearSvg(q,{cls:'rear lob'})+'</div><div class="binfo"><b>'+esc(q.char.en)+'</b><span class="ar">'+esc(q.char.ar)+'</span><span>'+esc(q.weapon.en)+' · '+esc(q.armour.en)+'</span>'+statsHtml()+'<span class="wins">🏆 Wins: <b>'+(s.wins||0)+'</b> · 🏟 '+esc(q.field.en)+'</span><div class="brow"><a class="btn sm" href="#shop">Upgrade in the shop →</a></div></div></div>';
  h+='<div class="howto"><b>How to fight</b><span><kbd>←</kbd><kbd>→</kbd> or <kbd>A</kbd><kbd>D</kbd> dodge</span><span><kbd>↓</kbd> or <kbd>S</kbd> hold to block</span><span><kbd>J</kbd> light</span><span><kbd>K</kbd> heavy</span><span><kbd>L</kbd> or <kbd>Space</kbd> special</span><span>On a phone, use the buttons under the fight.</span></div>';
  h+='<h3 class="aeh">Select your opponent <small>'+ENEMIES.length+' creatures · '+ENEMIES.filter(function(e){return s.beatK[e.k]}).length+' beaten</small></h3><div class="egrid">'+ENEMIES.map(function(e,i){
    var rw=foeReward(i,g),open=foeOpen(i),beat=!!s.beatK[e.k];
    var inner='<div class="fpic">'+backSvg(e.bg)+foeSvg(e)+(beat?'<span class="fbeat">✓ Beaten</span>':'')+(i===ENEMIES.length-1?'<span class="fboss">BOSS</span>':'')+(open?'':'<span class="flock">🔒</span>')+'</div><div class="fbody"><b>'+esc(e.en)+'</b><p class="ar">'+esc(e.ar)+'</p>'+stars(foeStars(i))+
      '<div class="fst"><span>❤ '+e.hp+'</span><span>⚔ '+foeHit(e)+'</span></div><span class="rw">'+COIN+'Win '+rw+' XP</span></div>';
    return open?'<button type="button" class="foe" data-act="arenastart" data-t="'+i+'">'+inner+'</button>':'<div class="foe locked" title="Beat the '+esc(ENEMIES[i-1].en)+' first" aria-disabled="true">'+inner+'</div>';
  }).join('')+'</div></section>';
  V.innerHTML=h;
}
var FX={
  slash:'<svg class="fx slash" viewBox="0 0 120 120" aria-hidden="true"><path d="M14 98 Q54 50 108 18" pathLength="1" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M22 106 Q62 62 112 34" pathLength="1" stroke="#FFE066" stroke-width="5" fill="none" stroke-linecap="round"/></svg>',
  claw:'<svg class="fx claw" viewBox="0 0 120 120" aria-hidden="true"><path d="M30 20 Q46 60 40 100 M50 16 Q66 58 60 104 M70 20 Q86 60 80 100" pathLength="1" stroke="#D62828" stroke-width="6" fill="none" stroke-linecap="round"/></svg>',
  sting:'<svg class="fx sting" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="26" fill="#9BE564" opacity=".55"/><circle cx="40" cy="44" r="8" fill="#6BCB3A"/><circle cx="78" cy="38" r="6" fill="#6BCB3A"/><circle cx="74" cy="80" r="9" fill="#6BCB3A"/><circle cx="44" cy="78" r="5" fill="#6BCB3A"/></svg>',
  fire:'<svg class="fx fire" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="56" fill="url(#gFire)"/></svg>',
  burst:'<svg class="fx burst" viewBox="0 0 120 120" aria-hidden="true">'+spark(60,60,46,'#FFF3B0')+spark(60,60,26,'#FFFFFF')+'</svg>',
  bite:'<svg class="fx bite" viewBox="0 0 120 120" aria-hidden="true"><path d="M14 40 L26 62 L38 40 L50 62 L62 40 L74 62 L86 40 L98 62 L108 40" stroke="#fff" stroke-width="7" fill="none" stroke-linejoin="round" stroke-linecap="round"/><path d="M14 84 L26 62 L38 84 L50 62 L62 84 L74 62 L86 84 L98 62 L108 84" stroke="#D62828" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/></svg>',
  stomp:'<svg class="fx stomp" viewBox="0 0 120 120" aria-hidden="true"><ellipse cx="60" cy="68" rx="52" ry="16" fill="none" stroke="#fff" stroke-width="6"/><ellipse cx="60" cy="68" rx="34" ry="10" fill="none" stroke="#FFD27A" stroke-width="5"/></svg>',
  shield:'<svg class="fx shield" viewBox="0 0 120 120" aria-hidden="true"><path d="M60 8 L102 22 V60 C102 88 82 106 60 114 C38 106 18 88 18 60 V22Z" fill="#6FA8FF" opacity=".5" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></svg>',
  heal:'<svg class="fx heal" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="44" fill="#4CC58C" opacity=".28"/>'+spark(36,40,10,'#C8FFE0')+spark(86,36,8,'#C8FFE0')+spark(70,84,12,'#C8FFE0')+'</svg>'
};
function arPos(el,stage){var r=el.getBoundingClientRect(),s=stage.getBoundingClientRect();return {x:r.left+r.width/2-s.left,y:r.top+r.height/2-s.top,w:r.width,h:r.height,l:r.left-s.left,t:r.top-s.top,sw:s.width,sh:s.height}}
function arPop(txt,cls,x,y){
  var L=document.getElementById('fxL');if(!L)return;var d=document.createElement('span');d.className='dmg '+(cls||'');d.textContent=txt;d.style.left=x+'px';d.style.top=y+'px';L.appendChild(d);setTimeout(function(){d.remove()},1100);
}
function arFx(name,x,y,size,rot,tint){
  var L=document.getElementById('fxL');if(!L)return;var d=document.createElement('div');d.className='fxw';d.style.cssText='left:'+x+'px;top:'+y+'px;width:'+size+'px;height:'+size+'px;'+(rot?'--r:'+rot+'deg;':'')+(tint?'filter:drop-shadow(0 0 10px '+tint+') drop-shadow(0 0 4px '+tint+')':'');d.innerHTML=FX[name];L.appendChild(d);setTimeout(function(){d.remove()},900);
}
function arArrow(){
  var st=document.getElementById('arStage'),hand=st&&st.querySelector('.hand'),foe=document.getElementById('foeW');if(!hand||!foe)return;
  var h=arPos(hand,st),f=arPos(foe,st),L=document.getElementById('fxL'),d=document.createElement('div');
  var ang=Math.atan2(f.x-h.x,-(f.y-h.y))*180/Math.PI;
  d.className='arrowf';d.style.cssText='left:'+h.x+'px;top:'+h.y+'px;--dx:'+(f.x-h.x)+'px;--dy:'+(f.y-h.y)+'px;--a:'+ang.toFixed(1)+'deg';
  d.innerHTML='<svg viewBox="0 0 12 60" aria-hidden="true"><path d="M6 2 V52" stroke="#6A4C28" stroke-width="2.6" stroke-linecap="round"/><path d="M6 0 L11 12 H1Z" fill="#CDD5DE" stroke="#4E5965" stroke-width=".8"/><path d="M6 48 L1 58 M6 48 L11 58 M6 40 L1 50 M6 40 L11 50" stroke="#D6313F" stroke-width="2" stroke-linecap="round"/></svg>';
  L.appendChild(d);setTimeout(function(){d.remove()},500);
}
function aimWeapon(){
  [].forEach.call(document.querySelectorAll('.rear .wp'),function(wp){
    var svg=wp.ownerSVGElement,hand=svg.querySelector('.hand'),foe=document.getElementById('foeW');
    var hr=hand.getBoundingClientRect(),fr=foe?foe.getBoundingClientRect():null,ang=28;
    if(fr&&fr.width){var dx=fr.left+fr.width/2-(hr.left+hr.width/2),dy=fr.top+fr.height*.4-(hr.top+hr.height/2);ang=Math.atan2(dx,-dy)*180/Math.PI}
    ang=Math.max(10,Math.min(74,ang));
    var gx=+wp.dataset.gx,gy=+wp.dataset.gy;
    wp.setAttribute('transform','translate('+RW.hx+' '+RW.hy+') rotate('+ang.toFixed(1)+') scale('+RW.s+') translate('+(-gx)+' '+(-gy)+')');
    var gm=leftArmGeom(ang);
    [].forEach.call(svg.querySelectorAll('.larm .lp'),function(p){p.setAttribute('d',gm.d)});
    [].forEach.call(svg.querySelectorAll('.larm .lbr'),function(p){p.setAttribute('d','M'+gm.bx+' '+gm.by+' L'+gm.hx.toFixed(1)+' '+gm.hy.toFixed(1))});
    var lh=svg.querySelector('.larm .lh');if(lh)lh.setAttribute('transform','translate('+gm.hx.toFixed(1)+' '+gm.hy.toFixed(1)+')');
  });
}
function fBar(id,v,m){var el=document.getElementById(id);if(!el)return;var p=Math.max(0,Math.min(100,v/m*100));el.querySelector('i').style.width=p+'%';var lag=el.querySelector('u');if(lag)lag.style.width=p+'%';el.classList.toggle('low',p<=25)}
function fPips(n){return '<i></i><i></i>'.replace(/<i>/g,function(){return '<i class="'+(n-->0?'on':'')+'">'})}
function arenaView(){
  var A=AR_S;if(!A){arenaLobby();return}
  ensureDefs();
  var q=eqItems(),e=ENEMIES[A.tier];
  V.innerHTML='<section class="arena battle fight">'+
    '<div class="fhud"><div class="fside me"><span class="pp">'+charIcon(q.char)+'</span><div class="fbars"><b>'+esc(q.char.en)+'</b><div class="fhp" id="fhpP"><u></u><i></i></div><div class="fsp" id="fspP"><i></i><em>Special</em></div></div><span class="pips" id="pipP">'+fPips(0)+'</span></div>'+
    '<div class="ftime"><b id="fT">60</b><small id="fR">Round 1</small></div>'+
    '<div class="fside them"><span class="pips" id="pipE">'+fPips(0)+'</span><div class="fbars"><b>'+esc(e.en)+' <span class="ar">'+esc(e.ar)+'</span></b><div class="fhp" id="fhpE"><u></u><i></i></div></div><span class="pp">'+foeSvg(e,'ppf')+'</span></div></div>'+
    '<div class="astage" id="arStage">'+fieldSvg(q.field,'abg')+fieldFx(q.field)+'<div class="foew" id="foeW" data-s="idle"><div class="foei">'+foeSvg(e)+'</div><div class="ftell" id="fTell"></div></div><div class="mew" id="meW" data-s="idle"'+(q.mount&&q.mount.id!=='m0'?' data-m="1"':'')+'>'+rearSvg(q,{cls:'rear'})+'</div><div class="fxl" id="fxL"></div><div class="hurtv"></div><div class="fann" id="fAnn"></div><div class="fcombo" id="fCombo"></div></div>'+
    '<div class="fpad" id="fPad"><div class="fgrp"><button type="button" data-fk="dl" aria-label="Dodge left">◀<small>Dodge</small></button><button type="button" data-fk="bl" aria-label="Block">🛡<small>Block</small></button><button type="button" data-fk="dr" aria-label="Dodge right">▶<small>Dodge</small></button></div>'+
    '<div class="fgrp"><button type="button" data-fk="li" class="atkb">⚔<small>Light</small></button><button type="button" data-fk="he" class="atkb">💥<small>Heavy</small></button><button type="button" data-fk="sp" class="atkb spb" id="spBtn">★<small>Special</small></button></div></div>'+
    '<div class="frow"><button class="btn sm ghost" type="button" data-act="arenaquit">← Leave the fight</button><span class="muted sm">Keys: ← → dodge · ↓ block · J light · K heavy · L special</span></div><div id="arRes"></div></section>';
  aimWeapon();fHud();
}
function fHud(){
  var A=AR_S;if(!A)return;
  fBar('fhpP',A.p,A.pm);fBar('fhpE',A.e,A.em);
  var sp=document.getElementById('fspP');if(sp){sp.querySelector('i').style.width=A.sp+'%';sp.classList.toggle('full',A.sp>=100)}
  var b=document.getElementById('spBtn');if(b)b.classList.toggle('ready',A.sp>=100);
  var pp=document.getElementById('pipP'),pe=document.getElementById('pipE');if(pp)pp.innerHTML=fPips(A.wP);if(pe)pe.innerHTML=fPips(A.wE);
}
function fAnn(txt,cls,ms){var el=document.getElementById('fAnn');if(!el)return;el.className='fann on '+(cls||'');el.innerHTML=txt;void el.offsetWidth;arT(function(){if(el.innerHTML===txt)el.className='fann'},ms||900)}
/* set a state on the champion or the creature; the same state again restarts its animation */
function fSet(who,st){
  var A=AR_S,el=document.getElementById(who==='p'?'meW':'foeW');var o=who==='p'?A.P:A.E;o.st=st;o.t=0;
  if(!el)return;el.removeAttribute('data-s');void el.offsetWidth;el.setAttribute('data-s',st);
}
function fCombo(){var A=AR_S,el=document.getElementById('fCombo');if(!el)return;if(A.combo>=2){el.innerHTML='<b>'+A.combo+'</b> hit combo';el.className='fcombo on';void el.offsetWidth}else el.className='fcombo'}
function gearNow(){var g=gearStats(),w=eqItems().weapon;return {atk:g.atk,def:g.def,time:g.time,xp:g.xp,fx:w.fx||'',bow:w.k==='bow'}}
/* one round: full health for both, then the announcer */
function fRound(){
  var A=AR_S,e=ENEMIES[A.tier];
  A.round++;A.p=A.pm;A.e=A.em;A.clock=60000;A.live=false;A.combo=0;A.dot=0;A.slow=0;A.recent=[];
  A.P={st:'idle',t:0};A.E={st:'idle',t:0,wait:1400};
  var mw=document.getElementById('meW'),fw=document.getElementById('foeW');if(mw)mw.setAttribute('data-s','idle');if(fw)fw.setAttribute('data-s','idle');
  var r=document.getElementById('fR');if(r)r.textContent=A.round===3?'Final round':'Round '+A.round;
  var t=document.getElementById('fT');if(t)t.textContent='60';
  fHud();fCombo();
  fAnn(A.round===3?'Final round':'Round '+A.round,'rnd',1000);
  arT(function(){fAnn('Fight!','go',700);A.live=true},1050);
}
function fLoop(ts){
  var A=AR_S;if(!A||A.dead)return;
  var dt=A.last?Math.min(50,ts-A.last):16;A.last=ts;
  if(A.stop>0){A.stop-=dt;dt=0}
  if(A.live&&dt){if(A.g3&&typeof G3!=='undefined'&&G3.step)G3.step(dt);else fStep(dt)}
  A.raf=requestAnimationFrame(fLoop);
}
function fStep(dt){
  var A=AR_S,P=A.P,E=A.E,e=ENEMIES[A.tier],g=A.g;
  P.t+=dt;E.t+=dt;A.clock-=dt;
  var tt=document.getElementById('fT');if(tt)tt.textContent=Math.max(0,Math.ceil(A.clock/1000));
  /* the champion */
  var act=FT[P.st];
  if(act){
    act.hits.forEach(function(h,n){if(P.t-dt<h&&P.t>=h)fPlayerHit(P.st,n)});
    if(P.t>=act.dur){fSet('p','idle');if(A.buf&&Date.now()-A.bufT<260){var b=A.buf;A.buf=null;fInput(b)}}
  }else if(P.st==='dodgeL'||P.st==='dodgeR'){if(P.t>=420)fSet('p','idle')}
  else if(P.st==='hurt'){if(P.t>=380)fSet('p',A.hold?'block':'idle')}
  else if(P.st==='block'&&!A.hold&&P.t>=150)fSet('p','idle');
  if(P.st==='idle'&&A.hold)fSet('p','block');
  /* poison ticks */
  if(A.dot>0){A.dot-=dt;A.dotT=(A.dotT||0)+dt;if(A.dotT>=500){A.dotT=0;var pd=Math.max(1,Math.round(A.em*.02));A.e-=pd;fPopFoe('−'+pd,'poison');fHud();if(A.e<=0)return fKO(true)}}
  if(A.slow>0)A.slow-=dt;
  /* the creature */
  var spd=1-Math.min(.42,A.tier*.03),slow=A.slow>0?1.45:1,fw=document.getElementById('foeW');
  if(E.st==='idle'){
    if(E.t>=E.wait){
      var r=Math.random(),heavy=r<.38+A.tier*.012;
      if(r>.82&&A.round>0&&Math.random()<.6){fSet('e','guard');E.len=900+Math.random()*700}
      else{E.kind=heavy?'slam':'swipe';E.len=((heavy?1050:760)*spd+g.time*30)*slow;fSet('e','tele');
        var tl=document.getElementById('fTell');if(tl){tl.className='ftell on '+E.kind;tl.innerHTML=heavy?'<b>!!</b><small>Dodge</small>':'<b>!</b>'}}
    }
  }else if(E.st==='tele'){
    if(fw)fw.dataset.left=Math.round(E.len-E.t);
    if(E.t>=E.len)fFoeStrike();
  }else if(E.st==='strike'){if(E.t>=300)fSet('e',E.next||'idle'),E.wait=E.waitN||900}
  else if(E.st==='open'){if(E.t>=1150)fIdle()}
  else if(E.st==='guard'){if(E.t>=E.len)fIdle()}
  else if(E.st==='hurt'){if(E.t>=360)fIdle()}
  if(E.st!=='tele'){var tl2=document.getElementById('fTell');if(tl2&&tl2.className!=='ftell')tl2.className='ftell'}
  if(A.clock<=0){A.live=false;fAnn('Time!','ko',1200);arT(function(){fRoundEnd(A.p/A.pm>=A.e/A.em)},1300)}
}
function fIdle(){var A=AR_S,spd=1-Math.min(.42,A.tier*.03);fSet('e','idle');A.E.wait=(700+Math.random()*1100)*spd}
function fPopFoe(txt,cls){var st=document.getElementById('arStage'),fw=document.getElementById('foeW');if(!st||!fw)return;var f=arPos(fw,st);arPop(txt,cls,f.x+(Math.random()*40-20),f.y-f.h*.3)}
/* the champion's blow lands */
function fPlayerHit(kind,n){
  var A=AR_S,E=A.E,g=A.g,st=document.getElementById('arStage'),fw=document.getElementById('foeW');if(!st||!fw)return;
  if(g.bow&&kind!=='special')arArrow();
  var f=arPos(fw,st),base=g.atk*FT[kind].mul,cls='',note='';
  if(kind==='special'){
    if(g.fx==='gold')base*=1.5;
    if(g.fx==='holy'&&n===2)arT(function(){if(AR_S===A&&A.live)fPlayerHit('special',3)},160);
  }
  if(E.st==='guard'){
    if(kind==='light'){base*=.2;cls='blk';note='Blocked'}
    else{fSet('e','hurt');note='Guard break!';cls='big'}
  }else if(E.st==='open'){base*=1.6;cls='big';note=n===0?'Counter!':''}
  else if(E.st==='tele'&&kind!=='light'){fSet('e','hurt');var tl=document.getElementById('fTell');if(tl)tl.className='ftell';note='Interrupted!';cls='big'}
  else if(E.st==='idle'||E.st==='hurt'){
    /* too many quick hits in a row and the creature raises its guard */
    var now=Date.now();A.recent=A.recent.filter(function(x){return now-x<1300});A.recent.push(now);
    if(kind==='light'&&A.recent.length>=4&&Math.random()<.55){fSet('e','guard');E.len=800+Math.random()*500;A.recent=[]}
  }
  var dmg=Math.max(1,Math.round(base));A.e-=dmg;
  fw.classList.remove('hit');void fw.offsetWidth;fw.classList.add('hit');
  var tint=kind==='special'&&FOE_SPECIAL[g.fx]?FOE_SPECIAL[g.fx][1]:'';
  arFx(kind==='heavy'?'stomp':'slash',f.x,f.y,Math.min(f.w*(kind==='light'?1:1.3),280),kind==='light'?(n%2?-24:6):-40,tint);
  if(cls!=='blk')arFx('burst',f.x,f.y,Math.min(f.w*(kind==='light'?.7:1),220),0,tint);
  if(kind==='special'&&g.fx==='fire')arFx('fire',f.x,f.y,Math.min(f.w,240));
  arPop('−'+dmg,cls,f.x+(n%3-1)*22,f.y-f.h*.3);
  if(note)arT(function(){fPopFoe(note,'note')},90);
  if(cls!=='blk'){A.combo++;A.sp=Math.min(100,A.sp+(kind==='special'?0:kind==='heavy'?14:9));fCombo()}
  if(kind!=='light'){A.stop=70;st.classList.remove('shake');void st.offsetWidth;st.classList.add('shake')}
  if(kind==='special'&&n===0){
    if(g.fx==='poison'){A.dot=4000;A.dotT=0}
    if(g.fx==='ice')A.slow=5000;
  }
  fHud();
  if(A.e<=0)fKO(true);
}
/* the creature's blow lands, or misses */
function fFoeStrike(){
  var A=AR_S,E=A.E,P=A.P,e=ENEMIES[A.tier],g=A.g,st=document.getElementById('arStage'),mw=document.getElementById('meW');
  var dodging=(P.st==='dodgeL'||P.st==='dodgeR')&&P.t>=30&&P.t<=390;
  fSet('e','strike');E.next='idle';E.waitN=(800+Math.random()*900)*(1-Math.min(.42,A.tier*.03));
  if(!st||!mw)return;var m=arPos(mw,st);
  if(dodging){E.next='open';A.sp=Math.min(100,A.sp+25);arT(function(){fPopFoe('Open!','note')},120);arPop('Dodged!','heal',m.x,m.y-m.h*.35);fHud();return}
  var dmg=foeHit(e)*(E.kind==='slam'?1.5:1)*60/(60+g.def*3);
  if(P.st==='block'&&E.kind==='swipe'){dmg*=.22;arFx('shield',m.x,m.y-m.h*.2,Math.min(m.w*.6,200));arPop('Blocked','blk',m.x,m.y-m.h*.35);A.sp=Math.min(100,A.sp+6)}
  else{fSet('p','hurt');A.combo=0;fCombo();A.sp=Math.min(100,A.sp+8);st.classList.remove('shake','rflash');void st.offsetWidth;st.classList.add('shake','rflash');arFx(e.fx||'claw',m.x,m.y-m.h*.15,Math.min(m.w*.8,240))}
  dmg=Math.max(1,Math.round(dmg));A.p-=dmg;arPop('−'+dmg,'hurtp',m.x+20,m.y-m.h*.2);
  fHud();
  if(A.p<=0)fKO(false);
}
function fKO(win){
  var A=AR_S;if(!A.live)return;A.live=false;A.stop=0;
  fSet(win?'e':'p','ko');fAnn('K.O.','ko',1500);
  arT(function(){fRoundEnd(win)},1700);
}
function fRoundEnd(win){
  var A=AR_S;if(win)A.wP++;else A.wE++;fHud();
  if(A.wP>=2||A.wE>=2)return arEnd(A.wP>=2);
  arT(fRound,400);
}
function arEnd(win){
  var A=AR_S;if(!A)return;var e=ENEMIES[A.tier],s=shopState(),g=gearStats();
  A.over=true;A.win=win;cancelAnimationFrame(A.raf);
  A.reward=win?foeReward(A.tier,g):5;
  if(win){s.wins=(s.wins||0)+1;A.firstBeat=!s.beatK[e.k];s.beatK[e.k]=1}
  S.prog.xp=(S.prog.xp||0)+A.reward;saveProg();
  if(win)arT(function(){celebrate(0)},350);
  var pad=document.getElementById('fPad');if(pad)pad.classList.add('off');
  var box=document.getElementById('arRes');if(!box)return;
  box.innerHTML='<div class="card result aend '+(win?'win':'lose')+'">'+(win?'<svg class="trophy" viewBox="0 0 80 80" aria-hidden="true"><path d="M22 10 H58 V26 C58 40 50 48 40 48 C30 48 22 40 22 26Z" fill="url(#gGold)" stroke="#8C620E" stroke-width="2"/><path d="M22 14 H12 C12 28 18 34 24 34 M58 14 H68 C68 28 62 34 56 34" fill="none" stroke="#8C620E" stroke-width="3"/><rect x="36" y="48" width="8" height="12" fill="url(#gGold)"/><rect x="26" y="60" width="28" height="9" rx="2" fill="#5A3416"/>'+spark(30,22,4,'#FFFBE0')+'</svg>':'')+
    '<h2>'+(win?'Victory! <span class="ar">مَا شَاءَ اللَّهُ</span>':'Defeated')+'</h2><p>'+(win?'You beat the '+esc(e.en)+' '+A.wP+'–'+A.wE+' and earned '+COIN+'<b>'+A.reward+'</b> XP.'+(A.tier<ENEMIES.length-1&&A.firstBeat?' The '+esc(ENEMIES[A.tier+1].en)+' is now ready to fight.':''):'The '+esc(e.en)+' won '+A.wE+'–'+A.wP+'. You earned '+COIN+'<b>'+A.reward+'</b> XP for trying. Dodge at the last moment, or upgrade your gear!')+'</p>'+
    '<div class="row" style="justify-content:center"><button class="btn" type="button" data-act="arenastart" data-t="'+A.tier+'">Fight again</button>'+(win&&A.tier<ENEMIES.length-1?'<button class="btn gold" type="button" data-act="arenastart" data-t="'+(A.tier+1)+'">Next: '+esc(ENEMIES[A.tier+1].en)+' →</button>':'')+'<button class="btn ghost" type="button" data-act="arenaquit">Back to the Arena</button></div></div>';
  try{box.scrollIntoView({block:'nearest',behavior:'smooth'})}catch(err){}
}
/* input: dodge left/right, block (held), light, heavy, special */
function fInput(k){
  var A=AR_S;if(!A||!A.live)return;var P=A.P;
  if(k==='bl'){A.hold=true;if(P.st==='idle')fSet('p','block');return}
  if(P.st==='hurt'||P.st==='ko')return;
  if(P.st!=='idle'&&P.st!=='block'){A.buf=k;A.bufT=Date.now();return}
  if(k==='dl'||k==='dr'){fSet('p',k==='dl'?'dodgeL':'dodgeR');return}
  if(k==='li')fSet('p','light');
  else if(k==='he')fSet('p','heavy');
  else if(k==='sp'){if(A.sp<100){fPopFoe('Special not ready','note');return}A.sp=0;fHud();fSet('p','special');var nm=FOE_SPECIAL[A.g.fx];fAnn(nm?nm[0]:'Special!','sp',800)}
}
function fRelease(k){var A=AR_S;if(!A)return;if(k==='bl'){A.hold=false;if(A.P&&A.P.st==='block'&&A.P.t>=150)fSet('p','idle')}}
var FKEYS={ArrowLeft:'dl',a:'dl',A:'dl',ArrowRight:'dr',d:'dr',D:'dr',ArrowDown:'bl',s:'bl',S:'bl',Shift:'bl',j:'li',J:'li',z:'li',Z:'li',k:'he',K:'he',x:'he',X:'he',l:'sp',L:'sp',c:'sp',C:'sp',' ':'sp'};
document.addEventListener('keydown',function(ev){
  var A=AR_S;if(!A||A.over||A.g3||ev.ctrlKey||ev.metaKey||ev.altKey)return;var k=FKEYS[ev.key];if(!k)return;
  if(ev.target&&/INPUT|TEXTAREA|SELECT/.test(ev.target.tagName))return;
  ev.preventDefault();if(ev.repeat)return;fInput(k);
});
document.addEventListener('keyup',function(ev){var k=FKEYS[ev.key];if(k)fRelease(k)});
document.addEventListener('pointerdown',function(ev){var b=ev.target.closest&&ev.target.closest('[data-fk]');if(!b)return;ev.preventDefault();b.classList.add('down');fInput(b.dataset.fk)});
['pointerup','pointercancel','pointerleave'].forEach(function(t){document.addEventListener(t,function(ev){var b=ev.target.closest&&ev.target.closest('[data-fk]');if(!b)return;b.classList.remove('down');fRelease(b.dataset.fk)},true)});
document.addEventListener('contextmenu',function(ev){if(ev.target.closest&&ev.target.closest('.fpad'))ev.preventDefault()});
function viewArena(){arenaStop();arenaLobby();aimWeapon()}
ACT.arenastart=function(b){
  var t=+b.dataset.t,e=ENEMIES[t];
  if(!foeOpen(t)){toast('Beat the '+ENEMIES[t-1].en+' first.');return}
  arenaStop();var g=gearNow(),hp=120;
  AR_S={tier:t,g:g,p:hp,pm:hp,e:e.hp,em:e.hp,round:0,wP:0,wE:0,sp:0,combo:0,tm:[]};
  arenaView();fRound();AR_S.raf=requestAnimationFrame(fLoop);try{window.scrollTo(0,0)}catch(err){}
};
ACT.arenaquit=function(){arenaStop();arenaLobby();aimWeapon()};
window.addEventListener('resize',function(){if(document.querySelector('.rear .wp'))aimWeapon()});
