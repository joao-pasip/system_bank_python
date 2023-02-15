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
