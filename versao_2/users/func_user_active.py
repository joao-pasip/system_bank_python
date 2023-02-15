def user_active(*, usuario):
    user_info = {
      "nome_do_usuario": usuario['nome_do_usuario'],
      "data_de_nascimento": usuario['data_de_nascimento'],
      "cpf": usuario['cpf'],
      "endereço": usuario['endereço']
    }
    return user_info
