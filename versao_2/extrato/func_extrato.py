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
