const readline = require('readline');
 
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
rl.question('Digite o valor total da compra: R$ ', (valor) => {
  const valorCompra = parseFloat(valor);
 
  if (isNaN(valorCompra)) {
    console.log('Por favor, digite um número válido.');
  } else {
    let valorFinal = valorCompra;
 
    if (valorCompra > 100) {
      valorFinal = valorCompra * 0.9;
      console.log(`Desconto de 10% aplicado! Valor final: R$ ${valorFinal.toFixed(2)}`);
    } else {
      console.log(`Sem desconto. Valor final: R$ ${valorFinal.toFixed(2)}`);
    }
  }
 
  rl.close();
});