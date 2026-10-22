const CHAVE = 'nexashop_carrinho_v1';
let carrinho = [];
try { carrinho = JSON.parse(localStorage.getItem(CHAVE)) || []; if (!Array.isArray(carrinho)) carrinho = []; } catch { carrinho = []; }
const dinheiro = valor => Number(valor).toLocaleString('pt-BR', {style:'currency', currency:'BRL'});
function salvar() { localStorage.setItem(CHAVE, JSON.stringify(carrinho)); renderizarCarrinho(); }
function renderizarCarrinho() {
  document.querySelector('#contador').textContent = carrinho.reduce((s,p)=>s+p.quantidade,0);
  const destino = document.querySelector('#itens-carrinho');
  destino.replaceChildren();
  if (!carrinho.length) { const p=document.createElement('p');p.className='painel-vazio';p.textContent='Seu carrinho está vazio. Explore nosso catálogo!';destino.append(p); }
  for (const item of carrinho) {
    const linha=document.createElement('div');linha.className='linha-carrinho';
    const texto=document.createElement('span');texto.textContent=`${item.nome} × ${item.quantidade} — ${dinheiro(item.preco*item.quantidade)}`;
    const remover=document.createElement('button');remover.textContent='Remover';remover.addEventListener('click',()=>{carrinho=carrinho.filter(p=>p.id!==item.id);salvar();});
    linha.append(texto,remover);destino.append(linha);
  }
  document.querySelector('#total-carrinho').textContent=`Total: ${dinheiro(carrinho.reduce((s,p)=>s+p.preco*p.quantidade,0))}`;
}
function navegar() {
  const aba=location.hash==='#carrinho'?'carrinho':location.hash==='#compras'?'compras':'inicio';
  document.querySelectorAll('.pagina').forEach(el=>el.hidden=el.id!==aba);
}
document.querySelectorAll('.adicionar').forEach(botao=>botao.addEventListener('click',()=>{
  const {id,nome,preco}=botao.dataset;
  const existente=carrinho.find(item=>item.id===id);
  if(existente) existente.quantidade++; else carrinho.push({id,nome,preco:Number(preco),quantidade:1});
  salvar();botao.textContent='Adicionado ✓';setTimeout(()=>{botao.textContent='Adicionar ao carrinho';},1100);
}));
document.querySelector('#busca').addEventListener('input',event=>{
  const busca=event.target.value.toLocaleLowerCase('pt-BR');
  document.querySelectorAll('.card').forEach(card=>{card.hidden=!(card.dataset.nome.includes(busca)||card.dataset.categoria.includes(busca));});
});
window.addEventListener('hashchange',navegar);
navegar();renderizarCarrinho();
