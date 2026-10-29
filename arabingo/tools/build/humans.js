/* ---- human enemies: fighters in the shop's own gear, placed between the creatures ---- */
var HUMANS=[
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
function humanGear(e){var g=e.gear;return {weapon:itemById(g[0])||ITEMS.weapon[0],armour:itemById(g[1])||ITEMS.armour[0],char:itemById(g[2])||ITEMS.char[0],mount:null,field:ITEMS.field[0]}}
function humanSvg(e,cls){return fighterSvg(humanGear(e),'-5 0 175 170',cls||'foeart').replace('<svg ','<svg style="transform:scaleX(-1)" ')}
