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
              "data": str_date_time,
              "valor": f"R$ {valor_deposito:.2f}"
            })
            print(valor_deposito)
            print(saldo)
            print(depositos)
        else:
            print("Valor inválido, pois o valor para depósito está negativo.")
    elif opcao_user.lower() == 's':
        sacar = input("Quanto deseja sacar? ")
        valor_saque = float(sacar)
        if valor_saque > 500:
            print("""
            Não foi possível sacar,
            o seu limite de saque diário é de R$ 500,00.
            """)
        elif numero_de_saques > LIMITE_DE_SAQUES_DIA:
            print("""
            Não foi possível sacar,
            o seu limite de vezes para sacar por dia é de 3 saques.
            """)
        elif valor_saque > saldo:
            print("""
            Desculpe :(, não foi possível sacar. Saldo insuficiente.
            """)
        elif (
          (valor_saque <= 500)
          and (numero_de_saques <= LIMITE_DE_SAQUES_DIA)
          and (valor_saque <= saldo)
        ):
            saldo = saldo - valor_saque
            numero_de_saques = numero_de_saques + 1
            saques.append({
              "data": str_date_time,
              "valor": valor_saque
            })
            print(saldo)
            print(numero_de_saques)
        else:
            print("Não é possível sacar, aconteceu um problema.")