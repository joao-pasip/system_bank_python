from deposito.func_deposito import func_deposito as deposito
from saldo.func_saldo import func_saldo
from extrato.func_extrato import extrato
from saque.func_saque import saque
from saque.func_aux_saque import aux_quantidade_saque_dia


menu = """
  Seja bem-vindo(a) ao seu banco.

  De acordo com o MENU abaixo, fala para a gente...

  Como podemos te ajudar?

  [d] - Digite 'd' para Depositar;
  [s] - Digite 's' para Sacar;
  [e] - Digite 'e' para ter o Extrato;
  [q] - Digite 'q' para Sair do sistema.

"""

valor_deposito = 0
depositos = []

# v_saque = 0
total_sacado_dia = 0
saques = []
numero_de_saques = 0
LIMITE_DE_SAQUES_DIA = 3


while True:
    opcao_user = input(menu)

    if opcao_user.lower() == 'd':
        print(deposito(
          func_saldo,
          valor_deposito,
          extrato,
          depositos,
          saques
        ))
    elif opcao_user.lower() == 's':
        print(saque(
          func_saldo=func_saldo,
          numero_de_saques=numero_de_saques,
          LIMITE_DE_SAQUES_DIA=LIMITE_DE_SAQUES_DIA,
          extrato=extrato,
          saques=saques,
          depositos=depositos,
          total_sacado_dia=total_sacado_dia,
          aux_quantidade_saque_dia=aux_quantidade_saque_dia
        ))
    elif opcao_user.lower() == 'e':
        print(extrato(func_saldo, depositos=depositos, saques=saques))
    elif opcao_user.lower() == 'q':
        break
    else:
        print("Opção inválida, veja as disponíveis no 'MENU'.")
