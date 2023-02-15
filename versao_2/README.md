# Versão 2 do Sistema

Nessa pasta existe um arquivo chamado system_v2.py que seria a segunda versão do sistema, no qual é nele que roda o script para a execução do mesmo. Desta forma, pode perceber que existem pastas - date, deposito, extrato, saldo, saque, acessos, conta, users, validacoes - que guardam trechos da funcionalidade do projeto.

Pode-se perceber, portanto, que nessa segunda versão estamos aplicando o paradigma funcional. Deixando assim, o código mais modularizado.

Nessa etapa do projeto, cada usuário pode criar uma conta no nosso banco com as seguintes informações: Nome, data de nascimeto (no formato dd/mm/yyyy), CPF (apenas números) e endereço.

No momento que uma conta é criada em nosso banco, seu número é único e permite que as operações ali realizadas - depósitos, saques, extratos e saldo - sejam apenas da conta logada.

Temos validações de alguns processos, como o de verificar se o CPF e data de nascimento estão de acordo com a estrutura exigida pelo banco.