# DEIXANDO A FRUSTRAÇÃO AQUI, NAS TENTATIVAS

# def saque(
#   *,
#   func_saldo,
#   numero_de_saques,
#   LIMITE_DE_SAQUES_DIA,
#   extrato,
#   saques,
#   depositos,
#   total_sacado_dia
# ):
#     sacar = input("Quanto deseja sacar? ")
#     v_saque = float(sacar)
#     saldo = func_saldo(depositos=depositos, saques=saques)
#     total_sacado_dia += total_sacado_dia
#     numero_de_saques += numero_de_saques
#     result_saque = ''
#     if v_saque > 500:
#         result_saque = ("""
#         Não foi possível sacar,
#         o seu limite de saque diário é de R$ 500,00.
#         """)
#     elif v_saque > saldo:
#         result_saque = (
#           f"Desculpe :(, não foi possível sacar. Saldo insuficiente.\n"
#           f"################################################\n"
#           f"Você sacou da sua conta R$ {v_saque:.2f}\n"
#           f"################################################\n"
#           f"Atualmente seu saldo é de R$ {saldo:.2f}"
#         )
#     elif (
#       (v_saque <= 500)
#       and (numero_de_saques <= LIMITE_DE_SAQUES_DIA)
#       and (v_saque <= saldo)
#       and (total_sacado_dia <= 500)
#       and (v_saque > 0)
#     ):
#         # saldo = saldo - v_saque
#         # # numero_de_saques = numero_de_saques + 1
#         saques.append({
#           "natureza": "saque",
#           "data": str_date_time,
#           "valor": v_saque
#         })
#         for operacao in saques:
#             operacoes_mesmo_dia = []
#             saques_inverse = saques[::-1]
#             for operacao_saque_inverse in saques_inverse:
#                 if (
#                   operacao['data'].split(',')[0]
#                   == operacao_saque_inverse['data'].split(',')[0]
#                 ):
#                     operacoes_mesmo_dia.append(operacao_saque_inverse)
#         for transacoes_mesmo_dia in operacoes_mesmo_dia:
#             total_sacado_dia += transacoes_mesmo_dia['valor']
#             numero_de_saques = numero_de_saques + 1
#         if total_sacado_dia > 500:
#             result_saque = (
#               f"################################################\n"
#               f"Não foi possível sacar,\n"
#               f"o seu limite de saque diário é de R$ 500,00.\n"
#               f"E, você já sacou R$ {total_sacado_dia - v_saque:.2f} hoje.\n"
#               f"################################################\n"
#               f"Atualmente seu saldo é de R$ {saldo:.2f}"
#             )
#         elif numero_de_saques >= LIMITE_DE_SAQUES_DIA:
#             result_saque = ("""
#             Não foi possível sacar,
#             o seu limite de vezes para sacar por dia é de 3 saques.
#             """)
#         else:
#             saldo = saldo - v_saque
#             result_extrato = extrato(
#               func_saldo, depositos=depositos, saques=saques
#             )
#             return (
#               f"{result_saque}"
#               f"{result_extrato}"
#             )

#             # numero_de_saques = numero_de_saques + 1
#             # saques.append({
#             #   "natureza": "saque",
#             #   "data": str_date_time,
#             #   "valor": v_saque
#             # })
#         print(
#           f"TOTAL SACADO POR DIA: {total_sacado_dia}\n"
#           f"TOTAL SAQUES POR DIA: {numero_de_saques}\n"
#         )
#         return result_saque
#     else:
#         print("Não é possível sacar, aconteceu um problema.")
#     result_extrato = extrato(func_saldo, depositos=depositos, saques=saques)
#     return (
#       f"{result_saque}"
#       f"{result_extrato}"
#     )