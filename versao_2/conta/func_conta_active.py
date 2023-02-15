conta_ativa = {
  'exists': False,
  'conta': ''
}


def conta_active(*, conta_only, numero_da_conta, contas, numero_da_agencia):
    global conta_ativa
    conta = conta_only(
      contas=contas,
      numero_da_conta=numero_da_conta,
      numero_da_agencia=numero_da_agencia
    )

    if conta == 'Conta não encontrada':
        conta_ativa = {
          'exists': False,
          'conta': conta
        }
    else:
        conta_ativa = {
          'exists': True,
          'conta': conta
        }
    return conta_ativa['conta']


def operacao_em_qual_conta(*, conta_only, contas):
    global conta_ativa
    numero_da_conta = conta_ativa['conta']['numero_da_conta']
    numero_da_agencia = conta_ativa['conta']['numero_da_agencia']
    result_conta = conta_only(
      contas=contas,
      numero_da_conta=numero_da_conta,
      numero_da_agencia=numero_da_agencia
    )
    if result_conta == 'Conta não encontrada':
        conta_ativa = {
          'exists': False,
          'conta': result_conta
        }
    else:
        conta_ativa = {
          'exists': True,
          'conta': result_conta
        }
    return conta_ativa
