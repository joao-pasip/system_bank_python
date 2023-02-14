from date.func_date_correctly import str_date_time

# Filtrar pelos dias para somar com o total_sacado_dia quando tiver uma
# operação no mesmo dia


def aux_quantidade_saque_dia(
  *,
  saques,
  numero_de_saques,
  total_sacado_dia,
  LIMITE_DE_SAQUES_DIA,
  v_saque,
  operacao_em_qual_conta,
  contas,
  conta_only,
  saques_conta_especifica
  ):
    result_aux_saque = ''
    # print(
    #   f"AUX_SAQUES: {saques}\n"
    # )
    conta_correct = operacao_em_qual_conta(
      conta_only=conta_only,
      contas=contas,
    )
    if len(saques_conta_especifica) > 0:
        for operacao in saques_conta_especifica:
            operacoes_mesmo_dia = []
            saques_inverse = saques_conta_especifica[::-1]
            for operacao_saque_inverse in saques_inverse:
                if (
                  operacao['data'].split(',')[0]
                  == operacao_saque_inverse['data'].split(',')[0]
                ):
                    operacoes_mesmo_dia.append(operacao_saque_inverse)
        for transacoes_mesmo_dia in operacoes_mesmo_dia:
            total_sacado_dia += transacoes_mesmo_dia['valor']
            numero_de_saques = numero_de_saques + 1
        aux_quantidade_saque_dia = {
          "numero_de_saques": numero_de_saques,
          "total_sacado_dia": total_sacado_dia
        }
        if (
          aux_quantidade_saque_dia["numero_de_saques"]
          > LIMITE_DE_SAQUES_DIA
        ):
            result_aux_saque = ("""
            Não foi possível sacar,
            o seu limite de vezes para sacar por dia é de 3 saques.
            """)
        elif aux_quantidade_saque_dia["total_sacado_dia"] > 500:
            result_aux_saque = (
              f"""
              ################################################
              Não foi possível sacar,"
              o seu limite de saque diário é de R$ 500,00."

              VALOR SACADO HOJE:
              R$ {total_sacado_dia - v_saque}
              """
            )
        else:
            saques.append({
              "natureza": "saque",
              "data": str_date_time(),
              "valor": v_saque,
              "conta": conta_correct['conta']
            })
            msg_personalite = (
              f"""
              Você realizou mais um saque no dia.

              No valor de R$ {v_saque:.2f}.
            
              Lembrando que, o limite do valor de saque diário é de R$ 500,00.
              E, o limite de saques por dia é de 3.
         
              INFORMAÇÕES SOBRE SAQUES DE HOJE:

              Valor: R$ {aux_quantidade_saque_dia["total_sacado_dia"]:.2f}
              Quantidade: {numero_de_saques} saques.
              """
            )
            result_aux_saque = msg_personalite
    else:
        result_aux_saque = (
          "Ainda não foi realizados saques."
        )
    # print(
    #   f"AUX_QUANTIDADE_DE_SAQUES: {numero_de_saques}\n"
    #   f"AUX_TOTAL_SACADO: {total_sacado_dia}\n"
    # )
    # result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
    return (
      f"{result_aux_saque}\n"
    )
