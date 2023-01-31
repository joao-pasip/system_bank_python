from deposito.func_deposito import func_deposito as deposito
from saldo.func_saldo import func_saldo
from extrato.func_extrato import extrato
from saque.func_saque import saque
from saque.func_aux_saque import aux_quantidade_saque_dia


menu_before_login = """
  O que deseja fazer?

  De acordo com o MENU abaixo, fala para a gente...

  Como podemos te ajudar?

  [c] - Digite 'c' para Criar Conta;
  [l] - Digite 'l' para Entrar na Conta;
  [q] - Digite 'q' para Sair do sistema.

"""

menu_after_login = """
  Seja bem-vindo(a) ao seu banco.

  De acordo com o MENU abaixo, fala para a gente...

  Como podemos te ajudar?

  [d] - Digite 'd' para Depositar;
  [s] - Digite 's' para Sacar;
  [e] - Digite 'e' para ter o Extrato;
  [n] - Digite 'n' para Criar Nova Conta;
  [q] - Digite 'q' para Sair do sistema.

"""


valor_deposito = 0
depositos = []

# v_saque = 0
total_sacado_dia = 0
saques = []
numero_de_saques = 0
LIMITE_DE_SAQUES_DIA = 3

usuarios = []
contas = []
numero_da_conta = 0
numero_da_agencia = '0001'

login_activate = False


def func_numero_da_conta(*, contas):
    numero_da_conta = len(contas)
    numero_da_conta += 1
    return numero_da_conta


def user_active(*, usuario):
    # print(f"TESTE: {usuario}")
    user_info = {
      "nome_do_usuario": usuario['nome_do_usuario'],
      "data_de_nascimento": usuario['data_de_nascimento'],
      "cpf": usuario['cpf'],
      "endereço": usuario['endereço']
    }
    return user_info


def search_user_only(*, usuarios, cpf):
    # copia_users = usuarios.copy()
    # inverse_list_user = copia_users[::-1]
    result_user_only = ''
    for user in usuarios:
        if user["cpf"] == cpf:
            result_user_only = user
        else:
            result_user_only = False
    return result_user_only


def conta_only(*, contas, numero_da_conta, numero_da_agencia):
    result_user_only = ''
    for conta in contas:
        if (
          conta["numero_da_conta"] == numero_da_conta
          and conta["numero_da_agencia"] == numero_da_agencia
        ):
            result_user_only = conta
        else:
            result_user_only = 'Conta não encontrada'
    return result_user_only


def on_and_off_login(*, login_activate):
    # global login_activate
    if login_activate is False:
        login_activate = True
    elif login_activate is True:
        login_activate = False
    return login_activate


def login(
  *,
  usuarios,
  contas,
  login_activate,
  on_and_off_login
):
    user_cpf = int(input('Informe o CPF da sua conta (apenas números): '))
    user_numero_da_agencia = input('Informe o número da sua agência: ')
    user_numero_da_conta = int(input('Informe o número da sua conta: '))

    if len(usuarios) == 0:
        on_and_off_login(login_activate=True)
        search_only_account = 'Usuário não encontrado!'
    else:
        user_info = search_user_only(usuarios=usuarios, cpf=user_cpf)
        user_active(usuario=user_info)
        on_and_off_login(login_activate=login_activate)

        search_only_account = conta_only(
          contas=contas,
          numero_da_conta=user_numero_da_conta,
          numero_da_agencia=user_numero_da_agencia
        )

    return search_only_account


def criar_usuario_e_conta(
  *,
  usuarios,
  contas,
  numero_da_agencia,
  login_activate,
  on_and_off_login,
  user_active,
):
    print("Agradecemos pela preferência em nosso banco! :)")
    nome_usuario = input('Qual o seu nome: ')
    data_de_nascimento = input('Quando você nasceu (dd/mm/aaaa): ')
    cpf = input('Informe o seu CPF (apenas números): ')
    endereco = input(
      'Informe seu endereço (logradouro, número - bairro - city/state: '
    )
    result_criar_user = ''

    user_info = {
      "nome_do_usuario": nome_usuario,
      "data_de_nascimento": data_de_nascimento,
      "cpf": cpf,
      "endereço": endereco
    }

    user_only_one = usuarios.count(cpf)
    if user_only_one == 0:
        usuarios.append(user_info)
        conta_criada = criar_conta(
          contas=contas,
          numero_da_agencia=numero_da_agencia,
          usuario=user_info,
          func_numero_da_conta=func_numero_da_conta
        )
        on_and_off_login(login_activate=login_activate)
        user_active(usuario=user_info)
        result_criar_user = (
          f"INFORMAÇÕES PESSOAIS\n"
          f"{user_info}\n"
          f"########################\n"
          f"INFORMAÇÕES DA CONTA\n"
          f"{conta_criada}"
        )
    else:
        result_criar_user = 'Usuário existente no banco'
    return result_criar_user


def criar_conta(
  *,
  contas,
  numero_da_agencia,
  usuario,
  func_numero_da_conta
):
    numero_da_conta = func_numero_da_conta(contas=contas)
    criando_conta = {
      "numero_da_agencia": numero_da_agencia,
      "numero_da_conta": numero_da_conta,
      "usuario": usuario
    }
    contas.append(criando_conta)
    return criando_conta


def criar_nova_conta(
  *,
  usuarios,
  search_user_only,
  contas,
  numero_da_agencia,
  func_numero_da_conta
):
    cpf = input('Informe o seu CPF (apenas números): ')
    usuario = search_user_only(usuarios=usuarios, cpf=cpf)
    print(f"USUÁRIO: {usuario}")
    if usuario is False:
        criando_conta = 'Usuário não encontrado! :('
    else:
        print(f"TESTE 1: {numero_da_conta}")
        numero_da_conta_of = func_numero_da_conta(
          contas=contas
        )
        print(f"TESTE 2: {numero_da_conta_of}")
        criando_conta = {
          "numero_da_agencia": numero_da_agencia,
          "numero_da_conta": numero_da_conta_of,
          "usuario": usuario
        }
        contas.append(criando_conta)
    return criando_conta


while True:
    if login_activate is False:
        opcao_new_user = input((menu_before_login))
        if opcao_new_user.lower() == 'c':
            print(
              criar_usuario_e_conta(
                usuarios=usuarios,
                contas=contas,
                numero_da_agencia=numero_da_agencia,
                login_activate=login_activate,
                on_and_off_login=on_and_off_login,
                user_active=user_active
              )
            )
            login_activate = on_and_off_login(login_activate=login_activate)
        elif opcao_new_user.lower() == 'l':
            if login(
                usuarios=usuarios,
                contas=contas,
                login_activate=login_activate,
                on_and_off_login=on_and_off_login
              ) == "Usuário não encontrado!":
                print("########################")
                print("Usuário não encontrado!")
                print("########################")
                login_activate = on_and_off_login(login_activate=True)
            else:
                login_activate = on_and_off_login(
                  login_activate=login_activate
                )
                print(
                  login(
                    usuarios=usuarios,
                    contas=contas,
                    login_activate=login_activate,
                    on_and_off_login=on_and_off_login
                  )
                )
        elif opcao_new_user.lower() == 'q':
            break
        else:
            print("Opção inválida, veja as disponíveis no 'MENU'.")
    elif login_activate is True:
        opcao_user = input(menu_after_login)
        if opcao_user.lower() == 'd':
            print(deposito(
              func_saldo,
              valor_deposito,
              extrato,
              depositos,
              saques
            ))
        elif opcao_user.lower() == 's':
            print(saque(
              func_saldo=func_saldo,
              numero_de_saques=numero_de_saques,
              LIMITE_DE_SAQUES_DIA=LIMITE_DE_SAQUES_DIA,
              extrato=extrato,
              saques=saques,
              depositos=depositos,
              total_sacado_dia=total_sacado_dia,
              aux_quantidade_saque_dia=aux_quantidade_saque_dia
            ))
        elif opcao_user.lower() == 'e':
            print(extrato(func_saldo, depositos=depositos, saques=saques))
        elif opcao_user.lower() == 'n':
            print(
              criar_nova_conta(
                usuarios=usuarios,
                search_user_only=search_user_only,
                contas=contas,
                numero_da_agencia=numero_da_agencia,
                func_numero_da_conta=func_numero_da_conta
              )
            )
        elif opcao_user.lower() == 'q':
            break
        else:
            print("Opção inválida, veja as disponíveis no 'MENU'.")
