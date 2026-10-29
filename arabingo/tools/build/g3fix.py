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
G3=open(os.path.join(here,'arena3d.js'),encoding='utf-8').read()
END="window.addEventListener('resize',function(){if(document.querySelector('.rear .wp'))aimWeapon()});"
if 'var G3=(function(){' not in s:
    rep(END,END+'\n'+G3.rstrip('\n'))
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
open(f,'w',encoding='utf-8').write(s);print('g3 ok')
