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
  aux_quantidade_saque_dia,
  operacao_em_qual_conta,
  contas,
  conta_only
):
    conta_correct = operacao_em_qual_conta(
      conta_only=conta_only,
      contas=contas,
    )

    saques_conta_especifica = []

    for saque in saques:
        if (
          saque['conta']['numero_da_conta']
          == conta_correct['conta']['numero_da_conta']
        ):
            info_saque = {
              'natureza': saque['natureza'],
              'data': saque['data'],
              'valor': saque['valor']
            }
            saques_conta_especifica.append(info_saque)
    if conta_correct['exists'] is True:
        sacar = input("Quanto deseja sacar? ")
        v_saque = float(sacar)
        saldo = func_saldo(
          depositos=depositos,
          saques=saques,
          operacao_em_qual_conta=operacao_em_qual_conta,
          contas=contas,
          conta_only=conta_only
        )
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
              f"Você tentou sacar da sua conta R$ {v_saque:.2f}\n"
              f"################################################\n"
              f"Atualmente seu saldo é de R$ {saldo:.2f}\n"
            )
        elif len(saques_conta_especifica) == 0:
            saques.append({
              "natureza": "saque",
              "data": str_date_time(),
              "valor": v_saque,
              "conta": conta_correct['conta']
            })
            result_saque = (
              f"Você realizou o primeiro saque do dia.\n"
              f"No valor de R$ {v_saque:.2f}\n"
            )
        elif len(saques_conta_especifica) > 0:
            numero_de_saques += 1
            total_sacado_dia += v_saque
            valid_quantidade_e_total_sacado_dia = aux_quantidade_saque_dia(
              saques=saques,
              numero_de_saques=numero_de_saques,
              total_sacado_dia=total_sacado_dia,
              LIMITE_DE_SAQUES_DIA=LIMITE_DE_SAQUES_DIA,
              v_saque=v_saque,
              operacao_em_qual_conta=operacao_em_qual_conta,
              contas=contas,
              conta_only=conta_only,
              saques_conta_especifica=saques_conta_especifica
            )
            result_saque = valid_quantidade_e_total_sacado_dia
        result_extrato = extrato(
          func_saldo,
          depositos=depositos,
          saques=saques,
          operacao_em_qual_conta=operacao_em_qual_conta,
          contas=contas,
          conta_only=conta_only
        )
        # print(f"RESULT EXTRATO SAQUE: {result_extrato}")
        # return (
        #   f"{result_saque}"
        #   f"{result_extrato}"
        # )
    else:
        result_saque = 'Não foi possível sacar :('
        result_extrato = 'Não está na sua conta!!!'
    return (
      f"{result_saque}"
      f"{result_extrato}"
    )
