(function(){
const D=window.STUDY_DATA, $=s=>document.querySelector(s), main=$('#main');
const byId={}; D.disciplines.forEach(d=>byId[d.id]=d);
const store={get(k,def){try{const v=localStorage.getItem('estudos:'+k);return v?JSON.parse(v):def}catch(e){return def}},
 set(k,v){try{localStorage.setItem('estudos:'+k,JSON.stringify(v))}catch(e){}}};
let done=store.get('done',{}), qdone=store.get('q',{}), cardState=store.get('cards',{}), planDone=store.get('plan',{});
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const short=t=>t.replace(/^(Un)?[Ss]upervised ML — /,'').replace(/\s*\([^)]*\)/g,'').replace(/^Análise de /,'').replace(/^Introdução à /,'').replace(/ \+ .*$/,'').replace(/^Análise da /,'');
const pad=n=>String(n).padStart(2,'0');


const CALL={'exemplo':'ex','exemplo resolvido':'ex','na prática':'ex','atenção':'warn','cuidado':'warn','armadilha':'warn','memorize':'mem','regra de ouro':'mem','analogia':'ana','destaque do professor':'prof','dica do professor':'prof','em uma frase':'mem'};
function enhance(root){
  root.querySelectorAll('blockquote').forEach(b=>{const s=b.querySelector('p>strong');if(!s)return;const k=s.textContent.trim().replace(/[.:]$/,'').toLowerCase();const c=CALL[k];if(c){b.classList.add('callout','c-'+c);}});
  root.querySelectorAll('pre>code.language-mermaid').forEach(c=>{const d=document.createElement('div');d.className='mermaid';d.textContent=c.textContent;c.parentNode.replaceWith(d);});
  root.querySelectorAll('img').forEach(i=>{if(i.alt&&!i.closest('figure')){const f=document.createElement('figure');i.replaceWith(f);f.appendChild(i);const cp=document.createElement('figcaption');cp.textContent=i.alt;f.appendChild(cp);}});
  const go=()=>{try{if(window.renderMathInElement)renderMathInElement(root,{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],ignoredClasses:['mermaid'],throwOnError:false});}catch(e){}
    try{if(window.mermaid){const dark=(document.documentElement.dataset.theme||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light'))==='dark';mermaid.initialize({startOnLoad:false,theme:dark?'dark':'default',securityLevel:'loose',flowchart:{useMaxWidth:false,htmlLabels:true,curve:'basis'},themeVariables:{fontSize:'16px'}});
      root.querySelectorAll('.mermaid').forEach((n,k)=>{const src=n.textContent;n.dataset.src=src;mermaid.render('mmd'+Date.now()+'_'+k,src).then(r=>{n.innerHTML=r.svg;}).catch(e=>{n.innerHTML='<pre>'+src.replace(/</g,'&lt;')+'</pre>';});});}}catch(e){}};
  if(window.renderMathInElement&&window.mermaid)go();else window.addEventListener('load',go);
}

function buildNav(cur){
  let h='<div class="nav-top"><a class="nav-a'+(cur==='home'?' on':'')+'" href="#/">Início</a><a class="nav-a'+(cur==='plano'?' on':'')+'" href="#/plano">Plano</a><a class="nav-a'+(cur==='cards'?' on':'')+'" href="#/cards">Flashcards</a><a class="nav-a'+(cur==='quiz'?' on':'')+'" href="#/quiz">Autoteste</a></div>';
  D.groups.forEach(g=>{h+='<div class="nav-h">'+esc(g.name)+'</div>';
    g.ids.forEach(id=>{const d=byId[id];if(!d)return;
      h+='<a class="nav-a'+(cur==='d'+id?' on':'')+'" href="#/d/'+id+'"><span class="n">'+pad(id)+'</span><span title="'+esc(d.title)+'">'+esc(d.short)+'</span>'+(done[id]?'<span class="dn">✓</span>':'')+'</a>'});});
  $('#navList').innerHTML=h;
  const n=Object.values(done).filter(Boolean).length;
  $('#globalProgress').textContent=n+'/'+D.disciplines.length+' estudadas';
}
function prog(p){return '<div class="bar"><i style="width:'+Math.round(p*100)+'%"></i></div>'}

function home(){
  buildNav('home');
  const n=Object.values(done).filter(Boolean).length, tot=D.disciplines.length;
  const cards=D.disciplines.reduce((a,d)=>a+d.cards.length,0), qs=D.disciplines.reduce((a,d)=>a+d.questions.length,0);
  const known=Object.values(cardState).filter(v=>v==='ok').length, qd=Object.values(qdone).filter(Boolean).length;
  let h='<h1>Estudos — MBA Data Science e Analytics</h1><p class="meta">Resumos de '+tot+' disciplinas, plano de estudos, flashcards e autoteste. Seu progresso fica salvo neste navegador.</p>';
  h+='<div class="card"><div class="row"><b>Disciplinas estudadas</b><span class="meta">'+n+' de '+tot+'</span></div>'+prog(n/tot)+
     '<div class="row" style="margin-top:12px"><b>Flashcards dominados</b><span class="meta">'+known+' de '+cards+'</span></div>'+prog(cards?known/cards:0)+
     '<div class="row" style="margin-top:12px"><b>Perguntas que consigo responder</b><span class="meta">'+qd+' de '+qs+'</span></div>'+prog(qs?qd/qs:0)+'</div>';
  h+='<div class="row"><a class="btn" href="#/plano">Abrir plano de estudos</a><a class="btn ghost" href="#/cards">Flashcards</a><a class="btn ghost" href="#/quiz">Autoteste</a></div>';
  D.groups.forEach(g=>{h+='<h2>'+esc(g.name)+'</h2><div class="home-grid">';
    g.ids.forEach(id=>{const d=byId[id];if(!d)return;h+='<a href="#/d/'+id+'"><span class="tag">'+pad(id)+'</span>'+(d.priority?'<span class="tag">'+esc(d.priority.toLowerCase())+'</span>':'')+(done[id]?'<span class="tag" style="color:var(--ok)">✓</span>':'')+'<div><b>'+esc(d.title)+'</b></div><div class="meta">'+d.cards.length+' cards · '+d.questions.length+' perguntas</div></a>'});
    h+='</div>'});
  main.innerHTML=h;
}

function disc(id){
  const d=byId[id]; if(!d)return home();
  buildNav('d'+id);
  const i=D.disciplines.indexOf(d), prev=D.disciplines[i-1], next=D.disciplines[i+1];
  let h='<div class="meta">'+(d.priority?'<span class="tag">prioridade: '+esc(d.priority.toLowerCase())+'</span>':'')+'</div>';
  const tocLinks=d.toc.map(t=>'<a href="#" data-sec="'+t.id+'">'+esc(t.name)+'</a>').join('');
  h='<div class="page"><article>'+h+'<details class="toc-m"><summary>Nesta página</summary><div class="toc-l">'+tocLinks+'</div></details><div id="doc">'+d.html+'</div>';
  h+='<div class="card row"><label><input type="checkbox" id="doneCb" '+(done[id]?'checked':'')+'> Marcar como estudada</label><span class="spacer" style="flex:1"></span>'+
     (d.cards.length?'<a class="btn ghost" href="#/cards/'+id+'">Flashcards ('+d.cards.length+')</a>':'')+(d.questions.length?'<a class="btn ghost" href="#/quiz/'+id+'">Autoteste ('+d.questions.length+')</a>':'')+'</div>';
  h+='<div class="row">'+(prev?'<a class="btn ghost" href="#/d/'+prev.id+'">← '+esc(prev.title)+'</a>':'')+'<span style="flex:1"></span>'+(next?'<a class="btn ghost" href="#/d/'+next.id+'">'+esc(next.title)+' →</a>':'')+'</div>';
  h+='</article><aside class="page-toc"><div class="pt-h">Nesta página</div>'+tocLinks+'</aside></div>';
  main.innerHTML=h;enhance(main);
  main.querySelectorAll('[data-sec]').forEach(a=>a.onclick=e=>{e.preventDefault();const el=document.getElementById(a.dataset.sec);if(el)el.scrollIntoView()});
  $('#doneCb').onchange=e=>{done[id]=e.target.checked;store.set('done',done);buildNav('d'+id)};
}

function plan(){
  buildNav('plano');
  main.innerHTML='<div id="planDoc">'+D.plan+'</div>';enhance(main);
  const rows=[...main.querySelectorAll('#planDoc tbody tr')].filter(tr=>/^\d+$/.test(tr.cells[0].textContent.trim()));
  rows.forEach(tr=>{const day=tr.cells[0].textContent.trim();const cb=document.createElement('input');cb.type='checkbox';cb.className='plan-cb';cb.checked=!!planDone[day];
    const apply=()=>tr.classList.toggle('plan-done',cb.checked);apply();
    cb.onchange=()=>{planDone[day]=cb.checked;store.set('plan',planDone);apply();upd()};
    tr.cells[0].prepend(cb)});
  const bar=document.createElement('div');bar.className='card';main.prepend(bar);
  function upd(){const n=rows.filter(r=>planDone[r.cells[0].textContent.trim()]).length;bar.innerHTML='<div class="row"><b>Progresso do plano</b><span class="meta">'+n+' de '+rows.length+' dias concluídos</span></div>'+prog(rows.length?n/rows.length:0)}
  upd();
}

function allCards(only){const out=[];D.disciplines.forEach(d=>{if(only&&d.id!==only)return;d.cards.forEach((c,i)=>out.push({k:d.id+':'+i,d:d,q:c.q,a:c.a}))});return out}
function cards(only){
  buildNav('cards');
  only=only?+only:0;
  let deck=allCards(only), mode=store.get('cardMode','pend');
  const sel='<select id="cdSel" class="btn ghost" style="max-width:100%"><option value="0">Todas as disciplinas</option>'+D.disciplines.filter(d=>d.cards.length).map(d=>'<option value="'+d.id+'"'+(d.id===only?' selected':'')+'>'+pad(d.id)+' · '+esc(d.title)+' ('+d.cards.length+')</option>').join('')+'</select>';
  let cur=null, flipped=false;
  function pick(){let pool=deck;if(mode==='pend')pool=deck.filter(c=>cardState[c.k]!=='ok');if(!pool.length)return null;
    const bad=pool.filter(c=>cardState[c.k]==='no');const src=(bad.length&&Math.random()<.5)?bad:pool;return src[Math.floor(Math.random()*src.length)]}
  function draw(){
    const ok=deck.filter(c=>cardState[c.k]==='ok').length;
    let h='<h1>Flashcards</h1><div class="row">'+sel+'<label><input type="checkbox" id="pendCb" '+(mode==='pend'?'checked':'')+'> só os que ainda não domino</label></div>';
    h+='<div class="meta" style="margin:10px 0">'+ok+' de '+deck.length+' dominados</div>'+prog(deck.length?ok/deck.length:0);
    if(!cur){h+='<div class="card">'+(deck.length?'Parabéns! Você dominou todos os cards desta seleção. 🎉':'Esta disciplina não tem cards automáticos.')+'</div>'}
    else{h+='<div class="card flash'+(flipped?' back':'')+'" id="fc"><div>'+(flipped?esc(cur.a):'<div class="meta" style="font-size:.8rem">'+pad(cur.d.id)+' · '+esc(cur.d.title)+'</div>'+esc(cur.q))+'</div></div>'+
      '<div class="row">'+(flipped?'<button class="btn bad" id="no">Não sei</button><button class="btn ok" id="yes">Sei</button>':'<button class="btn" id="show">Mostrar resposta</button>')+'<a class="btn ghost" href="#/d/'+cur.d.id+'">Ver no resumo</a></div>'}
    main.innerHTML=h;
    $('#cdSel').onchange=e=>{location.hash='#/cards'+(+e.target.value?'/'+e.target.value:'')};
    $('#pendCb').onchange=e=>{mode=e.target.checked?'pend':'all';store.set('cardMode',mode);cur=pick();flipped=false;draw()};
    if(cur){const fc=$('#fc');fc.onclick=()=>{flipped=!flipped;draw()};
      if($('#show'))$('#show').onclick=()=>{flipped=true;draw()};
      if($('#yes'))$('#yes').onclick=()=>{cardState[cur.k]='ok';store.set('cards',cardState);cur=pick();flipped=false;draw()};
      if($('#no'))$('#no').onclick=()=>{cardState[cur.k]='no';store.set('cards',cardState);cur=pick();flipped=false;draw()}}
  }
  cur=pick();draw();
}

function quiz(only){
  buildNav('quiz');only=only?+only:0;
  let h='<h1>Autoteste</h1><p class="meta">Responda cada pergunta em voz alta ou por escrito, sem olhar. Marque as que você consegue responder; as que sobrarem voltam para o resumo.</p>';
  D.disciplines.forEach(d=>{if(!d.questions.length||(only&&d.id!==only))return;
    const n=d.questions.filter((q,i)=>qdone[d.id+':'+i]).length;
    h+='<div class="card"><div class="row"><b>'+pad(d.id)+' · '+esc(d.title)+'</b><span class="meta">'+n+'/'+d.questions.length+'</span><span style="flex:1"></span><a href="#/d/'+d.id+'">resumo</a></div>'+
      d.questions.map((q,i)=>'<label class="q'+(qdone[d.id+':'+i]?' done':'')+'"><input type="checkbox" data-k="'+d.id+':'+i+'" '+(qdone[d.id+':'+i]?'checked':'')+'><span>'+esc(q)+'</span></label>').join('')+'</div>'});
  main.innerHTML=h;
  main.querySelectorAll('input[data-k]').forEach(cb=>cb.onchange=()=>{qdone[cb.dataset.k]=cb.checked;store.set('q',qdone);cb.parentNode.classList.toggle('done',cb.checked)});
}

function search(q){
  buildNav('');q=q.trim().toLowerCase();
  const hits=[];D.disciplines.forEach(d=>{let idx=d.text.indexOf(q),c=0,p=idx;while(p>=0){c++;p=d.text.indexOf(q,p+q.length)}if(c)hits.push({d:d,c:c,i:idx})});
  hits.sort((a,b)=>b.c-a.c);
  let h='<h1>Busca: “'+esc(q)+'”</h1><p class="meta">'+hits.length+' disciplina(s) com resultados.</p>';
  hits.forEach(r=>{const t=r.d.text,s=Math.max(0,r.i-70),sn=esc(t.slice(s,r.i+q.length+110)).replace(new RegExp(esc(q).replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi'),m=>'<mark>'+m+'</mark>');
    h+='<div class="hit"><a href="#/d/'+r.d.id+'"><b>'+pad(r.d.id)+' · '+esc(r.d.title)+'</b></a> <span class="meta">'+r.c+' ocorrência(s)</span><div class="meta">…'+sn+'…</div></div>'});
  main.innerHTML=h;
}

function route(){
  document.body.classList.remove('menu');
  const p=location.hash.replace(/^#\/?/,'').split('/');
  if(p[0]==='d')disc(+p[1]);else if(p[0]==='plano')plan();else if(p[0]==='cards')cards(p[1]);else if(p[0]==='quiz')quiz(p[1]);else home();
  if(p[0]!=='d')window.scrollTo(0,0);else window.scrollTo(0,0);
}
window.addEventListener('hashchange',route);
$('#menuBtn').onclick=()=>{if(matchMedia('(max-width:860px)').matches)document.body.classList.toggle('menu');else{const c=document.body.classList.toggle('collapsed');store.set('collapsed',c)}};
if(store.get('collapsed',false))document.body.classList.add('collapsed');
$('#themeBtn').onclick=()=>{const r=document.documentElement,cur=r.dataset.theme||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');r.dataset.theme=cur==='dark'?'light':'dark';store.set('theme',r.dataset.theme)};
const th=store.get('theme',null);if(th)document.documentElement.dataset.theme=th;
let st;$('#search').addEventListener('input',e=>{clearTimeout(st);const v=e.target.value;st=setTimeout(()=>{if(v.trim().length>=2)search(v);else route()},200)});
route();
})();
