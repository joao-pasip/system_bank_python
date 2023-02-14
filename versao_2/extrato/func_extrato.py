def extrato(
  func_saldo,
  /,
  *,
  depositos,
  saques,
  operacao_em_qual_conta,
  contas,
  conta_only
):
    conta_correct = operacao_em_qual_conta(
      conta_only=conta_only,
      contas=contas,
    )

    # print(f"CONTA CORRECT EXTRATO: {conta_correct}")
    if conta_correct['exists'] is True:
        list_extrato = []
        list_extrato = depositos + saques
        conta_extrato = []
        print(f"EXTRATO SAQUES: {saques}")
        for operacao in list_extrato:
            if (
              operacao['conta']['numero_da_conta']
              == conta_correct['conta']['numero_da_conta']
            ):
                # operacao.pop("conta")
                info_extrato = {
                  'natureza': operacao['natureza'],
                  'data': operacao['data'],
                  'valor': operacao['valor']
                }
                # print(f"OPERAÇÃO EXTRATO: {operacao}")
                conta_extrato.append(info_extrato)
        saldo = func_saldo(
          depositos=depositos,
          saques=saques,
          operacao_em_qual_conta=operacao_em_qual_conta,
          contas=contas,
          conta_only=conta_only
        )
        if len(conta_extrato) == 0 and saldo == 0:
            excecao_extrato = (
              f"################################################\n"
              f"Não foram realizadas movimentações.\n"
              f"Seu saldo é de R$ {saldo:.2f}"
            )
            return excecao_extrato
        result_extract = (
          f"################################################\n"
          f"Seu extrato: {conta_extrato}.\n"
          f"Seu saldo é de R$ {saldo:.2f}"
        )
    else:
        result_extract = 'Não foi possível ver o extrato :('
    return result_extract
