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
  function weapon(w){
    var g=grp(),k=w&&w.k||'stick',wood=M('#7A4E2A',{r:.8}),steel=M('#C9D1DA',{m:.9,r:.25}),gold=M('#F2C14E',{m:1,r:.3}),tip;
    var sw=k.indexOf('sw_')===0&&typeof SWORDS!=='undefined'?SWORDS[k.slice(3)]:WK[k];
    if(sw)tip=blade(g,sw);
    else if(k==='spear'||k==='trident'){cyl(.016,.016,1.7,wood,0,.55,0,g);if(k==='spear'){var sp=cone(.04,.22,steel,0,1.5,0,g);sp.scale.z=.4;tip=grp(g,0,1.62,0);tor(.025,.008,M('#C0392B'),0,1.36,0,g)}else{[-1,0,1].forEach(function(s){var c=cone(.018,.2,steel,s*.06,1.5+(s?0:.04),0,g)});box(.15,.02,.02,steel,0,1.4,0,g);tip=grp(g,0,1.62,0)}}
    else if(k==='mace'){cyl(.018,.018,.7,wood,0,.25,0,g);var hd=sph(.08,steel,0,.65,0,g);for(var i=0;i<8;i++){var c2=cone(.02,.07,steel,0,0,0,hd);var a=i/8*Math.PI*2;c2.position.set(Math.cos(a)*.08,(i%2?.03:-.03),Math.sin(a)*.08);c2.lookAt(Math.cos(a)*2,0,Math.sin(a)*2);c2.rotateX(Math.PI/2)}tip=grp(g,0,.7,0)}
    else if(k==='axe'){cyl(.018,.018,.8,wood,0,.3,0,g);var ax=new T.Shape();ax.moveTo(0,-.1);ax.quadraticCurveTo(.22,-.14,.24,0);ax.quadraticCurveTo(.22,.14,0,.1);ax.lineTo(0,-.1);[1,-1].forEach(function(s){var m2=mesh(new T.ExtrudeGeometry(ax,{depth:.01,bevelEnabled:true,bevelSize:.005,bevelThickness:.005}),steel,0,.62,-.005,g);m2.scale.x=s});tip=grp(g,.24,.62,0)}
    else if(k==='hammer'||k==='thunder'){cyl(.02,.02,.8,wood,0,.3,0,g);box(.26,.13,.13,k==='thunder'?M('#7FA8FF',{m:.6,r:.2,e:'#2A6BFF',ei:.9}):steel,0,.7,0,g);if(k==='thunder')sprite('#7FC0FF',.6,g,.6).position.y=.7;tip=grp(g,.13,.7,0)}
    else if(k==='staff'){cyl(.016,.02,1.3,wood,0,.45,0,g);sph(.06,M('#8EE7FF',{r:.1,e:'#2B9BFF',ei:1}),0,1.13,0,g);tor(.07,.012,gold,0,1.13,0,g);sprite('#7FD8FF',.5,g,.6).position.y=1.13;tip=grp(g,0,1.13,0)}
    else if(k==='bow'||k==='phoenix'){var bw=tor(.45,.016,k==='phoenix'?M('#FF8A3A',{e:'#FF4A00',ei:.7}):wood,0,0,0,g,Math.PI*.9);bw.rotation.z=Math.PI*.55;box(.004,.86,.004,M('#F3EBD8'),-.16,0,0,g);tip=grp(g,.3,0,0);if(k==='phoenix')sprite('#FF7A1A',.9,g,.4)}
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
    if(mt){[-1,1].forEach(function(s){var l=limb(hips,.08,.55,low,s*.16,-.02,0);l.rotation.set(-1.25,0,s*.55);sph(.085,boot,0,-.58,0,l)})}
    else{
      P.legL=limb(hips,.085,.78,low,-.13,0,0);P.legR=limb(hips,.085,.78,low,.13,0,0);
      box(.17,.1,.28,boot,0,-.83,-.05,P.legL);box(.17,.1,.28,boot,0,-.83,-.05,P.legR);
      if(robe)cyl(.21,.31,.84,a.id==='a0'?M(robeC,{r:.85}):M(hex(a.col,'#999'),{r:.75}),0,-.43,0,hips,24);
      else if(a.skirt)cyl(.26,.36,.42,arm,0,-.2,0,hips,20);
    }
    var chest=grp(hips,0,.04,0);P.chest=chest;
    cyl(.25,.21,.52,arm,0,.26,0,chest,22);sph(.255,arm,0,.52,0,chest,1,.52,.82);
    cyl(.232,.232,.09,M(hex(a.belt,robe?'#8A6A3A':hex(a.edge,'#555')),{r:.6,m:metal?.4:0}),0,.03,0,chest,22);
    sph(.03,M('#F2C14E',{m:1,r:.3}),0,.03,-.235,chest);
    if(metal){sph(.13,arm,-.29,.5,0,chest,1.15,.75,1.05);sph(.13,arm,.29,.5,0,chest,1.15,.75,1.05);box(.34,.3,.06,edge,0,.3,-.19,chest);if(a.trim)tor(.1,.014,M(hex(a.trim,'#fff'),{m:.8,r:.3}),0,.56,0,chest).rotation.x=Math.PI/2}
    var cape=a.cape||ch.cape;
    if(cape){var cg=new T.PlaneGeometry(.58,1.05,6,12),cp=grp(chest,0,.56,.2),c=mesh(cg,M(hex(cape,'#8E1F2A'),{r:.8,ds:true}),0,-.52,0,cp);P.cape=c;P.capeBase=cg.attributes.position.array.slice()}
    var neck=grp(chest,0,.56,0);cyl(.07,.08,.14,skin,0,.04,0,neck);
    var head=grp(neck,0,.2,0);P.head=head;sph(.15,skin,0,0,0,head,1,1.08,1);
    face(head,ch);hat(head,ch,robeC);
    /* arms: shoulder, elbow and hand pivots; the sleeves follow the armour */
    function side(sx){var sh=grp(chest,.33*sx,.47,0),up=limb(sh,.072,.3,arm),el=grp(up,0,-.3,0),fo=limb(el,.064,.27,a.full||robe?arm:M(hex(a.col,'#999'),metal?{m:.72,r:.3}:{r:.72})),hand=grp(el,0,-.3,0);sph(.068,skin,0,0,0,hand);return {sh:sh,el:el,hand:hand}}
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
  function hat(h,ch,wc){
    var t=ch.t,white=M('#F7F4EC',{r:.9}),black=M('#1E1E22',{r:.6}),gold=M('#F2C14E',{m:1,r:.28}),wm=M(wc,{r:.85});
    function cap(m,r,deep){return mesh(new T.SphereGeometry(r||.168,22,12,0,Math.PI*2,0,Math.PI*(deep||.55)),m,0,.012,0,h)}
    function drape(m,len,open){var g=new T.CylinderGeometry(.168,.215,len||.4,26,1,true,Math.PI+(open||.62),Math.PI*2-2*(open||.62));return mesh(g,m.side===T.DoubleSide?m:M('#'+m.color.getHexString(),{r:.9,ds:true}),0,-.15,.01,h)}
    function agal(){[.07,.105].forEach(function(y){var o=tor(.163,.017,black,0,y,0,h);o.rotation.x=Math.PI/2})}
    if(t==='ghutra'||t==='nomad'||t==='prince'){
      var cm=t==='nomad'?checkMat():white;cap(cm);drape(cm,.42);agal();
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
    var ec=o.eye||'#FFD43B',eyes=[];[-1,1].forEach(function(s){var e=sph(o.head*.15,M(ec,{e:ec,ei:o.glowEye?1.6:.5,r:.2}),s*o.head*.5,o.head*.28,o.head*.72,H);sph(o.head*.07,M('#111'),s*o.head*.52,o.head*.28,o.head*.84,H);eyes.push(e)});
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
  function creature(e){
    var k=e.k,o=FOEQ[k],R,F={};
    if(o){var c={};for(var x in o)c[x]=o[x];F=quad(c);R=F.root;F.kind='quad'}
    else if(k==='scorpion'){R=grp();var sm=M('#9A5426',{r:.38,m:.15}),dk=M('#5A2A10',{r:.45}),B=grp(R,0,.32,0);F.body=B;
      for(var i=0;i<5;i++)sph(.3-i*.025,sm,0,i*.01,.42-i*.26,B,1.25,.55,.95);sph(.24,sm,0,.03,.66,B,1.1,.55,1);
      [-1,1].forEach(function(s){for(var l=0;l<4;l++){var lg=grp(B,s*.28,0,.4-l*.26);lg.rotation.y=s*(.35-l*.25);var up=limb(lg,.04,.42,dk);up.rotation.z=s*1.95;var kn=grp(up,0,-.42,0),lo=limb(kn,.032,.5,dk);lo.rotation.z=-s*1.55;F.legs=F.legs||[];F.legs.push(lg)}
        var cl=grp(B,s*.26,.02,.8);F['cl'+s]=cl;var ua=limb(cl,.07,.38,sm);ua.rotation.set(-1.75,s*.35,0);var fa=grp(ua,0,-.38,0),fo=limb(fa,.06,.3,sm);fo.rotation.x=.9;var pin=grp(fo,0,-.32,0);sph(.14,sm,0,0,0,pin,.9,1,1.5);var f1=cone(.05,.3,sm,s*.04,-.02,-.22,pin);f1.rotation.x=-Math.PI/2;var f2=cone(.04,.26,dk,-s*.06,.04,-.2,pin);f2.rotation.x=-Math.PI/2});
      var tl=grp(B,0,.05,-.82),sg=tl;F.tail=[];for(var t=0;t<6;t++){var g=grp(sg,0,0,t?-.22:0);sph(.14-t*.012,sm,0,0,0,g,1,.9,1.1);g.rotation.x=t?.58:.5;sg=g;F.tail.push(g)}
      var st=cone(.06,.3,M('#2A1408',{r:.3}),0,.05,.12,sg);st.rotation.x=2.4;var stg=sprite('#7CFC5A',.35,sg,.6);stg.position.set(0,.1,.25);
      F.eyes=[-1,1].map(function(s){return sph(.04,M('#FF3A1A',{e:'#FF3A1A',ei:1.6}),s*.08,.16,.86,B)});F.head=B;F.kind='scorp'}
    else if(k==='viper'){R=grp();var vm=M('#3E8A3A',{r:.45}),pts=[];for(var p=0;p<40;p++){var a2=p/40*Math.PI*4.2,rr=.85-p*.012;pts.push(new T.Vector3(Math.cos(a2)*rr,.12+p*.02,Math.sin(a2)*rr-.4))}
      pts.push(new T.Vector3(0,1.05,.2),new T.Vector3(0,1.25,.55));var cur=new T.CatmullRomCurve3(pts);var tube=mesh(new T.TubeGeometry(cur,140,.14,12,false),vm,0,0,0,R);
      F.body=grp(R);var H=grp(R,0,1.28,.6);F.head=H;sph(.2,vm,0,0,0,H,1.1,.6,1.5);sph(.14,M('#C8E89A'),0,-.06,.12,H,1,.4,1.3);
      F.eyes=[-1,1].map(function(s){return sph(.04,M('#FFD43B',{e:'#FFB300',ei:1.2}),s*.12,.06,.18,H)});var tg=box(.015,.01,.25,M('#D6313F'),0,-.05,.42,H);F.tongue=tg;F.kind='snake'}
    else if(k==='eagle'){R=grp();var em=M('#5A3A22',{r:.8}),wh=M('#F4EFE2',{r:.8});var B2=grp(R,0,1.4,0);F.body=B2;sph(.4,em,0,0,0,B2,.9,1,1.3);var H2=grp(B2,0,.35,.35);F.head=H2;sph(.2,wh,0,0,0,H2);var bk=cone(.07,.25,M('#F2C14E',{r:.4}),0,-.05,.25,H2);bk.rotation.x=Math.PI/2;
      F.eyes=[-1,1].map(function(s){return sph(.035,M('#FFD43B',{e:'#FFB300',ei:.8}),s*.1,.06,.15,H2)});
      F.wings=[-1,1].map(function(s){var wg=grp(B2,s*.3,.1,0),sh=new T.Shape();sh.moveTo(0,.25);sh.lineTo(s*1.9,.4);sh.lineTo(s*2.2,0);sh.lineTo(s*1.7,-.25);sh.lineTo(s*1.2,-.1);sh.lineTo(s*.8,-.35);sh.lineTo(0,-.3);var m2=mesh(new T.ShapeGeometry(sh),M('#5A3A22',{r:.85,ds:true}),0,0,0,wg);m2.rotation.x=-Math.PI/2;return wg});
      [-1,1].forEach(function(s){limb(B2,.05,.35,M('#F2C14E'),s*.15,-.35,.1)});var tl2=mesh(new T.ConeGeometry(.3,.6,4),wh,0,-.05,-.6,B2);tl2.rotation.x=-Math.PI/2;tl2.scale.set(1,1,.3);F.kind='bird'}
    else if(k==='gorilla'){R=grp();var gm=M('#2A2A2E',{r:.9}),gf=M('#4A4448',{r:.8});var B3=grp(R,0,.9,0);F.body=B3;sph(.6,gm,0,.2,0,B3,1.1,1,.85);sph(.35,gf,0,.1,.38,B3,1,1.1,.5);var H3=grp(B3,0,.85,.15);F.head=H3;sph(.3,gm,0,0,0,H3);sph(.2,gf,0,-.05,.2,H3,1.2,.8,.7);
      F.eyes=[-1,1].map(function(s){return sph(.04,M('#FFB300',{e:'#FF8A00',ei:.9}),s*.1,.07,.26,H3)});
      F.arms=[-1,1].map(function(s){var a=limb(B3,.17,.95,gm,s*.62,.55,.05);a.rotation.z=s*.25;sph(.2,gf,0,-1,0,a);return a});[-1,1].forEach(function(s){limb(B3,.17,.55,gm,s*.3,-.3,0)});F.kind='ape'}
    else{ /* the giant spider, and anything new */ R=grp();var spm=M('#2A1E2E',{r:.6}),B4=grp(R,0,.75,0);F.body=B4;sph(.55,spm,0,.2,-.55,B4,1,.85,1.2);sph(.32,spm,0,0,.2,B4);var H4=grp(B4,0,.05,.48);F.head=H4;
      F.eyes=[];for(var ei=0;ei<6;ei++)F.eyes.push(sph(.035,M('#FF2A2A',{e:'#FF2A2A',ei:1.8}),(ei%3-1)*.07,.08+(ei>2?.06:0),0,H4));[-1,1].forEach(function(s){var fg=cone(.03,.15,M('#E8E2D0'),s*.06,-.12,.05,H4);fg.rotation.x=Math.PI});
      F.legs=[];[-1,1].forEach(function(s){for(var l2=0;l2<4;l2++){var lg2=grp(B4,s*.25,0,.3-l2*.2),up=limb(lg2,.045,.6,spm);up.rotation.set(0,0,s*2.1);var kn=grp(up,0,-.6,0),lo=limb(kn,.035,.75,spm);lo.rotation.z=-s*1.5;F.legs.push(lg2)}});F.kind='spider'}
    var sc=({scorpion:2.1,wolf:1.9,hyena:1.9,eagle:1.5,bull:1.55,lion:1.7,panther:1.8,viper:1.7,bear:1.6,crocodile:1.6,tiger:1.7,gorilla:1.4,rhino:1.4,elephant:1.25,dragon:1.6,spider:1.5}[k]||1.5)*(1+Math.min(.25,ENEMIES.indexOf(e)*.015));R.scale.setScalar(sc);
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
  function world(scene,fk,show){
    var F=FIELD[fk]||FIELD.sand,W={F:F,anim:[]};
    var sky=new T.Mesh(new T.SphereGeometry(60,32,16),new T.ShaderMaterial({side:T.BackSide,depthWrite:false,fog:false,
      uniforms:{top:{value:new T.Color(F.sky[0])},mid:{value:new T.Color(F.sky[1])},bot:{value:new T.Color(F.fog)}},
      vertexShader:'varying vec3 vP;void main(){vP=position;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}',
      fragmentShader:'uniform vec3 top;uniform vec3 mid;uniform vec3 bot;varying vec3 vP;void main(){float h=normalize(vP).y;vec3 c=h>0.0?mix(mid,top,smoothstep(0.0,0.45,h)):mix(mid,bot,smoothstep(0.0,0.15,-h));gl_FragColor=vec4(c,1.0);}'}));scene.add(sky);
    scene.fog=new T.Fog(lin(F.fog),20,58);
    var hemi=new T.HemisphereLight(lin(F.sky[0]),lin(F.floor),F.amb*.85);scene.add(hemi);
    var sun=new T.DirectionalLight(lin(F.sun),F.night?1.1:1.75);sun.position.set(-6,12,8);sun.castShadow=true;sun.shadow.mapSize.set(1024,1024);var sc=sun.shadow.camera;sc.left=-8;sc.right=8;sc.top=8;sc.bottom=-8;sc.near=1;sc.far=40;sun.shadow.bias=-.0006;scene.add(sun);scene.add(sun.target);
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
    r.setPixelRatio(Math.min(window.devicePixelRatio||1,1.75));r.outputEncoding=T.sRGBEncoding;r.toneMapping=T.ACESFilmicToneMapping;r.toneMappingExposure=1.15;r.shadowMap.enabled=true;r.shadowMap.type=T.PCFSoftShadowMap;
    var cv=r.domElement;cv.className='g3c';host.insertBefore(cv,host.firstChild);host.classList.add(cls);
    var scene=new T.Scene(),cam=new T.PerspectiveCamera(50,1,.1,200);
    CUR={r:r,scene:scene,cam:cam,host:host,raf:0,t:0,last:0};
    return CUR;
  }
  function fit(C){var w=C.host.clientWidth,h=C.host.clientHeight;if(!w||!h)return;if(C.w!==w||C.h!==h){C.w=w;C.h=h;C.r.setSize(w,h,false);C.cam.aspect=w/h;C.cam.updateProjectionMatrix()}}
  function loop(C,fn){function f(ts){if(CUR!==C)return;if(!document.body.contains(C.r.domElement)){stop();return}var dt=C.last?Math.min(.05,(ts-C.last)/1000):.016;C.last=ts;C.t+=dt;fit(C);fn(dt,C.t);C.r.render(C.scene,C.cam);C.raf=requestAnimationFrame(f)}C.raf=requestAnimationFrame(f)}
  var ease=function(x){return x<0?0:x>1?1:x*x*(3-2*x)};
  function pulse(t,a,b){return t<a?0:t>b?0:Math.sin((t-a)/(b-a)*Math.PI)}

  /* ---- the fight ---- */
  var FG=null;
  function arena(stage,q,e){
    var C=start(stage,'a3d',false),S3=C.scene;
    var W=world(S3,q.field&&q.field.k||'sand');
    var HX=-.95,HZ=1.7,FX=.45,FZ=-2.6;var H=hero(q);H.root.position.set(HX,0,HZ);S3.add(H.root);
    var F=creature(e);F.root.position.set(FX,0,FZ);var YAW=Math.atan2(HX-FX,HZ-FZ)+(F.kind==='quad'?.55:.2);F.root.rotation.y=YAW;S3.add(F.root);
    /* the block bubble, the creature's guard, the warning ring and the dizzy stars */
    var bub=sph(.95,M('#6FA8FF',{op:.28,add:1,r:.2}),0,1.2,-.5,H.root);bub.castShadow=false;bub.visible=false;
    var grd=sph(1.6,M('#7FB2FF',{op:.3,add:1,r:.2}),0,1,1.2,F.root,1,1,.35);grd.castShadow=false;grd.visible=false;
    var warn=new T.Mesh(new T.RingGeometry(.9,1.15,48),new T.MeshBasicMaterial({color:'#FF3A1A',transparent:true,opacity:0,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide}));warn.rotation.x=-Math.PI/2;warn.position.set(HX,.03,HZ);S3.add(warn);
    var stars=[0,1,2].map(function(){return sprite('#FFE066',.35,S3,1)});stars.forEach(function(s){s.visible=false});
    /* the weapon trail */
    var TN=16,tp=new Float32Array(TN*2*3),tg=new T.BufferGeometry();tg.setAttribute('position',new T.BufferAttribute(tp,3));var idx=[];for(var i=0;i<TN-1;i++){var a=i*2;idx.push(a,a+1,a+2,a+1,a+3,a+2)}tg.setIndex(idx);
    var tcol={fire:'#FF8A3A',poison:'#7CFC5A',ice:'#9BE6FF',gold:'#FFD94A',holy:'#FFF3B0'}[(q.weapon&&q.weapon.fx)||'']||'#FFFFFF';
    var trail=new T.Mesh(tg,new T.MeshBasicMaterial({color:tcol,transparent:true,opacity:.55,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide}));trail.frustumCulled=false;S3.add(trail);
    var hist=[],v1=new T.Vector3(),v2=new T.Vector3();
    /* hit sparks */
    var SP=60,sg=new T.BufferGeometry(),sp=new Float32Array(SP*3),sv=[];for(var k=0;k<SP;k++)sv.push({v:new T.Vector3(),life:0});sg.setAttribute('position',new T.BufferAttribute(sp,3));
    var spm=new T.PointsMaterial({map:glowTex(),color:'#FFE9A8',size:.22,transparent:true,blending:T.AdditiveBlending,depthWrite:false});var sparks=new T.Points(sg,spm);sparks.frustumCulled=false;S3.add(sparks);
    FG={C:C,H:H,F:F,shake:0,flashE:0,flashP:0,burst:function(pos,n,col){spm.color.set(col||'#FFE9A8');for(var i=0,c=0;i<SP&&c<n;i++){var s=sv[i];if(s.life>0)continue;s.life=.5+Math.random()*.3;s.v.set((Math.random()-.5)*6,Math.random()*5+1,(Math.random()-.2)*5);sp[i*3]=pos.x;sp[i*3+1]=pos.y;sp[i*3+2]=pos.z;c++}}};
    var base=new T.Vector3(.35,2.45,6.4),look=new T.Vector3(.05,1.05,-2.4),bb=new T.Box3(),corners=[0,0,0,0,0,0,0,0].map(function(){return new T.Vector3()});
    var foeW=document.getElementById('foeW'),meW=document.getElementById('meW');
    function place(el,obj){if(!el)return;bb.setFromObject(obj);var mn=bb.min,mx=bb.max,i=0;[mn.x,mx.x].forEach(function(x){[mn.y,mx.y].forEach(function(y){[mn.z,mx.z].forEach(function(z){corners[i++].set(x,y,z)})})});
      var l=1e9,t=1e9,r=-1e9,b=-1e9;corners.forEach(function(c){c.project(C.cam);var sx=(c.x+1)/2*C.w,sy=(1-c.y)/2*C.h;l=Math.min(l,sx);r=Math.max(r,sx);t=Math.min(t,sy);b=Math.max(b,sy)});
      el.style.left=Math.round(l)+'px';el.style.top=Math.round(t)+'px';el.style.width=Math.max(10,Math.round(r-l))+'px';el.style.height=Math.max(10,Math.round(b-t))+'px'}
    var lastE='',lastP='';
    loop(C,function(dt,t){
      var A=AR_S;if(!A)return;var P=A.P||{st:'idle',t:0},E=A.E||{st:'idle',t:0},pt=P.t||0,et=E.t||0;
      /* camera: a slow drift, pushed in a little on a wide stage, with shake on hits */
      var portrait=C.h>C.w;C.cam.fov=portrait?66:50;C.cam.updateProjectionMatrix();
      FG.shake=Math.max(0,FG.shake-dt*2.6);var sh=FG.shake*FG.shake*.22;
      C.cam.position.set(base.x+Math.sin(t*.3)*.1+(Math.random()-.5)*sh+(portrait?.45:0),base.y+Math.sin(t*.4)*.05+(Math.random()-.5)*sh,base.z+(portrait?1.6:0));C.cam.lookAt(look);
      /* the champion */
      var R=H.R,L=H.L,ch=H.chest,root=H.root;
      var br=Math.sin(t*2.2)*.025;var face0=Math.atan2(FX-HX,FZ-HZ)+Math.PI;ch.rotation.set(0,0,0);root.position.x=HX;root.position.z=HZ;root.rotation.set(0,face0,0);H.hips.rotation.set(0,0,0);
      var sx=1.05,sz=-.12,ex=.55,lx=1.0,lz=.48,lex=.6,wr=-2.0;
      if(P.st==='light'){var u=pt/300;var w1=ease(u/.3),w2=ease((u-.3)/.35);sx=1.05+1.25*w1-1.9*w2;sz=-.12-.45*w1+.95*w2;ch.rotation.y=-.35*w1+.75*w2;ex=.55-.3*w1+.1*w2}
      else if(P.st==='heavy'){var u2=pt/640,a1=ease(u2/.48),a2=ease((u2-.48)/.2);sx=1.05+1.85*a1-2.7*a2;ex=.55-.45*a1+.2*a2;lx=1.0+1.7*a1-2.3*a2;ch.rotation.x=-.22*a1+.45*a2;root.position.z=HZ-.7*a2*(1-ease((u2-.75)/.25))}
      else if(P.st==='special'){var u3=pt/1050;root.rotation.y=face0+ease(u3/.85)*Math.PI*2;sx=1.55;sz=1.15;ex=.1;root.position.z=HZ-.8*Math.sin(Math.min(1,u3)*Math.PI)}
      else if(P.st==='dodgeL'||P.st==='dodgeR'){var dd=P.st==='dodgeL'?-1:1,k2=Math.sin(Math.min(1,pt/420)*Math.PI);root.position.x=HX+dd*1.5*k2;root.rotation.z=-dd*.3*k2;ch.rotation.x=.18*k2}
      else if(P.st==='block'){sx=1.5;sz=-.5;ex=1.15;lx=1.5;lz=.6;lex=1.15;wr=-.35}
      else if(P.st==='hurt'){var k3=Math.sin(Math.min(1,pt/380)*Math.PI);root.position.z=HZ+.5*k3;ch.rotation.x=-.35*k3}
      else if(P.st==='ko'){var k4=ease(pt/800);root.rotation.x=-1.35*k4;root.position.y=-.1*k4}
      R.sh.rotation.set(sx+br,0,sz);R.el.rotation.set(ex,0,0);L.sh.rotation.set(lx-br,0,lz);L.el.rotation.set(lex,0,0);H.wpn.rotation.x=wr;
      if(H.legL&&!H.mount){var st2=P.st==='dodgeL'||P.st==='dodgeR'?Math.sin(pt/60)*.5:0;H.legL.rotation.x=st2;H.legR.rotation.x=-st2}
      H.head.rotation.set(Math.sin(t*1.3)*.03,Math.sin(t*.7)*.05,0);
      bub.visible=P.st==='block';if(bub.visible)bub.material.opacity=.22+Math.sin(t*8)*.06;
      if(H.cape){var ca=H.cape.geometry.attributes.position.array,cb=H.capeBase;for(var c=0;c<ca.length;c+=3){var yy=cb[c+1],d=(.52-yy);ca[c+2]=cb[c+2]+d*(.18+Math.sin(t*3+yy*4+cb[c]*3)*.06+(P.st!=='idle'?.25:0))}H.cape.geometry.attributes.position.needsUpdate=true}
      if(H.mount){var Mn=H.mount;if(Mn.body)Mn.body.position.y+=Math.sin(t*2.4)*.0008;if(Mn.legs)Mn.legs.forEach(function(l,i){l.rotation.x=(P.st==='dodgeL'||P.st==='dodgeR')?Math.sin(pt/50+i*1.6)*.6:Math.sin(t*1.5+i)*.03});if(Mn.tail)Mn.tail.forEach(function(s,i){s.rotation.y=Math.sin(t*2+i*.5)*.12});if(Mn.wings)Mn.wings.forEach(function(w,i){w.rotation.z=(i?-1:1)*Math.sin(t*4)*.35});if(Mn.carpet){var pa=Mn.cg.attributes.position.array,pb=Mn.base;for(var j=0;j<pa.length;j+=3)pa[j+2]=pb[j+2]+Math.sin(t*3+pb[j+1]*2)*.06;Mn.cg.attributes.position.needsUpdate=true}}
      FG.flashP=Math.max(0,FG.flashP-dt*4);flash(H.mats,'#FF2A1A',FG.flashP*.9);
      /* the creature */
      var fr=F.root,fz=FZ,tele=E.st==='tele',heavy=E.kind==='slam';
      fr.position.set(FX,0,fz);fr.rotation.set(0,YAW,0);
      var body=F.body||fr;body.rotation.set(0,0,0);
      var breath=1+Math.sin(t*2)*.02;body.scale.set(1,breath,1);
      if(tele){var tu=Math.min(1,et/(E.len||800));fr.translateZ(-.5*ease(tu));body.rotation.x=-.12*ease(tu);fr.position.x+=Math.sin(et/22)*.03*tu;flash(F.mats,heavy?'#FF1A00':'#FF5A10',(.12+.3*tu)*(.6+.4*Math.sin(et/40)));warn.material.opacity=(heavy?.85:.5)*tu;warn.scale.setScalar(1+(1-tu)*1.2);warn.material.color.set(heavy?'#FF1A00':'#FFC21A')}
      else{warn.material.opacity=Math.max(0,warn.material.opacity-dt*3)}
      if(E.st==='strike'){var su=et/300,lu=su<.45?ease(su/.45):1-ease((su-.45)/.55);fr.translateZ(3.4*lu);body.rotation.x=.18*lu;if(lastE!=='strike')FG.shake=Math.max(FG.shake,.5)}
      if(E.st==='hurt'){var hu=Math.sin(Math.min(1,et/360)*Math.PI);fr.translateZ(-.4*hu);body.rotation.x=-.15*hu}
      if(E.st==='open'){fr.rotation.z=Math.sin(t*5)*.1;var hp=new T.Vector3();(F.head||fr).getWorldPosition(hp);stars.forEach(function(s,i){s.visible=true;var a=t*3+i*2.1;s.position.set(hp.x+Math.cos(a)*.6,hp.y+.55+Math.sin(t*6+i)*.05,hp.z+Math.sin(a)*.6)})}else stars.forEach(function(s){s.visible=false});
      grd.visible=E.st==='guard';if(grd.visible)grd.material.opacity=.25+Math.sin(t*6)*.08;
      if(E.st==='ko'){var ku=ease(et/900);fr.rotation.z=1.5*ku;fr.position.y=-.2*ku}
      if(!tele){FG.flashE=Math.max(0,FG.flashE-dt*5);flash(F.mats,'#FFFFFF',FG.flashE)}
      if(F.tail)F.tail.forEach(function(s,i){if(F.kind==='quad'||!F.kind)s.rotation.y=Math.sin(t*2.2+i*.6)*.18;else s.rotation.x=(i?.58:.5)+Math.sin(t*2+i)*.05+(tele?.22*Math.min(1,et/(E.len||800)):0)+(E.st==='strike'?.3:0)});
      if(F.legs&&F.kind!=='spider')F.legs.forEach(function(l,i){l.rotation.x=E.st==='strike'?Math.sin(et/40+i*1.6)*.7:Math.sin(t*1.2+i)*.04});
      if(F.kind==='spider'&&F.legs)F.legs.forEach(function(l,i){l.rotation.x=Math.sin(t*3+i)*.08});
      if(F.wings)F.wings.forEach(function(w,i){w.rotation.z=(i?-1:1)*(Math.sin(t*(tele?9:3))*.55+.45)});
      if(F.arms)F.arms.forEach(function(a,i){a.rotation.x=tele?-2.4*Math.min(1,et/(E.len||800)):E.st==='strike'?-.2:Math.sin(t*1.5+i)*.08});
      if(F.head&&F.kind!=='snake')F.head.rotation.y=Math.sin(t*.9)*.1;
      if(F.kind==='snake'){F.head.position.y=1.28+Math.sin(t*2)*.05;if(F.tongue)F.tongue.scale.z=Math.sin(t*9)>.3?1:.2}
      if(F.trunk)F.trunk.rotation.x=Math.sin(t*1.4)*.25-(tele?.9*Math.min(1,et/(E.len||800)):0);
      ['cl1','cl-1'].forEach(function(kk,i){if(F[kk])F[kk].rotation.y=(i?1:-1)*(Math.sin(t*2)*.1+(tele?.4:0))});
      /* sparks, the trail and the world */
      var a3=sg.attributes.position.array,alive=0;for(var s=0;s<SP;s++){var p=sv[s];if(p.life<=0){a3[s*3+1]=-50;continue}p.life-=dt;p.v.y-=9*dt;a3[s*3]+=p.v.x*dt;a3[s*3+1]+=p.v.y*dt;a3[s*3+2]+=p.v.z*dt;alive++}sg.attributes.position.needsUpdate=true;spm.opacity=alive?1:0;
      var swing=P.st==='light'||P.st==='heavy'||P.st==='special';H.tip.getWorldPosition(v1);H.wpn.getWorldPosition(v2);v2.lerp(v1,.35);
      hist.unshift([v1.x,v1.y,v1.z,v2.x,v2.y,v2.z]);if(hist.length>TN)hist.pop();
      for(var h2=0;h2<TN;h2++){var e2=hist[Math.min(h2,hist.length-1)];var o2=h2*6;if(!swing){e2=hist[0]}for(var q2=0;q2<6;q2++)tp[o2+q2]=e2[q2]}tg.attributes.position.needsUpdate=true;trail.material.opacity=swing?.6:0;
      W.anim.forEach(function(f){f(t,dt)});
      var cr=W.crowd,dm=W.dm;W.seats.forEach(function(sd,i){dm.position.set(sd[0],sd[1]+Math.max(0,Math.sin(t*(4+sd[3]%2)+sd[3]))*.12*(A.combo>=3?2.2:1),sd[2]);dm.lookAt(0,sd[1],0);dm.updateMatrix();cr.setMatrixAt(i,dm.matrix);dm.position.y+=.36;dm.updateMatrix();W.heads.setMatrixAt(i,dm.matrix)});cr.instanceMatrix.needsUpdate=true;W.heads.instanceMatrix.needsUpdate=true;
      W.torches.forEach(function(tc){var f=.85+Math.sin(t*13+tc[3])*.08+Math.sin(t*7.3+tc[3])*.07;tc[0].scale.setScalar(1.1*f);tc[2].intensity=(W.F.night?1.8:.6)*f});
      W.bans.forEach(function(bn){var pa=bn[1].attributes.position.array,pb=bn[2];for(var j=0;j<pa.length;j+=3)pa[j+2]=pb[j+2]+Math.sin(t*3+pb[j]*4+bn[3])*.08*(pb[j]+.45);bn[1].attributes.position.needsUpdate=true});
      /* keep the 2D boxes over the models */
      place(foeW,F.root);place(meW,H.chest);
      lastE=E.st;lastP=P.st;
    });
  }
  function ev(kind,a){
    if(!FG||!CUR||FG.C!==CUR)return;
    if(kind==='hitE'){FG.flashE=a==='light'?.7:1;FG.shake=Math.max(FG.shake,a==='light'?.25:.7);var p=new T.Vector3();(FG.F.head||FG.F.root).getWorldPosition(p);p.z+=.4;FG.burst(p,a==='light'?14:30,a==='special'?'#FFB34A':'#FFE9A8')}
    if(kind==='hitP'){FG.flashP=1;FG.shake=Math.max(FG.shake,.8)}
    if(kind==='block'){var b=new T.Vector3();FG.H.chest.getWorldPosition(b);b.z-=.8;FG.burst(b,18,'#9BC4FF');FG.shake=Math.max(FG.shake,.3)}
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
  return {ok:true,arena:arena,show:show,stop:stop,ev:ev};
})();
function g3ev(k,a){if(G3.ok)G3.ev(k,a)}
