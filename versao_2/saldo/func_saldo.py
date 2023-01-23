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
