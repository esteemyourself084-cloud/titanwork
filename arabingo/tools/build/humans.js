/* ---- human enemies: fighters in the shop's own gear, placed between the creatures ---- */
var HUMANS=[
  /* riders: their mount is the fourth piece of gear */
  ['wolf',{k:'h_rider',ar:'الفَارِسُ البَدَوِيُّ',en:'The Bedouin Rider',hp:150,hit:13,fx:'slash',bg:'dunes',gear:['w2','a1','c10','m2'],kit:['charge','swipe']}],
  ['tiger',{k:'h_camel',ar:'هَجَّانُ الغُزَاةِ',en:'The Camel Raider',hp:300,hit:20,fx:'slash',bg:'canyon',gear:['w4','a5','c4','m3'],kit:['arrow','charge'],ranged:1}],
  ['elephant',{k:'h_cavalier',ar:'الفَارِسُ المَمْلُوكِيُّ',en:'The Mamluk Cavalier',hp:420,hit:26,fx:'slash',bg:'night',gear:['w8','a13','c117','m15'],kit:['charge','swipe','slam']}],
  ['dragon',{k:'h_lancer',ar:'فَارِسُ الرُّمْحِ',en:'The Desert Lancer',hp:520,hit:31,fx:'slash',bg:'volcano',gear:['w5','a14','c122','m126'],kit:['charge','swipe']}],
  ['scorpion',{k:'h_thief',ar:'اللِّصُّ',en:'The Thief',hp:85,hit:10,fx:'slash',bg:'dunes',gear:['w1','a1','c116'],kit:['swipe','charge']}],
  ['hyena',{k:'h_highway',ar:'قَاطِعُ الطَّرِيقِ',en:'The Highwayman',hp:140,hit:13,fx:'slash',bg:'canyon',gear:['w2','a5','c10'],kit:['swipe','slam']}],
  ['bull',{k:'h_archer',ar:'رَامِي الغُزَاةِ',en:'The Raider Archer',hp:170,hit:14,fx:'slash',bg:'savanna',gear:['w4','a1','c4'],kit:['arrow','swipe'],ranged:1}],
  ['panther',{k:'h_merc',ar:'المُرْتَزِقُ',en:'The Mercenary',hp:235,hit:17,fx:'slash',bg:'night',gear:['w6','a2','c2'],kit:['swipe','slam']}],
  ['viper',{k:'h_duel',ar:'المُبَارِزَةُ',en:'The Swordswoman',hp:265,hit:19,fx:'slash',bg:'canyon',gear:['w7','a7','c8'],kit:['swipe','charge'],fast:1}],
  ['crocodile',{k:'h_knight',ar:'الفَارِسُ الأَسْوَدُ',en:'The Black Knight',hp:330,hit:22,fx:'slash',bg:'night',gear:['w8','a15','c117'],kit:['swipe','slam']}],
  ['rhino',{k:'h_chief',ar:'قَائِدُ الغُزَاةِ',en:'The Raider Chief',hp:445,hit:28,fx:'slash',bg:'dunes',gear:['w5','a13','c122'],kit:['swipe','charge','slam']}],
  [null,{k:'h_champ',ar:'بَطَلُ السَّاحَةِ',en:'The Arena Champion',hp:620,hit:36,fx:'slash',bg:'volcano',gear:['w9','a14','c125'],kit:['swipe','charge','slam']}]];
HUMANS.forEach(function(h){
  var e=h[1];e.human=1;if(ENEMIES.some(function(x){return x.k===e.k}))return;
  var i=h[0]?ENEMIES.map(function(x){return x.k}).indexOf(h[0]):-1;
  if(i<0)ENEMIES.push(e);else ENEMIES.splice(i+1,0,e);
});
function humanGear(e){var g=e.gear;return {weapon:itemById(g[0])||ITEMS.weapon[0],armour:itemById(g[1])||ITEMS.armour[0],char:itemById(g[2])||ITEMS.char[0],mount:g[3]&&itemById(g[3])||null,field:ITEMS.field[0]}}
function humanSvg(e,cls){return fighterSvg(humanGear(e),'-5 0 175 170',cls||'foeart').replace('<svg ','<svg style="transform:scaleX(-1)" ')}
