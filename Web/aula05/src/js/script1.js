console.log("Script externo rodando para o DOM");

const tituloElemento = document.getElementById('tituloDinamico'); 
tituloElemento.textContent = "Texto alterado pelo JavaScript";
tituloElemento.style.color = 'green'

const botaoElemento = document.getElementById('meuBotao')
botaoElemento.addEventListener('click',function(){
    alert('Botão foi clicado')
})