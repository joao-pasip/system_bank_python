from deposito.func_deposito import func_deposito as deposito
from saldo.func_saldo import func_saldo
from extrato.func_extrato import extrato
from saque.func_saque import saque
from saque.func_aux_saque import aux_quantidade_saque_dia
from users.func_listar_users import listar_users
from conta.func_listar_contas import listar_contas
from conta.func_conta_active import operacao_em_qual_conta
from validacoes.func_validate_cpf import validate_cpf
from conta.func_numero_da_conta import func_numero_da_conta
from users.func_user_active import user_active
from users.func_search_user_only import search_user_only
from conta.func_conta_only import conta_only
from acessos.func_login import login
from acessos.func_criar_user_e_conta import criar_usuario_e_conta
from conta.func_criar_nova_conta import criar_nova_conta
from conta.func_conta_active import conta_active


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

login_activate = False


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


while True:
    if login_activate is False:
        opcao_new_user = input((menu_before_login))
        if opcao_new_user.lower() == 'c':
            print(
              criar_usuario_e_conta(
                usuarios=usuarios,
                contas=contas,
                numero_da_agencia=numero_da_agencia,
                on_and_off_login=on_and_off_login,
                user_active=user_active,
                validate_cpf=validate_cpf,
                search_user_only=search_user_only,
                conta_active=conta_active
              )
            )
        elif opcao_new_user.lower() == 'l':
            print(
              login(
                usuarios=usuarios,
                contas=contas,
                on_and_off_login=on_and_off_login,
                validate_cpf=validate_cpf,
                conta_only=conta_only,
                conta_active=conta_active
              )
            )
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
        else:
            print("Opção inválida, veja as disponíveis no 'MENU'.")
