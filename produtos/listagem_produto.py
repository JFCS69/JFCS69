produto_registrado = {}
lista_produtos = []

def registrar_produto():
    produto_registrado["ID"] = int(input("ID do produto: "))
    produto_registrado["Nome"] = input("Nome do produto: ").upper().strip()
    produto_registrado["Preço"] = float(input("Preço do produto: R$"))
    lista_produtos.append(produto_registrado.copy())
    return lista_produtos

def selecionar_produto_para_edicao(lista_produtos):
    print("LISTA DE PRODUTOS:")
    for produto in lista_produtos:
        print(f"{produto}")
        id_produto = int(input("Digite o ID do produto que deseja editar: "))
        for produto in lista_produtos:
            if produto["ID"] == id_produto:
                return produto
    print("ID inválido.")

def editar_detalhes_produto(produto, chave, novo_valor):
    if chave in produto:
        produto[chave] = novo_valor
        return True
    else:
        print(f"O campo {chave} não existe para este produto.")
        return False

def exibir_lista_de_produtos():
    print("LISTA DE PRODUTOS CADASTRADOS: ")
    for produto in lista_produtos:
        print(f"{produto}")

def excluir_produto_da_lista(lista_produtos, id_produto):
    for produto in lista_produtos:
        if produto["ID"] == id_produto:
            lista_produtos.remove(produto)
            print(f"Produto com o ID {id_produto} removido!")
            return True
    print(f"Produto com o ID {id_produto} não está na lista.")
    return False

def menu_principal():
    while True:
        print("""
            1- Registrar Produto
            2- Editar Produto
            3- Exibir Lista de Produtos
            4- Excluir Produto
            X- Sair
        """)
        try:
            opcao = input("Digite a opção desejada: ").upper()
            if opcao == "1":
                _ = registrar_produto()
                print("Produto registrado com sucesso!")
                continue
            elif opcao == "2":
                produto_selecionado_para_edicao = selecionar_produto_para_edicao(lista_produtos)
                detalhe_a_editar = input("Digite o detalhe que deseja editar: ").capitalize().strip()
                novo_valor = input(f"Digite o novo {detalhe_a_editar}: ")
                if editar_detalhes_produto(produto_selecionado_para_edicao, detalhe_a_editar, novo_valor):
                    print("Detalhe do produto editado.")
                continue
            elif opcao == "3":
                exibir_lista_de_produtos()
                continue
            elif opcao == "4":
                id_produto_para_excluir = int(input("Digite o ID do produto que deseja excluir: "))
                excluir_produto_da_lista(lista_produtos, id_produto_para_excluir)
                continue
            elif opcao == "X":
                break
            else:
                print("Por favor, escolha uma opção válida!")
                continue
        except ValueError:
            print("Saindo...")
            break
