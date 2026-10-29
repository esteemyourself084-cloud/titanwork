# 3D: load Three.js, add tools/build/arena3d.js, and hook it into the fight, the arena lobby and the shop.
# Applied after build_fight.py, rearfix.py and learnfix.py. usage: python3 g3fix.py index.html
import os,sys
f=sys.argv[1];s=open(f,encoding='utf-8').read()
here=os.path.dirname(os.path.abspath(__file__))
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a));s=s.replace(a,b)
THREE='<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n'
if THREE not in s:
    i=s.index('<script>');s=s[:i]+THREE+s[i:]
CSS=r'''
/* 3D: the canvas sits under the HUD layers; the 2D drawings are hidden but kept, so their boxes still place effects */
.g3c{position:absolute;inset:0;width:100%!important;height:100%!important;display:block;z-index:0;outline:0}
.astage.a3d>.abg,.astage.a3d>.fxp,.astage.a3d::after{display:none}
.astage.a3d .foew,.astage.a3d .mew{right:auto;bottom:auto;animation:none!important;transform:none!important;pointer-events:none;z-index:3}
.astage.a3d .foei,.astage.a3d .mew .rear,.astage.a3d .foew::after{visibility:hidden}
.astage.a3d .foew::before{display:none}
.astage.a3d .fxl{z-index:5}
.astage.a3d~.fpad,.astage.a3d~.frow .muted{display:none}
.g3pad{position:absolute;inset:0;z-index:6;pointer-events:none}
.g3pad .joy{position:absolute;width:110px;height:110px;margin:-55px 0 0 -55px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.08),rgba(255,255,255,.18));box-shadow:inset 0 0 0 2px rgba(255,255,255,.4);display:none}
.g3pad .joy.on{display:block}.g3pad .joy i{position:absolute;left:30px;top:30px;width:50px;height:50px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#FFF0C2,#E8B54A 60%,#A86A14);box-shadow:0 4px 10px rgba(0,0,0,.5)}
.g3b{position:absolute;right:max(10px,env(safe-area-inset-right,0px));bottom:10px;display:grid;grid-template-columns:repeat(3,auto);grid-template-areas:". sp he" "ro bl li";gap:8px;align-items:end;pointer-events:none}
.g3k{pointer-events:auto;width:62px;height:62px;border-radius:50%;border:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;cursor:pointer;color:#fff;font-size:22px;line-height:1;
  background:radial-gradient(circle at 40% 30%,rgba(255,255,255,.28),rgba(40,10,6,.72));box-shadow:inset 0 0 0 2px rgba(247,192,74,.7),0 4px 12px rgba(0,0,0,.45);-webkit-tap-highlight-color:transparent;touch-action:none}
.g3k small{font:600 12px/1 var(--f-fn,sans-serif);letter-spacing:.06em;text-transform:uppercase;margin-top:2px}
.g3k.k-light{grid-area:li;width:84px;height:84px;font-size:30px;background:radial-gradient(circle at 40% 30%,#FF8A5A,#8E1A0A)}
.g3k.k-heavy{grid-area:he}.g3k.k-special{grid-area:sp;background:radial-gradient(circle at 40% 30%,#6A8AFF,#121A52)}.g3k.k-special.ready{background:radial-gradient(circle at 40% 30%,#FFF0C2,#E8B54A 60%,#A86A14);color:#2A1600;animation:spglow .5s ease-in-out infinite alternate}
.g3k.k-roll{grid-area:ro}.g3k.k-block{grid-area:bl}
.g3k.down{transform:scale(.92);filter:brightness(1.3)}
.g3hint{position:absolute;left:12px;bottom:10px;margin:0;max-width:46%;padding:6px 10px;border-radius:8px;background:rgba(0,0,0,.45);color:#fff;font-size:12px;line-height:1.4;pointer-events:none}
@media (pointer:coarse){.g3hint{display:none}}
@media (max-width:640px){.g3k{width:52px;height:52px;font-size:18px}.g3k.k-light{width:70px;height:70px;font-size:26px}.g3b{gap:6px}.g3hint{display:none}}
.stagebox.s3d .fighter,.stagebox.s3d .pedestal{visibility:hidden}
.stagebox.s3d .g3c{z-index:1;cursor:grab}.stagebox.s3d .vtog,.stagebox.s3d .pvtag{z-index:3}
.champ3d{position:absolute;left:0;top:0;bottom:0;width:44%;z-index:1}.champ3d .g3c{cursor:grab}.abanner.has3d .champ{visibility:hidden}
@media (max-width:640px){.champ3d{position:relative;width:100%;height:300px;order:-1}}
.itm .pic>svg{animation:itemFloat 3.2s ease-in-out infinite alternate}
.itm:nth-child(3n+1) .pic>svg{animation-delay:-1.1s}.itm:nth-child(3n+2) .pic>svg{animation-delay:-2.2s}
@keyframes itemFloat{from{translate:0 3px;rotate:-2deg}to{translate:0 -5px;rotate:2deg}}
@media (prefers-reduced-motion:reduce){.itm .pic>svg{animation:none}}
'''
if '/* 3D: the canvas sits under the HUD layers' not in s:
    rep('@media (max-width:520px){.nav{gap:2px}',CSS+'@media (max-width:520px){.nav{gap:2px}')
# the fight: start the 3D stage, stop it, and pass on hits
rep("function arenaStop(){if(AR_S){AR_S.dead=1;","function arenaStop(){if(typeof G3!=='undefined')G3.stop();if(AR_S){AR_S.dead=1;")
rep("  aimWeapon();fHud();\n}","  aimWeapon();fHud();\n  if(G3.ok)try{G3.arena(document.getElementById('arStage'),q,e)}catch(err){G3.stop()}\n}")
rep("  var dmg=Math.max(1,Math.round(base));A.e-=dmg;","  var dmg=Math.max(1,Math.round(base));A.e-=dmg;g3ev('hitE',cls==='blk'?'light':kind);")
rep("if(P.st==='block'&&E.kind==='swipe'){dmg*=.22;","if(P.st==='block'&&E.kind==='swipe'){g3ev('block');dmg*=.22;")
rep("else{fSet('p','hurt');A.combo=0;","else{fSet('p','hurt');g3ev('hitP');A.combo=0;")
# the lobby and the shop: the champion on a turntable
rep("""    return open?'<button type="button" class="foe" data-act="arenastart" data-t="'+i+'">'+inner+'</button>':'<div class="foe locked" title="Beat the '+esc(ENEMIES[i-1].en)+' first" aria-disabled="true">'+inner+'</div>';
  }).join('')+'</div></section>';
  V.innerHTML=h;
}""","""    return open?'<button type="button" class="foe" data-act="arenastart" data-t="'+i+'">'+inner+'</button>':'<div class="foe locked" title="Beat the '+esc(ENEMIES[i-1].en)+' first" aria-disabled="true">'+inner+'</div>';
  }).join('')+'</div></section>';
  V.innerHTML=h;
  if(G3.ok)try{var ab=document.querySelector('.abanner'),c3=document.createElement('div');c3.className='champ3d';ab.appendChild(c3);ab.classList.add('has3d');G3.show(c3,q,{back:1})}catch(err){G3.stop()}
}""")
i=s.index('function viewShop(){');j=s.index('\n}\n',i)
body=s[i:j]
assert body.count('  V.innerHTML=h;')==1
s=s[:i]+body.replace('  V.innerHTML=h;',"  V.innerHTML=h;\n  if(G3.ok)try{G3.show(document.querySelector('.stagebox'),q,{back:S.shopView==='back'})}catch(err){G3.stop()}")+s[j:]
G3=open(os.path.join(here,'arena3d.js'),encoding='utf-8').read()
END="window.addEventListener('resize',function(){if(document.querySelector('.rear .wp'))aimWeapon()});"
if 'var G3=(function(){' not in s:
    rep(END,END+'\n'+G3.rstrip('\n'))
open(f,'w',encoding='utf-8').write(s);print('g3 ok')
