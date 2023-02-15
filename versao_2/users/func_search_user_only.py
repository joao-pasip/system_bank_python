def search_user_only(*, usuarios, cpf):
    # copia_users = usuarios.copy()
    # inverse_list_user = copia_users[::-1]
    # print(f"CPF SEARCH USER ONLY: {type(cpf)}")
    # print(f"USERS SEARCH USER ONLY: {usuarios}")
    result_user_only = ''
    for user in usuarios:
        # print(f"USER: {user}")
        # print(f"USER CPF: {cpf}")
        if user["cpf"] == cpf:
            result_user_only = user
            break
        else:
            result_user_only = False
    # print(f"RESULT SEARCH USER ONLY: {result_user_only}")
    return result_user_only
