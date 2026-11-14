(function(){
const T=window.T||{};
const picked=new Set();
const C=T.cats||{},TG=T.tags||{},TSN=T.ts||{};
const grid=document.getElementById('grid'),moreBtn=document.getElementById('more'),cnt=document.getElementById('cnt'),srch=document.getElementById('srch');
let P=[],cat='all',q='',shown=0;const STEP=20;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function card(p){const [code,img,k,t,z,n]=p;const main=k[0]==='basics'?k[1]:k[0];
 const name=TSN[code]||C[main]||'';const tags=t.map(x=>TG[x]).filter(Boolean).slice(0,2);
 return `<article class="item${n?' made':''}"><div class="ph"><img src="/img/${img}.jpg" alt="${esc(name+' '+code)}" loading="lazy" width="560" height="700">${n?`<span class="mk">${esc(n)} ${esc(T.shipped)}</span>`:''}</div>
<div class="tx"><div class="row"><span>${esc(code)}</span><span class="sz">${esc(z)}</span></div><h3>${esc(name)}</h3>${tags.length?`<p class="tg">${tags.map(esc).join(' · ')}</p>`:''}
<button type="button" class="add" data-code="${esc(code)}" aria-pressed="${picked.has(code)}">${picked.has(code)?T.added:T.add}</button></div></article>`}
function list(){const Q=q.trim().toUpperCase();return P.filter(p=>(cat==='all'||p[2].includes(cat))&&(!Q||p[0].toUpperCase().includes(Q)))}
function draw(reset){const L=list();if(reset){shown=0;grid.innerHTML=''}
 const next=L.slice(shown,shown+STEP);grid.insertAdjacentHTML('beforeend',next.map(card).join(''));shown+=next.length;
 cnt.textContent=(T.count||'{n}').replace('{n}',L.length);moreBtn.parentElement.hidden=shown>=L.length}
function setCat(c){cat=c;document.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.c===c));if(P.length)draw(true)}
moreBtn.addEventListener('click',()=>draw(false));
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>setCat(b.dataset.c)));
document.querySelectorAll('a[data-c]').forEach(a=>a.addEventListener('click',()=>setCat(a.dataset.c)));
let st;srch.addEventListener('input',()=>{clearTimeout(st);st=setTimeout(()=>{q=srch.value;draw(true)},150)});
fetch('/products.json').then(r=>r.json()).then(d=>{P=d;draw(true)}).catch(()=>{cnt.textContent=''});
const box=document.getElementById('picked'),cta=document.getElementById('top-cta'),ctaTxt=cta.textContent;
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
