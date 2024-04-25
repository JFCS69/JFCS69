def realizar_cadastro_usuario():
    registro_usuario = {}
    nome = input("Insira seu nome: ").upper().strip()
    telefone = str(input("Insira seu telefone: "))
    email = input("Insira seu email: ").lower().strip()
    senha = ""
    while True:
        senha = input("Insira a senha (mínimo 6 caracteres): ")
        if len(senha) < 6:
            print("A senha precisa ter no mínimo 6 caracteres!")
            continue
        else:
            break
    registro_usuario["Nome"] = nome
    registro_usuario["Telefone"] = telefone
    registro_usuario[email] = senha
    return registro_usuario

def validar_credenciais(email, senha, registro):
    if email in registro:
        if registro[email] == senha:
            print("Login bem-sucedido!")
            return True
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Email não encontrado.")
        return False
