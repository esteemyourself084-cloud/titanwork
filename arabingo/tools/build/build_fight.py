import sys,re,subprocess
sp=sys.argv[1]
s=open(sys.argv[2],encoding='utf-8').read() if len(sys.argv)>2 else subprocess.run(['git','show','HEAD:arabingo/index.html'],capture_output=True,text=True).stdout
R=lambda n:open(sp+'/'+n,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(a[:80],c);s=s.replace(a,b)
def between(a,b,new,keep_b=True):
    global s
    i=s.index(a);j=s.index(b,i);s=s[:i]+new+(s[j:] if keep_b else s[j+len(b):])
rep('family=Lilita+One&display=swap','family=Lilita+One&family=Teko:wght@500;600&family=Lalezar&display=swap')
between('/* shop and arena skin: a 3D game lobby.','/* arena vignette + grade */' if '/* arena vignette + grade */' in s else '@media (max-width:520px){.nav',R('skin2.css'))
rep("""'<radialGradient id="gOrb\"""","""XG('gDam',[[0,'#5D6874'],[.4,'#C4CCD6'],[.55,'#9AA5B1'],[1,'#46505B']],1,0)+XG('gDarkS',[[0,'#2A2F37'],[.45,'#8C96A3'],[.6,'#5A636E'],[1,'#1E2229']],1,0)+
    XG('gBright',[[0,'#9FB2C6'],[.42,'#FFFFFF'],[.58,'#E6F2FF'],[1,'#8AA0B8']],1,0)+XG('gPoison',[[0,'#3E6A38'],[.45,'#C8F5B4'],[.6,'#86C46E'],[1,'#2E5A26']],1,0)+
    XG('gBlunt',[[0,'#6E737A'],[.5,'#B3B8BE'],[1,'#5C6168']],1,0)+'<filter id="swGlow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2.4"/></filter>'+
    '<radialGradient id="gOrb\"""")
rep('/* ===== extra gradients, clip paths and patterns ===== */',R('swords.js')+'/* ===== extra gradients, clip paths and patterns ===== */')
W=R('weapons.js')
NEWW=['w%d'%n for n in range(17,42)]
W=re.sub(r"id:'(w\d+)'",lambda m:"id:'w1%02d'"%int(m.group(1)[1:]) if m.group(1) in NEWW else m.group(0),W)
bi=s.index('  weapon:[\n');bj=s.index('  armour:[\n',bi)
mineids=set(re.findall(r"id:'(w\d+)'",W))
extra=[l.rstrip().rstrip(',').rstrip(']') for l in s[bi:bj].splitlines() if re.match(r"\s*\{id:'(w\d+)'",l) and re.match(r"\s*\{id:'(w\d+)'",l).group(1) not in mineids]
if extra:W=W.rstrip().rstrip(',')[:-1]+',\n'+',\n'.join(extra)+'],\n'
between('  weapon:[\n','  armour:[\n',W)
ARM="""
    {id:'a16',ar:'الدِّرْعُ التُّبَّعِيَّةُ',en:'Tubbaʿi Mail',price:1650,def:17,col:'#C9A15A',edge:'#6A4A1E',g:'gLaboos',pat:'ring',trim:'#F4CB4C',skirt:1,full:1,belt:'#5A3416',d:'Mail of the Tubbaʿ, the old kings of Yemen.'},
    {id:'a17',ar:'الدِّرْعُ الحُطَمِيَّةُ',en:'Hutamiyya Mail',price:2400,def:21,col:'#5A636E',edge:'#1E2229',g:'gSteel2',pat:'plate',trim:'#C9D0D8',full:1,d:'Heavy mail so strong that swords break on it.'}],"""
MNT="""
    {id:'m20',ar:'الحِصَانُ العُبَيَّانُ',en:'ʿUbayyan Stallion',price:380,time:2,xp:1.3,kind:'horse',col:'#6B4A2E',dk:'#3E2814',mane:'#1A0E06',blanket:'#C9A227',d:'A dark bay of the ʿUbayyan, one of the five classic Arabian strains.'},
    {id:'m21',ar:'النَّاقَةُ العُمَانِيَّةُ',en:'Omani Camel',price:560,time:3,xp:1.55,kind:'camel',col:'#E0C49A',dk:'#A88A5E',mane:'#8A6434',blanket:'#2F6FB0',d:'The light, fast racing camel of Oman.'},
    {id:'m22',ar:'الحِصَانُ الحَمْدَانِيُّ',en:'Hamdani Grey',price:750,time:3,xp:1.7,kind:'horse',col:'#B9BCC2',dk:'#7D8189',mane:'#4A4C52',blanket:'#7A1F3D',d:'A grey of the Hamdani strain, strong and tireless.'},
    {id:'m23',ar:'نَاقَةُ المَجَاهِيمِ',en:'Majahim Camel',price:850,time:4,xp:1.8,kind:'camel',col:'#3A2E28',dk:'#1E1712',mane:'#120C08',blanket:'#C9A227',d:'The great black camels of Najd, prized for their size.'},
    {id:'m24',ar:'الفَرَسُ الهَدْبَاءُ',en:'Hadban Mare',price:1000,time:4,xp:2,kind:'mare',col:'#C46A3A',dk:'#7A3A18',mane:'#F3E3C0',blanket:'#1F5E8C',gold:1,d:'A chestnut mare of the Hadban strain with a pale mane.'},
    {id:'m25',ar:'نَاقَةُ المَغَاتِيرِ',en:'Maghatir Camel',price:1250,time:4,xp:2.2,kind:'camel',col:'#F4EEE2',dk:'#C8BDA8',mane:'#B8AA90',blanket:'#7A1F3D',d:'The famous white camels of the Arabian Peninsula.'},
    {id:'m26',ar:'الحِصَانُ المُعَنَّقِيُّ',en:'Muniqi Racer',price:1550,time:5,xp:2.4,kind:'horse',col:'#2A1C14',dk:'#120B07',mane:'#050302',blanket:'#D9A21B',d:'A black Muniqi, the fastest racing strain of the desert.'}],"""
CHR="""
    {id:'c16',ar:'الصُّعْلُوكُ',en:'The Suʿluk',price:650,t:'nomad',d:'A wandering desert warrior-poet, like al-Shanfarā.',wear:'#4A3A2A'},
    {id:'c19',ar:'الطَّبِيبَةُ',en:'The Physician',price:500,t:'khimar',girl:1,d:'Heals the wounded after every battle.',wear:'#3D7A9E'},
    {id:'c20',ar:'الفَلَكِيُّ',en:'The Astronomer',price:750,t:'turban',d:'Finds the way by the stars.',wear:'#2A2F5E'},
    {id:'c21',ar:'الشَّاعِرَةُ',en:'The Poet',price:850,t:'hijab',girl:1,d:'Her verses are sharper than swords, like al-Khansāʾ.',wear:'#7A1F3D'},
    {id:'c18',ar:'السِّنْدِبَادُ',en:'Sindbad',price:950,t:'turban',d:'The sailor of the Thousand and One Nights, back from seven voyages.',wear:'#1F5E8C'},
    {id:'c17',ar:'المَمْلُوكُ',en:'The Mamluk',price:1100,t:'helmet',d:'A heavy cavalryman of the Mamluk army.',wear:'#8E1F2A',cape:'#5A0E14'},
    {id:'c22',ar:'شَيْخُ القَبِيلَةِ',en:'The Shaykh',price:1300,t:'ghutra',d:'The wise leader of his tribe, in his cloak.',wear:'#5A3416',cape:'#3A2410'},
    {id:'c23',ar:'القَائِدَةُ',en:'The Commander',price:1700,t:'warrg',girl:1,d:'Leads the riders into battle.',wear:'#2F4A8A',cape:'#1E2E5A'},
    {id:'c25',ar:'عَنْتَرَةُ',en:'ʿAntara',price:1800,t:'helmet',d:'The legendary knight-poet ʿAntara ibn Shaddād.',wear:'#2A2A2E',cape:'#7A1F3D'},
    {id:'c24',ar:'الخَلِيفَةُ',en:'The Caliph',price:2000,t:'sultan',d:'Rules a great empire from his palace.',wear:'#1E5E3A',cape:'#0E3A22'}],"""
def hund(t):return re.sub(r"id:'([amc])(\d+)'",lambda m:"id:'%s1%02d'"%(m.group(1),int(m.group(2))),t)
ARM,MNT,CHR=hund(ARM),hund(MNT),hund(CHR)
for cat,add in (('armour',ARM),('mount',MNT),('char',CHR)):
    i=s.index('  '+cat+':[\n');j=s.index('}],\n',i)
    s=s[:j]+'},'+add[:-1]+s[j+2:]
if "it.rar=Math.floor(i/3)" in s: rep("ITEMS[k].forEach(function(it,i){it.rar=Math.floor(i/3)})","ITEMS[k].forEach(function(it,i,a){it.rar=Math.floor(i*5/a.length)})")
if "var STAT_MAX={weapon:38," in s: rep("var STAT_MAX={weapon:38,","var STAT_MAX={weapon:48,")
rep('<h2>Item Shop</h2>','<h2>Armory</h2>')
i=s.index('/* ================= arena ================= */')
endm='\n\n/* shop tiles and enemy cards tilt' if '\n\n/* shop tiles and enemy cards tilt' in s[i:] else '\n\n/* ---------- words ---------- */'
j=s.index(endm,i)
aim=re.search(r'\nfunction aimWeapon\(\)\{.*?\n\}\n',s[i:j],re.S).group(0)
F=R('fight.js')
F=re.sub(r'\nfunction aimWeapon\(\)\{.*?\n\}\n',lambda m:aim,F,count=1,flags=re.S)
s=s[:i]+F.rstrip('\n')+s[j:]
open('index.html','w',encoding='utf-8').write(s)
print('ok')
