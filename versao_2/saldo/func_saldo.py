def func_saldo(
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
    list_extrato = depositos + saques
    conta_extrato = []
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
    saldo = 0
    if len(conta_extrato) == 0:
        return saldo
    else:
        for operacao in conta_extrato:
            if operacao['natureza'] == 'depósito':
                saldo += operacao['valor']
            elif operacao['natureza'] == 'saque':
                saldo -= operacao['valor']
    return saldo
