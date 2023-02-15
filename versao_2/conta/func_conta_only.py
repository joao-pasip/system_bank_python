def conta_only(*, contas, numero_da_conta, numero_da_agencia):
    result_user_only = ''
    # print(f"CONTA ONLY Nº: {numero_da_conta}")
    for conta in contas:
        if (
          conta["numero_da_conta"] == numero_da_conta
          and conta["numero_da_agencia"] == numero_da_agencia
        ):
            result_user_only = conta
            break
        else:
            result_user_only = 'Conta não encontrada'
    return result_user_only
