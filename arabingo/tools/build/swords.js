/* ===== the named swords of the Arabs: one drawing routine, many blades =====
   Every sword is drawn upright in the 64 x 64 weapon box, held at the grip (32, 48.5) like WPN.sword.
   o.len blade length, o.w blade width, o.cv how far the tip curves to the right, o.tip point|round|clip,
   o.metal steel|dam|gold|dark|bright|poison|blunt, o.guard bar|cross|drop|disc|wide, o.mark notch|saw|wave,
   o.fork split tip, o.glow colour of a glow behind the blade, o.grip and o.wrap the handle colours,
   o.pom ball|cap|hook, o.gem a stone in the guard. */
function swordArt(key,o){
  var len=o.len||32,w=(o.w||5)*1.3,cv=o.cv||0,N=14,L=[],R=[],C=[];
  var metal={steel:'gSteel',dam:'gDam',gold:'gGold',dark:'gDarkS',bright:'gBright',poison:'gPoison',blunt:'gBlunt'}[o.metal||'steel'];
  var edge={gold:'#8C620E',dark:'#1E2229',poison:'#245A1E',blunt:'#555B63'}[o.metal]||'#4E5965';
  function cen(t){return [32+cv*t*t,40-len*t]}
  function nrm(t){var dx=2*cv*t,dy=-len,m=Math.sqrt(dx*dx+dy*dy);return [-dy/m,dx/m]}
  function half(t){
    var b=w/2*(1-.18*t);
    if(o.tip==='round')return t>.9?b*Math.sqrt(Math.max(0,1-Math.pow((t-.9)/.1,2))):b;
    if(o.tip==='clip')return t<.62?b:b*(1-(t-.62)/.38)*(t<.8?1:.9);
    return t<.74?b:b*(1-(t-.74)/.26);
  }
  for(var i=0;i<=N;i++){
    var t=i/N,c=cen(t),n=nrm(t),h=half(t),kl=cv?1.18:1,kr=cv?.82:1;
    C.push(c);L.push([c[0]-n[0]*h*kl,c[1]-n[1]*h*kl]);R.push([c[0]+n[0]*h*kr,c[1]+n[1]*h*kr]);
  }
  var P=function(p){return p[0].toFixed(2)+' '+p[1].toFixed(2)},d,s='',top=cen(1);
  if(o.fork){
    var k=Math.round(N*.68),c1=cen(1),n1=nrm(1),c2=cen(.96),n2=nrm(.96),hv=w*.5;
    d='M'+L.slice(0,k+1).map(P).join(' L')+' L'+P([c1[0]-n1[0]*hv,c1[1]-n1[1]*hv])+' L'+P(cen(.8))+' L'+P([c2[0]+n2[0]*hv,c2[1]+n2[1]*hv])+' L'+R.slice(0,k+1).reverse().map(P).join(' L')+'Z';
  }else d='M'+L.map(P).join(' L')+' L'+R.slice().reverse().map(P).join(' L')+'Z';
  var cid='cl'+key;
  if(o.glow)s+='<ellipse cx="'+((32+top[0])/2).toFixed(1)+'" cy="'+(40-len/2).toFixed(1)+'" rx="'+(w*1.7+3).toFixed(1)+'" ry="'+(len*.62).toFixed(1)+'" fill="'+o.glow+'" opacity=".38" filter="url(#swGlow)"/>';
  s+='<clipPath id="'+cid+'"><path d="'+d+'"/></clipPath>';
  s+='<path d="'+d+'" fill="url(#'+metal+')" stroke="'+edge+'" stroke-width="1.1" stroke-linejoin="round"/>';
  s+='<g clip-path="url(#'+cid+')">';
  /* a darker back edge gives the blade its thickness */
  s+='<path d="M'+R.map(P).join(' L')+'" stroke="rgba(0,0,0,.28)" stroke-width="'+(w*.42).toFixed(2)+'" fill="none"/>';
  if(o.metal==='dam')for(var j=0;j<7;j++){var q='';for(var u=0;u<=N;u++){var tt=u/N,cc=cen(tt),nn=nrm(tt),off=(j-3)*w*.15+Math.sin(tt*15+j*1.7)*w*.12;q+=(u?' L':'M')+P([cc[0]+nn[0]*off,cc[1]+nn[1]*off])}s+='<path d="'+q+'" stroke="#2F3A46" stroke-width=".45" fill="none" opacity=".55"/>'}
  if(o.mark==='wave')for(var j2=0;j2<4;j2++){var q2='';for(var u2=0;u2<=N;u2++){var t2=u2/N,c2b=cen(t2),n2b=nrm(t2),of2=Math.sin(t2*22+j2)*w*.22;q2+=(u2?' L':'M')+P([c2b[0]+n2b[0]*of2,c2b[1]+n2b[1]*of2])}s+='<path d="'+q2+'" stroke="#FFF3B0" stroke-width=".5" fill="none" opacity=".7"/>'}
  s+='</g>';
  /* the fuller (the groove down the blade) and a bright edge line */
  if(o.fuller!==false){var f0=Math.round(N*.04),f1=Math.round(N*(o.tip==='clip'?.55:.66));s+='<path d="M'+C.slice(f0,f1).map(P).join(' L')+'" stroke="rgba(40,50,60,.55)" stroke-width="'+Math.max(.8,w*.16).toFixed(2)+'" fill="none" stroke-linecap="round"/>'}
  var hl=L.map(function(p,ii){var c=C[ii];return [p[0]+(c[0]-p[0])*.4,p[1]+(c[1]-p[1])*.4]});
  s+='<path d="M'+hl.slice(1,N-1).map(P).join(' L')+'" stroke="#fff" stroke-width=".9" fill="none" opacity="'+(o.metal==='dark'?.35:.85)+'"/>';
  if(o.mark==='notch')for(var m=2;m<N*.7;m+=2){var pr=R[m];s+='<circle cx="'+pr[0].toFixed(2)+'" cy="'+pr[1].toFixed(2)+'" r="'+(w*.24).toFixed(2)+'" fill="#1E2229" stroke="#fff" stroke-width=".35"/>'}
  if(o.mark==='saw')for(var m2=1;m2<N*.78;m2++){var a=R[m2],b=R[m2+1],n3=nrm(m2/N);s+='<path d="M'+P(a)+' L'+P([(a[0]+b[0])/2+n3[0]*1.6,(a[1]+b[1])/2+n3[1]*1.6])+' L'+P(b)+'Z" fill="url(#'+metal+')" stroke="'+edge+'" stroke-width=".6" stroke-linejoin="round"/>'}
  if(o.metal==='poison')s+='<path d="M'+P(L[5])+' q-1.2 3 0 4.2 q1.2 -1.2 0 -4.2Z M'+P(L[9])+' q-1 2.4 0 3.4 q1 -1 0 -3.4Z" fill="#7CFC5A" stroke="#245A1E" stroke-width=".4"/>';
  if(o.metal==='bright')s+=spark(top[0]-1,top[1]+5,3.4,'#FFFFFF')+spark(32+cv*.3-2,40-len*.45,2.2,'#E8FFFF');
  if(o.metal==='blunt')s+='<path d="M'+P(R[4])+' l1 1.4 l-1.2 1 M'+P(R[8])+' l1.2 1 l-1.2 1.4" stroke="#3A3F46" stroke-width=".7" fill="none"/>';
  /* guard, grip and pommel */
  var gold='url(#gGold)',gs='#8C620E',gc=o.gcol||gold;
  var gd={
    bar:'<rect x="24" y="39.4" width="16" height="4" rx="2" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/>',
    cross:'<path d="M19 41 Q21.5 37.5 25.5 39.4 H38.5 Q42.5 37.5 45 41 Q42.5 44.5 38.5 42.6 H25.5 Q21.5 44.5 19 41Z" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/>',
    drop:'<path d="M20 38.6 Q22 44.6 28 42.4 H36 Q42 44.6 44 38.6 Q45.8 40.8 44.6 43 Q41 47.6 36 44.6 H28 Q23 47.6 19.4 43 Q18.2 40.8 20 38.6Z" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/><circle cx="20" cy="38.4" r="1.4" fill="'+gc+'" stroke="'+gs+'" stroke-width=".6"/><circle cx="44" cy="38.4" r="1.4" fill="'+gc+'" stroke="'+gs+'" stroke-width=".6"/>',
    disc:'<ellipse cx="32" cy="41.2" rx="7.4" ry="2.6" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/>',
    wide:'<path d="M22 40 Q32 36 42 40 L40.6 43.4 Q32 40.6 23.4 43.4Z" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/>'
  }[o.guard||'cross'];
  s+='<rect x="29.6" y="42.6" width="4.8" height="11.4" rx="1.4" fill="'+(o.grip||'#4A2A10')+'" stroke="rgba(0,0,0,.45)" stroke-width=".6"/>';
  for(var yy=44.6;yy<53.6;yy+=2.6)s+='<path d="M29.6 '+yy.toFixed(1)+' L34.4 '+(yy+1.5).toFixed(1)+'" stroke="'+(o.wrap||'#9B6A3A')+'" stroke-width="1.1"/>';
  s+=gd;
  if(o.gem)s+='<circle cx="32" cy="41.2" r="1.6" fill="'+o.gem+'" stroke="#fff" stroke-width=".4"/>';
  if(o.pom==='hook')s+='<path d="M29.6 53.4 Q28 58.6 24.6 59.6 Q29.8 61.6 34.4 55.6 V53.4Z" fill="'+gc+'" stroke="'+gs+'" stroke-width=".8" stroke-linejoin="round"/>';
  else if(o.pom==='cap')s+='<path d="M28.4 53.6 H35.6 L37 57.8 Q32 59.6 27 57.8Z" fill="'+gc+'" stroke="'+gs+'" stroke-width=".8"/>';
  else s+='<circle cx="32" cy="57.4" r="3.1" fill="'+gc+'" stroke="'+gs+'" stroke-width=".9"/><circle cx="31" cy="56.4" r=".9" fill="#FFF7CF"/>';
  return {g:[32,48.5],a:s,sc:(o.sc||1)*1.12};
}
var SWORDS={
  dadan:{len:27,w:5.2,tip:'round',metal:'blunt',guard:'bar',fuller:false,gcol:'#7A7F86'},
  mishmal:{len:17,w:4.6,cv:1.5,metal:'steel',guard:'disc',pom:'cap',grip:'#2E1A0A',sc:1.15},
  janbiya:{len:16,w:6.2,cv:6,metal:'bright',guard:'wide',pom:'cap',grip:'#6A1F1F',wrap:'#E3B53C',gem:'#2F9E6E',fuller:false,sc:1.15},
  sadhij:{len:30,w:4.8,metal:'steel',guard:'bar',fuller:false},
  qashib:{len:31,w:5,metal:'bright',guard:'cross',glow:'#BFEFFF'},
  midad:{len:24,w:8.4,cv:2,tip:'clip',metal:'dark',guard:'bar',grip:'#5A3416',fuller:false},
  dhaliq:{len:33,w:4.2,cv:4,metal:'steel',guard:'drop',pom:'hook'},
  safiha:{len:30,w:9,tip:'round',metal:'steel',guard:'cross',gem:'#2F7FD1'},
  adb:{len:34,w:4.6,cv:2,metal:'bright',guard:'drop',glow:'#DDF6FF'},
  matin:{len:32,w:6.6,metal:'dark',guard:'cross',grip:'#1E1E26',wrap:'#7A8794'},
  arqab:{len:32,w:7.4,cv:3,tip:'clip',metal:'steel',guard:'bar',grip:'#3E220C'},
  barraq:{len:35,w:4.8,metal:'bright',guard:'cross',glow:'#FFFFFF',gem:'#7FD8FF'},
  lahdham:{len:35,w:4.2,cv:5,metal:'steel',guard:'drop',pom:'hook',grip:'#1E1E26'},
  batir:{len:34,w:5.4,cv:7,metal:'bright',guard:'drop',pom:'hook',gem:'#D6313F'},
  dhakar:{len:34,w:5.6,metal:'dam',guard:'cross',grip:'#2E1A0A'},
  rasub:{len:37,w:4.4,metal:'dark',guard:'drop',glow:'#7FA8FF',grip:'#13215E'},
  mufaqqar:{len:34,w:6.2,metal:'steel',guard:'cross',mark:'notch',gem:'#E3B53C'},
  dair:{len:33,w:5.4,cv:4,metal:'dam',guard:'drop',pom:'hook',grip:'#4A2A10',wrap:'#C9A15A'},
  bilarak:{len:35,w:5.2,cv:8,metal:'dam',guard:'drop',pom:'hook',gem:'#2F9E6E',glow:'#9BE7C4'},
  qirdab:{len:33,w:6.4,cv:2,metal:'dark',guard:'bar',mark:'saw',grip:'#3A0E0E',glow:'#FF6A5E'},
  mudharrab:{len:34,w:5.6,cv:3,metal:'poison',guard:'drop',pom:'hook',glow:'#7CFC5A',grip:'#1E3A14'},
  islit:{len:38,w:6.8,metal:'steel',guard:'cross',grip:'#2E1A0A',gem:'#8E44C9',sc:.94},
  husam:{len:37,w:5.6,cv:5,metal:'bright',guard:'drop',pom:'hook',glow:'#FFD27A',gem:'#D6313F',sc:.96},
  mudajjal:{len:35,w:5.6,cv:4,metal:'gold',guard:'drop',pom:'hook',mark:'wave',glow:'#FFD94A',gem:'#D6313F'},
  dimashqi:{len:35,w:5.4,cv:3,metal:'dam',guard:'drop',pom:'hook',gem:'#2F7FD1',glow:'#C9D6FF'},
  fiqar:{len:37,w:7.6,metal:'bright',guard:'drop',fork:1,glow:'#FFE9A8',gem:'#2F9E6E',pom:'cap',sc:.95}
};
Object.keys(SWORDS).forEach(function(k){WPN['sw_'+k]=swordArt(k,SWORDS[k])});
