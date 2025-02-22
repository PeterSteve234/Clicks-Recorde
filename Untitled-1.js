const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite a idade do seu Pai: ", (idadePai) => {
  rl.question("Digite a idade da sua Mãe: ", (idadeMae) => {
    // Convertendo strings para números inteiros
    let idadePaiNum = Number(idadePai.trim());
    let idadeMaeNum = Number(idadeMae.trim());

    if (isNaN(idadePaiNum) || isNaN(idadeMaeNum)) {
      console.log("Por favor, digite números válidos!");
    } else {
      let soma = idadePaiNum + idadeMaeNum;
      console.log("A soma das idades é: " + soma);
    }

    rl.close();
  });
});

