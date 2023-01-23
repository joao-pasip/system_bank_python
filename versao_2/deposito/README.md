No arquivo func_deposito.py, temos a função que executa a operação de depósito do nosso sistema.

Ela funciona basicamente da seguinte forma:

- Recebe uma entrada do valor pelo usuário;
- Como esse valor vem em string é transformado em número float;
- É chamada a função saldo que retorna essa informação para o sistema;
- Foi criada uma variável auxiliar "result_deposit" vazia que será reatribuída;
- Verifica se o valor do depósito é negativo ou positivo;
- Em caso de valor positivo: Aumenta o saldo e adiciona a operação em depósito;
- Além de reatribuir o valor para a variável auxiliar "result_deposit";
- Em caso negativo: Exibimos uma mensagem com alerta de erro;
- A função de extrato é chamada e soma as listas de depósitos e saques;
- Retorna o valor da variável "result_deposit" e do extrato.