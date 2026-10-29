/* ===== 3D: the arena fight and the shop turntable, drawn with Three.js (loaded from cdnjs) when WebGL works.
   Without it the 2D drawings are used. The fight rules stay in the fight code above; this only draws them:
   it reads AR_S every frame, and it places the hidden 2D boxes (#foeW, #meW) over the 3D models so the damage
   numbers, warnings and slash effects line up with them. ===== */
var G3=(function(){
  var T=window.THREE,ok=false;
  try{if(T){var tc=document.createElement('canvas');ok=!!(tc.getContext('webgl2')||tc.getContext('webgl'))}}catch(err){ok=false}
  if(!ok)return {ok:false,stop:function(){},ev:function(){}};
  var CUR=null,MC={};
  function stop(){
    if(AR_S)AR_S.g3=0;FG=null;KEY={};JOY=null;MOUSE=null;
    if(!CUR)return;var c=CUR;CUR=null;cancelAnimationFrame(c.raf);
    c.scene.traverse(function(o){if(o.geometry)o.geometry.dispose();if(o.material)[].concat(o.material).forEach(function(m){if(m.map)m.map.dispose();m.dispose()})});
    try{c.r.dispose();c.r.forceContextLoss()}catch(err){}
    if(c.r.domElement.parentNode)c.r.domElement.remove();if(c.host)c.host.classList.remove('a3d','s3d');MC={};
  }
  /* ---- small helpers ---- */
  function M(col,o){o=o||{};var k=col+JSON.stringify(o);if(MC[k])return MC[k];
    var m=new T.MeshStandardMaterial({color:lin(col),roughness:o.r!=null?o.r:.62,metalness:o.m||0,emissive:lin(o.e||'#000000'),emissiveIntensity:o.ei!=null?o.ei:1,transparent:!!o.op,opacity:o.op||1,side:o.ds?T.DoubleSide:T.FrontSide,depthWrite:o.op?false:true});
    if(o.add){m.blending=T.AdditiveBlending}return MC[k]=m}
  function lin(c){return new T.Color(c).convertSRGBToLinear()}
  function mesh(g,m,x,y,z,p){var o=new T.Mesh(g,m);o.position.set(x||0,y||0,z||0);o.castShadow=true;o.receiveShadow=true;if(p)p.add(o);return o}
  function sph(r,m,x,y,z,p,sx,sy,sz){var o=mesh(new T.SphereGeometry(r,20,14),m,x,y,z,p);if(sx)o.scale.set(sx,sy,sz);return o}
  function cyl(rt,rb,h,m,x,y,z,p,seg,open){return mesh(new T.CylinderGeometry(rt,rb,h,seg||16,1,!!open),m,x,y,z,p)}
  function box(w,h,d,m,x,y,z,p){return mesh(new T.BoxGeometry(w,h,d),m,x,y,z,p)}
  function cone(r,h,m,x,y,z,p,seg){return mesh(new T.ConeGeometry(r,h,seg||14),m,x,y,z,p)}
  function tor(r,t,m,x,y,z,p,arc){return mesh(new T.TorusGeometry(r,t,8,28,arc||Math.PI*2),m,x,y,z,p)}
  function grp(p,x,y,z){var g=new T.Group();g.position.set(x||0,y||0,z||0);if(p)p.add(g);return g}
  /* a capsule hanging down from its pivot */
  function limb(p,r,len,m,x,y,z){var g=grp(p,x,y,z);cyl(r,r*.88,len,m,0,-len/2,0,g);sph(r,m,0,0,0,g);sph(r*.88,m,0,-len,0,g);return g}
  function hex(c,f){return /^#[0-9a-f]{3,8}$/i.test(String(c||''))?c:f}
  function canvasTex(w,h,draw,rep){var c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);var t=new T.CanvasTexture(c);t.encoding=T.sRGBEncoding;if(rep){t.wrapS=t.wrapT=T.RepeatWrapping;t.repeat.set(rep[0],rep[1])}t.anisotropy=4;return t}
  var GLOW=null;function glowTex(){if(GLOW)return GLOW;return GLOW=canvasTex(64,64,function(x,w){var g=x.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,'rgba(255,255,255,1)');g.addColorStop(.35,'rgba(255,255,255,.55)');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;x.fillRect(0,0,64,64)})}
  function sprite(col,s,p,op){var m=new T.SpriteMaterial({map:glowTex(),color:lin(col),transparent:true,opacity:op||1,blending:T.AdditiveBlending,depthWrite:false});var o=new T.Sprite(m);o.scale.set(s,s,s);if(p)p.add(o);return o}
  /* every mesh gets its own material copy, so a hit can flash one model without flashing the others */
  function own(root){var list=[];root.traverse(function(o){if(o.isMesh&&o.material&&!o.material.transparent){o.material=o.material.clone();list.push(o.material)}});return list}
  function flash(list,col,amt){var c=lin(col);list.forEach(function(m){if(!m._e)m._e=m.emissive.clone();m.emissive.copy(m._e).lerp(c,amt)})}

  /* ---- weapons, built along +Y from the grip ---- */
  var METAL={steel:['#D5DCE4',.92,.22],dam:['#A3AEBB',.85,.34],gold:['#F2C14E',1,.28],dark:['#4A515C',.85,.38],bright:['#FFFFFF',.95,.1],poison:['#9BD77F',.6,.3,'#3AFF2A'],blunt:['#9AA0A6',.5,.62],ice:['#B8EEFF',.5,.15,'#38C8FF'],fire:['#FFB05A',.5,.25,'#FF5A10'],void:['#5A2A8A',.6,.3,'#A040FF']};
  function bladeShape(len,w,cv,tip,fork){
    var N=16,L=[],R=[];
    for(var i=0;i<=N;i++){var t=i/N,cx=cv*t*t,b=w/2*(1-.18*t),h=tip==='round'?(t>.9?b*Math.sqrt(Math.max(0,1-Math.pow((t-.9)/.1,2))):b):tip==='clip'?(t<.62?b:b*(1-(t-.62)/.38)):(t<.74?b:b*(1-(t-.74)/.26));
      L.push([cx-h*(cv?1.18:1),t*len]);R.push([cx+h*(cv?.82:1),t*len])}
    var s=new T.Shape();s.moveTo(L[0][0],L[0][1]);
    if(fork){var k=Math.round(N*.68);for(var a=1;a<=k;a++)s.lineTo(L[a][0],L[a][1]);s.lineTo(cv-w*.5,len);s.lineTo(cv*.64,len*.8);s.lineTo(cv*.92+w*.5,len*.96);for(var b2=k;b2>=0;b2--)s.lineTo(R[b2][0],R[b2][1])}
    else{for(var a2=1;a2<=N;a2++)s.lineTo(L[a2][0],L[a2][1]);for(var b3=N;b3>=0;b3--)s.lineTo(R[b3][0],R[b3][1])}
    return s;
  }
  function blade(p,o){
    var mt=METAL[o.metal||'steel']||METAL.steel,len=(o.len||32)*.03,w=(o.w||5)*1.3*.011,cv=(o.cv||0)*.012;
    var g=new T.ExtrudeGeometry(bladeShape(len,w,cv,o.tip,o.fork),{depth:.012,bevelEnabled:true,bevelThickness:.008,bevelSize:.006,bevelSegments:2,steps:1});g.translate(0,0,-.006);
    var bm=M(mt[0],{m:mt[1],r:mt[2],e:mt[3]||'#000000',ei:mt[3]?.8:1});var b=mesh(g,bm,0,.04,0,p);
    if(o.mark==='wave'||o.metal==='dam'){var lines=M(o.metal==='gold'?'#FFF3B0':'#59636F',{r:.5,m:.6});for(var i=0;i<3;i++)box(.004,len*.6,.026,lines,(i-1)*w*.22+cv*.2,.04+len*.38,0,p)}
    var gc=hex(o.gcol,'#F2C14E'),gm=M(gc,{m:.95,r:.3});
    if(o.guard==='drop'){var dg=tor(.07,.012,gm,0,.045,0,p,Math.PI);dg.rotation.z=Math.PI}else if(o.guard==='disc')cyl(.05,.05,.014,gm,0,.04,0,p);else box(o.guard==='bar'?.13:.17,.022,.04,gm,0,.04,0,p);
    if(o.gem)sph(.014,M(o.gem,{r:.2,m:.2,e:o.gem,ei:.4}),0,.04,-.025,p);
    cyl(.016,.018,.13,M(hex(o.grip,'#4A2A10'),{r:.8}),0,-.03,0,p);
    if(o.pom==='hook'){var hk=tor(.03,.012,gm,-.02,-.1,0,p,Math.PI*1.1);hk.rotation.z=Math.PI*.6}else sph(.026,gm,0,-.105,0,p);
    if(mt[3]||o.glow){var gl=sprite(mt[3]||o.glow,len*1.1,p,.35);gl.position.y=.04+len*.5}
    var tipO=grp(p,cv,.04+len,0);return tipO;
  }
  var WK={sword:{len:30,w:5},scimitar:{len:30,w:5.6,cv:8,guard:'drop',pom:'hook'},gsword:{len:31,w:5.4,cv:6,metal:'gold',guard:'drop',pom:'hook'},fsword:{len:31,w:6,cv:3,metal:'fire'},isword:{len:31,w:6,metal:'ice',gem:'#38C8FF'},dsword:{len:32,w:6,metal:'ice'},
    katana:{len:34,w:3.4,cv:3,metal:'dark',guard:'disc',glow:'#9AE7FF'},voidblade:{len:34,w:5,cv:2,metal:'void'},venom:{len:15,w:5,cv:3,metal:'poison',guard:'bar'},dagger:{len:15,w:4.6,cv:4,guard:'bar'}};
  WK.kris={len:16,w:4.2,cv:6,metal:'poison',guard:'bar'};WK.claymore={len:38,w:6.5,cv:2,metal:'void',guard:'bar'};
  function weapon(w){
    var g=grp(),k=w&&w.k||'stick',wood=M('#7A4E2A',{r:.8}),steel=M('#C9D1DA',{m:.9,r:.25}),gold=M('#F2C14E',{m:1,r:.3}),tip;
    var sw=k.indexOf('sw_')===0&&typeof SWORDS!=='undefined'?SWORDS[k.slice(3)]:WK[k];
    if(sw)tip=blade(g,sw);
    else if(k==='spear'||k==='trident'){cyl(.016,.016,1.7,wood,0,.55,0,g);if(k==='spear'){var sp=cone(.04,.22,steel,0,1.5,0,g);sp.scale.z=.4;tip=grp(g,0,1.62,0);tor(.025,.008,M('#C0392B'),0,1.36,0,g)}else{[-1,0,1].forEach(function(s){var c=cone(.018,.2,steel,s*.06,1.5+(s?0:.04),0,g)});box(.15,.02,.02,steel,0,1.4,0,g);tip=grp(g,0,1.62,0)}}
    else if(k==='mace'||k==='flail'){cyl(.018,.018,.7,wood,0,.25,0,g);var hd=sph(.08,steel,0,.65,0,g);for(var i=0;i<8;i++){var c2=cone(.02,.07,steel,0,0,0,hd);var a=i/8*Math.PI*2;c2.position.set(Math.cos(a)*.08,(i%2?.03:-.03),Math.sin(a)*.08);c2.lookAt(Math.cos(a)*2,0,Math.sin(a)*2);c2.rotateX(Math.PI/2)}tip=grp(g,0,.7,0)}
    else if(k==='axe'){cyl(.018,.018,.8,wood,0,.3,0,g);var ax=new T.Shape();ax.moveTo(0,-.1);ax.quadraticCurveTo(.22,-.14,.24,0);ax.quadraticCurveTo(.22,.14,0,.1);ax.lineTo(0,-.1);[1,-1].forEach(function(s){var m2=mesh(new T.ExtrudeGeometry(ax,{depth:.01,bevelEnabled:true,bevelSize:.005,bevelThickness:.005}),steel,0,.62,-.005,g);m2.scale.x=s});tip=grp(g,.24,.62,0)}
    else if(k==='hammer'||k==='thunder'){cyl(.02,.02,.8,wood,0,.3,0,g);box(.26,.13,.13,k==='thunder'?M('#7FA8FF',{m:.6,r:.2,e:'#2A6BFF',ei:.9}):steel,0,.7,0,g);if(k==='thunder')sprite('#7FC0FF',.6,g,.6).position.y=.7;tip=grp(g,.13,.7,0)}
    else if(k==='staff'){cyl(.016,.02,1.3,wood,0,.45,0,g);sph(.06,M('#8EE7FF',{r:.1,e:'#2B9BFF',ei:1}),0,1.13,0,g);tor(.07,.012,gold,0,1.13,0,g);sprite('#7FD8FF',.5,g,.6).position.y=1.13;tip=grp(g,0,1.13,0)}
    else if(k==='bow'||k==='phoenix'||k==='longbow'||k==='crossbow'||k==='boomerang'||k==='chakram'){var bw=tor(.45,.016,k==='phoenix'||k==='longbow'?M('#FF8A3A',{e:'#FF4A00',ei:.7}):wood,0,0,0,g,Math.PI*.9);bw.rotation.z=Math.PI*.55;box(.004,.86,.004,M('#F3EBD8'),-.16,0,0,g);tip=grp(g,.3,0,0);if(k==='phoenix')sprite('#FF7A1A',.9,g,.4)}
    else{var st=cyl(.018,.022,1.1,wood,0,.35,0,g);st.rotation.z=.04;tip=grp(g,.02,.9,0)}
    return {g:g,tip:tip};
  }

  /* ---- the champion: face toward -Z, back toward +Z ---- */
  var SKN='#E2AE80';
  var ARMET=/gIron|gSilver|gGold|gSteel|gDiamond|gChain|gBronze|gRuby|gEmerald|gObsid|gRoyal|gDscale|gLaboos/;
  var HOODS={shadow:'#7A5CFF',ember:'#FF7A1A',frost:'#7FE8FF',jade:'#4CFF9A',void:'#C04AFF'};
  function hero(eq){
    var a=eq.armour,ch=eq.char,w=eq.weapon,mt=eq.mount&&eq.mount.id!=='m0'?eq.mount:null;
    var root=grp(),body=grp(root),P={root:root,body:body};
    var metal=a.id!=='a0'&&ARMET.test(a.g||''),robeC=hex(ch.wear,'#F4F1EA');
    var arm=a.id==='a0'?M(robeC,{r:.85}):M(hex(a.col,'#999'),metal?{m:.72,r:.3}:{r:.72});
    var edge=M(hex(a.edge,'#555'),{m:metal?.6:0,r:.45}),skin=M(SKN,{r:.55});
    var low=a.full?arm:M('#3A3F4A',{r:.8}),boot=a.full?arm:M('#4A2E18',{r:.8});
    var robe=a.id==='a0'||!metal;
    var hips=grp(body,0,mt?0:.95,0);P.hips=hips;
    /* legs: hip, knee and ankle joints, with sandals under a robe and boots under armour */
    var sandal=robe&&!a.full,shin=sandal?skin:low,soleM=M('#5A3416',{r:.85}),strap=M('#8A5A2E',{r:.7});
    function foot(an){
      if(sandal){sph(.05,skin,0,-.035,-.045,an,1,.6,1.9);[-.03,-.01,.012,.03].forEach(function(x,i){sph(.016-i*.002,skin,x,-.045,-.14,an)});box(.105,.022,.25,soleM,0,-.075,-.05,an);box(.11,.02,.03,strap,0,-.035,-.09,an);box(.02,.05,.02,strap,0,-.02,-.02,an)}
      else{cyl(.072,.08,.13,boot,0,-.01,0,an,14);sph(.07,boot,0,-.04,-.08,an,1,.75,1.5);box(.12,.03,.27,M('#2A1A10',{r:.8}),0,-.075,-.05,an)}
    }
    function leg(sx){var hip=grp(hips,sx*.12,-.02,0),th=limb(hip,.088,.42,low),kn=grp(th,0,-.42,0),sh2=limb(kn,.072,.4,shin);if(sandal){cyl(.08,.075,.12,low,0,-.06,0,kn,12)}var an=grp(kn,0,-.42,0);foot(an);return {hip:hip,kn:kn,an:an}}
    P.legL=leg(-1);P.legR=leg(1);
    if(mt){[P.legL,P.legR].forEach(function(l,i){var s2=i?1:-1;l.hip.rotation.set(1.35,0,s2*.4);l.kn.rotation.x=-1.45;l.an.rotation.x=.2})}
    else{
      if(robe)cyl(.21,.3,.6,a.id==='a0'?M(robeC,{r:.85}):M(hex(a.col,'#999'),{r:.75}),0,-.3,0,hips,24);
      else if(a.skirt)cyl(.26,.36,.42,arm,0,-.2,0,hips,20);
    }
    var chest=grp(hips,0,.04,0);P.chest=chest;
    cyl(.25,.21,.52,arm,0,.26,0,chest,22);sph(.255,arm,0,.52,0,chest,1,.52,.82);
    cyl(.232,.232,.09,M(hex(a.belt,robe?'#8A6A3A':hex(a.edge,'#555')),{r:.6,m:metal?.4:0}),0,.03,0,chest,22);
    sph(.03,M('#F2C14E',{m:1,r:.3}),0,.03,-.235,chest);
    if(metal){sph(.13,arm,-.29,.5,0,chest,1.15,.75,1.05);sph(.13,arm,.29,.5,0,chest,1.15,.75,1.05);box(.34,.3,.06,edge,0,.3,-.19,chest);if(a.trim)tor(.1,.014,M(hex(a.trim,'#fff'),{m:.8,r:.3}),0,.56,0,chest).rotation.x=Math.PI/2}
    if(robe&&!a.cape&&!ch.cape&&!HOODS[ch.t]){
      var bc=ch.girl?hex(ch.wear,'#6C4A8A'):({ghutra:'#4A2E18',nomad:'#3A2A1E',prince:'#1E1A2E',turban:'#2E3A5E',sultan:'#5A1A22'}[ch.t]||'#4A2E18'),bm=M(bc,{r:.78,ds:true}),gt=M('#E3B53C',{m:.9,r:.3});
      var bg=new T.CylinderGeometry(.27,.4,1.15,26,1,true,Math.PI+.42,Math.PI*2-.84);mesh(bg,bm,0,.0,0,chest);
      [-1,1].forEach(function(sd){var a2=Math.PI+sd*.42,tr=box(.035,1.15,.035,gt,Math.sin(a2)*.335,0,Math.cos(a2)*.335,chest);tr.rotation.z=sd*.11});
      sph(.27,bm,0,.5,0,chest,1.05,.45,.86);
    }
    var cape=a.cape||ch.cape;
    if(cape){var cg=new T.PlaneGeometry(.58,1.05,6,12),cp=grp(chest,0,.56,.2),c=mesh(cg,M(hex(cape,'#8E1F2A'),{r:.8,ds:true}),0,-.52,0,cp);P.cape=c;P.capeBase=cg.attributes.position.array.slice()}
    var neck=grp(chest,0,.56,0);cyl(.07,.08,.14,skin,0,.04,0,neck);
    var head=grp(neck,0,.2,0);P.head=head;sph(.15,skin,0,0,0,head,1,1.08,1);
    face(head,ch);hat(head,ch,robeC);
    /* arms: shoulder, elbow and hand pivots; the sleeves follow the armour */
    function fist(h,sx,m){
      sph(.058,m,0,-.01,0,h,1.05,1.12,.82);
      for(var i=0;i<4;i++){var x=(i-1.5)*.027;sph(.019,m,x,-.06,-.03,h,1,1,1.1);sph(.017,m,x,-.072,-.005,h,1,1.1,1)}
      var th=sph(.02,m,sx*-.05,-.03,-.035,h,1,1.7,1);th.rotation.z=sx*.5;
    }
    function side(sx){var sh=grp(chest,.33*sx,.47,0),up=limb(sh,.072,.3,arm),el=grp(up,0,-.3,0),fo=limb(el,.064,.27,a.full||robe?arm:M(hex(a.col,'#999'),metal?{m:.72,r:.3}:{r:.72})),hand=grp(el,0,-.3,0);fist(hand,sx,a.full?arm:skin);return {sh:sh,el:el,hand:hand}}
    P.R=side(1);P.L=side(-1);
    var W=weapon(w);P.R.hand.add(W.g);W.g.rotation.set(-1.75,0,0);P.tip=W.tip;P.wpn=W.g;
    P.mount=mt?mountModel(mt,root):null;
    if(P.mount){hips.position.y=P.mount.seat}
    P.mats=own(root);
    return P;
  }
  function face(h,ch){
    if(HOODS[ch.t])return;
    var white=M('#FFFFFF',{r:.3}),dk=M('#1E1610',{r:.5});
    [-1,1].forEach(function(s){sph(.03,white,s*.055,.03,-.128,h);sph(.017,dk,s*.055,.03,-.153,h);box(.05,.012,.012,M('#3A2410'),s*.054,.068,-.14,h).rotation.z=s*.12});
    sph(.022,M(SKN),0,-.01,-.155,h);
    if(!ch.girl){sph(.1,M('#2E1E12',{r:.9}),0,-.1,-.07,h,1,.62,.75);box(.07,.014,.02,M('#2E1E12'),0,-.04,-.148,h)}
    else sph(.015,M('#C0565A'),0,-.07,-.142,h,1.6,.6,.6);
  }

  function hcap(h,m,r,d){return mesh(new T.SphereGeometry(r||.168,22,12,0,Math.PI*2,0,Math.PI*(d||.55)),m,0,.012,0,h)}
  function hdrape(h,m,len,open){return mesh(new T.CylinderGeometry(.168,.215,len||.4,26,1,true,Math.PI+(open||.62),Math.PI*2-2*(open||.62)),m,0,-.15,.01,h)}
  var HATN={
    pirate:function(h){var bk=M('#16161C',{r:.7}),gd=M('#F2C14E',{m:1,r:.3});cyl(.21,.21,.03,bk,0,.1,0,h,22);cyl(.14,.17,.14,bk,0,.17,0,h,22);tor(.17,.012,gd,0,.12,0,h).rotation.x=Math.PI/2;sph(.036,bk,-.055,.03,-.152,h,1,1,.5);box(.2,.012,.012,bk,-.03,.07,-.14,h).rotation.z=-.4},
    gladiator:function(h){var br=M('#C9964E',{m:.85,r:.3}),rd=M('#C0392B',{r:.8});hcap(h,br,.172,.5);box(.03,.12,.3,rd,0,.19,0,h);[-1,1].forEach(function(s){box(.03,.14,.07,br,s*.15,-.02,-.04,h)})},
    huntress:function(h){var gm=M('#4A6A3A',{r:.85,ds:true});hcap(h,gm,.178,.58);hdrape(h,gm,.46,.55);cone(.02,.2,M('#F4EFE2'),.1,.14,.08,h).rotation.z=-.5},
    elder:function(h){var wt=M('#F7F4EC',{r:.9});for(var j=0;j<3;j++)tor(.15-j*.01,.04,wt,0,.04+j*.04,0,h).rotation.x=Math.PI/2;hcap(h,wt,.14,.5).position.y=.11;sph(.11,wt,0,-.13,-.06,h,1,1.7,.7)},
    northman:function(h){var ir=M('#9AA2AC',{m:.9,r:.3});hcap(h,ir,.172,.5);[-1,1].forEach(function(s){cone(.03,.22,M('#F4EFE2'),s*.17,.1,0,h).rotation.z=-s*.9});sph(.1,M('#C9762A',{r:.9}),0,-.1,-.07,h,1,.9,.7)},
    samgirl:function(h){var bk=M('#1E1610',{r:.8});hcap(h,bk,.17,.58);sph(.07,bk,0,0,.17,h,1,2.2,1);tor(.16,.012,M('#C0392B'),0,.07,0,h).rotation.x=Math.PI/2},
    engineer:function(h){hcap(h,M('#6A4A2A',{r:.85}),.17,.5);[-1,1].forEach(function(s){tor(.04,.012,M('#37E6FF',{e:'#37E6FF',ei:.6}),s*.06,.13,-.12,h)});tor(.165,.01,M('#2A2A2A'),0,.1,0,h).rotation.x=Math.PI/2},
    rogue:function(h){var dk=M('#2A2438',{r:.85,ds:true});hcap(h,dk,.178,.58);hdrape(h,dk,.46,.55);box(.24,.1,.04,M('#16161C'),0,-.075,-.14,h)},
    berserk:function(h){var rd=M('#B8321A',{r:.9});hcap(h,rd,.17,.45);for(var i=0;i<9;i++){var a=i/9*Math.PI*2;cone(.03,.12,rd,Math.cos(a)*.12,.13,Math.sin(a)*.12,h)}},
    marksman:function(h){var gm=M('#3A5A3A',{r:.85});hcap(h,gm,.17,.5);box(.2,.015,.1,gm,0,.08,-.15,h);cone(.015,.2,M('#F4EFE2'),.1,.15,.05,h).rotation.z=-.5},
    medic:function(h){var wt=M('#F7F4EC',{r:.9}),rd=M('#D6313F');hcap(h,wt,.17,.5);box(.08,.02,.012,rd,0,.1,-.168,h);box(.02,.08,.012,rd,0,.1,-.168,h)},
    samurai:function(h){var bk=M('#16161C',{r:.8});hcap(h,bk,.17,.55);sph(.05,bk,0,.2,.04,h);tor(.165,.012,M('#F7F4EC'),0,.08,0,h).rotation.x=Math.PI/2},
    general:function(h){var gm=M('#3A4A2A',{r:.8});cyl(.17,.17,.12,gm,0,.15,0,h,24);cyl(.19,.19,.02,gm,0,.09,-.01,h,24);box(.2,.015,.1,M('#16161C'),0,.08,-.17,h);sph(.02,M('#F2C14E',{m:1,r:.3}),0,.14,-.17,h)},
    runner:function(h){hcap(h,M('#16161C',{r:.8}),.17,.5);tor(.165,.012,M('#1F8AA8'),0,.08,0,h).rotation.x=Math.PI/2},
    wizard:function(h){var bl=M('#3A2A6A',{r:.8}),wt=M('#F7F4EC',{r:.9});cone(.2,.55,bl,0,.38,0,h,20);cyl(.28,.28,.02,bl,0,.11,0,h,24);sph(.03,M('#F2C14E',{m:1,r:.3}),0,.3,-.12,h);sph(.1,wt,0,-.2,-.07,h,1,2.2,.7)},
    witch:function(h){var pl=M('#4A2A5A',{r:.8});cone(.19,.5,pl,0,.36,0,h,20);cyl(.27,.27,.02,pl,0,.11,0,h,24);hdrape(h,M('#2A1830',{r:.9,ds:true}),.6,.5)},
    pharaoh:function(h){var gd=M('#E3B53C',{m:.9,r:.3});hcap(h,gd,.175,.6);hdrape(h,M('#E3B53C',{m:.6,r:.4,ds:true}),.5,.5);tor(.168,.016,M('#2F7FD1',{r:.4}),0,.07,0,h).rotation.x=Math.PI/2;sph(.03,gd,0,.1,-.17,h)},
    queen:function(h){var gd=M('#F2C14E',{m:1,r:.28});hcap(h,M('#1E1610',{r:.8}),.172,.58);hdrape(h,M('#1E1610',{r:.9,ds:true}),.55,.5);tor(.15,.02,gd,0,.15,0,h).rotation.x=Math.PI/2;for(var i=0;i<6;i++){var a=i/6*Math.PI*2;cone(.02,.07,gd,Math.cos(a)*.15,.2,Math.sin(a)*.15,h)}},
    astro:function(h){mesh(new T.SphereGeometry(.2,24,16),new T.MeshStandardMaterial({color:'#BFE8FF',transparent:true,opacity:.3,roughness:.08}),0,0,0,h);tor(.2,.03,M('#F7F4EC',{r:.5}),0,-.14,0,h).rotation.x=Math.PI/2},
    cyborg:function(h){var st=M('#9AA6B2',{m:.9,r:.3});hcap(h,st,.172,.5);sph(.03,M('#FF3A3A',{e:'#FF3A3A',ei:1.5}),.055,.03,-.158,h);box(.1,.18,.03,st,.08,0,-.14,h)}
  };
  function hat(h,ch,wc){
    if(HATN[ch.t]){HATN[ch.t](h,ch,wc);return}
    var t=ch.t,white=M('#F7F4EC',{r:.9}),black=M('#1E1E22',{r:.6}),gold=M('#F2C14E',{m:1,r:.28}),wm=M(wc,{r:.85});
    function cap(m,r,deep){return mesh(new T.SphereGeometry(r||.168,22,12,0,Math.PI*2,0,Math.PI*(deep||.55)),m,0,.012,0,h)}
    function drape(m,len,open){var g=new T.CylinderGeometry(.168,.215,len||.4,26,1,true,Math.PI+(open||.62),Math.PI*2-2*(open||.62));return mesh(g,m.side===T.DoubleSide?m:M('#'+m.color.getHexString(),{r:.9,ds:true}),0,-.15,.01,h)}
    function agal(){[.07,.105].forEach(function(y){var o=tor(.163,.017,black,0,y,0,h);o.rotation.x=Math.PI/2})}
    if(t==='ghutra'||t==='nomad'||t==='prince'){
      var cm=t==='nomad'?checkMat():white;cap(cm);drape(cm,.42);agal();var fl=box(.26,.4,.02,cm,0,-.3,.17,h);fl.rotation.x=.12;
      if(t==='prince'){var cr=tor(.15,.02,gold,0,.15,0,h);cr.rotation.x=Math.PI/2;for(var i=0;i<6;i++){var a=i/6*Math.PI*2;cone(.02,.07,gold,Math.cos(a)*.15,.2,Math.sin(a)*.15,h)}}
    }else if(t==='turban'||t==='sultan'||t==='smith'){
      if(t==='smith'){cap(M('#8E1F2A',{r:.8}),.165,.5);return}
      var tm=t==='sultan'?white:white;for(var j=0;j<4;j++){var o=tor(.15-j*.012,.045,tm,0,.04+j*.045,0,h);o.rotation.x=Math.PI/2}
      cap(tm,.14,.5).position.y=.12;
      if(t==='sultan'){var b=tor(.158,.02,gold,0,.06,0,h);b.rotation.x=Math.PI/2;sph(.03,M('#D6313F',{r:.2,e:'#D6313F',ei:.4}),0,.1,-.17,h);cone(.012,.12,white,0,.32,.02,h)}
      else sph(.025,M('#2F9E6E',{r:.2}),0,.1,-.165,h);
    }else if(t==='helmet'||t==='warrg'){
      var hm=M('#C9D1DA',{m:.92,r:.25});cap(hm,.178,.52);cyl(.18,.18,.05,hm,0,.02,0,h,22);box(.02,.12,.03,hm,0,-.02,-.17,h);
      var pl=sph(.06,M('#C0392B',{r:.8}),0,.2,.06,h,.6,1.4,2.2);pl.rotation.x=.6;
      if(t==='warrg')drape(M(wc,{r:.85,ds:true}),.36,.7);
    }else if(t==='explorer'){var hb=M('#C9A46A',{r:.9});cyl(.32,.32,.02,hb,0,.1,0,h,26);cyl(.15,.17,.13,hb,0,.17,0,h,22);tor(.16,.012,M('#5A3416'),0,.12,0,h).rotation.x=Math.PI/2}
    else if(HOODS[t]){var hd=M(wc,{r:.85,ds:true});cap(hd,.19,.6);drape(hd,.5,.5);var ec=HOODS[t];sph(.13,M('#07080E',{r:1}),0,-.01,-.06,h,1,1,.9);[-1,1].forEach(function(s){sph(.022,M(ec,{e:ec,ei:2}),s*.05,.02,-.16,h);sprite(ec,.12,h,.8).position.set(s*.05,.02,-.18)})}
    else{ // hijab, khimar, princess, archer, ranger, falconer: a hood or headscarf in the character's colour
      var hm2=M(wc,{r:.85,ds:true});cap(hm2,.178,.58);drape(hm2,.46,.55);
      if(t==='princess'){var ti=tor(.12,.016,gold,0,.17,-.03,h,Math.PI);ti.rotation.set(Math.PI/2,0,Math.PI);cone(.02,.07,gold,0,.22,-.1,h)}
      if(t==='archer'||t==='ranger'||t==='falconer'){var pk=cone(.08,.2,hm2,0,.06,.17,h);pk.rotation.x=1.9}
    }
  }
  var CHECK=null;function checkMat(){if(CHECK&&MC.__chk)return MC.__chk;CHECK=canvasTex(64,64,function(x){x.fillStyle='#F4F1EA';x.fillRect(0,0,64,64);x.fillStyle='#C0392B';for(var i=0;i<64;i+=16){x.fillRect(i,0,6,64);x.fillRect(0,i,64,6)}},[4,4]);return MC.__chk=new T.MeshStandardMaterial({map:CHECK,roughness:.9,side:T.DoubleSide})}

  /* ---- four-legged animals: mounts and creatures. They face +Z. ---- */
  function quad(o){
    var R=grp(),B=grp(R,0,o.h+o.r*.8,0),c=M(o.col,{r:o.rough||.72}),bel=M(o.belly||o.col,{r:.78}),dk=M(o.dark||'#2A2420',{r:.7});
    var bd=sph(o.r,c,0,0,0,B,1,o.ry||.92,o.len/o.r/2);
    var legs=[],lr=o.leg||o.r*.3;
    [[-1,1],[1,1],[-1,-1],[1,-1]].forEach(function(s){var lh=o.h+o.r*.45+(s[1]>0&&o.front?o.front:0),g=limb(B,lr,lh,c,s[0]*o.r*.6,-o.r*.25,s[1]*o.len*.33);sph(lr*1.15,dk,0,-lh,lr*.2,g,1,.6,1.3);legs.push(g)});
    var N=grp(B,0,o.r*.3,o.len*.42),H=grp(N,0,o.neck||o.r*.4,o.r*.45);
    if(o.neck){var nk=cyl(o.r*.32,o.r*.42,o.neck*1.1,c,0,-o.neck*.45,-o.r*.2,H);nk.rotation.x=-.5}
    sph(o.head,c,0,0,0,H,1,.95,o.hz||1.1);
    var sn=sph(o.head*.62,bel,0,-o.head*.22,o.head*(o.snz||.8),H,1,.78,o.snl||1.25);
    sph(o.head*.16,dk,0,-o.head*.05,o.head*(o.snz||.8)+o.head*.62*(o.snl||1.25)*.9,H);
    var ec=o.eye||'#FF7A1A',eyes=[],brow=M('#140A06',{r:.8}),fang=M('#F4EFE2',{r:.35});[-1,1].forEach(function(s){var e=sph(o.head*.15,M(ec,{e:ec,ei:o.glowEye?1.8:.9,r:.2}),s*o.head*.5,o.head*.28,o.head*.72,H);sph(o.head*.07,M('#111'),s*o.head*.52,o.head*.28,o.head*.84,H,.35,1.25,.35);eyes.push(e);var bw=box(o.head*.5,o.head*.1,o.head*.16,brow,s*o.head*.48,o.head*.47,o.head*.76,H);bw.rotation.z=s*.55;bw.rotation.y=-s*.2;var fg=cone(o.head*.065,o.head*.26,fang,s*o.head*.2,-o.head*.5,o.head*(o.snz||.8)+o.head*.55,H);fg.rotation.x=Math.PI});sph(o.head*.36,M('#3A0A08',{r:.7}),0,-o.head*.48,o.head*(o.snz||.8)+o.head*.25,H,1,.35,1.1);
    if(o.ear==='point')[-1,1].forEach(function(s){var e=cone(o.head*.28,o.head*.6,c,s*o.head*.55,o.head*.75,-o.head*.1,H);e.rotation.z=-s*.3});
    else if(o.ear==='round')[-1,1].forEach(function(s){sph(o.head*.26,c,s*o.head*.7,o.head*.62,-o.head*.1,H,1,1,.5)});
    else if(o.ear==='long')[-1,1].forEach(function(s){var e=sph(o.head*.22,c,s*o.head*.4,o.head*1.05,-o.head*.2,H,.7,2.4,.5);e.rotation.z=-s*.25});
    else if(o.ear==='big')[-1,1].forEach(function(s){var e=sph(o.head*.9,c,s*o.head*.95,o.head*.1,-o.head*.3,H,.18,1,1);e.rotation.y=s*.5});
    if(o.mane){var mm=M(o.mane,{r:.95});sph(o.head*1.55,mm,0,-o.head*.1,-o.head*.35,H,1,1.05,.75)}
    if(o.hairMane){var hm=M(o.hairMane,{r:.95});for(var i=0;i<6;i++)box(.04,.14,.1,hm,0,o.r*.5+i*.01,o.len*.42-i*.07,B).rotation.x=-.4}
    if(o.horns)[-1,1].forEach(function(s){var hg=grp(H,s*o.head*.6,o.head*.55,-o.head*.1);var hn=tor(o.head*.45,o.head*.08,M(o.horns,{r:.4}),0,0,0,hg,Math.PI*.6);hn.rotation.set(0,Math.PI/2,s>0?Math.PI*.15:Math.PI*.85)});
    if(o.horn){var hr=cone(o.head*.25,o.head*.9,M('#E8E2D0',{r:.5}),0,o.head*.15,o.head*1.55,H);hr.rotation.x=.5;cone(o.head*.15,o.head*.45,M('#E8E2D0',{r:.5}),0,o.head*.35,o.head*1.1,H).rotation.x=.3}
    if(o.trunk){var tg=grp(H,0,-o.head*.2,o.head*.9);var seg=tg;for(var k=0;k<6;k++){var sg=grp(seg,0,-.09,0);cyl(o.head*.2-k*.012,o.head*.18-k*.012,.1,c,0,-.045,0,sg);seg=sg;sg.rotation.x=.18}o.trunkG=tg;
      [-1,1].forEach(function(s){var tu=cone(o.head*.09,o.head*.8,M('#F4EFE2',{r:.4}),s*o.head*.35,-o.head*.45,o.head*.95,H);tu.rotation.x=2.2})}
    if(o.hump)for(var q=0;q<o.hump;q++)sph(o.r*.5,c,0,o.r*.75,(q-(o.hump-1)/2)*o.len*.25,B,1,.9,1.1);
    if(o.stripes){var smat=M(o.stripes,{r:.8});for(var z=-3;z<=3;z++){var st=tor(o.r*.96,o.r*.06,smat,0,0,z*o.len*.1,B,Math.PI);st.rotation.z=Math.PI*0;st.scale.set(1,o.ry||.92,1)}}
    if(o.spots){var spm=M(o.spots,{r:.8});for(var sp=0;sp<10;sp++){var aa=Math.random()*Math.PI,zz=(Math.random()-.5)*o.len*.7;sph(o.r*.12,spm,Math.cos(aa)*o.r*.92,Math.sin(aa)*o.r*.85,zz,B,1,1,.4).lookAt(0,0,zz)}}
    if(o.spikes){var spk=M(o.spikes,{r:.5});for(var n=0;n<6;n++){cone(o.r*.12,o.r*.4,spk,0,o.r*.95,o.len*.35-n*o.len*.14,B)}}
    if(o.wings){var wm=M(o.wings,{r:.7,ds:true});o.wingG=[];[-1,1].forEach(function(s){var wg=grp(B,s*o.r*.5,o.r*.6,0),sh=new T.Shape();sh.moveTo(0,0);sh.lineTo(s*1.6,.9);sh.lineTo(s*1.9,.2);sh.lineTo(s*1.5,-.1);sh.lineTo(s*1.1,.05);sh.lineTo(s*.7,-.2);sh.lineTo(0,-.3);var m2=mesh(new T.ShapeGeometry(sh),wm,0,0,0,wg);m2.rotation.x=-Math.PI/2.2;o.wingG.push(wg)})}
    /* the tail: a chain of segments */
    var tl=grp(B,0,o.r*.2,-o.len*.47),seg2=tl,tm=o.tailCol?M(o.tailCol,{r:.9}):c;o.tailG=[];
    var tn=o.tail==='none'?0:o.tail==='long'?7:o.tail==='thick'?7:5;
    for(var u=0;u<tn;u++){var g2=grp(seg2,0,0,u?-(o.tseg||.13):0),r2=o.tail==='thick'?o.r*(.7-u*.09):o.tail==='bushy'?o.r*(.18+(u>2?.12:0)):o.r*.07;sph(Math.max(.02,r2),u===tn-1&&o.tail==='tuft'?M(o.mane||'#5A3416',{r:.95}):tm,0,0,0,g2);g2.rotation.x=u?.22:(o.tail==='thick'?.1:.7);seg2=g2;o.tailG.push(g2)}
    if(o.low){B.position.y=o.h+o.r*.55}
    return {root:R,body:B,head:H,neck:N,legs:legs,tail:o.tailG,trunk:o.trunkG,wings:o.wingG,eyes:eyes,seat:o.h+o.r*1.55};
  }
  var MOUNTQ={
    horse:{col:'#9A6233',len:1.7,r:.36,h:.72,head:.17,hz:1.7,snl:1.5,neck:.42,ear:'point',tail:'long',tailCol:'#2E1A0C',hairMane:'#2E1A0C',dark:'#2A1A10'},
    donkey:{col:'#B8B6B0',len:1.3,r:.32,h:.55,head:.16,hz:1.6,snl:1.4,neck:.3,ear:'long',tail:'tuft'},
    camel:{col:'#CFA56B',len:1.7,r:.38,h:.95,head:.14,hz:1.6,snl:1.4,neck:.7,ear:'round',tail:'tuft',hump:1},
    wolf:{col:'#8A929E',belly:'#D8DCE2',len:1.5,r:.32,h:.45,head:.2,ear:'point',tail:'bushy'},
    lion:{col:'#D9A24A',mane:'#7A3F14',len:1.7,r:.42,h:.5,head:.26,ear:'round',tail:'tuft'},
    tiger:{col:'#E08A2E',belly:'#F4EFE2',stripes:'#1E1610',len:1.8,r:.4,h:.5,head:.25,ear:'round',tail:'long'},
    hound:{col:'#3A1C1E',len:1.5,r:.33,h:.5,head:.21,ear:'point',tail:'long',eye:'#FF5A1F',glowEye:1},
    panther:{col:'#232733',len:1.6,r:.33,h:.48,head:.22,ear:'round',tail:'long',eye:'#7CFC5A',glowEye:1},
    rhino:{col:'#8E959E',len:2,r:.6,h:.45,head:.32,hz:1.4,ear:'round',horn:1,tail:'tuft'},
    elephant:{col:'#9AA0A8',len:2.2,r:.82,h:.85,head:.5,snl:.6,ear:'big',trunk:1,tail:'tuft'},
    dragon:{col:'#1F8A63',belly:'#9BE7A0',len:2.2,r:.55,h:.55,head:.3,hz:1.4,horns:'#E8E2D0',spikes:'#F2C14E',wings:'#C0392B',tail:'thick',tseg:.24,eye:'#FFB300',glowEye:1},
    icedrake:{col:'#7FD8FF',belly:'#E8FFFF',len:2.2,r:.55,h:.55,head:.3,hz:1.4,horns:'#FFFFFF',spikes:'#E8FFFF',wings:'#9BE6FF',tail:'thick',tseg:.24,eye:'#38C8FF',glowEye:1}
  };
  MOUNTQ.mare=MOUNTQ.horse;MOUNTQ.pegasus=MOUNTQ.horse;
  Object.assign(MOUNTQ,{
    bull:{col:'#6A3A22',len:1.8,r:.46,h:.55,head:.28,hz:1.2,ear:'round',horns:'#F4EFE2',tail:'tuft'},
    boar:{col:'#6A5A4A',len:1.5,r:.4,h:.4,head:.25,hz:1.5,snl:1,ear:'point',tail:'tuft',spikes:'#2A2018'},
    zebra:{col:'#F4F1EA',stripes:'#16161A',len:1.7,r:.36,h:.72,head:.17,hz:1.7,snl:1.5,neck:.4,ear:'point',tail:'tuft'},
    ram:{col:'#EDE6D4',len:1.3,r:.36,h:.45,head:.18,ear:'round',horns:'#C8B890',tail:'none'},
    bear:{col:'#6A4A32',len:1.6,r:.55,h:.42,head:.3,ear:'round',tail:'none'},
    stag:{col:'#9A6A3A',len:1.6,r:.34,h:.75,head:.16,hz:1.6,neck:.45,ear:'point',horns:'#D8C8A0',tail:'tuft'},
    hippo:{col:'#8A7A9A',len:1.9,r:.6,h:.3,head:.38,hz:1.3,snl:1.1,ear:'round',tail:'none'},
    giraffe:{col:'#E0B050',spots:'#7A4A1A',len:1.5,r:.38,h:1.1,head:.15,hz:1.7,snl:1.3,neck:1.1,ear:'round',tail:'tuft'},
    komodo:{col:'#6A7A4A',len:2.2,r:.3,ry:.6,h:.12,low:1,head:.2,snl:2,ear:'none',tail:'thick',tseg:.22},
    croc:{col:'#4A6A30',belly:'#C8C88A',len:2.6,r:.32,ry:.55,h:.06,low:1,head:.22,hz:1,snl:2.6,snz:1.2,ear:'none',tail:'thick',tseg:.22,spikes:'#2E4A1E'},
    gorilla:{col:'#2A2A2E',len:1.2,r:.55,h:.5,head:.28,ear:'round',tail:'none'},
    turtle:{col:'#4A7A4A',len:1.5,r:.55,ry:.7,h:.2,head:.16,snl:.8,ear:'none',tail:'none',low:1,hump:1},
    leopard:{col:'#E8B84A',spots:'#2A1608',len:1.7,r:.32,h:.45,head:.2,ear:'round',tail:'long'},
    scorpion:{col:'#8A4A26',len:1.5,r:.38,ry:.55,h:.3,head:.18,ear:'none',tail:'thick',tseg:.2,spikes:'#2A1408'},
    mammoth:{col:'#6A4A32',len:2.2,r:.8,h:.85,head:.5,snl:.6,ear:'big',trunk:1,tail:'tuft'},
    spider:{col:'#2A1E2E',len:1.2,r:.5,ry:.7,h:.5,head:.22,ear:'none',tail:'none',eye:'#FF2A2A',glowEye:1},
    unicorn:{col:'#F7F4F8',len:1.7,r:.36,h:.72,head:.17,hz:1.7,snl:1.5,neck:.42,ear:'point',tail:'long',tailCol:'#E87ACF',hairMane:'#E87ACF',horn:1},
    griffin:{col:'#C9964E',len:1.8,r:.42,h:.5,head:.24,ear:'point',wings:'#E8D8B0',tail:'tuft',mane:'#F4EFE2'},
    phoenix:{col:'#FF8A2E',len:1.6,r:.38,h:.6,head:.2,ear:'point',wings:'#FFB13A',tail:'long',tailCol:'#FFD24A',eye:'#FFFFFF',glowEye:1},
    skelhorse:{col:'#E8E2D0',len:1.7,r:.34,h:.72,head:.17,hz:1.7,snl:1.5,neck:.42,ear:'point',tail:'long',tailCol:'#B8B09A',hairMane:'#B8B09A',eye:'#7CFC5A',glowEye:1}
  });

  function mountModel(m,parent){
    var k=m.kind,base=MOUNTQ[k],o;
    if(base){o={};for(var x in base)o[x]=base[x];if(m.col&&/^#/.test(m.col))o.col=m.col;if(m.mane&&/^#/.test(m.mane)&&(k==='horse'||k==='mare'||k==='pegasus')){o.hairMane=m.mane;o.tailCol=m.mane}
      if(k==='pegasus')o.wings='#F7F7FB';var Q=quad(o);Q.root.rotation.y=Math.PI;parent.add(Q.root);
      if(m.blanket&&/^#/.test(m.blanket))box(o.r*1.5,.04,o.len*.36,M(m.blanket,{r:.8}),0,o.r*.85,0,Q.body);
      Q.seat=(o.h+o.r*.8)+o.r*.85+.05;return Q}
    var R=grp(parent);
    if(k==='carpet'){var cm=canvasTex(128,64,function(x,w,h){x.fillStyle='#8E1F2A';x.fillRect(0,0,w,h);x.strokeStyle='#F2C14E';x.lineWidth=5;x.strokeRect(6,6,w-12,h-12);x.fillStyle='#2F6FB0';x.beginPath();x.moveTo(64,14);x.lineTo(92,32);x.lineTo(64,50);x.lineTo(36,32);x.fill()});
      var cg=new T.PlaneGeometry(1.4,2,8,8);var c=mesh(cg,new T.MeshStandardMaterial({map:cm,side:T.DoubleSide,roughness:.9}),0,.5,0,R);c.rotation.x=-Math.PI/2;sprite('#FFE9A8',1.6,R,.25).position.y=.4;return {root:R,carpet:c,cg:cg,base:cg.attributes.position.array.slice(),seat:.55}}
    if(k==='chariot'){var wd=M('#5A3416',{r:.8});box(1,.5,.8,wd,0,.55,0,R);[-1,1].forEach(function(s){var wh=tor(.38,.05,M('#C9964E',{r:.6}),s*.58,.4,0,R);wh.rotation.y=Math.PI/2});return {root:R,seat:.75}}
    /* birds: ostrich, falcon (the Rukh) */
    var bc=hex(m.col,k==='ostrich'?'#2A2420':'#6A4A2A'),bm=M(bc,{r:.85}),bh=k==='ostrich'?1:.4;
    var B=grp(R,0,bh+.35,0);sph(.45,bm,0,0,0,B,1,.85,1.3);var nk=grp(B,0,.2,-.45);cyl(.06,.09,k==='ostrich'?.8:.3,M(k==='ostrich'?'#E8B9A0':bc),0,.35,0,nk);var hd=sph(.12,M(k==='falcon'?'#F4EFE2':'#E8B9A0'),0,k==='ostrich'?.8:.4,-.05,nk);cone(.05,.18,M('#F2C14E'),0,k==='ostrich'?.78:.38,-.18,nk).rotation.x=-Math.PI/2;
    [-1,1].forEach(function(s){limb(B,.04,bh,M('#E8B9A0'),s*.18,-.2,0)});
    var wings=[];[-1,1].forEach(function(s){var wg=grp(B,s*.4,.15,0);sph(.32,bm,s*.45,0,0,wg,1.6,.25,.9);wings.push(wg)});
    return {root:R,body:B,wings:wings,seat:bh+.75};
  }

  /* ---- the creatures ---- */
  var FOEQ={
    wolf:MOUNTQ.wolf,hyena:{col:'#B89A6A',spots:'#4A3A2A',len:1.4,r:.34,h:.45,front:.12,head:.22,ear:'round',tail:'bushy'},
    bull:{col:'#5A3A24',len:1.9,r:.5,h:.55,head:.3,hz:1.2,ear:'round',horns:'#F4EFE2',tail:'tuft',eye:'#FF4A2A'},
    lion:MOUNTQ.lion,panther:MOUNTQ.panther,tiger:MOUNTQ.tiger,rhino:MOUNTQ.rhino,elephant:MOUNTQ.elephant,
    bear:{col:'#5A3A22',len:1.6,r:.58,h:.42,head:.32,ear:'round',tail:'none',eye:'#FFB300'},
    crocodile:{col:'#4A6A30',belly:'#C8C88A',len:2.6,r:.32,ry:.55,h:.06,low:1,head:.22,hz:1,snl:2.6,snz:1.2,ear:'none',tail:'thick',tseg:.22,spikes:'#2E4A1E',eye:'#FFD43B'},
    dragon:MOUNTQ.dragon
  };

  Object.assign(FOEQ,{
    jackal:{col:'#C9964E',belly:'#EAD9B0',len:1.3,r:.28,h:.5,head:.19,ear:'point',tail:'bushy'},
    boar:Object.assign({},MOUNTQ.boar,{eye:'#FF4A2A'}),komodo:MOUNTQ.komodo,hippo:MOUNTQ.hippo,leopard:MOUNTQ.leopard,mammoth:MOUNTQ.mammoth,griffin:MOUNTQ.griffin,
    polar:{col:'#F4F4F6',len:1.7,r:.6,h:.42,head:.32,ear:'round',tail:'none',eye:'#222'},
    dire:{col:'#3A3E48',belly:'#8A929E',len:1.9,r:.4,h:.6,head:.26,ear:'point',tail:'bushy',eye:'#FF3A1A',glowEye:1},
    manticore:{col:'#B8452A',mane:'#3A1408',len:1.9,r:.45,h:.52,head:.28,ear:'round',tail:'long',wings:'#6A1A1A',horns:'#E8E2D0',spikes:'#2A1408',eye:'#FF3A1A',glowEye:1},
    chimera:{col:'#C9964E',mane:'#5A2A10',len:2,r:.46,h:.55,head:.28,ear:'round',tail:'thick',tseg:.22,wings:'#3A6A3A',horns:'#E8E2D0',eye:'#FF8A00',glowEye:1},
    hydra:{col:'#2F7A4A',belly:'#A8E8A0',len:2.2,r:.5,h:.4,head:.26,hz:1.3,ear:'none',tail:'thick',tseg:.24,spikes:'#16401F',horns:'#E8E2D0',eye:'#C8FF3A',glowEye:1},
    wyvern:Object.assign({},MOUNTQ.dragon,{col:'#6A4A8A',belly:'#C8A8E8',wings:'#3A2A5A'}),
    basilisk:{col:'#5A7A2A',belly:'#E8D86A',len:2.2,r:.3,ry:.6,h:.15,low:1,head:.24,snl:1.6,ear:'none',tail:'thick',tseg:.22,spikes:'#C8FF3A',eye:'#C8FF3A',glowEye:1},
    shark:{col:'#6A8294',belly:'#E8EEF2',len:2.4,r:.34,ry:.6,h:.1,low:1,head:.24,snl:2.2,snz:1.1,ear:'none',tail:'thick',tseg:.22,spikes:'#4A6272',eye:'#111'},
    shadow:{col:'#1A1026',len:1.8,r:.36,h:.55,head:.24,ear:'point',tail:'long',eye:'#C04AFF',glowEye:1,horns:'#3A2A5A'}
  });
  var FOTINT={cobra:{as:'viper',c:'#2E7A3A'},python:{as:'viper',c:'#8A6A2A',s:1.25},vulture:{as:'eagle',c:'#3A2A22',c2:'#D9A0A0'},bat:{as:'eagle',c:'#2A2438',c2:'#4A3A58',s:.85},phoenix:{as:'eagle',c:'#FF7A1A',c2:'#FFD24A',s:1.1},crab:{as:'scorpion',c:'#D04A30',s:.8},mantis:{as:'scorpion',c:'#5AA838',s:.9},kraken:{as:'spider',c:'#5A2A7A',s:1.3}};
  function creature(e){
    var TN=FOTINT[e.k]||{},k=TN.as||e.k,o=FOEQ[k],R,F={};
    if(e.human){var HH=hero(humanGear(e));R=HH.root;F={kind:'human',H:HH,root:R,head:HH.head,body:grp(R),mats:HH.mats};if(e.k==='h_champ')R.scale.setScalar(1.08);return F}
    if(o){var c={};for(var x in o)c[x]=o[x];F=quad(c);R=F.root;F.kind='quad'}
    else if(k==='scorpion'){R=grp();var sm=M(TN.c||'#9A5426',{r:.38,m:.15}),dk=M('#5A2A10',{r:.45}),B=grp(R,0,.32,0);F.body=B;
      for(var i=0;i<5;i++)sph(.3-i*.025,sm,0,i*.01,.42-i*.26,B,1.25,.55,.95);sph(.24,sm,0,.03,.66,B,1.1,.55,1);
      [-1,1].forEach(function(s){for(var l=0;l<4;l++){var lg=grp(B,s*.28,0,.4-l*.26);lg.rotation.y=s*(.35-l*.25);var up=limb(lg,.04,.42,dk);up.rotation.z=s*1.95;var kn=grp(up,0,-.42,0),lo=limb(kn,.032,.5,dk);lo.rotation.z=-s*1.55;F.legs=F.legs||[];F.legs.push(lg)}
        var cl=grp(B,s*.26,.02,.8);F['cl'+s]=cl;var ua=limb(cl,.07,.38,sm);ua.rotation.set(-1.75,s*.35,0);var fa=grp(ua,0,-.38,0),fo=limb(fa,.06,.3,sm);fo.rotation.x=.9;var pin=grp(fo,0,-.32,0);sph(.14,sm,0,0,0,pin,.9,1,1.5);var f1=cone(.05,.3,sm,s*.04,-.02,-.22,pin);f1.rotation.x=-Math.PI/2;var f2=cone(.04,.26,dk,-s*.06,.04,-.2,pin);f2.rotation.x=-Math.PI/2});
      var tl=grp(B,0,.05,-.82),sg=tl;F.tail=[];for(var t=0;t<6;t++){var g=grp(sg,0,0,t?-.22:0);sph(.14-t*.012,sm,0,0,0,g,1,.9,1.1);g.rotation.x=t?.58:.5;sg=g;F.tail.push(g)}
      var st=cone(.06,.3,M('#2A1408',{r:.3}),0,.05,.12,sg);st.rotation.x=2.4;var stg=sprite('#7CFC5A',.35,sg,.6);stg.position.set(0,.1,.25);
      F.eyes=[-1,1].map(function(s){return sph(.04,M('#FF3A1A',{e:'#FF3A1A',ei:1.6}),s*.08,.16,.86,B)});F.head=B;F.kind='scorp'}
    else if(k==='viper'){R=grp();var vm=M(TN.c||'#3E8A3A',{r:.45}),pts=[];for(var p=0;p<40;p++){var a2=p/40*Math.PI*4.2,rr=.85-p*.012;pts.push(new T.Vector3(Math.cos(a2)*rr,.12+p*.02,Math.sin(a2)*rr-.4))}
      pts.push(new T.Vector3(0,1.05,.2),new T.Vector3(0,1.25,.55));var cur=new T.CatmullRomCurve3(pts);var tube=mesh(new T.TubeGeometry(cur,140,.14,12,false),vm,0,0,0,R);
      F.body=grp(R);var H=grp(R,0,1.28,.6);F.head=H;sph(.2,vm,0,0,0,H,1.1,.6,1.5);sph(.14,M('#C8E89A'),0,-.06,.12,H,1,.4,1.3);
      F.eyes=[-1,1].map(function(s){var bw=box(.12,.03,.05,M('#0E2A0A'),s*.12,.13,.17,H);bw.rotation.z=s*.5;var fg=cone(.02,.09,M('#F4EFE2'),s*.06,-.1,.28,H);fg.rotation.x=Math.PI;return sph(.04,M('#FFD43B',{e:'#FFB300',ei:1.2}),s*.12,.06,.18,H)});var tg=box(.015,.01,.25,M('#D6313F'),0,-.05,.42,H);F.tongue=tg;F.kind='snake'}
    else if(k==='eagle'){R=grp();var em=M(TN.c||'#5A3A22',{r:.8}),wh=M(TN.c2||'#F4EFE2',{r:.8});var B2=grp(R,0,1.4,0);F.body=B2;sph(.4,em,0,0,0,B2,.9,1,1.3);var H2=grp(B2,0,.35,.35);F.head=H2;sph(.2,wh,0,0,0,H2);var bk=cone(.07,.25,M('#F2C14E',{r:.4}),0,-.05,.25,H2);bk.rotation.x=Math.PI/2;
      F.eyes=[-1,1].map(function(s){var bw=box(.1,.025,.04,M('#140A06'),s*.09,.12,.14,H2);bw.rotation.z=s*.5;return sph(.035,M('#FF7A1A',{e:'#FF4A00',ei:1.2}),s*.1,.06,.15,H2)});
      F.wings=[-1,1].map(function(s){var wg=grp(B2,s*.3,.1,0),sh=new T.Shape();sh.moveTo(0,.25);sh.lineTo(s*1.9,.4);sh.lineTo(s*2.2,0);sh.lineTo(s*1.7,-.25);sh.lineTo(s*1.2,-.1);sh.lineTo(s*.8,-.35);sh.lineTo(0,-.3);var m2=mesh(new T.ShapeGeometry(sh),M(TN.c||'#5A3A22',{r:.85,ds:true}),0,0,0,wg);m2.rotation.x=-Math.PI/2;return wg});
      [-1,1].forEach(function(s){limb(B2,.05,.35,M('#F2C14E'),s*.15,-.35,.1)});var tl2=mesh(new T.ConeGeometry(.3,.6,4),wh,0,-.05,-.6,B2);tl2.rotation.x=-Math.PI/2;tl2.scale.set(1,1,.3);F.kind='bird'}
    else if(k==='gorilla'){R=grp();var gm=M('#2A2A2E',{r:.9}),gf=M('#4A4448',{r:.8});var B3=grp(R,0,.9,0);F.body=B3;sph(.6,gm,0,.2,0,B3,1.1,1,.85);sph(.35,gf,0,.1,.38,B3,1,1.1,.5);var H3=grp(B3,0,.85,.15);F.head=H3;sph(.3,gm,0,0,0,H3);sph(.2,gf,0,-.05,.2,H3,1.2,.8,.7);
      F.eyes=[-1,1].map(function(s){var bw=box(.14,.04,.06,M('#140A06'),s*.1,.14,.27,H3);bw.rotation.z=s*.45;return sph(.04,M('#FF4A1A',{e:'#FF2A00',ei:1.4}),s*.1,.07,.26,H3)});sph(.11,M('#3A0A08'),0,-.13,.27,H3,1.2,.5,.5);[-1,1].forEach(function(s){var fg=cone(.025,.08,M('#F4EFE2'),s*.06,-.12,.31,H3);fg.rotation.x=Math.PI});
      F.arms=[-1,1].map(function(s){var a=limb(B3,.17,.95,gm,s*.62,.55,.05);a.rotation.z=s*.25;sph(.2,gf,0,-1,0,a);return a});[-1,1].forEach(function(s){limb(B3,.17,.55,gm,s*.3,-.3,0)});F.kind='ape'}
    else{ /* the giant spider, and anything new */ R=grp();var spm=M(TN.c||'#2A1E2E',{r:.6}),B4=grp(R,0,.75,0);F.body=B4;sph(.55,spm,0,.2,-.55,B4,1,.85,1.2);sph(.32,spm,0,0,.2,B4);var H4=grp(B4,0,.05,.48);F.head=H4;
      F.eyes=[];for(var ei=0;ei<6;ei++)F.eyes.push(sph(.035,M('#FF2A2A',{e:'#FF2A2A',ei:1.8}),(ei%3-1)*.07,.08+(ei>2?.06:0),0,H4));[-1,1].forEach(function(s){var fg=cone(.03,.15,M('#E8E2D0'),s*.06,-.12,.05,H4);fg.rotation.x=Math.PI});
      F.legs=[];[-1,1].forEach(function(s){for(var l2=0;l2<4;l2++){var lg2=grp(B4,s*.25,0,.3-l2*.2),up=limb(lg2,.045,.6,spm);up.rotation.set(0,0,s*2.1);var kn=grp(up,0,-.6,0),lo=limb(kn,.035,.75,spm);lo.rotation.z=-s*1.5;F.legs.push(lg2)}});F.kind='spider'}
    var sc=({scorpion:2.1,wolf:1.9,hyena:1.9,eagle:1.5,bull:1.55,lion:1.7,panther:1.8,viper:1.7,bear:1.6,crocodile:1.6,tiger:1.7,gorilla:1.4,rhino:1.4,elephant:1.25,dragon:1.6,spider:1.5,jackal:1.9,boar:1.7,komodo:1.6,leopard:1.8,hippo:1.4,polar:1.6,dire:1.7,mammoth:1.2,griffin:1.5,manticore:1.6,chimera:1.5,hydra:1.4,wyvern:1.5,basilisk:1.5,shark:1.5,shadow:1.7}[k]||1.5)*(TN.s||1)*(1+Math.min(.25,ENEMIES.indexOf(e)*.015));R.scale.setScalar(sc);
    F.root=R;F.mats=own(R);return F;
  }

  /* ---- the arena: sky, sand, walls with a crowd, torches and a few props that change with the battlefield ---- */
  var FIELD={
    sand:{sky:['#5FB4F0','#FCE3B0'],floor:'#E2B979',wall:'#B88A56',fog:'#F6D9A8',sun:'#FFF1CF',amb:.75,props:'dunes',fx:'dust'},
    oasis:{sky:['#58B8E8','#E9F4D8'],floor:'#E8C88A',wall:'#B8925A',fog:'#E0EED0',sun:'#FFF6D8',amb:.8,props:'palms',fx:'dust'},
    moon:{sky:['#0B1640','#3A4F8A'],floor:'#8A8FB0',wall:'#4A4F70',fog:'#1E2A55',sun:'#BFD0FF',amb:.45,props:'stars',fx:'stars',night:1},
    jungle:{sky:['#5FA8D8','#C8E8B8'],floor:'#6A8A4A',wall:'#5A6A3A',fog:'#9AC890',sun:'#FFF0C8',amb:.7,props:'trees',fx:'fireflies'},
    snow:{sky:['#9EC8F0','#F4F8FF'],floor:'#F4F8FF',wall:'#C8D8E8',fog:'#E8F0FF',sun:'#FFFFFF',amb:.9,props:'peaks',fx:'snow'},
    pyramid:{sky:['#F08A4A','#FCD8A0'],floor:'#E8B872',wall:'#C08A50',fog:'#F6C890',sun:'#FFD8A0',amb:.75,props:'pyramids',fx:'dust'},
    castle:{sky:['#6AA8E0','#E8F0F8'],floor:'#A89A8A',wall:'#8A8070',fog:'#D0D8E0',sun:'#FFF6E0',amb:.75,props:'towers',fx:'dust'},
    volcano:{sky:['#2A0A0A','#8A2A10'],floor:'#4A2A22',wall:'#3A1A16',fog:'#5A1A0A',sun:'#FF9A5A',amb:.5,props:'volcano',fx:'embers',night:1},
    crystal:{sky:['#1A0E3A','#5A3A9A'],floor:'#4A3A6A',wall:'#3A2A5A',fog:'#3A2A6A',sun:'#D8B8FF',amb:.55,props:'crystals',fx:'fireflies',night:1},
    sky:{sky:['#4AA0F0','#E8F6FF'],floor:'#9AC86A',wall:'#8AA870',fog:'#E8F4FF',sun:'#FFFFFF',amb:.85,props:'clouds',fx:'dust'},
    colosseum:{sky:['#E8904A','#FCE0B0'],floor:'#D8A870',wall:'#C8A080',fog:'#F0C8A0',sun:'#FFD8A8',amb:.7,props:'towers',fx:'embers'},
    falls:{sky:['#6ABCE8','#E8F8F0'],floor:'#7A9A6A',wall:'#6A8A7A',fog:'#C8E8E8',sun:'#FFFFFF',amb:.8,props:'trees',fx:'bubbles'},
    ship:{sky:['#4A9AD8','#D8F0FF'],floor:'#8A5A32',wall:'#6A4424',fog:'#C8E0F0',sun:'#FFF6E0',amb:.8,props:'clouds',fx:'dust'},
    coral:{sky:['#0A3A6A','#2A8AB0'],floor:'#C8B890',wall:'#2A6A8A',fog:'#1A5A8A',sun:'#9BE6FF',amb:.6,props:'crystals',fx:'bubbles',night:1},
    neon:{sky:['#0A0A2A','#3A0A5A'],floor:'#1A1A2E',wall:'#2A1A3E',fog:'#2A0A4A',sun:'#FF4AD8',amb:.5,props:'neon',fx:'fireflies',night:1},
    bloodmoon:{sky:['#2A0406','#9A2A1A'],floor:'#8A3A2A',wall:'#5A2018',fog:'#5A1410',sun:'#FF6A4A',amb:.5,props:'stars',fx:'embers',night:1},
    frozen:{sky:['#7AA8D8','#E8F4FF'],floor:'#D8ECFF',wall:'#A8C8E8',fog:'#D8E8FF',sun:'#E8F6FF',amb:.85,props:'peaks',fx:'snow'},
    ruins:{sky:['#8AA8C8','#E8E0D0'],floor:'#A89A7A',wall:'#7A7060',fog:'#C8C0B0',sun:'#FFF0D8',amb:.7,props:'towers',fx:'dust'},
    haunted:{sky:['#0A0A14','#2A3A3A'],floor:'#3A3A30',wall:'#2A2A26',fog:'#1A2A2A',sun:'#9AFFC8',amb:.4,props:'trees',fx:'fireflies',night:1},
    lunar:{sky:['#000006','#0A0A2A'],floor:'#9A9AA0',wall:'#6A6A70',fog:'#0A0A1A',sun:'#FFFFFF',amb:.55,props:'stars',fx:'stars',night:1}
  };

  Object.assign(FIELD,{
    savanna:{sky:['#F2994A','#FCE3B0'],floor:'#D8B070',wall:'#A8804A',fog:'#F6D0A0',sun:'#FFE2B0',amb:.8,props:'palms',fx:'dust'},
    bamboo:{sky:['#8AC8A8','#E8F4E0'],floor:'#7A9A5A',wall:'#5A7A4A',fog:'#C8E4C8',sun:'#FFF6D8',amb:.75,props:'trees',fx:'fireflies'},
    blossom:{sky:['#F0A8C8','#FFE8F0'],floor:'#D8B8B0',wall:'#B88A8A',fog:'#F8D8E0',sun:'#FFF0F0',amb:.85,props:'trees',fx:'snow'},
    cove:{sky:['#F07A4A','#FFD8A0'],floor:'#D8B880',wall:'#7A5A3A',fog:'#F6C890',sun:'#FFD0A0',amb:.75,props:'dunes',fx:'dust'},
    grave:{sky:['#1A1A2A','#4A4A60'],floor:'#4A4A44',wall:'#2A2A30',fog:'#3A3A4A',sun:'#C8D0FF',amb:.45,props:'stars',fx:'fireflies',night:1},
    camp:{sky:['#0A1030','#4A3A6A'],floor:'#C8A870',wall:'#6A4A2A',fog:'#2A2A4A',sun:'#FFD8A0',amb:.5,props:'stars',fx:'embers',night:1},
    souk:{sky:['#F0A050','#FCE0B0'],floor:'#C8A070',wall:'#A8683A',fog:'#F0C890',sun:'#FFD8A8',amb:.75,props:'towers',fx:'dust'},
    canyon:{sky:['#E87A4A','#FCD8A0'],floor:'#C8683A',wall:'#9A4A2A',fog:'#F0A070',sun:'#FFE0B0',amb:.75,props:'peaks',fx:'dust'},
    village:{sky:['#7AB8E0','#F0F4E8'],floor:'#A8A070',wall:'#8A7A60',fog:'#D8E0D0',sun:'#FFF6E0',amb:.8,props:'towers',fx:'dust'},
    fjord:{sky:['#0A2A4A','#4A8A8A'],floor:'#6A8A9A',wall:'#3A5A6A',fog:'#2A5A6A',sun:'#9AFFD8',amb:.55,props:'peaks',fx:'snow',night:1},
    shroom:{sky:['#1A0A3A','#4A2A7A'],floor:'#3A4A3A',wall:'#2A3A3A',fog:'#2A2A5A',sun:'#7AFFC8',amb:.55,props:'crystals',fx:'fireflies',night:1},
    library:{sky:['#2A1A0A','#6A4A2A'],floor:'#6A4A2A',wall:'#4A2A14',fog:'#4A3018',sun:'#FFD8A0',amb:.55,props:'towers',fx:'embers',night:1},
    storm:{sky:['#1A2230','#5A6A7A'],floor:'#8A8A80',wall:'#4A5058',fog:'#4A5868',sun:'#BFD8FF',amb:.5,props:'clouds',fx:'snow',night:1},
    glacier:{sky:['#6AA8D8','#D8F0FF'],floor:'#C8E4F8',wall:'#7AB0D8',fog:'#C8E4F4',sun:'#E8F8FF',amb:.85,props:'crystals',fx:'snow'},
    atlantis:{sky:['#052A5A','#1A7AA8'],floor:'#B8C8B0',wall:'#1A5A7A',fog:'#0F4A7A',sun:'#9BE6FF',amb:.6,props:'towers',fx:'bubbles',night:1},
    lavatemple:{sky:['#2A0A06','#9A3A10'],floor:'#4A2A22',wall:'#3A1810',fog:'#5A200A',sun:'#FF8A4A',amb:.5,props:'towers',fx:'embers',night:1},
    skytemple:{sky:['#4AA0F0','#F4F8FF'],floor:'#D8D8E0',wall:'#B8B8C8',fog:'#E8F0FF',sun:'#FFFFFF',amb:.9,props:'clouds',fx:'dust'},
    mars:{sky:['#8A3A1A','#E8986A'],floor:'#B8582E',wall:'#7A3418',fog:'#D88A5A',sun:'#FFD0A0',amb:.65,props:'peaks',fx:'dust'},
    retro:{sky:['#1A0A3A','#E84AB8'],floor:'#1A1030',wall:'#3A1A5A',fog:'#5A1A6A',sun:'#FF9A4A',amb:.55,props:'neon',fx:'fireflies',night:1},
    station:{sky:['#000010','#0A1A3A'],floor:'#8A929E',wall:'#4A525E',fog:'#0A1226',sun:'#BFD8FF',amb:.6,props:'stars',fx:'stars',night:1}
  });
  function world(scene,fk,show){
    var F=FIELD[fk]||FIELD.sand,W={F:F,anim:[]};
    var sky=new T.Mesh(new T.SphereGeometry(60,32,16),new T.ShaderMaterial({side:T.BackSide,depthWrite:false,fog:false,
      uniforms:{top:{value:new T.Color(F.sky[0])},mid:{value:new T.Color(F.sky[1])},bot:{value:new T.Color(F.fog)}},
      vertexShader:'varying vec3 vP;void main(){vP=position;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}',
      fragmentShader:'uniform vec3 top;uniform vec3 mid;uniform vec3 bot;varying vec3 vP;void main(){float h=normalize(vP).y;vec3 c=h>0.0?mix(mid,top,smoothstep(0.0,0.45,h)):mix(mid,bot,smoothstep(0.0,0.15,-h));gl_FragColor=vec4(c,1.0);}'}));scene.add(sky);
    scene.fog=new T.Fog(lin(F.fog),20,58);
    var hemi=new T.HemisphereLight(lin(F.sky[0]),lin(F.floor),F.amb*.85);scene.add(hemi);
    var sun=new T.DirectionalLight(lin(F.sun),F.night?1.1:1.75);sun.position.set(-6,12,8);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);var sc=sun.shadow.camera;sc.left=-8;sc.right=8;sc.top=8;sc.bottom=-8;sc.near=1;sc.far=40;sun.shadow.bias=-.0006;scene.add(sun);scene.add(sun.target);
    var rim=new T.DirectionalLight(F.night?F.sun:'#FFE2B0',F.night?.9:.6);rim.position.set(4,5,-10);scene.add(rim);
    if(F.night){var moon=sprite(F.sun,9,scene,.9);moon.position.set(12,16,-40);sprite('#FFFFFF',3.4,scene,1).position.set(12,16,-39.5)}else{var sn=sprite('#FFE9B0',7,scene,.55);sn.position.set(-16,20,-44)}
    /* sand floor with rings */
    var fl=canvasTex(512,512,function(x,w,h){x.fillStyle=F.floor;x.fillRect(0,0,w,h);x.fillStyle='rgba(60,30,10,.12)';x.fillRect(0,0,w,h);for(var i=0;i<5000;i++){var v=Math.random();x.fillStyle=v<.5?'rgba(0,0,0,'+(Math.random()*.07)+')':'rgba(255,255,255,'+(Math.random()*.09)+')';x.fillRect(Math.random()*w,Math.random()*h,2,2)}
      x.strokeStyle='rgba(0,0,0,.12)';x.lineWidth=5;[90,170,240].forEach(function(r){x.beginPath();x.arc(256,256,r,0,Math.PI*2);x.stroke()});x.lineWidth=2;for(var a=0;a<16;a++){x.beginPath();x.moveTo(256,256);x.lineTo(256+Math.cos(a/16*Math.PI*2)*250,256+Math.sin(a/16*Math.PI*2)*250);x.stroke()}});
    var floor=new T.Mesh(new T.CircleGeometry(16,72),new T.MeshStandardMaterial({map:fl,roughness:.95}));floor.rotation.x=-Math.PI/2;floor.receiveShadow=true;scene.add(floor);
    /* wall with arches, a crowd, banners and torches */
    var wt=canvasTex(512,128,function(x,w,h){x.fillStyle=F.wall;x.fillRect(0,0,w,h);x.fillStyle='rgba(0,0,0,.18)';x.fillRect(0,0,w,10);for(var i=0;i<8;i++){var cx=i*64+32;x.fillStyle='rgba(0,0,0,.55)';x.beginPath();x.moveTo(cx-20,h);x.lineTo(cx-20,54);x.arc(cx,54,20,Math.PI,0);x.lineTo(cx+20,h);x.fill();x.fillStyle='rgba(255,255,255,.12)';x.fillRect(cx+26,14,4,h-14)}},[6,1]);
    var wall=new T.Mesh(new T.CylinderGeometry(13,13,3.2,64,1,true),new T.MeshStandardMaterial({map:wt,side:T.DoubleSide,roughness:.9}));wall.position.y=1.6;wall.receiveShadow=true;scene.add(wall);
    var ring=new T.Mesh(new T.CylinderGeometry(13.6,13.2,.35,64,1,true),M(F.wall,{r:.8,ds:true}));ring.position.y=3.3;scene.add(ring);
    var crowd=new T.InstancedMesh(new T.BoxGeometry(.34,.46,.26),new T.MeshStandardMaterial({roughness:.8}),220),heads=new T.InstancedMesh(new T.SphereGeometry(.13,10,8),new T.MeshStandardMaterial({color:'#C98E5F',roughness:.7}),220),dm=new T.Object3D(),cols=['#D6336C','#2F7FD1','#2F9E6E','#F4CB4C','#8E44C9','#E8590C','#FFFFFF','#C0392B'],seats=[];
    for(var i=0;i<220;i++){var a=i/220*Math.PI*2+Math.random()*.02,row=i%3,r=13.4+row*.5;seats.push([Math.cos(a)*r,3.65+row*.38,Math.sin(a)*r,Math.random()*6]);crowd.setColorAt(i,new T.Color(cols[i%cols.length]))}
    scene.add(crowd);scene.add(heads);W.heads=heads;W.crowd=crowd;W.seats=seats;W.dm=dm;
    var torches=[];[[-4.6,-1],[4.6,-1],[-7,-6],[7,-6]].forEach(function(p){var g=grp(scene,p[0],0,p[1]);cyl(.08,.12,2.2,M('#3A2410',{r:.8}),0,1.1,0,g);cyl(.2,.12,.25,M('#2A2A2A',{m:.6,r:.4}),0,2.3,0,g);var fl1=sprite('#FF6A10',.9,g,.75);fl1.position.y=2.62;var fl2=sprite('#FFC060',.4,g,.8);fl2.position.y=2.55;var L=new T.PointLight('#FF9A4A',F.night?1.8:.6,9,2);L.position.y=2.6;g.add(L);torches.push([fl1,fl2,L,Math.random()*6])});W.torches=torches;
    var bans=[];for(var b=0;b<10;b++){var aa=b/10*Math.PI*2,bg=grp(scene,Math.cos(aa)*12.8,0,Math.sin(aa)*12.8);cyl(.04,.04,4.6,M('#5A3416'),0,2.3,0,bg);var bgm=new T.PlaneGeometry(.9,1.3,4,6),bn=mesh(bgm,M(b%2?'#C0392B':'#2F6FB0',{r:.8,ds:true}),.45,3.9,0,bg);bg.lookAt(0,0,0);bans.push([bn,bgm,bgm.attributes.position.array.slice(),b])}W.bans=bans;
    props(scene,F.props,W);
    particles(scene,F.fx,W);
    return W;
  }
  function props(scene,k,W){
    var far=function(n,fn){for(var i=0;i<n;i++){var a=-Math.PI/2+(i/(n-1)-.5)*2.4;fn(Math.cos(a)*(26+Math.random()*8),Math.sin(a)*(26+Math.random()*8),i)}};
    if(k==='dunes')far(7,function(x,z){var d=sph(6,M('#E8BE80',{r:1}),x,-3.6,z,scene,1.6,.75,1);d.castShadow=false});
    if(k==='pyramids')far(3,function(x,z,i){var p=cone(5+i,7+i,M('#E0B070',{r:.9}),x,3.5+i/2,z,scene,4);p.rotation.y=Math.PI/4});
    if(k==='volcano'){var v=cone(14,12,M('#3A1A16',{r:1}),0,5,-40,scene,24);var lava=sprite('#FF5A10',12,scene,.9);lava.position.set(0,11.5,-39);W.anim.push(function(t){lava.material.opacity=.7+Math.sin(t*3)*.2})}
    if(k==='palms'||k==='trees')far(9,function(x,z,i){var g=grp(scene,x,0,z),tm=M(k==='palms'?'#8A6A3A':'#4A3A2A',{r:.9});var tr=cyl(.3,.45,8,tm,0,4,0,g);tr.rotation.z=(i%2?.08:-.08);var lm=M(k==='palms'?'#3E8A3A':'#2E6A2E',{r:.8,ds:true});
      if(k==='palms')for(var l=0;l<6;l++){var lf=box(4,.08,1,lm,0,8,0,g);lf.rotation.set(0,l/6*Math.PI*2,-.4);lf.translateX(1.8)}else sph(3,lm,0,9,0,g,1,1.1,1)});
    if(k==='towers')far(5,function(x,z){var g=grp(scene,x,0,z),sm=M('#9A8A78',{r:.9});cyl(2,2.2,12,sm,0,6,0,g,10);cone(2.6,4,M('#8E1F2A',{r:.8}),0,14,0,g,10)});
    if(k==='peaks')far(5,function(x,z,i){var g=grp(scene,x,0,z);cone(8+i,14+i*2,M('#8A9AB0',{r:1}),0,6,0,g,6);cone(3.4,5,M('#FFFFFF',{r:.8}),0,12.5+i,0,g,6)});
    if(k==='crystals'||k==='neon'){var cs=[];far(8,function(x,z,i){var c=['#B66BFF','#5FD3EA','#FF4AD8','#7CFC5A'][i%4],m2=mesh(new T.OctahedronGeometry(1.6+Math.random()*1.4),M(c,{r:.1,m:.3,e:c,ei:.8}),x*.7,2.5,z*.7,scene);m2.scale.y=2.2;cs.push(m2)});W.anim.push(function(t){cs.forEach(function(c,i){c.rotation.y=t*.2+i})})}
    if(k==='clouds'){var cl=[];for(var i=0;i<8;i++){var g=grp(scene,(Math.random()-.5)*70,10+Math.random()*8,-30-Math.random()*15);for(var j=0;j<4;j++)sph(2+Math.random()*1.5,M('#FFFFFF',{r:1}),j*2-3,Math.random(),0,g).castShadow=false;cl.push(g)}W.anim.push(function(t,dt){cl.forEach(function(c){c.position.x+=dt*.6;if(c.position.x>40)c.position.x=-40})})}
  }
  function particles(scene,k,W){
    var n=k==='stars'?300:160,g=new T.BufferGeometry(),pos=new Float32Array(n*3),vel=[];
    for(var i=0;i<n;i++){var p=seed(i);pos.set(p,i*3);vel.push(Math.random())}
    function seed(i){if(k==='stars'){var a=Math.random()*Math.PI*2,e=Math.random()*1.2+.15;return [Math.cos(a)*50*Math.cos(e),50*Math.sin(e),Math.sin(a)*50*Math.cos(e)]}return [(Math.random()-.5)*22,Math.random()*(k==='snow'?10:6),(Math.random()-.5)*18-1]}
    g.setAttribute('position',new T.BufferAttribute(pos,3));
    var col={dust:'#FFF0C8',embers:'#FF8A2A',snow:'#FFFFFF',stars:'#FFFFFF',fireflies:'#C8FF7A',bubbles:'#BFF0FF'}[k]||'#FFFFFF';
    var m=new T.PointsMaterial({map:glowTex(),color:col,size:k==='stars'?.7:k==='snow'?.16:k==='dust'?.09:.18,transparent:true,opacity:k==='dust'?.5:.9,blending:T.AdditiveBlending,depthWrite:false,sizeAttenuation:true});
    if(k==='stars')m.fog=false;
    var pts=new T.Points(g,m);scene.add(pts);
    W.anim.push(function(t,dt){if(k==='stars'){m.opacity=.7+Math.sin(t*2)*.2;return}var a=g.attributes.position.array;for(var i=0;i<n;i++){var j=i*3,v=vel[i];
      if(k==='snow'){a[j+1]-=dt*(.6+v);a[j]+=Math.sin(t+i)*dt*.3;if(a[j+1]<0)a[j+1]=10}
      else if(k==='embers'||k==='bubbles'){a[j+1]+=dt*(.5+v*.8);a[j]+=Math.sin(t*2+i)*dt*.3;if(a[j+1]>7){a[j+1]=0}}
      else if(k==='fireflies'){a[j]+=Math.sin(t*.8+i)*dt*.4;a[j+1]+=Math.cos(t*.9+i*1.3)*dt*.3;a[j+2]+=Math.sin(t*.7+i*.7)*dt*.4}
      else{a[j]+=dt*(.25+v*.3);if(a[j]>11)a[j]=-11}}g.attributes.position.needsUpdate=true});
  }

  /* ---- a renderer on a host element ---- */
  function start(host,cls,alpha){
    stop();var r=new T.WebGLRenderer({antialias:true,alpha:!!alpha,powerPreference:'high-performance'});
    r.setPixelRatio(Math.min(window.devicePixelRatio||1,2));r.outputEncoding=T.sRGBEncoding;r.toneMapping=T.ACESFilmicToneMapping;r.toneMappingExposure=1.15;r.shadowMap.enabled=true;r.shadowMap.type=T.PCFSoftShadowMap;
    var cv=r.domElement;cv.className='g3c';host.insertBefore(cv,host.firstChild);host.classList.add(cls);
    var scene=new T.Scene(),cam=new T.PerspectiveCamera(50,1,.1,200);
    CUR={r:r,scene:scene,cam:cam,host:host,raf:0,t:0,last:0};
    return CUR;
  }
  function fit(C){var w=C.host.clientWidth,h=C.host.clientHeight;if(!w||!h)return;if(C.w!==w||C.h!==h){C.w=w;C.h=h;C.r.setPixelRatio(Math.max(1,Math.min(3,Math.max(window.devicePixelRatio||1,2),Math.sqrt(2.1e6/(w*h)))));C.r.setSize(w,h,false);C.cam.aspect=w/h;C.cam.updateProjectionMatrix()}}
  function loop(C,fn){function f(ts){if(CUR!==C)return;if(!document.body.contains(C.r.domElement)){stop();return}var dt=C.last?Math.min(.05,(ts-C.last)/1000):.016;C.last=ts;C.t+=dt;fit(C);fn(dt,C.t);C.r.render(C.scene,C.cam);C.raf=requestAnimationFrame(f)}C.raf=requestAnimationFrame(f)}
  var ease=function(x){return x<0?0:x>1?1:x*x*(3-2*x)};
  function pulse(t,a,b){return t<a?0:t>b?0:Math.sin((t-a)/(b-a)*Math.PI)}

  /* ---- the fight: you move freely around the arena; the creature chases, circles and attacks an area ----
     Every actor keeps x, z and a (the direction it faces: forward is (sin a, 0, cos a)). The fight state lives in
     AR_S.P and AR_S.E, so the shared fight code (rounds, K.O., HUD, rewards) works unchanged. */
  var FG=null,KEY={},PAD={},JOY=null,MOUSE=null;
  var REACH={stick:1.9,dagger:1.6,venom:1.6,sw_mishmal:1.6,sw_janbiya:1.6,spear:2.8,trident:2.7,mace:2.1,hammer:2.2,thunder:2.2,axe:2.2,staff:2.4,bow:10,phoenix:10,longbow:10,crossbow:10,boomerang:10,chakram:10,kris:1.6,flail:2.2,claymore:2.5};
  var FOEKIT={scorpion:['swipe','slam'],wolf:['swipe','slam'],hyena:['swipe','slam'],eagle:['swipe','slam'],bull:['swipe','charge'],lion:['swipe','slam'],panther:['swipe','slam'],
    viper:['swipe','slam'],bear:['swipe','slam'],crocodile:['swipe','charge'],tiger:['swipe','slam'],gorilla:['swipe','slam'],rhino:['swipe','charge'],elephant:['swipe','charge'],dragon:['swipe','breath','slam'],spider:['swipe','slam']};
  Object.assign(FOEKIT,{boar:['swipe','charge'],hippo:['swipe','charge'],mammoth:['swipe','charge'],komodo:['swipe','charge'],shark:['swipe','charge'],chimera:['swipe','breath','slam'],wyvern:['swipe','breath','slam'],hydra:['swipe','breath','slam'],basilisk:['swipe','breath'],phoenix:['swipe','breath'],manticore:['swipe','slam','charge']});
  var ARENA_R=10.6;
  function ang(a){while(a>Math.PI)a-=2*Math.PI;while(a<-Math.PI)a+=2*Math.PI;return a}
  function faceTo(x,z,tx,tz){return Math.atan2(tx-x,tz-z)}
  function dist(a,b){var dx=a.x-b.x,dz=a.z-b.z;return Math.sqrt(dx*dx+dz*dz)}
  function decal(col,geo){var m=new T.Mesh(geo,new T.MeshBasicMaterial({color:lin(col),transparent:true,opacity:0,depthWrite:false,side:T.DoubleSide,toneMapped:false}));m.rotation.x=-Math.PI/2;return m}
  function blob(p,r){var t=canvasTex(64,64,function(x){var g=x.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,'rgba(0,0,0,.55)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(0,0,64,64)});
    var m=new T.Mesh(new T.PlaneGeometry(r*2,r*2),new T.MeshBasicMaterial({map:t,transparent:true,depthWrite:false}));m.rotation.x=-Math.PI/2;m.position.y=.02;p.add(m);return m}
  /* the pose of a person (the champion or a human enemy) for a state, its time in that state and the clock */
  function poseHero(H,st,pt,t,o){
    var R=H.R,L=H.L,ch=H.chest,root=H.root,chg=st==='charge';if(chg){st='heavy';pt=Math.min(pt,300)}
      root.position.set(o.x,0,o.z);root.rotation.set(0,o.a+Math.PI,0);ch.rotation.set(0,0,0);ch.position.y=.04;H.hips.rotation.set(0,0,0);
      var br=Math.sin(t*2.2)*.025,run=o.run,cyc=t*11;
      var sx=1.05,sz=-.12,ex=.55,lx=1.0,lz=.48,lex=.6,wr=-2.0,legA=0;
      if(run){legA=Math.sin(cyc)*.75;sx=.9+Math.sin(cyc)*.25;lx=.9-Math.sin(cyc)*.35;ch.rotation.x=.16;ch.position.y=.04+Math.abs(Math.sin(cyc))*.04}
      if(st==='light'){var u=pt/(o.dur||300),w1=ease(u/.3),w2=ease((u-.3)/.35),cs=o.combo===1?-1:1;sx=1.05+1.25*w1-1.9*w2;sz=(-.12-.45*w1+.95*w2)*cs;ch.rotation.y=(-.35*w1+.75*w2)*cs;ex=.55-.3*w1+.1*w2;if(o.combo===2){sx=1.05+2*w1-2.8*w2;ch.rotation.x=.3*w2}}
      else if(st==='heavy'){var u2=pt/640,a1=ease(u2/.48),a2=ease((u2-.48)/.2);sx=1.05+1.85*a1-2.7*a2;ex=.55-.45*a1+.2*a2;lx=1.0+1.7*a1-2.3*a2;ch.rotation.x=-.22*a1+.45*a2;if(chg)ch.rotation.z=Math.sin(t*45)*.035*(o.pow||0)}
      else if(st==='special'){var u3=pt/1050;root.rotation.y=o.a+Math.PI+ease(u3/.85)*Math.PI*4;sx=1.55;sz=1.15;ex=.1;root.position.y=Math.sin(Math.min(1,u3)*Math.PI)*.35}
      else if(st==='roll'){var r1=Math.min(1,pt/420);H.hips.rotation.x=-r1*Math.PI*2;root.position.y=Math.sin(r1*Math.PI)*.15-.35*Math.sin(r1*Math.PI);sx=2.2;lx=2.2;ex=1.4;lex=1.4}
      else if(st==='block'){sx=1.5;sz=-.5;ex=1.15;lx=1.5;lz=.6;lex=1.15;wr=-.35}
      else if(st==='hurt'){var k3=Math.sin(Math.min(1,pt/(o.hd||380))*Math.PI);ch.rotation.x=-.4*k3}
      else if(st==='wind'){var tw=ease(o.tu||0);if(o.aim){sx=1.57;sz=.1;ex=.05;lx=1.57;lz=.35;lex=.05;wr=-1.57}else{sx=1.05+1.9*tw;ex=.55-.4*tw;lx=1.0+.9*tw;ch.rotation.y=-.45*tw;ch.rotation.x=-.15*tw}}
      else if(st==='swing'){var sw=ease((o.su||0)*2.2);sx=2.95-2.8*sw;ex=.15+.3*sw;ch.rotation.y=-.45+.9*sw;ch.rotation.x=.3*sw}
      else if(st==='thrust'){sx=1.6;ex=.05;lx=1.4;ch.rotation.x=.35;H.hips.rotation.x=.15}
      else if(st==='dash'){var ud=ease(Math.min(1,pt/170));sx=1.25+.35*ud;sz=.05;ex=.45-.4*ud;lx=1.3;lz=.3;ch.rotation.x=.22+.18*ud;H.hips.rotation.x=.12}
      else if(st==='down'){var kd=pt<680?ease(Math.min(1,pt/240)):1-ease((pt-680)/270);root.rotation.x=-1.4*kd;root.position.y=-.1*kd;sx=.4;lx=.4}
      else if(st==='dazed'){ch.rotation.x=.45;ch.rotation.z=Math.sin(t*3)*.12;sx=.3;lx=.3;ex=.2;lex=.2;wr=-1.2;H.hips.rotation.x=-.1}
      else if(st==='ko'){var k4=ease(pt/800);root.rotation.x=-1.35*k4;root.position.y=-.1*k4}
      R.sh.rotation.set(sx+br,0,sz);R.el.rotation.set(ex,0,0);L.sh.rotation.set(lx-br,0,lz);L.el.rotation.set(lex,0,0);H.wpn.rotation.x=wr;
      if(H.legL&&!H.mount){H.legL.hip.rotation.x=legA;H.legR.hip.rotation.x=-legA;H.legL.kn.rotation.x=run?-Math.max(0,Math.sin(cyc+1.2))*1.2:0;H.legR.kn.rotation.x=run?-Math.max(0,Math.sin(cyc+1.2+Math.PI))*1.2:0;var st3=st==='block'||st==='wind'?.25:0;if(!run){H.legL.hip.rotation.set(st3*.6,0,-.06);H.legR.hip.rotation.set(-st3,0,.06);H.legL.kn.rotation.x=-st3;H.legR.kn.rotation.x=-st3*.5}}
    H.head.rotation.set(Math.sin(t*1.3)*.03,Math.sin(t*.7)*.05,0);
  }
  function arena(stage,q,e){
    var C=start(stage,'a3d',false),S3=C.scene,A0=AR_S;
    var fb1=document.querySelector('.fside.me .fbars'),fb2=document.querySelector('.fside.them .fbars');
    if(fb1&&!document.getElementById('fstP'))fb1.insertAdjacentHTML('beforeend','<div class="g3st" id="fstP" title="Stamina: rolls and blocks use it"><i></i></div>');
    if(fb2&&!document.getElementById('fpoE'))fb2.insertAdjacentHTML('beforeend','<div class="g3po" id="fpoE" title="Poise: break it to stagger the enemy"><i></i></div>');
    var W=world(S3,q.field&&q.field.k||'sand');
    var H=hero(q);S3.add(H.root);var hb=blob(S3,.7);
    var F=creature(e);S3.add(F.root);var fsize=new T.Box3().setFromObject(F.root),fdep=Math.max(fsize.max.x-fsize.min.x,fsize.max.z-fsize.min.z);
    var FR=Math.max(.7,Math.min(1.7,fdep*.32)),fbl=blob(S3,FR*1.3);
    var kit=e.kit||FOEKIT[e.k]||['swipe','slam'],reachE=e.human?(REACH[humanGear(e).weapon.k]||2)+.4:FR+1.3,tier=ENEMIES.indexOf(e),spdE=(['panther','tiger','lion','wolf','hyena'].indexOf(e.k)>=0?2.9:2.2)+tier*.06;
    var wk=q.weapon&&q.weapon.k||'stick',reachP=REACH[wk]||2.05,ranged=reachP>5;
    /* telegraphs on the ground: a cone, a circle and a lane, each with a fill that grows during the wind-up */
    var tcone=grp(S3),tconeO=decal('#FF3A1A',new T.RingGeometry(.2,1,32,1,-Math.PI/2-.95,1.9)),tconeF=decal('#FF6A2A',new T.CircleGeometry(1,32,-Math.PI/2-.95,1.9));tcone.add(tconeO);tcone.add(tconeF);
    var tcirc=grp(S3),tcircO=decal('#FF1A00',new T.RingGeometry(.92,1,40)),tcircF=decal('#FF4A1A',new T.CircleGeometry(1,40));tcirc.add(tcircO);tcirc.add(tcircF);
    var tlane=grp(S3),tlO=decal('#FF3A1A',new T.PlaneGeometry(1,1)),tlF=decal('#FF6A2A',new T.PlaneGeometry(1,1));tlO.position.z=.5;tlF.position.z=.5;tlane.add(tlO);tlane.add(tlF);
    [tcone,tcirc,tlane].forEach(function(g){g.position.y=.035;g.visible=false});
    var ring=decal('#FF3A1A',new T.RingGeometry(.92,1,48));S3.add(ring);
    var bub=sph(.95,M('#6FA8FF',{op:.28,add:1,r:.2}),0,1.2,-.5,H.root);bub.castShadow=false;bub.visible=false;
    var grd=sph(1.6,M('#7FB2FF',{op:.3,add:1,r:.2}),0,1,1.2,F.root,1,1,.35);grd.castShadow=false;grd.visible=false;
    var stars=[0,1,2].map(function(){var s=sprite('#FFE066',.35,S3,1);s.visible=false;return s});
    /* the weapon trail and the swing arcs */
    var TN=16,tp=new Float32Array(TN*2*3),tg=new T.BufferGeometry();tg.setAttribute('position',new T.BufferAttribute(tp,3));var idx=[];for(var i=0;i<TN-1;i++){var a=i*2;idx.push(a,a+1,a+2,a+1,a+3,a+2)}tg.setIndex(idx);
    var tcol={fire:'#FF8A3A',poison:'#7CFC5A',ice:'#9BE6FF',gold:'#FFD94A',holy:'#FFF3B0'}[(q.weapon&&q.weapon.fx)||'']||'#FFFFFF';
    var trail=new T.Mesh(tg,new T.MeshBasicMaterial({color:lin(tcol),transparent:true,opacity:.6,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide}));trail.frustumCulled=false;S3.add(trail);
    var hist=[],v1=new T.Vector3(),v2=new T.Vector3(),arcs=[],puffs=[],arrows=[];
    function arc(x,z,a,r,col,big){var m=new T.Mesh(new T.RingGeometry(r*.72,r,28,1,-Math.PI/2-1.1,2.2),new T.MeshBasicMaterial({color:lin(col),transparent:true,opacity:.85,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide}));
      var g=grp(S3,x,big?.9:1.15,z);g.rotation.y=a;m.rotation.x=-Math.PI/2+(big?.0:.35);g.add(m);arcs.push([g,m,0])}
    function puff(x,z,s){var p=sprite(W.F.night?'#9A8A7A':'#E8D2A8',s||.6,S3,.55);p.position.set(x,.2,z);puffs.push([p,0,(Math.random()-.5)*.6,(Math.random()-.5)*.6])}
    /* hit sparks */
    var SP=70,sg=new T.BufferGeometry(),sp=new Float32Array(SP*3),sv=[];for(var k=0;k<SP;k++){sv.push({v:new T.Vector3(),life:0});sp[k*3+1]=-50}sg.setAttribute('position',new T.BufferAttribute(sp,3));
    var spm=new T.PointsMaterial({map:glowTex(),color:lin('#FFE9A8'),size:.24,transparent:true,blending:T.AdditiveBlending,depthWrite:false});var sparks=new T.Points(sg,spm);sparks.frustumCulled=false;S3.add(sparks);
    function burst(pos,n,col){spm.color.copy(lin(col||'#FFE9A8'));for(var i=0,c=0;i<SP&&c<n;i++){var s=sv[i];if(s.life>0)continue;s.life=.45+Math.random()*.3;s.v.set((Math.random()-.5)*6,Math.random()*5+1,(Math.random()-.5)*6);sp[i*3]=pos.x;sp[i*3+1]=pos.y;sp[i*3+2]=pos.z;c++}}
    var foeW=document.getElementById('foeW'),meW=document.getElementById('meW'),bb=new T.Box3(),corners=[0,0,0,0,0,0,0,0].map(function(){return new T.Vector3()}),pv=new T.Vector3();
    function place(el,obj){if(!el||!C.w)return;bb.setFromObject(obj);var mn=bb.min,mx=bb.max,i=0;[mn.x,mx.x].forEach(function(x){[mn.y,mx.y].forEach(function(y){[mn.z,mx.z].forEach(function(z){corners[i++].set(x,y,z)})})});
      var l=1e9,t=1e9,r=-1e9,b=-1e9;corners.forEach(function(c){c.project(C.cam);var sx=(c.x+1)/2*C.w,sy=(1-c.y)/2*C.h;l=Math.min(l,sx);r=Math.max(r,sx);t=Math.min(t,sy);b=Math.max(b,sy)});
      el.style.left=Math.round(l)+'px';el.style.top=Math.round(t)+'px';el.style.width=Math.max(10,Math.round(r-l))+'px';el.style.height=Math.max(10,Math.round(b-t))+'px'}
    function pop(x,y,z,txt,cls){pv.set(x,y,z).project(C.cam);arPop(txt,cls,(pv.x+1)/2*C.w+(Math.random()*30-15),(1-pv.y)/2*C.h)}
    /* on-screen controls: a joystick (drag on the left half) and the action buttons */
    var pad=document.createElement('div');pad.className='g3pad';pad.innerHTML='<div class="joy" id="g3joy"><i></i></div><button type="button" class="g3fs" data-g3="full" aria-label="Full screen">⛶</button><div class="g3b">'+
      [['roll','⟲','Roll'],['block','🛡','Block'],['heavy','💥','Heavy','Heavy, hold to charge'],['special','★','Special'],['light','⚔','Attack']].map(function(b){return '<button type="button" data-g3="'+b[0]+'" class="g3k k-'+b[0]+'" aria-label="'+(b[3]||b[2])+'"><span>'+b[1]+'</span><small>'+b[2]+'</small></button>'}).join('')+'</div>'+
      '<p class="g3hint">Move: WASD / arrows or hold the mouse · J attack · hold K or right-click to charge a heavy · L special · Space roll · Shift block · attack after a roll to dash · break the yellow bar, then heavy for a critical</p>';
    stage.appendChild(pad);
    var cam=C.cam,camPos=new T.Vector3(0,3,9),camLook=new T.Vector3(0,1,0),ray=new T.Raycaster(),ndc=new T.Vector2(),ground=new T.Plane(new T.Vector3(0,1,0),0),gp=new T.Vector3();
    function groundAt(cx,cy){var r=C.r.domElement.getBoundingClientRect();ndc.set((cx-r.left)/r.width*2-1,-((cy-r.top)/r.height)*2+1);ray.setFromCamera(ndc,cam);return ray.ray.intersectPlane(ground,gp)?gp.clone():null}
    FG={C:C,H:H,F:F,shake:0,flashE:0,flashP:0,burst:burst,pop:pop,arc:arc,arrows:arrows,groundAt:groundAt,stb:document.getElementById('fstP'),pob:document.getElementById('fpoE'),reachP:reachP,ranged:ranged,reachE:reachE,FR:FR,kit:kit,spdE:spdE,tier:tier,e:e,q:q};
    var lastRound=-1;if(A0)A0.g3=1;
    loop(C,function(dt,t){
      var A=AR_S;if(!A)return;var P=A.P||{},E=A.E||{};
      if(P.x==null||A.round!==lastRound)resetPos(A);lastRound=A.round;P=A.P;E=A.E;
      var pt=P.t||0,et=E.t||0;
      /* the camera: behind the champion, turned so the creature stays in view, a little to the right */
      var portrait=C.h>C.w,dx=P.x-E.x,dz=P.z-E.z,dl=Math.sqrt(dx*dx+dz*dz)||1,ux=dx/dl,uz=dz/dl,back=portrait?5.9:5.2,side=portrait?1.1:2.1;
      var want=new T.Vector3(P.x+ux*back-uz*side,portrait?3.4:2.7,P.z+uz*back+ux*side),lk=new T.Vector3(P.x+(E.x-P.x)*.55,1.05,P.z+(E.z-P.z)*.55);
      var kk=1-Math.exp(-dt*5);camPos.lerp(want,kk);camLook.lerp(lk,kk);
      cam.fov=portrait?66:55;cam.updateProjectionMatrix();FG.shake=Math.max(0,FG.shake-dt*2.6);var sh=FG.shake*FG.shake*.25;
      cam.position.set(camPos.x+(Math.random()-.5)*sh,camPos.y+(Math.random()-.5)*sh,camPos.z+(Math.random()-.5)*sh);cam.lookAt(camLook);
      /* the champion */
      var run=P.st==='run'||P.st==='block'&&P.mv||P.st==='dash'&&pt<200;poseHero(H,P.st,pt,t,{run:run,combo:P.combo,dur:P.dur,a:P.a||0,x:P.x,z:P.z,hd:P.hd,pow:P.st==='charge'?cPow(pt):0});
      bub.visible=P.st==='block';if(bub.visible)bub.material.opacity=.22+Math.sin(t*8)*.06;
      if(H.cape){var ca=H.cape.geometry.attributes.position.array,cb=H.capeBase;for(var c=0;c<ca.length;c+=3){var yy=cb[c+1],d=(.52-yy);ca[c+2]=cb[c+2]+d*(.18+Math.sin(t*3+yy*4+cb[c]*3)*.06+(run||P.st!=='idle'?.35:0))}H.cape.geometry.attributes.position.needsUpdate=true}
      if(H.mount){var Mn=H.mount;if(Mn.legs)Mn.legs.forEach(function(l,i){l.rotation.x=run||P.st==='roll'?Math.sin(t*12+i*1.6)*.7:Math.sin(t*1.5+i)*.03});if(Mn.tail)Mn.tail.forEach(function(s,i){s.rotation.y=Math.sin(t*2+i*.5)*.12});if(Mn.wings)Mn.wings.forEach(function(w,i){w.rotation.z=(i?-1:1)*Math.sin(t*(run?8:4))*.4});if(Mn.carpet){var pa=Mn.cg.attributes.position.array,pb=Mn.base;for(var j=0;j<pa.length;j+=3)pa[j+2]=pb[j+2]+Math.sin(t*3+pb[j+1]*2)*.06;Mn.cg.attributes.position.needsUpdate=true}}
      FG.flashP=Math.max(0,FG.flashP-dt*4);if(P.st==='charge'){var cw=cPow(pt);flash(H.mats,'#FFC94A',.12+.4*cw*(.75+.25*Math.sin(t*22)));if(cw>=1&&Math.random()<dt*14){H.tip.getWorldPosition(v1);burst(v1,3,'#FFE08A')}}else flash(H.mats,'#FF2A1A',FG.flashP*.9);
      hb.position.set(P.x,.02,P.z);
      if((run&&Math.random()<dt*9)||(P.st==='roll'&&Math.random()<dt*25))puff(P.x,P.z,.5);
      /* the creature */
      var fr=F.root,body=F.body||fr,tele=E.st==='tele',atk=E.atk||'swipe';
      fr.position.set(E.x,0,E.z);fr.rotation.set(0,E.a||0,0);body.rotation.set(0,0,0);body.scale.set(1,1+Math.sin(t*2)*.02,1);
      var mv=E.mv||0,wc=t*(8+mv*2);
      if(tele){var tu=Math.min(1,et/(E.len||800));body.rotation.x=(atk==='slam'?.18:-.14)*ease(tu);if(atk==='slam')fr.position.y=-.12*ease(tu);fr.position.x+=Math.sin(et/22)*.03*tu;flash(F.mats,atk==='slam'||atk==='breath'?'#FF1A00':'#FF5A10',(.12+.3*tu)*(.6+.4*Math.sin(et/40)))}
      if(E.st==='strike'){var su=Math.min(1,et/(E.slen||300));if(atk==='slam'){fr.position.y=Math.sin(su*Math.PI)*1.4}else if(atk==='swipe'){body.rotation.x=.25*Math.sin(su*Math.PI)}}
      if(E.st==='hurt'){body.rotation.x=-.15*Math.sin(Math.min(1,et/360)*Math.PI)}
      if(E.st==='stagger'&&F.kind!=='human'){var sg2=Math.min(1,et/300);body.rotation.x=.3*sg2;fr.position.y=-.18*sg2}
      if(E.st==='roar'&&F.kind!=='human'){body.rotation.x=-.35*Math.sin(Math.min(1,et/800)*Math.PI)}
      if(E.st==='open'||E.st==='stagger'){fr.rotation.z=Math.sin(t*5)*.1;var hp=new T.Vector3();(F.head||fr).getWorldPosition(hp);stars.forEach(function(s,i){s.visible=true;var a2=t*3+i*2.1;s.position.set(hp.x+Math.cos(a2)*.6,hp.y+.55+Math.sin(t*6+i)*.05,hp.z+Math.sin(a2)*.6)})}else stars.forEach(function(s){s.visible=false});
      grd.visible=E.st==='guard';if(grd.visible)grd.material.opacity=.25+Math.sin(t*6)*.08;
      if(E.st==='ko'){var ku=ease(et/900);fr.rotation.z=1.5*ku;fr.position.y=-.2*ku}
      if(!tele){FG.flashE=Math.max(0,FG.flashE-dt*5);if(FG.flashE>.04)flash(F.mats,'#FFFFFF',FG.flashE);else if(E.st==='roar')flash(F.mats,'#FF2A00',.45*Math.sin(Math.min(1,et/800)*Math.PI));else flash(F.mats,'#FF2A00',E.rage?.12+.06*Math.sin(t*6):0)}
      if(F.tail)F.tail.forEach(function(s,i){if(F.kind==='quad'||!F.kind)s.rotation.y=Math.sin(t*2.2+i*.6)*.18;else s.rotation.x=(i?.58:.5)+Math.sin(t*2+i)*.05+(tele?.22*Math.min(1,et/(E.len||800)):0)+(E.st==='strike'?.3:0)});
      if(F.legs)F.legs.forEach(function(l,i){l.rotation.x=mv>.2||E.st==='strike'&&atk==='charge'?Math.sin(wc+i*1.6)*.7:Math.sin(t*1.2+i)*.04});
      if(F.wings)F.wings.forEach(function(w,i){w.rotation.z=(i?-1:1)*(Math.sin(t*(tele||mv>.2?9:3))*.55+.45)});
      if(F.arms)F.arms.forEach(function(a3,i){a3.rotation.x=tele?-2.4*Math.min(1,et/(E.len||800)):E.st==='strike'?-.2:mv>.2?Math.sin(wc+i*Math.PI)*.6:Math.sin(t*1.5+i)*.08});
      if(F.head&&F.kind!=='snake'&&F.kind!=='scorp')F.head.rotation.y=Math.sin(t*.9)*.1;
      if(F.kind==='snake'){F.head.position.y=1.28+Math.sin(t*2)*.05;if(F.tongue)F.tongue.scale.z=Math.sin(t*9)>.3?1:.2}
      if(F.trunk)F.trunk.rotation.x=Math.sin(t*1.4)*.25-(tele?.9*Math.min(1,et/(E.len||800)):0);
      ['cl1','cl-1'].forEach(function(kk2,i){if(F[kk2])F[kk2].rotation.y=(i?1:-1)*(Math.sin(t*2)*.1+(tele?.4:0))});
      if(F.kind==='human'){var hs=E.st==='idle'?(mv>.2?'run':'idle'):E.st==='tele'?'wind':E.st==='strike'?(atk==='charge'?'thrust':'swing'):E.st==='guard'?'block':E.st==='open'?'hurt':E.st==='stagger'?'dazed':E.st==='roar'?'wind':E.st;
        poseHero(F.H,hs,et,t,{run:hs==='run',a:E.a||0,x:E.x,z:E.z,tu:tele?Math.min(1,et/(E.len||800)):E.st==='roar'?1:0,su:E.st==='strike'?Math.min(1,et/(E.slen||300)):0,aim:atk==='arrow'});
        if(E.st==='strike'&&atk==='slam')fr.position.y=Math.sin(Math.min(1,et/(E.slen||420))*Math.PI)*1.2;if(E.st==='ko'){fr.rotation.x=-1.35*ease(et/800)}}
      fbl.position.set(E.x,.02,E.z);ring.position.set(E.x,.03,E.z);ring.scale.setScalar(FR*1.25);ring.material.opacity=E.st==='ko'?0:.32+Math.sin(t*4)*.08;
      if(mv>.5&&Math.random()<dt*6)puff(E.x,E.z,.9);
      /* the telegraphs */
      [tcone,tcirc,tlane].forEach(function(g){g.visible=false});
      if(tele){var tu2=Math.min(1,et/(E.len||800)),pulse2=.45+Math.sin(et/60)*.15;
        if(atk==='swipe'||atk==='breath'){var rr=atk==='breath'?6.5:reachE+.4;tcone.visible=true;tcone.position.set(E.x,.035,E.z);tcone.rotation.y=E.a;tcone.scale.set(rr,1,rr);tconeO.material.opacity=pulse2;tconeF.scale.setScalar(tu2);tconeF.material.opacity=.35}
        else if(atk==='burst'){tcirc.visible=true;tcirc.position.set(E.x,.035,E.z);tcirc.scale.setScalar(2.9);tcircO.material.opacity=pulse2+.25;tcircF.scale.setScalar(tu2);tcircF.material.opacity=.4}
        else if(atk==='arrow'){tlane.visible=true;tlane.position.set(E.x,.035,E.z);tlane.rotation.y=E.a;tlO.scale.set(.9,11,1);tlO.position.z=5.5;tlF.scale.set(.9,11*tu2,1);tlF.position.z=5.5*tu2;tlO.material.opacity=pulse2*.7;tlF.material.opacity=.4}
        else if(atk==='slam'){tcirc.visible=true;tcirc.position.set(E.tx,.035,E.tz);tcirc.scale.setScalar(1.9);tcircO.material.opacity=pulse2+.2;tcircF.scale.setScalar(tu2);tcircF.material.opacity=.38}
        else if(atk==='charge'){tlane.visible=true;tlane.position.set(E.x,.035,E.z);tlane.rotation.y=E.a;tlO.scale.set(FR*2,7.5,1);tlO.position.z=3.75;tlF.scale.set(FR*2,7.5*tu2,1);tlF.position.z=3.75*tu2;tlO.material.opacity=pulse2*.6;tlF.material.opacity=.35}}
      if(E.st==='strike'&&atk==='breath'&&Math.random()<.7){var fs=sprite(['#FF7A1A','#FFB34A','#FF3A1A'][Math.floor(Math.random()*3)],.9,S3,.9);var fd=Math.random()*6;fs.position.set(E.x+Math.sin(E.a)*fd+(Math.random()-.5)*fd*.5,1+Math.random()*.6,E.z+Math.cos(E.a)*fd+(Math.random()-.5)*fd*.5);puffs.push([fs,0,0,0,1])}
      /* effects */
      var a4=sg.attributes.position.array,alive=0;for(var s=0;s<SP;s++){var p=sv[s];if(p.life<=0){a4[s*3+1]=-50;continue}p.life-=dt;p.v.y-=9*dt;a4[s*3]+=p.v.x*dt;a4[s*3+1]+=p.v.y*dt;a4[s*3+2]+=p.v.z*dt;alive++}sg.attributes.position.needsUpdate=true;spm.opacity=alive?1:0;
      var swing=P.st==='light'||P.st==='heavy'||P.st==='special';H.tip.getWorldPosition(v1);H.wpn.getWorldPosition(v2);v2.lerp(v1,.35);
      hist.unshift([v1.x,v1.y,v1.z,v2.x,v2.y,v2.z]);if(hist.length>TN)hist.pop();
      for(var h2=0;h2<TN;h2++){var e2=swing?hist[Math.min(h2,hist.length-1)]:hist[0],o2=h2*6;for(var q2=0;q2<6;q2++)tp[o2+q2]=e2[q2]}tg.attributes.position.needsUpdate=true;trail.material.opacity=swing?.65:0;
      for(var ai=arcs.length-1;ai>=0;ai--){var ar=arcs[ai];ar[2]+=dt;ar[1].material.opacity=Math.max(0,.85-ar[2]*4.5);ar[0].scale.setScalar(1+ar[2]*1.6);if(ar[2]>.22){S3.remove(ar[0]);ar[1].geometry.dispose();ar[1].material.dispose();arcs.splice(ai,1)}}
      for(var pi=puffs.length-1;pi>=0;pi--){var pf=puffs[pi];pf[1]+=dt;pf[0].position.x+=pf[2]*dt;pf[0].position.z+=pf[3]*dt;pf[0].position.y+=dt*(pf[4]?1.5:.5);pf[0].scale.setScalar((pf[4]?.9:.5)+pf[1]*1.5);pf[0].material.opacity=Math.max(0,(pf[4]?.9:.45)-pf[1]*(pf[4]?1.6:.9));if(pf[1]>(pf[4]?.55:.6)){S3.remove(pf[0]);pf[0].material.dispose();puffs.splice(pi,1)}}
      for(var ri=arrows.length-1;ri>=0;ri--){var aw=arrows[ri];aw.t+=dt;var k5=Math.min(1,aw.t/aw.d);aw.m.position.set(aw.x0+(aw.x1-aw.x0)*k5,1.25,aw.z0+(aw.z1-aw.z0)*k5);if(k5>=1){S3.remove(aw.m);arrows.splice(ri,1)}}
      W.anim.forEach(function(f){f(t,dt)});
      var cr=W.crowd,dm=W.dm;W.seats.forEach(function(sd,i){dm.position.set(sd[0],sd[1]+Math.max(0,Math.sin(t*(4+sd[3]%2)+sd[3]))*.12*(A.combo>=3?2.2:1),sd[2]);dm.lookAt(0,sd[1],0);dm.updateMatrix();cr.setMatrixAt(i,dm.matrix);dm.position.y+=.36;dm.updateMatrix();W.heads.setMatrixAt(i,dm.matrix)});cr.instanceMatrix.needsUpdate=true;W.heads.instanceMatrix.needsUpdate=true;
      W.torches.forEach(function(tc){var f=.85+Math.sin(t*13+tc[3])*.08+Math.sin(t*7.3+tc[3])*.07;tc[0].scale.setScalar(.9*f);tc[2].intensity=(W.F.night?1.8:.6)*f});
      W.bans.forEach(function(bn){var pa=bn[1].attributes.position.array,pb=bn[2];for(var j=0;j<pa.length;j+=3)pa[j+2]=pb[j+2]+Math.sin(t*3+pb[j]*4+bn[3])*.08*(pb[j]+.45);bn[1].attributes.position.needsUpdate=true});
      place(foeW,F.root);place(meW,H.chest);
      var jy=document.getElementById('g3joy');if(jy){jy.classList.toggle('on',!!JOY);if(JOY){jy.style.left=JOY.bx+'px';jy.style.top=JOY.by+'px';jy.firstChild.style.transform='translate('+(JOY.dx*36)+'px,'+(JOY.dy*36)+'px)'}}
      var spb=pad.querySelector('.k-special');if(spb)spb.classList.toggle('ready',A.sp>=100);
    });
  }
  function resetPos(A){A.P.x=0;A.P.z=4.2;A.P.a=Math.PI;A.P.combo=0;A.P.st=A.P.st||'idle';A.P.stam=100;A.P.sT=999;A.E.pm=50+Math.min(FG?FG.tier:0,30)*3;A.E.poise=A.E.pm;A.E.pT=0;A.E.rage=0;A.hHeld=false;A.E.x=0;A.E.z=-3.2;A.E.a=0;A.E.mv=0;A.E.wait=1300;if(FG){FG.ai=0}}
  /* ---- the rules of the 3D fight, run by the shared fight loop (dt in milliseconds) ---- */
  function moveInput(){
    var x=0,y=0;if(KEY.w||KEY.ArrowUp)y+=1;if(KEY.s||KEY.ArrowDown)y-=1;if(KEY.a||KEY.ArrowLeft)x-=1;if(KEY.d||KEY.ArrowRight)x+=1;
    if(JOY){x+=JOY.dx;y-=JOY.dy}
    var c=FG.C.cam,f=new T.Vector3();c.getWorldDirection(f);f.y=0;f.normalize();var r=new T.Vector3(-f.z,0,f.x),v=new T.Vector3();
    if(x||y){v.addScaledVector(f,y).addScaledVector(r,x)}
    if(MOUSE&&MOUSE.held&&MOUSE.p){var P=AR_S.P,dx=MOUSE.p.x-P.x,dz=MOUSE.p.z-P.z,dl=Math.sqrt(dx*dx+dz*dz);if(dl>.4)v.set(dx/dl,0,dz/dl)}
    var l=v.length();if(l>1)v.multiplyScalar(1/l);return v;
  }
  function pSet(st,extra){var P=AR_S.P;P.st=st;P.t=0;P.hit={};P.hd=0;if(extra)for(var k in extra)P[k]=extra[k];var mw=document.getElementById('meW');if(mw)mw.setAttribute('data-s',st)}
  function eSet(st,extra){var E=AR_S.E;E.st=st;E.t=0;E.hl=0;if(st==='tele')E.feint=0;if(extra)for(var k in extra)E[k]=extra[k];var fw=document.getElementById('foeW');if(fw)fw.setAttribute('data-s',st)}
  function faceFoe(range){var A=AR_S,P=A.P,E=A.E,d=dist(P,E);P.lunge=0;if(d<range&&E.st!=='ko'){P.a=faceTo(P.x,P.z,E.x,E.z);if(!FG.ranged)P.lunge=Math.min(2.6,Math.max(0,d-(FG.reachP*.7+FG.FR*.55)))}}
  function cPow(t){return Math.max(0,Math.min(1,(t-300)/600))}
  function hitAt(P){return P.st==='light'?[130,130,150,250][P.combo||0]:P.st==='heavy'?380:P.st==='dash'?170:1e9}
  function spend(n){var P=AR_S.P;P.stam=Math.max(0,(P.stam==null?100:P.stam)-n);P.sT=0}
  /* a key or button: attacks queue up while busy; a roll cancels an attack once its blow has landed */
  function act(k,fromBuf){
    if(k==='full'){var fs=document.querySelector('.fight');try{if(document.fullscreenElement)document.exitFullscreen();else if(fs&&fs.requestFullscreen)fs.requestFullscreen().catch(function(){})}catch(err){}return}
    var A=AR_S;if(!A||!A.live||!FG)return;var P=A.P;
    if(k==='heavy'&&!fromBuf)A.hHeld=true;
    if(P.st==='ko'||P.st==='hurt')return;
    if(P.st==='down'&&!(k==='roll'&&P.t>350&&P.t<820))return;
    if(k==='block'){if(!A.hold)P.blockT=Date.now();A.hold=true;return}
    var busy=P.st==='light'||P.st==='heavy'||P.st==='special'||P.st==='roll'||P.st==='dash'||P.st==='charge';
    var cancel=k==='roll'&&(P.st==='charge'||(P.st==='light'||P.st==='heavy'||P.st==='dash')&&P.t>=hitAt(P)+60);
    if(busy&&!cancel){A.buf=k;A.bufT=Date.now();return}
    if(k==='roll'){if((P.stam==null?100:P.stam)<14){FG.pop(P.x,2.2,P.z,'Tired!','note');return}spend(22);var v=moveInput();if(v.lengthSq()<.01){var E=A.E;v.set(P.x-E.x,0,P.z-E.z).normalize()}P.a=Math.atan2(v.x,v.z);pSet('roll',{rx:v.x,rz:v.z});return}
    if(k==='light'){if(P.rollEnd&&Date.now()-P.rollEnd<300){P.rollEnd=0;faceFoe(6.5);spend(8);pSet('dash');return}var chain=P.lastL&&Date.now()-P.lastL<450?(P.combo+1)%4:0;spend(5);faceFoe(FG.reachP+3.5);pSet('light',{combo:chain,dur:[280,280,320,470][chain]});return}
    if(k==='heavy'){faceFoe(FG.reachP+3.5);if(A.hHeld)pSet('charge',{full:0});else{spend(12);pSet('heavy',{pow:0})}return}
    if(k==='special'){if(A.sp<100){fPopFoe('Special not ready','note');return}A.sp=0;fHud();pSet('special');var nm=FOE_SPECIAL[A.g.fx];fAnn(nm?nm[0]:'Special!','sp',800)}
  }
  function release(k){var A=AR_S;if(!A)return;if(k==='block')A.hold=false;if(k==='heavy')A.hHeld=false}
  /* let go of a charged heavy: the longer the charge, the harder the blow */
  function releaseHeavy(){var P=AR_S.P,ct=P.t,pow=cPow(ct);spend(12+10*pow);faceFoe(FG.reachP+3.5);pSet('heavy',{pow:pow});P.t=Math.min(300,ct)}
  /* the enemy's poise is broken: it reels, and a heavy blow now is a critical */
  function stagger(){var A=AR_S,E=A.E;E.poise=0;E.chainNext=0;eSet('stagger',{len:2300});FG.slowmo=Math.max(FG.slowmo||0,260);FG.shake=Math.max(FG.shake,.6);fAnn('Staggered!','go',800);
    if(!A.critTip){A.critTip=1;arT(function(){if(AR_S===A&&A.live&&A.E.st==='stagger')FG.pop(A.E.x,2.8,A.E.z,'Heavy = critical!','note')},450)}}
  function step(dt){
    var A=AR_S;if(!A||!FG)return;if(FG.slowmo>0){FG.slowmo-=dt;dt*=.35}var P=A.P,E=A.E,e=FG.e,g=A.g,s=dt/1000;if(P.x==null)resetPos(A);
    P.t=(P.t||0)+dt;E.t=(E.t||0)+dt;A.clock-=dt;
    if(P.stam==null)P.stam=100;P.sT=(P.sT||0)+dt;if(P.sT>550&&P.st!=='roll')P.stam=Math.min(100,P.stam+(P.st==='block'?14:40)*s);
    if(E.pm==null){E.pm=50+Math.min(FG.tier,30)*3;E.poise=E.pm}E.pT=(E.pT||0)+dt;if(E.pT>2000&&E.st!=='stagger'&&E.poise<E.pm)E.poise=Math.min(E.pm,E.poise+18*s);
    if(FG.stb){FG.stb.firstChild.style.width=P.stam+'%';FG.stb.classList.toggle('low',P.stam<22)}
    if(FG.pob){FG.pob.firstChild.style.width=(E.st==='stagger'?100*Math.max(0,1-E.t/E.len):100*E.poise/E.pm)+'%';FG.pob.classList.toggle('brk',E.st==='stagger')}
    var tt=document.getElementById('fT');if(tt)tt.textContent=Math.max(0,Math.ceil(A.clock/1000));
    /* the champion moves */
    var v=moveInput(),spd=5+g.time*.2,moving=v.lengthSq()>.01;
    if(P.st==='idle'||P.st==='run'||P.st==='block'){
      if(A.hold&&P.st!=='block')pSet('block');if(!A.hold&&P.st==='block')pSet('idle');
      var sp2=P.st==='block'?spd*.35:spd;P.mv=moving;
      if(moving){P.x+=v.x*sp2*s;P.z+=v.z*sp2*s;if(P.st!=='block')P.a=P.a+ang(Math.atan2(v.x,v.z)-P.a)*Math.min(1,s*14);if(P.st==='idle')pSet('run')}
      else if(P.st==='run')pSet('idle');
      if(P.st==='block'){var fa=faceTo(P.x,P.z,E.x,E.z);P.a=P.a+ang(fa-P.a)*Math.min(1,s*10)}
      if(A.buf&&Date.now()-A.bufT<300){var b=A.buf;A.buf=null;act(b,1)}
    }else if(P.st==='roll'){var rp=Math.min(1,P.t/420);P.x+=P.rx*7.4*s*(1-rp*.6);P.z+=P.rz*7.4*s*(1-rp*.6);if(P.t>=420){P.rollEnd=Date.now();pSet(moving?'run':'idle');if(A.buf&&Date.now()-A.bufT<300){var b2=A.buf;A.buf=null;act(b2,1)}}}
    else if(P.st==='light'||P.st==='heavy'||P.st==='special'||P.st==='dash'){
      var dur=P.st==='light'?P.dur:P.st==='heavy'?640:P.st==='dash'?430:1050,hits=P.st==='light'?[[130,130,150,250][P.combo||0]]:P.st==='heavy'?[380]:P.st==='dash'?[170]:[260,520,780],lw=dur*(P.st==='heavy'?.55:.42);
      if(P.st==='dash'){if(P.t<210){P.x+=Math.sin(P.a)*10*s;P.z+=Math.cos(P.a)*10*s}}
      else if(P.lunge&&P.t<lw&&P.st!=='special'){var lv=P.lunge/(lw/1000);P.x+=Math.sin(P.a)*lv*s;P.z+=Math.cos(P.a)*lv*s}
      hits.forEach(function(h,n){if(P.t-dt<h&&P.t>=h)strikeFoe(P.st,n)});
      if(P.t>=dur){if(P.st==='light'){P.lastL=Date.now()}var was=P.st;pSet(moving?'run':'idle');if(A.buf&&Date.now()-A.bufT<380){var b3=A.buf;A.buf=null;if(!(was==='light'&&b3==='light'&&P.combo===3))act(b3,1)}}
    }else if(P.st==='charge'){var fa2=faceTo(P.x,P.z,E.x,E.z);if(dist(P,E)<FG.reachP+4)P.a=P.a+ang(fa2-P.a)*Math.min(1,s*8);if(!P.full&&cPow(P.t)>=1){P.full=1;FG.pop(P.x,2.3,P.z,'Charged!','heal')}if(!A.hHeld||P.t>=1150)releaseHeavy()}
    else if(P.st==='hurt'){var kf=Math.max(0,1-P.t/380);P.x+=(P.kx||0)*s*kf;P.z+=(P.kz||0)*s*kf;if(P.t>=(P.hd||380))pSet('idle')}
    else if(P.st==='down'){var kf2=Math.max(0,1-P.t/350);P.x+=(P.kx||0)*s*kf2;P.z+=(P.kz||0)*s*kf2;if(P.t>=950)pSet(moving?'run':'idle')}
    /* poison and the ice slow */
    if(A.dot>0){A.dot-=dt;A.dotT=(A.dotT||0)+dt;if(A.dotT>=500){A.dotT=0;var pd=Math.max(1,Math.round(A.em*.02));A.e-=pd;FG.pop(E.x,2,E.z,'−'+pd,'poison');fHud();if(A.e<=0)return fKO(true)}}
    if(A.slow>0)A.slow-=dt;
    /* the creature */
    var spd2=(1-Math.min(.42,FG.tier*.03))*(E.rage?.8:1),slow=A.slow>0?1.45:1,d=dist(P,E),fp=faceTo(E.x,E.z,P.x,P.z),fw=document.getElementById('foeW');E.mv=0;
    if(E.st==='idle'&&!E.rage&&FG.tier>=2&&A.e>0&&A.e<=A.em*.4){E.rage=1;eSet('roar',{len:800});fAnn('Enraged!','sp',1000);FG.shake=Math.max(FG.shake,.6)}
    if(E.st==='idle'){
      E.a=E.a+ang(fp-E.a)*Math.min(1,s*5);
      if(P.st==='charge'&&d<FG.reachE+1&&E.wait>250)E.wait=250;
      var want=e.ranged?6:FG.reachE*.9;
      if(e.ranged&&d<4){E.x-=Math.sin(E.a)*FG.spdE*.8*s;E.z-=Math.cos(E.a)*FG.spdE*.8*s;E.mv=1}
      else if(d>want+.2){var ms=FG.spdE/slow*(E.rage?1.15:1);E.x+=Math.sin(E.a)*ms*s;E.z+=Math.cos(E.a)*ms*s;E.mv=1}
      else{E.circ=E.circ||(Math.random()<.5?-1:1);var ca=E.a+Math.PI/2*E.circ;E.x+=Math.sin(ca)*1.1*s;E.z+=Math.cos(ca)*1.1*s;E.mv=.4}
      E.wait=(E.wait||1000)-dt;
      if(E.wait<=0){
        var kit=FG.kit,far=d>FG.reachE+1.5,choice;
        if(P.st==='block'&&kit.indexOf('slam')>=0&&Math.random()<.6)choice='slam';
        else if(E.rage&&d<3.4&&Math.random()<.25)choice='burst';
        else if(kit.indexOf('arrow')>=0&&d>2.6&&Math.random()<.75)choice='arrow';
        else if(far&&kit.indexOf('charge')>=0&&Math.random()<.6)choice='charge';
        else if(far&&kit.indexOf('breath')>=0&&d<7&&Math.random()<.6)choice='breath';
        else if(kit.indexOf('slam')>=0&&(far?Math.random()<.7:Math.random()<.35+FG.tier*.01))choice='slam';
        else if(!far)choice='swipe';
        if(!choice){E.wait=200}
        else if(choice==='swipe'&&A.recent&&A.recent.length>=3&&Math.random()<.4){eSet('guard',{len:900+Math.random()*600});A.recent=[]}
        else{var len=({swipe:760,slam:1050,charge:1150,breath:1250,arrow:950,burst:560})[choice]*spd2*slow*(e.fast?.8:1)+g.time*30;eSet('tele',{atk:choice,len:len,tx:P.x,tz:P.z,feint:choice==='swipe'&&FG.tier>=4&&Math.random()<.2?1:0})}
      }
    }else if(E.st==='tele'){
      var lockT=E.atk==='swipe'?.7:E.atk==='slam'?.82:E.atk==='arrow'?.8:E.atk==='burst'?0:.55;
      if(E.t<E.len*lockT){E.a=E.a+ang(fp-E.a)*Math.min(1,s*4);if(E.atk==='slam'){E.tx=P.x;E.tz=P.z}}
      if(fw)fw.dataset.left=Math.round(E.len-E.t);
      if(E.feint&&E.t>=E.len*.55)eSet('tele',{atk:'swipe',len:Math.max(360,E.len*.55),chain:1,tx:P.x,tz:P.z});
      else if(E.t>=E.len)foeStrike();
    }else if(E.st==='strike'){
      if(E.atk==='slam'){var su=Math.min(1,E.t/E.slen);E.x=E.sx+(E.tx-E.sx)*su;E.z=E.sz+(E.tz-E.sz)*su;if(!E.done&&su>=1){E.done=1;landSlam()}}
      if(E.atk==='charge'){E.x+=Math.sin(E.a)*14*s;E.z+=Math.cos(E.a)*14*s;if(!E.done&&dist(P,E)<FG.FR+.6){E.done=1;hitPlayer('charge')}}
      if(E.atk==='breath'&&!E.done&&E.t>200){E.done=1;if(Math.abs(ang(faceTo(E.x,E.z,P.x,P.z)-E.a))<.5&&d<6.8)hitPlayer('breath');else missed(false)}
      if(E.t>=E.slen){if(E.next==='open')eSet('open');else if(E.chainNext){E.chainNext=0;eSet('tele',{atk:'swipe',len:430*spd2*slow+g.time*25,chain:1})}else{eSet('idle');E.wait=(700+Math.random()*800)*spd2}}
    }else if(E.st==='open'){if(E.t>=(E.olen||1100)){eSet('idle');E.wait=(600+Math.random()*700)*spd2}}
    else if(E.st==='guard'){E.a=E.a+ang(fp-E.a)*Math.min(1,s*5);if(E.t>=E.len){eSet('idle');E.wait=500}}
    else if(E.st==='hurt'){if(E.t>=(E.hl||260)){eSet('idle');E.wait=Math.max(250,E.wait||350)}}
    else if(E.st==='stagger'){if(E.t>=E.len){E.poise=E.pm;eSet('idle');E.wait=450}}
    else if(E.st==='roar'){E.a=E.a+ang(fp-E.a)*Math.min(1,s*5);if(E.t-dt<260&&E.t>=260){FG.shake=Math.max(FG.shake,.9);FG.burst(new T.Vector3(E.x,.5,E.z),26,'#FF5A1A');if(d<4.2&&P.st!=='roll'&&P.st!=='down'&&P.st!=='ko'){var rx2=(P.x-E.x)/(d||1),rz2=(P.z-E.z)/(d||1);pSet('hurt',{kx:rx2*8,kz:rz2*8,hd:420})}}if(E.t>=E.len){eSet('idle');E.wait=350}}
    /* keep them apart and inside the arena */
    var sep=FG.FR+.45;d=dist(P,E);if(d<sep&&d>0){var px=(P.x-E.x)/d,pz=(P.z-E.z)/d,push=sep-d;if(E.st==='strike'&&E.atk==='charge'){P.x+=px*push;P.z+=pz*push}else{P.x+=px*push*.6;P.z+=pz*push*.6;E.x-=px*push*.4;E.z-=pz*push*.4}}
    [P,E].forEach(function(o){var r=Math.sqrt(o.x*o.x+o.z*o.z),lim=ARENA_R-(o===E?FG.FR:.5);if(r>lim){o.x*=lim/r;o.z*=lim/r}});
    if(A.clock<=0){A.live=false;fAnn('Time!','ko',1200);arT(function(){fRoundEnd(A.p/A.pm>=A.e/A.em)},1300)}
  }
  function foeStrike(){
    var A=AR_S,E=A.E,P=A.P;
    if(E.atk==='swipe'){var ch2=!E.chain&&(FG.tier>=3||E.rage)&&Math.random()<(E.rage?.65:.45);eSet('strike',{atk:'swipe',slen:300,next:'idle',done:1,chainNext:0});var d=dist(P,E),inArc=d<FG.reachE+.5&&Math.abs(ang(faceTo(E.x,E.z,P.x,P.z)-E.a))<.95;if(inArc){hitPlayer('swipe');if(ch2&&E.st==='strike')E.chainNext=1}else missed(true);E.chain=0}
    else if(E.atk==='burst'){eSet('strike',{atk:'burst',slen:260,next:'idle',done:1});FG.shake=Math.max(FG.shake,.7);FG.burst(new T.Vector3(E.x,.4,E.z),30,'#FFB34A');if(dist(P,E)<3.2)hitPlayer('burst');else missed(true)}
    else if(E.atk==='arrow'){eSet('strike',{atk:'arrow',slen:300,next:'idle',done:1});var ux=Math.sin(E.a),uz=Math.cos(E.a),rx=P.x-E.x,rz=P.z-E.z,al=rx*ux+rz*uz,pp=Math.abs(rx*uz-rz*ux);var aw=sprite('#FFF3B0',.4,FG.C.scene,1);FG.arrows.push({m:aw,x0:E.x,z0:E.z,x1:E.x+ux*11,z1:E.z+uz*11,t:0,d:.25});if(al>0&&al<11.5&&pp<.75)hitPlayer('arrow');else missed(true)}
    else if(E.atk==='slam'){eSet('strike',{atk:'slam',slen:420,sx:E.x,sz:E.z,next:'idle',done:0})}
    else if(E.atk==='charge'){eSet('strike',{atk:'charge',slen:520,next:'idle',done:0});FG.shake=Math.max(FG.shake,.4)}
    else if(E.atk==='breath'){eSet('strike',{atk:'breath',slen:700,next:'idle',done:0})}
  }
  function landSlam(){var A=AR_S,E=A.E,P=A.P;FG.shake=Math.max(FG.shake,.9);FG.burst(new T.Vector3(E.x,.3,E.z),24,'#E8D2A8');if(Math.sqrt(Math.pow(P.x-E.tx,2)+Math.pow(P.z-E.tz,2))<1.9)hitPlayer('slam');else missed(true)}
  function missed(near){var A=AR_S,E=A.E,P=A.P,rolled=P.st==='roll'&&P.t>20&&P.t<380,perfect=rolled&&P.t<200;E.next='open';E.olen=perfect?1500:rolled?1150:800;if(E.st!=='strike')eSet('open');if(rolled)P.stam=Math.min(100,(P.stam||0)+(perfect?20:8));if(perfect){FG.slowmo=650;A.sp=Math.min(100,A.sp+35);FG.pop(P.x,2.2,P.z,'Perfect!','big')}else if(rolled){A.sp=Math.min(100,A.sp+25);FG.pop(P.x,2,P.z,'Dodged!','heal')}fHud();arT(function(){fPopFoe('Open!','note')},120)}
  function hitPlayer(kind){
    var A=AR_S,E=A.E,P=A.P,e=FG.e,g=A.g;
    if(P.st==='roll'&&P.t>20&&P.t<380){missed(true);return}
    if(P.st==='down'||P.st==='ko')return;
    var dmg=foeHit(e)*({swipe:1,slam:1.5,charge:1.4,breath:1.3,burst:.8,arrow:.9})[kind]*60/(60+g.def*3),fa=faceTo(P.x,P.z,E.x,E.z);
    /* a parry: block just before the blow lands */
    if(P.st==='block'&&kind!=='slam'&&kind!=='breath'&&P.blockT&&Date.now()-P.blockT<220&&Math.abs(ang(fa-P.a))<1.4){E.chainNext=0;P.stam=Math.min(100,(P.stam||0)+20);E.poise-=30;E.pT=0;if(E.poise<=0){E.next='idle';stagger()}else{E.next='open';E.olen=1400;eSet('open',{olen:1400})}FG.slowmo=380;A.sp=Math.min(100,A.sp+30);g3ev('block');FG.pop(P.x,2.2,P.z,'Parry!','big');fHud();return}
    if(P.st==='block'&&kind!=='slam'&&Math.abs(ang(fa-P.a))<1.3){var bc=({swipe:20,charge:34,arrow:12,burst:22,breath:26})[kind]||20;if((P.stam||0)<bc){spend(100);dmg*=.6;var gx=P.x-E.x,gz=P.z-E.z,gl=Math.sqrt(gx*gx+gz*gz)||1;pSet('hurt',{kx:gx/gl*5,kz:gz/gl*5,hd:850});g3ev('hitP');FG.pop(P.x,2.2,P.z,'Guard broken!','big')}else{spend(bc);dmg*=.22;g3ev('block');FG.pop(P.x,2,P.z,'Blocked','blk');A.sp=Math.min(100,A.sp+6)}}
    else{var dx=P.x-E.x,dz=P.z-E.z,dl=Math.sqrt(dx*dx+dz*dz)||1;pSet(kind==='slam'||kind==='charge'?'down':'hurt',{kx:dx/dl*(kind==='swipe'?4:7),kz:dz/dl*(kind==='swipe'?4:7)});g3ev('hitP');A.combo=0;fCombo();A.sp=Math.min(100,A.sp+8);var st=document.getElementById('arStage');if(st){st.classList.remove('rflash');void st.offsetWidth;st.classList.add('rflash')}}
    dmg=Math.max(1,Math.round(dmg));A.p-=dmg;FG.pop(P.x,1.8,P.z,'−'+dmg,'hurtp');fHud();
    if(A.p<=0)fKO(false);
  }
  /* the champion's blow: it lands if the creature is in reach and in front (the special hits all around) */
  function strikeFoe(kind,n){
    var A=AR_S,E=A.E,P=A.P,g=A.g,d=dist(P,E),fa=faceTo(P.x,P.z,E.x,E.z),reach=FG.reachP+(kind==='heavy'?.4:kind==='dash'?.3:0)+FG.FR*.6,st0=E.st,crit=false;
    if(kind!=='special')FG.arc(P.x,P.z,P.a,Math.min(3,FG.reachP)*.9,kind==='heavy'?'#FFD27A':'#FFFFFF',kind==='heavy');
    else FG.arc(P.x,P.z,P.a+n*2.1,2.6,'#FFB34A',true);
    if(FG.ranged&&kind!=='special'){var aw=sprite('#FFF3B0',.35,FG.C.scene,1),tx=P.x+Math.sin(P.a)*Math.min(d,10),tz=P.z+Math.cos(P.a)*Math.min(d,10);FG.arrows.push({m:aw,x0:P.x,z0:P.z,x1:tx,z1:tz,t:0,d:.15})}
    var inFront=Math.abs(ang(fa-P.a))<(kind==='special'?Math.PI:FG.ranged?.25:1.05);
    if(!(d<(kind==='special'?2.6+FG.FR:reach)&&inFront))return;
    if(FG.ranged&&kind!=='special'&&E.st!=='tele'&&Math.random()<(FG.e.dg||.1)){FG.pop(E.x,2,E.z,'Dodged!','note');return}
    var fin=kind==='light'&&P.combo===3,base=g.atk*({light:[.46,.5,.58,1.05][P.combo||0],heavy:1.3*(1+.9*(P.pow||0)),special:1,dash:.85})[kind],cls=fin?'big':'',note=fin?'Finisher!':'';
    if(kind==='special'){if(g.fx==='gold')base*=1.5;if(g.fx==='holy'&&n===2)arT(function(){if(AR_S===A&&A.live)strikeFoe('special',3)},160)}
    if(E.st==='stagger'){if(kind==='heavy'||fin){crit=true;base*=2.6;cls='big';note='Critical!';FG.slowmo=480;E.poise=E.pm;eSet('hurt',{hl:700})}else base*=1.3}
    else if(E.st==='guard'){if(kind==='light'||kind==='dash'){base*=.2;cls='blk';note='Blocked'}else{eSet('hurt');note='Guard break!';cls='big'}}
    else if(E.st==='open'){base*=1.6;cls='big';note=n===0?'Counter!':''}
    else if(E.st==='tele'&&kind!=='light'){eSet('hurt');note='Interrupted!';cls='big'}
    else if(E.st==='idle'||E.st==='hurt'){var now=Date.now();A.recent=(A.recent||[]).filter(function(x){return now-x<1700});A.recent.push(now);
      if(A.recent.length>=6&&FG.tier>=1&&Math.random()<.6){A.recent=[];eSet('tele',{atk:'burst',len:480});note='Watch out!'}else if(!(E.rage&&(kind==='light'||kind==='dash')&&!fin))eSet('hurt')}
    var dmg=Math.max(1,Math.round(base));A.e-=dmg;g3ev('hitE',cls==='blk'?'light':kind);
    var hy=2;FG.pop(E.x,hy,E.z,'−'+dmg,cls);if(note)arT(function(){FG.pop(E.x,hy+.6,E.z,note,'note')},90);
    var kb=crit?2.8:fin?2.2:kind==='heavy'?.9+.8*(P.pow||0):kind==='special'?.5:.18,dx=E.x-P.x,dz=E.z-P.z,dl=Math.sqrt(dx*dx+dz*dz)||1;E.x+=dx/dl*kb;E.z+=dz/dl*kb;A.stop=crit?170:fin?110:kind==='heavy'?90+40*(P.pow||0):kind==='special'?55:45;
    if(crit)FG.shake=Math.max(FG.shake,1.3);
    if(cls!=='blk'&&!crit&&E.st!=='stagger'){var pz=({light:[7,7,9,16][P.combo||0],heavy:20+24*(P.pow||0),special:10,dash:12})[kind]*(st0==='open'?1.5:1);E.poise-=pz;E.pT=0;if(E.poise<=0&&A.e>0)stagger()}
    if(cls!=='blk'){A.combo++;A.sp=Math.min(100,A.sp+(kind==='special'?0:kind==='heavy'?14:9));fCombo()}
    if(kind==='special'&&n===0){if(g.fx==='poison'){A.dot=4000;A.dotT=0}if(g.fx==='ice')A.slow=5000;if(g.fx==='fire')FG.burst(new T.Vector3(E.x,1,E.z),30,'#FF7A1A')}
    fHud();if(A.e<=0)fKO(true);
  }
  /* input for the 3D fight: keys, a joystick on touch screens, and the mouse (hold to run toward the pointer, click to attack) */
  var K3={j:'light',J:'light',z:'light',Z:'light',k:'heavy',K:'heavy',x:'heavy',X:'heavy',l:'special',L:'special',c:'special',C:'special',' ':'roll',Shift:'block',e:'roll',E:'roll'};
  var RMB=null,HB=null;
  function on3(){return FG&&CUR&&FG.C===CUR&&AR_S&&AR_S.g3&&!AR_S.over}
  document.addEventListener('keydown',function(ev){if(!on3()||ev.ctrlKey||ev.metaKey||ev.altKey||(ev.target&&/INPUT|TEXTAREA|SELECT/.test(ev.target.tagName)))return;
    var k=ev.key.length===1?ev.key.toLowerCase():ev.key;if(/^(w|a|s|d|ArrowUp|ArrowDown|ArrowLeft|ArrowRight)$/.test(k)){KEY[k]=1;ev.preventDefault();return}var a=K3[ev.key];if(!a)return;ev.preventDefault();if(ev.repeat)return;act(a)});
  document.addEventListener('keyup',function(ev){var k=ev.key.length===1?ev.key.toLowerCase():ev.key;delete KEY[k];if(K3[ev.key])release(K3[ev.key])});
  window.addEventListener('blur',function(){KEY={};JOY=null;MOUSE=null;RMB=HB=null;if(AR_S){AR_S.hold=false;AR_S.hHeld=false}});
  document.addEventListener('pointerdown',function(ev){
    if(!on3())return;var b=ev.target.closest&&ev.target.closest('[data-g3]');
    if(b){ev.preventDefault();b.classList.add('down');if(b.dataset.g3==='heavy')HB=ev.pointerId;act(b.dataset.g3);return}
    var cv=CUR.r.domElement;if(ev.target!==cv)return;ev.preventDefault();
    var r=cv.getBoundingClientRect(),x=ev.clientX-r.left,y=ev.clientY-r.top;
    if(ev.pointerType==='mouse'){if(ev.button===2){RMB=ev.pointerId;act('heavy');return}MOUSE={id:ev.pointerId,held:true,t:Date.now(),x0:ev.clientX,y0:ev.clientY,p:FG.groundAt(ev.clientX,ev.clientY)};return}
    if(x<r.width*.5&&!JOY){JOY={id:ev.pointerId,bx:x,by:y,dx:0,dy:0}}else{var gp2=FG.groundAt(ev.clientX,ev.clientY),P=AR_S.P;if(gp2&&(P.st==='idle'||P.st==='run'))P.a=faceTo(P.x,P.z,gp2.x,gp2.z);act('light')}
  });
  document.addEventListener('pointermove',function(ev){
    if(!on3())return;
    if(JOY&&ev.pointerId===JOY.id){var r=CUR.r.domElement.getBoundingClientRect(),dx=(ev.clientX-r.left-JOY.bx)/50,dy=(ev.clientY-r.top-JOY.by)/50,l=Math.sqrt(dx*dx+dy*dy);if(l>1){dx/=l;dy/=l}JOY.dx=dx;JOY.dy=dy}
    if(MOUSE&&ev.pointerId===MOUSE.id&&MOUSE.held){MOUSE.p=FG.groundAt(ev.clientX,ev.clientY)}
  });
  function up(ev){
    var b=ev.target.closest&&ev.target.closest('[data-g3]');if(b){b.classList.remove('down');release(b.dataset.g3)}
    if(HB!=null&&ev.pointerId===HB){HB=null;release('heavy')}
    if(RMB!=null&&ev.pointerType==='mouse'&&ev.button===2){RMB=null;release('heavy');return}
    if(JOY&&ev.pointerId===JOY.id)JOY=null;
    if(MOUSE&&ev.pointerId===MOUSE.id){var quick=Date.now()-MOUSE.t<220&&Math.abs(ev.clientX-MOUSE.x0)+Math.abs(ev.clientY-MOUSE.y0)<10;if(quick&&on3()){var gp3=FG.groundAt(ev.clientX,ev.clientY),P=AR_S.P;if(gp3&&(P.st==='idle'||P.st==='run'))P.a=faceTo(P.x,P.z,gp3.x,gp3.z);act('light')}MOUSE=null}
  }
  document.addEventListener('pointerup',up);document.addEventListener('pointercancel',up);
  document.addEventListener('contextmenu',function(ev){if(on3()&&ev.target.closest&&ev.target.closest('.astage'))ev.preventDefault()});
  function ev(kind,a){
    if(!FG||!CUR||FG.C!==CUR)return;
    if(kind==='hitE'){FG.flashE=a==='light'?.7:1;FG.shake=Math.max(FG.shake,a==='light'?.25:.7);var p=new T.Vector3();(FG.F.head||FG.F.root).getWorldPosition(p);FG.burst(p,a==='light'?14:30,a==='special'?'#FFB34A':'#FFE9A8')}
    if(kind==='hitP'){FG.flashP=1;FG.shake=Math.max(FG.shake,.8)}
    if(kind==='block'){var b=new T.Vector3();FG.H.chest.getWorldPosition(b);FG.burst(b,18,'#9BC4FF');FG.shake=Math.max(FG.shake,.3)}
  }

  /* ---- the shop turntable and the arena lobby: the champion on a glowing stand ---- */
  function show(host,q,o){
    if(!host)return;o=o||{};var C=start(host,'s3d',true),S3=C.scene;
    S3.add(new T.HemisphereLight('#FFE9C8','#3A1A10',.9));var key=new T.DirectionalLight('#FFF1DC',1.6);key.position.set(3,5,5);key.castShadow=true;key.shadow.mapSize.set(1024,1024);S3.add(key);
    var rim=new T.DirectionalLight('#FF8A3A',1.2);rim.position.set(-4,3,-4);S3.add(rim);var rim2=new T.DirectionalLight('#6FA8FF',.8);rim2.position.set(4,2,-3);S3.add(rim2);
    var ped=cyl(1.1,1.2,.18,M('#2A1408',{r:.4,m:.5}),0,-.09,0,S3,48);ped.receiveShadow=true;
    var ringM=M('#FFB34A',{e:'#FF8A1A',ei:1.4,r:.3});var rg=tor(1.12,.025,ringM,0,.01,0,S3,Math.PI*2);rg.rotation.x=Math.PI/2;
    var glow=sprite('#FF9A3A',3.2,S3,.35);glow.position.y=.05;
    var H=hero(q),R=H.root;S3.add(R);H.R.sh.rotation.set(.55,0,.12);H.R.el.rotation.x=.75;H.wpn.rotation.x=-1.9;H.L.sh.rotation.set(.15,0,-.12);H.L.el.rotation.x=.25;
    var bb=new T.Box3().setFromObject(R),hgt=bb.max.y-bb.min.y,wid=Math.max(bb.max.x-bb.min.x,bb.max.z-bb.min.z);
    var dist=Math.max(hgt*1.45,wid*1.25)+1.2,cy=hgt*.5;
    var rot=o.back?0:Math.PI,drag=null,spin=.35,em=[];
    for(var i=0;i<26;i++){var s=sprite(['#FFB34A','#FF7A1A','#FFE08A'][i%3],.12,S3,.9);s.position.set((Math.random()-.5)*2.6,Math.random()*hgt,(Math.random()-.5)*2.6);em.push([s,Math.random()])}
    var cv=C.r.domElement;cv.style.touchAction='pan-y';
    cv.addEventListener('pointerdown',function(e){drag={x:e.clientX,r:rot};cv.setPointerCapture&&cv.setPointerCapture(e.pointerId)});
    cv.addEventListener('pointermove',function(e){if(drag){rot=drag.r+(e.clientX-drag.x)*.012}});
    ['pointerup','pointercancel'].forEach(function(n){cv.addEventListener(n,function(){drag=null})});
    loop(C,function(dt,t){
      if(!drag)rot+=dt*spin;R.rotation.y=rot;
      C.cam.fov=40;C.cam.position.set(0,cy+hgt*.12,dist);C.cam.lookAt(0,cy,0);C.cam.updateProjectionMatrix();
      H.chest.rotation.y=Math.sin(t*.8)*.05;H.R.sh.rotation.x=.55+Math.sin(t*1.6)*.04;H.head.rotation.y=Math.sin(t*.6)*.15;H.chest.position.y=.04+Math.sin(t*2)*.008;
      if(H.cape){var ca=H.cape.geometry.attributes.position.array,cb=H.capeBase;for(var c=0;c<ca.length;c+=3){var yy=cb[c+1];ca[c+2]=cb[c+2]+(.52-yy)*(.12+Math.sin(t*2.5+yy*4+cb[c]*3)*.05)}H.cape.geometry.attributes.position.needsUpdate=true}
      if(H.mount&&H.mount.tail)H.mount.tail.forEach(function(s2,i2){s2.rotation.y=Math.sin(t*2+i2*.5)*.15});if(H.mount&&H.mount.wings)H.mount.wings.forEach(function(w,i3){w.rotation.z=(i3?-1:1)*Math.sin(t*3)*.3});
      ringM.emissiveIntensity=1.1+Math.sin(t*3)*.4;glow.material.opacity=.3+Math.sin(t*3)*.08;
      em.forEach(function(p){p[0].position.y+=dt*(.25+p[1]*.4);if(p[0].position.y>hgt*1.1){p[0].position.y=0}p[0].material.opacity=.5+Math.sin(t*4+p[1]*9)*.4});
    });
  }
  return {ok:true,arena:arena,show:show,stop:stop,ev:ev,step:step};
})();
function g3ev(k,a){if(G3.ok)G3.ev(k,a)}
