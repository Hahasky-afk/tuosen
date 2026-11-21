(function(){
const T=window.T||{};
const picked=new Set();
const C=T.cats||{},TG=T.tags||{},TSN=T.ts||{};
const grid=document.getElementById('grid'),moreBtn=document.getElementById('more'),cnt=document.getElementById('cnt'),srch=document.getElementById('srch');
let P=[],cat='all',q='',shown=0;const STEP=matchMedia('(max-width:700px)').matches?8:20;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function card(p){const [code,img,k,t,z,n]=p;const main=k[0]==='basics'?k[1]:k[0];
 const name=TSN[code]||C[main]||'';const tags=t.map(x=>TG[x]).filter(Boolean).slice(0,2);
 return `<article class="item${n?' made':''}" data-open="${esc(code)}"><div class="ph"><img src="/img/${img}.jpg" alt="${esc(name+' '+code)}" loading="lazy" width="560" height="700">${n?`<span class="mk">${esc(n)} ${esc(T.shipped)}</span>`:''}</div>
<div class="tx"><div class="row"><span>${esc(code)}</span><span class="sz">${esc(z)}</span></div><h3>${esc(name)}</h3>${tags.length?`<p class="tg">${tags.map(esc).join(' · ')}</p>`:''}
<button type="button" class="add" data-code="${esc(code)}" aria-pressed="${picked.has(code)}">${picked.has(code)?T.added:T.add}</button></div></article>`}
const norm=s=>String(s).toUpperCase().replace(/[^A-Z0-9]/g,'');
function list(){const Q=norm(q);return P.filter(p=>(cat==='all'||p[2].includes(cat))&&(!Q||norm(p[0]).includes(Q)))}
function draw(reset){const L=list();if(reset){shown=0;grid.innerHTML=''}
 const next=L.slice(shown,shown+STEP);grid.insertAdjacentHTML('beforeend',next.map(card).join(''));shown+=next.length;
 let ctxt=(T.count||'{n}').replace('{n}',L.length);if(L.length===1)ctxt=ctxt.replace(/\bstyles\b/,'style');
 cnt.textContent=ctxt;moreBtn.parentElement.hidden=shown>=L.length}
function setCat(c){cat=c;document.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x.dataset.c===c));if(P.length)draw(true)}
moreBtn.addEventListener('click',()=>draw(false));
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>setCat(b.dataset.c)));
document.querySelectorAll('a[data-c]').forEach(a=>a.addEventListener('click',()=>setCat(a.dataset.c)));
let st;srch.addEventListener('input',()=>{clearTimeout(st);st=setTimeout(()=>{q=srch.value;draw(true)},150)});

/* 2026-11-21: Dynamic single-product detail view (?style=TS-07) + clickable cards */
const DL={
 en:{wa:'WhatsApp Yang about ',form:'Email / Inquiry Form',copy:'Copy link',copied:'Link copied ✓',note:'Direct factory production in Jieyang, China · Private label & custom sizing available · Send your target spec or quantity to Yang for a quote.',close:'Close'},
 es:{wa:'WhatsApp a Yang sobre ',form:'Formulario de consulta',copy:'Copiar enlace',copied:'Enlace copiado ✓',note:'Producción directa en fábrica en Jieyang, China · Marca privada y tallas a medida · Envía el modelo y cantidad a Yang para cotizar.',close:'Cerrar'},
 pt:{wa:'WhatsApp para Yang sobre ',form:'Formulário de orçamento',copy:'Copiar link',copied:'Link copiado ✓',note:'Produção direta na fábrica em Jieyang, China · Marca própria e grade sob medida · Envie o modelo e quantidade para Yang cotar.',close:'Fechar'},
 fr:{wa:'WhatsApp à Yang pour ',form:'Formulaire de demande',copy:'Copier le lien',copied:'Lien copié ✓',note:'Production directe en usine à Jieyang, Chine · Marque propre et tailles sur mesure · Envoyez le modèle et la quantité à Yang.',close:'Fermer'},
 ar:{wa:'واتساب يانغ حول ',form:'نموذج الاستفسار',copy:'نسخ الرابط',copied:'تم النسخ ✓',note:'تصنيع مباشر في مصنعنا في جييانغ، الصين · علامة تجارية خاصة ومقاسات مخصصة · أرسل الموديل والكمية إلى يانغ لعرض السعر.',close:'إغلاق'},
 zh:{wa:'WhatsApp 聯繫 Yang 詢問 ',form:'填寫詢價表單',copy:'複製款號連結',copied:'已複製 ✓',note:'廣東揭陽工廠直營生產 · 支援貼牌與按尺碼表開版 · 告知款號與數量，Yang 直接為您報價。',close:'關閉'}
};
const langKey=(document.documentElement.lang||'en').toLowerCase().slice(0,2);
const D=DL[langKey]||DL.en;
let modalEl=null,activeCode=null;
function ensureModal(){
 if(modalEl)return modalEl;
 modalEl=document.createElement('div');
 modalEl.className='pmodal';
 modalEl.hidden=true;
 modalEl.setAttribute('role','dialog');
 modalEl.setAttribute('aria-modal','true');
 modalEl.innerHTML='<div class="pm-bg"></div><div class="pm-box"><button type="button" class="pm-x" aria-label="'+esc(D.close)+'">×</button><div class="pm-body"></div></div>';
 document.body.appendChild(modalEl);
 modalEl.querySelector('.pm-bg').addEventListener('click',closeModal);
 modalEl.querySelector('.pm-x').addEventListener('click',closeModal);
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!modalEl.hidden)closeModal()});
 return modalEl;
}
function closeModal(){
 if(!modalEl)return;
 modalEl.hidden=true;activeCode=null;document.body.style.overflow='';
 try{const u=new URL(location.href);if(u.searchParams.has('style')){u.searchParams.delete('style');history.replaceState(null,'',u.pathname+u.search+u.hash)}}catch(e){}
}
function openStyle(rawCode,syncUrl){
 const target=norm(rawCode);
 const p=P.find(x=>norm(x[0])===target);
 if(!p)return false;
 const [code,img,k,t,z,n]=p;
 const main=k[0]==='basics'?k[1]:k[0];
 const name=TSN[code]||C[main]||code;
 const catLbl=C[main]||'';
 const tags=t.map(x=>TG[x]).filter(Boolean);
 const shareUrl=location.origin+location.pathname+'?style='+encodeURIComponent(code);
 const waMsg=`Hi Yang, I saw style ${code} (${name}) on your website and would like more details / a quote.\n${shareUrl}`;
 const waHref='https://wa.me/8615549315379?text='+encodeURIComponent(waMsg);
 const m=ensureModal();
 activeCode=code;
 m.querySelector('.pm-body').innerHTML=`
  <div class="pm-ph"><img src="/img/${img}.jpg" alt="${esc(name+' '+code)}">${n?`<span class="mk">${esc(n)} ${esc(T.shipped)}</span>`:''}</div>
  <div class="pm-info">
   <div class="pm-meta"><span class="pm-code">${esc(code)}</span>${catLbl?`<span>${esc(catLbl)}</span>`:''}${z?`<span class="pm-sz">${esc(z)}</span>`:''}</div>
   <h2>${esc(name)}</h2>
   ${tags.length?`<div class="pm-tags">${tags.map(x=>`<span>${esc(x)}</span>`).join('')}</div>`:''}
   <p class="pm-note">${esc(D.note)}</p>
   <div class="pm-acts">
    <a class="btn" href="${esc(waHref)}" target="_blank" rel="noopener">${esc(D.wa+code)}</a>
    <button type="button" class="btn o pm-inq" data-code="${esc(code)}">${esc(D.form)}</button>
    <button type="button" class="add pm-add" data-code="${esc(code)}" aria-pressed="${picked.has(code)}">${picked.has(code)?T.added:T.add}</button>
    <button type="button" class="pm-cp">${esc(D.copy)}</button>
   </div>
  </div>`;
 m.querySelector('.pm-add').addEventListener('click',()=>{picked.has(code)?picked.delete(code):picked.add(code);drawPicked();const b=m.querySelector('.pm-add');const on=picked.has(code);b.setAttribute('aria-pressed',on);b.textContent=on?T.added:T.add});
 m.querySelector('.pm-inq').addEventListener('click',()=>{if(!picked.has(code)){picked.add(code);drawPicked()}closeModal();const cEl=document.getElementById('contact');if(cEl)cEl.scrollIntoView({behavior:'smooth'})});
 m.querySelector('.pm-cp').addEventListener('click',e=>{const b=e.currentTarget;try{navigator.clipboard.writeText(shareUrl)}catch(err){}b.textContent=D.copied;setTimeout(()=>{b.textContent=D.copy},1800)});
 m.hidden=false;document.body.style.overflow='hidden';
 if(syncUrl){try{const u=new URL(location.href);u.searchParams.set('style',code);history.replaceState(null,'',u.pathname+u.search+u.hash)}catch(e){}}
 return true;
}
function checkUrlStyle(){
 try{const sp=new URLSearchParams(location.search);const s=sp.get('style')||sp.get('s');if(s)openStyle(s,false)}catch(e){}
}
(function load(n){fetch('/products.json?v='+(document.documentElement.dataset.pv||'')).then(r=>{if(!r.ok)throw 0;return r.json()}).then(d=>{P=d;draw(true);checkUrlStyle()}).catch(()=>{if(n<3)setTimeout(()=>load(n+1),800*(n+1));else cnt.textContent=''})})(0);
const box=document.getElementById('picked'),cta=document.getElementById('top-cta'),ctaTxt=cta.textContent;
const contactLinks = Array.from(document.querySelectorAll('a[href^="https://wa.me/"], a[href^="mailto:"]'), link => [link, link.href]);
function drawPicked(){
  for (const [link, original] of contactLinks) {
    const url = new URL(original);
    if (picked.size) {
      const field = url.protocol === 'mailto:' ? 'body' : 'text';
      const message = [url.searchParams.get(field), [...picked].join(', ')].filter(Boolean);
      url.searchParams.set(field, message.join('\n'));
    }
    link.href = url.href;
  }
  box.innerHTML=picked.size?'<span>'+T.picked+'</span>'+[...picked].map(c=>`<button type="button" data-code="${c}">${c} ×</button>`).join(''):'<span>'+T.none+'</span>';
  cta.textContent=picked.size?`${ctaTxt} (${picked.size})`:ctaTxt;
  grid.querySelectorAll('.add').forEach(b=>{const on=picked.has(b.dataset.code);b.setAttribute('aria-pressed',on);b.textContent=on?T.added:T.add});
}
grid.addEventListener('click',e=>{
 const b=e.target.closest('.add');
 if(b){const c=b.dataset.code;picked.has(c)?picked.delete(c):picked.add(c);drawPicked();return}
 const cardEl=e.target.closest('.item[data-open]');
 if(cardEl)openStyle(cardEl.dataset.open,true);
});
box.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;picked.delete(b.dataset.code);drawPicked()});
drawPicked();
document.getElementById('q').addEventListener('submit',e=>{
  e.preventDefault();const f=e.target;if(!f.checkValidity()){f.reportValidity();return}
  const v=id=>document.getElementById(id).value.trim();
  const body=['Name: '+v('f-name'),'Email: '+v('f-mail'),'Country: '+v('f-country'),'Company: '+v('f-co'),'Product: '+v('f-prod'),'Quantity per style: '+v('f-qty'),'Styles: '+([...picked].join(', ')||'-'),'Language: '+document.documentElement.lang,'','Details:',v('f-msg')].join('\n');
  const subj='Inquiry from '+(v('f-co')||v('f-name'))+(v('f-country')?' ('+v('f-country')+')':'');
  const mail=()=>{location.href='mailto:yang@tuosenapparel.com?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body+'\n\n(Attach reference photos or a tech pack to this email.)')};
  const btn=f.querySelector('button[type=submit]');if(btn)btn.disabled=true;
  const fl=[...document.getElementById('f-files').files].slice(0,5);
  if(fl.reduce((a,x)=>a+x.size,0)>10e6){alert('Max 10 MB');if(btn)btn.disabled=false;return}
  const data={_subject:subj,_replyto:v('f-mail'),email:v('f-mail'),_template:'box',_captcha:'false',name:v('f-name'),country:v('f-country'),company:v('f-co'),product:v('f-prod'),quantity:v('f-qty'),styles:[...picked].join(', ')||'-',language:document.documentElement.lang,message:v('f-msg'),_honey:v('f-hp')};
  let req;if(fl.length){const fd=new FormData();Object.entries(data).forEach(([k,x])=>fd.append(k,x));fl.forEach((x,i)=>fd.append('attachment'+(i?i+1:''),x));req={method:'POST',headers:{Accept:'application/json'},body:fd}}
  else req={method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)};
  fetch('https://formsubmit.co/ajax/yang@tuosenapparel.com',req)
  .then(r=>r.json()).then(d=>{if(String(d.success)!=='true')throw 0;document.getElementById('sent').hidden=false;f.reset()})
  .catch(mail).finally(()=>{if(btn)btn.disabled=false});
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

/* scroll reveal: blocks fade up as they enter the viewport (2026-11-16) */
(()=>{if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
const st=document.createElement('style');st.textContent='.rv{opacity:0;transform:translateY(28px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}.rv.in{opacity:1;transform:none}';document.head.appendChild(st);
const sel='section .hd,.cat,.ways article,.film-wrap>*,.facts>div,.step,.recs>*,.promise,.qc li,.qc figure,.terms>div,.about .w>*,.ownrow figure,.faq details,.side,.ct>*,.sizes .w>*,#contact form';
const els=[...document.querySelectorAll(sel)].filter(e=>!e.closest('.hero'));
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.08});
els.forEach(e=>{const sib=[...e.parentElement.children].filter(x=>els.includes(x));const i=Math.min(sib.indexOf(e),5);e.style.transitionDelay=(i*0.08)+'s';
 const r=e.getBoundingClientRect();if(r.top<innerHeight)return; e.classList.add('rv');io.observe(e)});
})();
/* hide floating WhatsApp over the hero on phones (2026-11-17) */
(()=>{const f=document.querySelector('.float'),h=document.querySelector('.hero');if(!f||!h)return;
const u=()=>f.classList.toggle('away',scrollY<h.offsetHeight*0.6);u();addEventListener('scroll',u,{passive:true});})();
