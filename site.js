(function(){
const T=window.T||{};
const P=[
["r078","T38","tees"],["r046","Z12","sets"],["r155","N04","polos"],["r104","NWY10","sweats"],["r134","G09","shirts"],
["r076","T52","tees"],["r054","TZ12","sets"],["r143","Z0114","polos"],["r047","Z11","tees"],["r139","G04","shirts"],
["r199","B01","sets"],["r250","N58","polos"],["r075","T53","tees"],["r188","NWY11","sweats"],["r053","TZ023","sets"],
["r135","G08","shirts"],["r079","T37","tees"],["r144","Z0113","polos"],["r147","TZ0113","sets"],["r137","G07","shirts"],
["r048","Z024","tees"],["r145","Z0112","polos"],["r140","G03","shirts"],["r142","G01","shirts"]];
const N=T.names||{};
const grid=document.getElementById('grid'),moreBtn=document.getElementById('more');
let cat='all',showAll=false;
grid.innerHTML=P.map(([img,code,c])=>`<article class="item" data-cat="${c}">
<img src="/img/p/${img}.jpg" alt="${(N[code]||'')} ${code}" loading="lazy" width="800" height="1000">
<div class="tx"><div class="row"><span>${code}</span><span class="sz">M–8XL</span></div>
<h3>${N[code]||code}</h3>
<button type="button" class="add" data-code="${code}" aria-pressed="false">${T.add}</button></div></article>`).join('');
const items=[...grid.querySelectorAll('.item')];
function draw(){let n=0;items.forEach(i=>{const ok=cat==='all'||i.dataset.cat===cat;const vis=ok&&(showAll||cat!=='all'||n<10);if(ok)n++;i.hidden=!vis});moreBtn.parentElement.hidden=showAll||cat!=='all'}
function setCat(c){cat=c;document.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.c===c));draw()}
draw();
moreBtn.addEventListener('click',()=>{showAll=true;draw()});
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>setCat(b.dataset.c)));
document.querySelectorAll('a[data-c]').forEach(a=>a.addEventListener('click',()=>setCat(a.dataset.c)));
const picked=new Set(),box=document.getElementById('picked'),cta=document.getElementById('top-cta'),ctaTxt=cta.textContent;
function drawPicked(){
  box.innerHTML=picked.size?'<span>'+T.picked+'</span>'+[...picked].map(c=>`<button type="button" data-code="${c}">${c} ×</button>`).join(''):'<span>'+T.none+'</span>';
  cta.textContent=picked.size?`${ctaTxt} (${picked.size})`:ctaTxt;
  grid.querySelectorAll('.add').forEach(b=>{const on=picked.has(b.dataset.code);b.setAttribute('aria-pressed',on);b.textContent=on?T.added:T.add});
}
grid.addEventListener('click',e=>{const b=e.target.closest('.add');if(!b)return;const c=b.dataset.code;picked.has(c)?picked.delete(c):picked.add(c);drawPicked()});
box.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;picked.delete(b.dataset.code);drawPicked()});
drawPicked();
document.getElementById('q').addEventListener('submit',e=>{
  e.preventDefault();const f=e.target;if(!f.checkValidity()){f.reportValidity();return}
  const v=id=>document.getElementById(id).value.trim();
  const body=['Name: '+v('f-name'),'Email: '+v('f-mail'),'Country: '+v('f-country'),'Company: '+v('f-co'),'Product: '+v('f-prod'),'Quantity per style: '+v('f-qty'),'Styles: '+([...picked].join(', ')||'-'),'Language: '+document.documentElement.lang,'','Details:',v('f-msg'),'','(Attach reference photos or a tech pack to this email.)'].join('\n');
  location.href='mailto:yang@tuosenapparel.com?subject='+encodeURIComponent('Inquiry from '+(v('f-co')||v('f-name'))+(v('f-country')?' ('+v('f-country')+')':''))+'&body='+encodeURIComponent(body);
  document.getElementById('sent').hidden=false;
});
const fv=document.getElementById('filmv'),fb=document.getElementById('filmbox');
document.getElementById('filmplay').addEventListener('click',()=>{fb.classList.add('on');fv.controls=true;fv.play()});
const bar=document.getElementById('top-bar');addEventListener('scroll',()=>bar.classList.toggle('s',scrollY>40),{passive:true});
document.addEventListener('click',e=>{const d=document.querySelector('.lang[open]');if(d&&!d.contains(e.target))d.removeAttribute('open')});
document.querySelectorAll('.lang a').forEach(a=>a.addEventListener('click',()=>{try{localStorage.setItem('lang',a.hreflang)}catch(e){}}));
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
if('IntersectionObserver' in window&&!rm){const io=new IntersectionObserver(es=>es.forEach(en=>{const v=en.target;if(en.isIntersecting){v.play().catch(()=>{})}else v.pause()}),{threshold:.35});document.querySelectorAll('video[data-auto]').forEach(v=>io.observe(v))}
if(rm){const h=document.querySelector('.hero video');h.removeAttribute('autoplay');h.pause()}
})();
