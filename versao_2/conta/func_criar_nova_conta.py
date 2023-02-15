from validacoes.func_validate_cpf import validate_cpf


def criar_nova_conta(
  *,
  usuarios,
  search_user_only,
  contas,
  numero_da_agencia,
  func_numero_da_conta,
  conta_active,
  conta_only
):
    cpf = input('Informe o seu CPF (apenas números): ')
    cpf_right = validate_cpf(cpf=cpf)
    usuario = search_user_only(usuarios=usuarios, cpf=cpf_right)
    # print(f"USUÁRIO NOVA CONTA: {usuario}")
    if usuario is False:
        criando_conta = 'Usuário não encontrado! :('
    else:
        # print(f"TESTE 1: {numero_da_conta}")
        numero_da_conta_of = func_numero_da_conta(
          contas=contas
        )
        # print(f"TESTE 2: {numero_da_conta_of}")
        criando_conta = {
          "numero_da_agencia": numero_da_agencia,
          "numero_da_conta": numero_da_conta_of,
          "usuario": usuario
        }
        # print(f"CRIANDO NOVA CONTA: {criando_conta}")
        contas.append(criando_conta)
        conta_active(
          conta_only=conta_only,
          numero_da_conta=criando_conta['numero_da_conta'],
          contas=contas,
          numero_da_agencia=criando_conta['numero_da_agencia']
        )
    return (
      f"########################\n"
      f"########################\n"
      f"Você está na sua nova conta com as seguintes informações :)\n"
      f"{criando_conta}"
    )
