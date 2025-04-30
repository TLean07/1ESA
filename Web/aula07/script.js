for(let i=0;i<5;i++){
    console.log(`Número: ${i}`);
}

let contador = 0;

while(contador < 3){ // usa quando não tem a qtd de vezes que vai rodar
    console.log(`Contador está em: ${contador}`);
    contador++;
}

const pessoa = {
    nome: 'Ana',
    idade: 30,
    cidade: 'São Paulo'
};

for(const propriedade in pessoa){
    console.log(`${propriedade}: ${pessoa [propriedade]}`);
}

const cores = ['vermerlho','azul','preto'];//criação de um array de cores

for(const cor of cores){//execução de um laço de repetição for...of percorre
    console.log(cor);
}

const resultadoDiv = document.getElementById('resultado')

const carro = {
    marca: 'Ford',
    modelo: 'Mustang',
    ano: '2007',
    cor: 'Azul',
    ligar: function(){
        console.log('O Carro está ligando!!! 🚗😁');
        exibirMensagemNoNavegador('O carro está ligando!!!🚗😀')
    },

obterDetalhes: function(){//obterDetalhes é outro método
    return `${this.marca} ${this.modelo} (${this.ano})`;
    //this se refere ao objeto 'carro' dentro dos seus métodos
}
};

console.log('---Objeto Literal---');
console.log(`Marca: ${carro.marca}`);//acessando a propriedade marca usando a notção de ponto
console.log(`Modelo: ${carro['modelo']}`);//acessando a propriedade modelo usando a notção de colchetes
carro.ligar();//chamado o metodo ligar usando a notção de ponto

const detalhesCarro = carro.obterDetalhes();
console.log(`Detalhes do carro: ${detalhesCarro}`);
exibirMensagemNoNavegador(`Detalhes do carro: ${detalhesCarro}`);

console.log('---Exibindo o objeto---')
for(const propriedade in carro){
    console.log(`${propriedade}: ${carro[propriedade]}`);
    exibirMensagemNoNavegador(`${propriedade}: ${carro[propriedade]}`);
}

//Outra forma de exibir um objeto (converte o objeto para uma String JSON)
const carroJSON = JSON.stringify(carro);


function exibirMensagemNoNavegador(mensagem){
    const paragrafo = document.createElement('p')//cria um novo elemento <p>
    paragrafo.textContent = mensagem;//define o texto do parágrafo com a mensagem
    resultadoDiv.appendChild(paragrafo);//add o parágrafo elemento 'resultado' no html
}