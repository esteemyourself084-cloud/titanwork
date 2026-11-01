# Back view: the champion faces the creature, so the forearms, hands and weapon are drawn behind the body and head,
# and the hands show their backs. Applied after build_fight.py.
import sys
f=sys.argv[1];s=open(f,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
HAND="""'<circle class="hand" cx="'+HX+'" cy="'+HY+'" r="13.5" fill="url(#gSkin)" stroke="'+SKIN2+'" stroke-width="1.4"/><path d="M'+(HX-8)+' '+(HY-6)+' q8 5 16 0 M'+(HX-8)+' '+(HY+1)+' q8 5 16 0 M'+(HX-7)+' '+(HY+8)+' q7 4 14 0" stroke="'+SKIN2+'" stroke-width="1.3" fill="none"/>'+rearLeftHand(40)+'</g>';"""
assert HAND in s
# 1. take the weapon arm apart: forearm, weapon and both hands go behind the body; the upper arm stays in front
old_arm=s[s.index("  /* weapon arm: the weapon is aimed at the enemy by aimWeapon() */"):s.index(HAND)+len(HAND)]
front="""  /* weapon arm, upper part: the shoulder and upper arm, in front of the body */
  h+='<g class="rarm" style="transform-origin:200px 128px"><path d="'+ua+'" stroke="'+e+'" stroke-width="36" fill="none" stroke-linecap="round"/><path d="'+ua+'" stroke="'+sl+'" stroke-width="32" fill="none" stroke-linecap="round"/><path d="'+ua+'" stroke="rgba(0,0,0,.2)" stroke-width="10" fill="none" stroke-linecap="round" transform="translate(-6 5)"/><path d="'+ua+'" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".32" transform="translate(4 -7)"/></g>';"""
rep(old_arm,front)
back="""  /* both arms reach forward, away from the camera, so the forearms, the hands (seen from the back) and the weapon
     are drawn first: the body and head then hide the parts behind them. The weapon is aimed by aimWeapon(). */
  var sl=full||!robe?a.col:'#F4F1EA';
  var W=w?(WPN[w.k]||WPN.stick):null,HX=RW.hx,HY=RW.hy,fa='M246 106 L'+HX+' '+HY,ua='M204 128 L246 106';
  h+=rearLeftArm(e,sl,full,f,40);
  h+='<g class="rarm" style="transform-origin:200px 128px"><path d="'+fa+'" stroke="'+e+'" stroke-width="28" fill="none" stroke-linecap="round"/><path d="'+fa+'" stroke="'+sl+'" stroke-width="24" fill="none" stroke-linecap="round"/>'+(full?'<path d="M240 92 L'+HX+' '+HY+'" stroke="'+e+'" stroke-width="27" stroke-linecap="round"/><path d="M240 92 L'+HX+' '+HY+'" stroke="'+f+'" stroke-width="22" stroke-linecap="round"/>':'');
  if(W)h+='<g class="wp" data-gx="'+W.g[0]+'" data-gy="'+W.g[1]+'" data-k="'+w.k+'" transform="translate('+HX+' '+HY+') rotate(26) scale(1.75) translate('+(-W.g[0])+' '+(-W.g[1])+')">'+W.a+'</g>';
  h+=backFist(HX,HY,12.5,'hand')+rearLeftHand(40)+'</g>';
  /* torso */"""
rep("  /* torso */\n",back+"\n")
# 2. the left arm and the colour of the sleeves are now set before the torso
rep("""  /* left arm */
  var sl=full||!robe?a.col:'#F4F1EA';
  h+=rearLeftArm(e,sl,full,f,40);
""","")
# 3. hands seen from the back: a fist with the knuckles on the far side and the thumb wrapped round the grip
rep("""function rearLeftHand(ang){""","""function backFist(x,y,r,cls){
  return '<g'+(cls?' class="'+cls+'"':'')+' transform="translate('+x+' '+y+')"><ellipse rx="'+r+'" ry="'+(r*.92).toFixed(1)+'" fill="url(#gSkin)" stroke="'+SKIN2+'" stroke-width="1.4"/>'+
    '<path d="M'+(-r*.72).toFixed(1)+' '+(-r*.38).toFixed(1)+' Q0 '+(-r*1.02).toFixed(1)+' '+(r*.72).toFixed(1)+' '+(-r*.38).toFixed(1)+'" stroke="'+SKIN2+'" stroke-width="1.5" fill="none" opacity=".75"/>'+
    '<ellipse cx="'+(-r*.18).toFixed(1)+'" cy="'+(r*.28).toFixed(1)+'" rx="'+(r*.5).toFixed(1)+'" ry="'+(r*.34).toFixed(1)+'" fill="rgba(0,0,0,.12)"/>'+
    '<path d="M'+(r*.55).toFixed(1)+' '+(r*.2).toFixed(1)+' q'+(r*.35).toFixed(1)+' '+(r*.3).toFixed(1)+' '+(r*.05).toFixed(1)+' '+(r*.72).toFixed(1)+'" stroke="'+SKIN2+'" stroke-width="1.3" fill="none"/></g>';
}
function rearLeftHand(ang){""")
rep("""return '<g class="lh" transform="translate('+g.hx.toFixed(1)+' '+g.hy.toFixed(1)+')"><circle r="12.2" fill="url(#gSkin)" stroke="'+SKIN2+'" stroke-width="1.4"/><path d="M-8 -5 q8 5 16 0 M-8 1 q8 5 16 0 M-7 7 q7 4 14 0" stroke="'+SKIN2+'" stroke-width="1.3" fill="none"/></g>';""",
    """return '<g class="lh" transform="translate('+g.hx.toFixed(1)+' '+g.hy.toFixed(1)+')">'+backFist(0,0,11.4)+'</g>';""")
open(f,'w',encoding='utf-8').write(s);print('rear ok')
