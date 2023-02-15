from conta.func_conta_only import conta_only
from conta.func_numero_da_conta import func_numero_da_conta
from validacoes.func_is_valid_date import is_valid_date
from conta.func_criar_conta import criar_conta


def criar_usuario_e_conta(
  *,
  usuarios,
  contas,
  numero_da_agencia,
  on_and_off_login,
  user_active,
  validate_cpf,
  search_user_only,
  conta_active
):
    print("Agradecemos pela preferência em nosso banco! :)")
    nome_usuario = input('Qual o seu nome: ')
    data_de_nascimento = input('Quando você nasceu (dd/mm/aaaa): ')
    cpf = input('Informe o seu CPF (apenas números): ')
    endereco = input(
      'Informe seu endereço (logradouro, número - bairro - city/state: '
    )
    result_criar_user = ''
    cpf_right = validate_cpf(cpf=cpf)
    data_de_nascimento_valid = is_valid_date(date_string=data_de_nascimento)
    # print(f"USERs: {usuarios}")
    user_only_one = False if search_user_only(
      usuarios=usuarios, cpf=cpf_right
    ) else True
    # print(f"USER ONLY ONE: {user_only_one}")
    # print(f"DATA DE NASCIMENTO VALID {data_de_nascimento_valid}")
    # print(f"CPF right: {cpf_right}")
    if cpf_right is False:
        result_criar_user = 'CPF inválido! :('
        on_and_off_login(key_activate=True)
    elif data_de_nascimento_valid is False:
        result_criar_user = 'Data de nascimento inválida no formato :('
        on_and_off_login(key_activate=True)
    elif user_only_one is not False:
        user_info = {
          "nome_do_usuario": nome_usuario,
          "data_de_nascimento": data_de_nascimento,
          "cpf": cpf_right,
          "endereço": endereco
        }
        # user_only_one = usuarios.count(cpf)
        # print(f"USER ONLY ONE: {user_only_one}")
        # if user_only_one == 0:
        usuarios.append(user_info)
        conta_criada = criar_conta(
          contas=contas,
          numero_da_agencia=numero_da_agencia,
          usuario=user_info,
          func_numero_da_conta=func_numero_da_conta
        )
        # print(f"CONTA CRIADA 1: {conta_criada}")
        on_and_off_login(key_activate=False)
        user_active(usuario=user_info)
        conta_active(
          conta_only=conta_only,
          numero_da_conta=conta_criada['numero_da_conta'],
          contas=contas,
          numero_da_agencia=conta_criada['numero_da_agencia']
        )
        result_criar_user = (
          f"########################\n"
          f"########################\n"
          f"INFORMAÇÕES PESSOAIS\n"
          f"{user_info}\n"
          f"########################\n"
          f"INFORMAÇÕES DA CONTA\n"
          f"{conta_criada}\n"
          f"########################\n"
          f"########################\n"
        )
    else:
        result_criar_user = 'Usuário existente no banco'
    return result_criar_user
