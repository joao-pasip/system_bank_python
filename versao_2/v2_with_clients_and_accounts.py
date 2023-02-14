from deposito.func_deposito import func_deposito as deposito
from saldo.func_saldo import func_saldo
from extrato.func_extrato import extrato
from saque.func_saque import saque
from saque.func_aux_saque import aux_quantidade_saque_dia
import datetime


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
  [q] - Digite 'q' para Sair da Conta.

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

conta_ativa = {
  'exists': False,
  'conta': ''
}
print(f"CONTA ATIVA: {conta_ativa}")
login_activate = False

# Necessário analisar melhores possibilidades de avaliar o CPF
# porque foi feito gambiarra. Basicamente o 0 a esquerda não é
# considerado, então em CPF com 10 digitios é acrescentado o 0.


def listar_users(*, usuarios):
    list_users = []
    for user in usuarios:
        list_users.append(user)
    return list_users


def listar_contas(*, contas):
    list_contas = []
    for conta in contas:
        list_contas.append(conta)
    return list_contas


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


def is_valid_date(*, date_string):
    try:
        datetime.datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def validate_cpf(*, cpf):
    cpf_valid = False
    cpf_number = ''
    if len(str(cpf)) == 11:
        cpf_valid = True
        cpf_number = str(cpf)
    elif len(str(cpf)) == 10:
        cpf_number = "0" + str(cpf)
        cpf_valid = True
    else:
        cpf_valid = False
    cpf_right_fatiamento = cpf_number if cpf_valid else False

    if cpf_right_fatiamento == cpf_number:
        fatia_um = cpf_right_fatiamento[:3]
        fatia_dois = cpf_right_fatiamento[3:6]
        fatia_tres = cpf_right_fatiamento[6:9]
        fatia_quatro = cpf_right_fatiamento[9:]
        cpf_formatado = f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}"
    else:
        cpf_formatado = False
    return cpf_formatado


def func_numero_da_conta(*, contas):
    numero_da_conta = len(contas)
    numero_da_conta += 1
    return numero_da_conta


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
    # return conta_ativa
    # conta_ativa = {
    #   'exists': True,
    #   'conta': conta
    # }
    # print(f"CONTA ATIVA Func.: {conta_ativa}")
    return conta_ativa['conta']


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
        # print(f"USER: {user}")
        # print(f"USER CPF: {cpf}")
        if user["cpf"] == cpf:
            result_user_only = user
        else:
            result_user_only = False
    return result_user_only


def conta_only(*, contas, numero_da_conta, numero_da_agencia):
    result_user_only = ''
    # print(f"CONTA ONLY Nº: {numero_da_conta}")
    for conta in contas:
        if (
          conta["numero_da_conta"] == numero_da_conta
          and conta["numero_da_agencia"] == numero_da_agencia
        ):
            result_user_only = conta
        else:
            result_user_only = 'Conta não encontrada'
    return result_user_only


def on_and_off_login(*, key_activate):
    global login_activate
    # print(f"LOGIN ACTIVATE 1: {login_activate}")
    # print(f"KEY ACTIVATE 1: {key_activate}")
    if login_activate is False and key_activate is False:
        login_activate = True
    elif login_activate is True and key_activate is True:
        login_activate = False
    # print(f"LOGIN ACTIVATE 2: {login_activate}")
    # print(f"KEY ACTIVATE 2: {key_activate}")
    return login_activate


def login(
  *,
  usuarios,
  contas,
  login_activate,
  on_and_off_login,
  validate_cpf,
  conta_only,
  conta_active
):
    user_cpf = input('Informe o CPF da sua conta (apenas números): ')
    user_numero_da_agencia = input('Informe o número da sua agência: ')
    user_numero_da_conta = int(input('Informe o número da sua conta: '))

    cpf_formatado = validate_cpf(cpf=user_cpf)
    if cpf_formatado is False:
        search_only_account = 'CPF inválido! :('
    else:
        user_info = search_user_only(usuarios=usuarios, cpf=cpf_formatado)
        if len(usuarios) == 0:
            on_and_off_login(key_activate=True)
            search_only_account = 'Usuário não encontrado!'
        elif user_info is False:
            search_only_account = 'Usuário não encontrado!'
        else:
            user_info = search_user_only(usuarios=usuarios, cpf=cpf_formatado)
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


def criar_usuario_e_conta(
  *,
  usuarios,
  contas,
  numero_da_agencia,
  login_activate,
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


while True:
    if login_activate is False:
        # print(f"LOGIN ACTIVATE I: {login_activate}")
        opcao_new_user = input((menu_before_login))
        if opcao_new_user.lower() == 'c':
            print(
              criar_usuario_e_conta(
                usuarios=usuarios,
                contas=contas,
                numero_da_agencia=numero_da_agencia,
                login_activate=login_activate,
                on_and_off_login=on_and_off_login,
                user_active=user_active,
                validate_cpf=validate_cpf,
                search_user_only=search_user_only,
                conta_active=conta_active
              )
            )
            # login_activate = on_and_off_login(login_activate=login_activate)
            # print(f"LOGIN ACTIVATE C: {login_activate}")
        elif opcao_new_user.lower() == 'l':
            # print(f"LOGIN ACTIVATE L: {login_activate}")
            print(
              login(
                usuarios=usuarios,
                contas=contas,
                login_activate=login_activate,
                on_and_off_login=on_and_off_login,
                validate_cpf=validate_cpf,
                conta_only=conta_only,
                conta_active=conta_active
              )
            )
            # login_activate = on_and_off_login(
            #   login_activate=login_activate
            # )
        elif opcao_new_user.lower() == 'q':
            break
        elif opcao_new_user.lower() == 'lu':
            print(listar_users(usuarios=usuarios))
        elif opcao_new_user.lower() == 'lc':
            print(listar_contas(contas=contas))
        else:
            print("Opção inválida, veja as disponíveis no 'MENU'.")
    elif login_activate is True:
        opcao_user = input(menu_after_login)
        print(f"CONTA ATIVA WHILE: {conta_ativa}")
        if opcao_user.lower() == 'd':
            print(deposito(
              func_saldo,
              valor_deposito,
              extrato,
              depositos,
              saques,
              operacao_em_qual_conta,
              contas,
              conta_only
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
              aux_quantidade_saque_dia=aux_quantidade_saque_dia,
              operacao_em_qual_conta=operacao_em_qual_conta,
              contas=contas,
              conta_only=conta_only
            ))
        elif opcao_user.lower() == 'e':
            print(extrato(
              func_saldo,
              depositos=depositos,
              saques=saques,
              operacao_em_qual_conta=operacao_em_qual_conta,
              contas=contas,
              conta_ativa=conta_ativa,
              conta_only=conta_only
              )
            )
        elif opcao_user.lower() == 'n':
            print(
              criar_nova_conta(
                usuarios=usuarios,
                search_user_only=search_user_only,
                contas=contas,
                numero_da_agencia=numero_da_agencia,
                func_numero_da_conta=func_numero_da_conta,
                conta_active=conta_active,
                conta_only=conta_only
              )
            )
        elif opcao_user.lower() == 'q':
            login_activate = on_and_off_login(key_activate=login_activate)
            # print(f"LOGIN ACTIVATE Q: {login_activate}")
            # opcao_new_user = input((menu_before_login))
        else:
            print("Opção inválida, veja as disponíveis no 'MENU'.")
