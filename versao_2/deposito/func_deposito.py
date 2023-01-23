from date.func_date_correctly import str_date_time


def func_deposito(func_saldo, valor_deposito, extrato, depositos, saques):
    depositar = input("Quanto deseja depositar? ")
    valor_deposito = float(depositar)
    saldo = func_saldo(depositos=depositos, saques=saques)
    result_deposit = ''
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        depositos.append({
          "natureza": "depósito",
          "data": str_date_time(),
          "valor": valor_deposito
        })
        result_deposit = (
          f"################################################\n"
          f"Você depositou R$ {valor_deposito:.2f} em sua conta.\n"
        )
    else:
        print(
          "Valor inválido, pois o valor para depósito está negativo."
        )
    result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
    return (
      f"{result_deposit}"
      f"{result_extrato}"
    )
