const frutas = ['maçã','melancia','banana'];

const numeros = [10,20,30,40];

const misturado = [1,'dois',3,'quatro',true,null,undefined,{chave:'valor'}];

const cores = new Array('vermelho','preto','branco');

const vazio = [];

const linguagens = ['javascript','java','pyto','c#'];

//Acessando o primeiro elemento do array
const primeiraLinguagem = linguagens[0];
console.log(`A priemeira linguagem é: ${primeiraLinguagem}`);

const ultimalinguagem = linguagens[linguagens.length-1];
console.log(`A última linguagem é: ${ultimalinguagem}`);

let coresMutaveis = ['branco','azul','rosa'];
coresMutaveis[1]='amarelo';
console.log(`Array após a alteração: ${coresMutaveis}`);
coresMutaveis[coresMutaveis.length]='roxo';

let planetas = ['Terra','Marte'];
//push()-->adiciona um ou mais elementos ao final do array e retorna o novo componente
const novoComprimentoPush = planetas.push('Saturno','Urano');

//pop()-->remove o último elemento do meu array
const ultimoPlanetaRemovido = planetas.pop();

//indexOf()-->retorna o primeiro indice em que um elemento pode ser encontrado no array
const indiceTerra = planetas.indexOf('Terra');

//join()-->cria e retorna uma nova string concatenando todos os elementos do array
const stringPlanetas = planetas.join('-');

const coresInteracao = ['laranja','ciano','magenta'];

for(let i=0;i<coresInteracao.length;i++){
    console.log(`Cor no índice ${i} : ${coresInteracao[i]}`);
}

//Laço 'for...of' (mais moderno e legível para interar sobre os valores)
for(const cor of coresInteracao){
    console.log(`Cor: ${cor}`);
}

coresInteracao.forEach(function(cor,indice){
    console.log(`Cor: ${cor} no índice: ${indice}`);
});

//Este trecho demonstra como criar um array em JavaScript
//recebendo dados do usuário através do terminal (Node.js)
const readLine = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

//Criar um array vazio para array armazenar os itens da lista de compras do usuário
const listaCompras = [];

//criar uma função para adicionar um item na lista de compras
function adicionarItem(){
    readLine.question('Digite um item para adicionar a lista de compras (ou "fim" para sair): ',(item) =>{
        const itemFormatado = item.trim();//remove os espaçoes em branco extras
        //Verifica se o usuário digitou "fim" (ignorando caixa alta/baixa)
        if(itemFormatado.toLowerCase()=== 'fim'){
            //se o usuário digitou "fim", encerra a interação com o terminal
            console.log('\nSua lista de compras completa: ');
            //itera sobre cada item no array 'listaCompras'
            listaCompras.forEach((produto,indice) =>{
                console.log(`${indice+1}. ${produto}`);
            });
            readLine.close();
        }else if(itemFormatado !== ''){
            listaCompras.push(itemFormatado);
            console.log(`"${itemFormatado}" foi adicionado à sua lista.`);
            adicionarItem();
        }else{
            //se o usuário digitou apenas espaços ou nada
            console.log('Por favor, digite um item válido');
            adicionarItem();
        }

    });
};
//inicializa o processo de adicionar itens à lista de compras chamando a função pela primeira vez
console.log('Bem vindo a sua lista de compra');
adicionarItem();