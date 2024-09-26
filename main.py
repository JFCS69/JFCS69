from usuarios.cadastro_usuario import realizar_cadastro_usuario, validar_credenciais
from produtos.listagem_produto import menu_principal

# Início do cadastro/login
while True: 
    print("""JF.COM
            1- CADASTRAR
            2- LOGIN
            X- SAIR""")
    try:
        # Escolha da ação inicial
        opcao = input("ESCOLHA A OPÇÃO DESEJADA: ").upper()
        if opcao == "1":
            registro = realizar_cadastro_usuario()
            print("CADASTRO FEITO COM SUCESSO!")
        elif opcao == "2":
            # Solicitar email e senha ao usuário
            autenticado = False
            # Verificar credenciais
            while not autenticado:
                email_login = input("DIGITE SEU EMAIL DE CADASTRO: ").lower()
                senha_login = input("DIGITE SUA SENHA DE CADASTRO: ")
                autenticado = validar_credenciais(email_login, senha_login, registro)
                if autenticado:
                    menu_principal()
        elif opcao == "X":
            break
        else:
            print("A OPÇÃO ESCOLHIDA É INVÁLIDA. POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA!")
            continue
    except ValueError:
        print("SAINDO...")
        break
 