from date.func_date_correctly import str_date_time


def saque(
  *,
  func_saldo,
  numero_de_saques,
  LIMITE_DE_SAQUES_DIA,
  extrato,
  saques,
  depositos,
  total_sacado_dia,
  aux_quantidade_saque_dia
):
    sacar = input("Quanto deseja sacar? ")
    v_saque = float(sacar)
    saldo = func_saldo(depositos=depositos, saques=saques)
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
    elif len(saques) == 0:
        saques.append({
          "natureza": "saque",
          "data": str_date_time(),
          "valor": v_saque
        })
        result_saque = (
          f"Você realizou o primeiro saque do dia.\n"
          f"No valor de R$ {v_saque:.2f}\n"
        )
    elif len(saques) > 0:
        numero_de_saques += 1
        total_sacado_dia += v_saque
        valid_quantidade_e_total_sacado_dia = aux_quantidade_saque_dia(
          saques=saques,
          numero_de_saques=numero_de_saques,
          total_sacado_dia=total_sacado_dia,
          LIMITE_DE_SAQUES_DIA=LIMITE_DE_SAQUES_DIA,
          v_saque=v_saque,
        )
        result_saque = valid_quantidade_e_total_sacado_dia
    result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
    return (
      f"{result_saque}"
      f"{result_extrato}"
    )
