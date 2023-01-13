from datetime import datetime


dt = datetime.now()
ts = datetime.timestamp(dt)
date_time = datetime.fromtimestamp(ts)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")

# print(dt)
# print(ts)
# print(date_time)
# print(str_date_time)

menu = """
  Seja bem-vindo(a) ao seu banco.

  De acordo com o MENU abaixo, fala para a gente...

  Como podemos te ajudar?

  [d] - Digite 'd' para depositar;
  [s] - Digite 's' para sacar;
  [e] - Digite 'e' para ter o extrato;
  [q] - Digite 'q' para sair do sistema.

"""

saldo = 0

valor_deposito = 0
depositos = []

valor_saque = 0
aux_saque = 0
saques = []
numero_de_saques = 0
LIMITE_DE_SAQUES_DIA = 3

extrato = []

while True:
    opcao_user = input(menu)

    if opcao_user.lower() == 'd':
        depositar = input("Quanto deseja depositar? ")
        valor_deposito = float(depositar)
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            depositos.append({
              "natureza": "depósito",
              "data": str_date_time,
              "valor": valor_deposito
            })
            print(
              f"################################################\n"
              f"Você depositou R$ {valor_deposito:.2f} em sua conta.\n"
              f"E, o seu saldo agora é de R$ {saldo:.2f}"
            )
        else:
            print(
              "Valor inválido, pois o valor para depósito está negativo."
            )
    elif opcao_user.lower() == 's':
        sacar = input("Quanto deseja sacar? ")
        valor_saque = float(sacar)
        aux_saque = aux_saque + valor_saque
        if aux_saque > 500:
            print(
              f"################################################\n"
              f"Não foi possível sacar,\n"
              f"o seu limite de saque diário é de R$ 500,00.\n"
              f"E, você já sacou R$ {aux_saque - valor_saque:.2f} hoje.\n"
              f"################################################\n"
              f"Atualmente seu saldo é de R$ {saldo:.2f}"
            )
        elif valor_saque > 500:
            print("""
            Não foi possível sacar,
            o seu limite de saque diário é de R$ 500,00.
            """)
        elif numero_de_saques >= LIMITE_DE_SAQUES_DIA:
            print("""
            Não foi possível sacar,
            o seu limite de vezes para sacar por dia é de 3 saques.
            """)
        elif valor_saque > saldo:
            print("""
            Desculpe :(, não foi possível sacar. Saldo insuficiente.
            """)
            break
        elif (
          (valor_saque <= 500)
          and (numero_de_saques <= LIMITE_DE_SAQUES_DIA)
          and (valor_saque <= saldo)
          and (aux_saque <= 500)
        ):
            saldo = saldo - valor_saque
            numero_de_saques = numero_de_saques + 1
            saques.append({
              "natureza": "saque",
              "data": str_date_time,
              "valor": valor_saque
            })
            print(
              f"################################################\n"
              f"Você sacou da sua conta R$ {valor_saque:.2f}\n"
              f"################################################\n"
              f"Atualmente seu saldo é de R$ {saldo:.2f}"
            )
        else:
            print("Não é possível sacar, aconteceu um problema.")
    elif opcao_user.lower() == 'e':
        extrato = depositos + saques
        if len(extrato) == 0:
            print(
              f"################################################\n"
              f"Não foram realizadas movimentações.\n"
              f"Seu saldo é de R$ {saldo:.2f}"
            )
        else:
            print(
              f"################################################\n"
              f"Seu extrato: {extrato}.\n"
              f"Seu saldo é de R$ {saldo:.2f}"
            )
    elif opcao_user.lower() == 'q':
        break
    else:
        print("Opção inválida, veja as disponíveis no 'MENU'.")
