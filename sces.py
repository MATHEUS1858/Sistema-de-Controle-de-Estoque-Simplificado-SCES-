rodando = True
produtos = [
    ["27300", "Rolamento de Rolos Cônicos", "3", "0"],
    ["13783", "Válvula Solenoide", "6", "1"],
    ["89243", "Engrenagem Helicoidal", "5", "2"],
]

def adicionar_produto():
    id = input("Digite o ID da peça: ")
    nomedapeca = input("Digite o nome da peça: ")
    quantidade = input("Digite a quantidade presente no estoque: ")
    localizacao = input("Digite a localização da peça: ")
    novoproduto = [id, nomedapeca, quantidade, localizacao]
    produtos.append(novoproduto)
    print("Peça adicionada com sucesso.")

def listar_produtos():
    for i in range(len(produtos)):
        print(produtos[i])

def buscar_por_id():
    buscar = input("Buscar Produto por ID: ")
    for i in range(len(produtos)):
        if buscar == produtos[i][0]:
            print(produtos[i])

def atualizar_estoque():
    global produtos
    posicao = input("Digite a posição no eixo y: ")
    produtos[posicao][2] = input("Digite a quantidade de produtos presentes: ")

while rodando == True:
    print("\nBem vindo ao Sistema de Controle de Estoque Simplificado (SCES). Selecione uma opção:")
    print("\n1 - Adicionar Produto\n2 - Listar Todos os Produtos\n3 - Buscar Produto por ID\n4 - Atualizar Estoque\n5 - Sair")
    opcao = input("\nEscolha: ")
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_por_id()
    elif opcao == "4":
        atualizar_estoque()
    else:
        rodando = False