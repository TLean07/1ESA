const readline = require('readline');
 
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
const USUARIO_CORRETO = 'admin';
const SENHA_CORRETA = '1234';
 
rl.question('Digite o nome de usuário: ', (usuario) => {
  rl.question('Digite a senha: ', (senha) => {
    if (usuario === USUARIO_CORRETO && senha === SENHA_CORRETA) {
      console.log('Login bem-sucedido!');
    } else {
      console.log('Credenciais inválidas.');
    }
    rl.close();
  });
});
