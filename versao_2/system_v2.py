from datetime import datetime


dt = datetime.now()
ts = datetime.timestamp(dt)
date_time = datetime.fromtimestamp(ts)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")

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


def func_saldo(*, depositos, saques):
    list_extrato = depositos + saques
    saldo = 0
    if len(list_extrato) == 0:
        return saldo
    else:
        for operacao in list_extrato:
            if operacao['natureza'] == 'depósito':
                saldo += operacao['valor']
            elif operacao['natureza'] == 'saque':
                saldo -= operacao['valor']
    return saldo

# Filtrar pelos dias para somar com o total_sacado_dia quando tiver uma
# operação no mesmo dia

# def aux_quantidade_saque_dia(*, saques):
#     if len(saques) == 0:
#         saques.append({
#           "natureza": "saque",
#           "data": str_date_time,
#           "valor": v_saque
#         })


def saque(
  *,
  func_saldo,
  numero_de_saques,
  LIMITE_DE_SAQUES_DIA,
  extrato,
  saques,
  depositos,
  total_sacado_dia
):
    sacar = input("Quanto deseja sacar? ")
    v_saque = float(sacar)
    saldo = func_saldo(depositos=depositos, saques=saques)
    total_sacado_dia += total_sacado_dia
    numero_de_saques += numero_de_saques
    result_saque = ''
    if v_saque > 500:
        result_saque = ("""
        Não foi possível sacar,
        o seu limite de saque diário é de R$ 500,00.
        """)
    elif v_saque > saldo:
        result_saque = (
          f"Desculpe :(, não foi possível sacar. Saldo insuficiente.\n"
          f"################################################\n"
          f"Você sacou da sua conta R$ {v_saque:.2f}\n"
          f"################################################\n"
          f"Atualmente seu saldo é de R$ {saldo:.2f}"
        )
    elif (
      (v_saque <= 500)
      and (numero_de_saques <= LIMITE_DE_SAQUES_DIA)
      and (v_saque <= saldo)
      and (total_sacado_dia <= 500)
      and (v_saque > 0)
    ):
        # saldo = saldo - v_saque
        # # numero_de_saques = numero_de_saques + 1
        saques.append({
          "natureza": "saque",
          "data": str_date_time,
          "valor": v_saque
        })
        for operacao in saques:
            operacoes_mesmo_dia = []
            saques_inverse = saques[::-1]
            for operacao_saque_inverse in saques_inverse:
                if (
                  operacao['data'].split(',')[0]
                  == operacao_saque_inverse['data'].split(',')[0]
                ):
                    operacoes_mesmo_dia.append(operacao_saque_inverse)
        for transacoes_mesmo_dia in operacoes_mesmo_dia:
            total_sacado_dia += transacoes_mesmo_dia['valor']
            numero_de_saques = numero_de_saques + 1
        if total_sacado_dia > 500:
            result_saque = (
              f"################################################\n"
              f"Não foi possível sacar,\n"
              f"o seu limite de saque diário é de R$ 500,00.\n"
              f"E, você já sacou R$ {total_sacado_dia - v_saque:.2f} hoje.\n"
              f"################################################\n"
              f"Atualmente seu saldo é de R$ {saldo:.2f}"
            )
        elif numero_de_saques >= LIMITE_DE_SAQUES_DIA:
            result_saque = ("""
            Não foi possível sacar,
            o seu limite de vezes para sacar por dia é de 3 saques.
            """)
        else:
            saldo = saldo - v_saque
            result_extrato = extrato(
              func_saldo, depositos=depositos, saques=saques
            )
            return (
              f"{result_saque}"
              f"{result_extrato}"
            )

            # numero_de_saques = numero_de_saques + 1
            # saques.append({
            #   "natureza": "saque",
            #   "data": str_date_time,
            #   "valor": v_saque
            # })
        print(
          f"TOTAL SACADO POR DIA: {total_sacado_dia}\n"
          f"TOTAL SAQUES POR DIA: {numero_de_saques}\n"
        )
        return result_saque
    else:
        print("Não é possível sacar, aconteceu um problema.")
    result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
    return (
      f"{result_saque}"
      f"{result_extrato}"
    )


def deposito(func_saldo, valor_deposito, extrato, depositos, saques):
    depositar = input("Quanto deseja depositar? ")
    valor_deposito = float(depositar)
    saldo = func_saldo(depositos=depositos, saques=saques)
    result_deposit = ''
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        depositos.append({
          "natureza": "depósito",
          "data": str_date_time,
          "valor": valor_deposito
        })
        result_deposit = (
          f"################################################\n"
          f"Você depositou R$ {valor_deposito:.2f} em sua conta.\n"
          # f"E, o seu saldo agora é de R$ {saldo:.2f}"
        )
    else:
        print(
          "Valor inválido, pois o valor para depósito está negativo."
        )
    result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
    return (
      f"{result_deposit}"
      f"{result_extrato}"
    )


def extrato(func_saldo, /, *, depositos, saques):
    list_extrato = []
    list_extrato = depositos + saques
    saldo = func_saldo(depositos=depositos, saques=saques)
    if len(list_extrato) == 0 and saldo == 0:
        excecao_extrato = (
          f"################################################\n"
          f"Não foram realizadas movimentações.\n"
          f"Seu saldo é de R$ {saldo:.2f}"
        )
        return excecao_extrato
    result_extract = (
      f"################################################\n"
      f"Seu extrato: {list_extrato}.\n"
      f"Seu saldo é de R$ {saldo:.2f}"
    )
    return result_extract


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
          total_sacado_dia=total_sacado_dia
        ))
    elif opcao_user.lower() == 'e':
        print(extrato(func_saldo, depositos=depositos, saques=saques))
    elif opcao_user.lower() == 'q':
        break
    else:
        print("Opção inválida, veja as disponíveis no 'MENU'.")
