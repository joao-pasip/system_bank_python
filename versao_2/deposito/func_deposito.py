from date.func_date_correctly import str_date_time


def func_deposito(
  func_saldo,
  valor_deposito,
  extrato, depositos,
  saques,
  operacao_em_qual_conta,
  contas,
  conta_only, /
):
    conta_correct = operacao_em_qual_conta(
      conta_only=conta_only,
      contas=contas,
    )
    # print(f"DEPÓSITO CONTA CORRECT: {conta_correct}")
    if conta_correct['exists'] is True:
        depositar = input("Quanto deseja depositar? ")
        valor_deposito = float(depositar)
        saldo = func_saldo(
          depositos=depositos,
          saques=saques,
          operacao_em_qual_conta=operacao_em_qual_conta,
          contas=contas,
          conta_only=conta_only
        )
        result_deposit = ''
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            depositos.append({
              "natureza": "depósito",
              "data": str_date_time(),
              "valor": valor_deposito,
              "conta": conta_correct['conta']
            })
            result_deposit = (
              f"################################################\n"
              f"Você depositou R$ {valor_deposito:.2f} em sua conta.\n"
            )
        else:
            print(
              "Valor inválido, pois o valor para depósito está negativo."
            )
        result_extrato = extrato(
          func_saldo,
          depositos=depositos,
          saques=saques,
          operacao_em_qual_conta=operacao_em_qual_conta,
          contas=contas,
          conta_only=conta_only
        )
        # return (
        #   f"{result_deposit}"
        #   f"{result_extrato}"
        # )
    else:
        result_deposit = "Não foi possível fazer o depósito :(\n"
        result_extrato = 'Não é a sua conta!!!'
        # return result_deposit
    return (
      f"{result_deposit}"
      f"{result_extrato}"
    )
