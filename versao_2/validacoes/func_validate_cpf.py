# Necessário analisar melhores possibilidades de avaliar o CPF
# porque foi feito gambiarra. Basicamente o 0 a esquerda - como
# primeiro número do CPF - não é considerado, então em CPF com
# 10 digitios é acrescentado o 0.


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
