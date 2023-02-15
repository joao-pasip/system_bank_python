from users.func_search_user_only import search_user_only
from users.func_user_active import user_active


def login(
  *,
  usuarios,
  contas,
  on_and_off_login,
  validate_cpf,
  conta_only,
  conta_active
):
    user_cpf = input('Informe o CPF da sua conta (apenas números): ')
    user_numero_da_agencia = input('Informe o número da sua agência: ')
    user_numero_da_conta = int(input('Informe o número da sua conta: '))

    cpf_formatado = validate_cpf(cpf=user_cpf)
    user_info = search_user_only(usuarios=usuarios, cpf=cpf_formatado)
    # print(f"USER INFO_LOGIN: {user_info}")
    # print(f"USERS LOGIN: {usuarios}")
    if cpf_formatado is False:
        search_only_account = 'CPF inválido! :('
    elif len(usuarios) == 0:
        on_and_off_login(key_activate=True)
        search_only_account = 'Usuário não encontrado! S/U'
    elif user_info is False:
        search_only_account = 'Usuário não encontrado!'
    else:
        # user_info = search_user_only(
        # usuarios=usuarios, cpf=cpf_formatado)
        # print(f"USER INFO: {user_info}")
        user_active(usuario=user_info)
        on_and_off_login(key_activate=False)
        search_only_account = conta_only(
          contas=contas,
          numero_da_conta=user_numero_da_conta,
          numero_da_agencia=user_numero_da_agencia
        )
        # print(f"SEARCH ONLY ACCOUNT LOGIN: {search_only_account}")
        conta_active(
          conta_only=conta_only,
          numero_da_conta=search_only_account['numero_da_conta'],
          contas=contas,
          numero_da_agencia=search_only_account['numero_da_agencia']
        )
    return search_only_account
