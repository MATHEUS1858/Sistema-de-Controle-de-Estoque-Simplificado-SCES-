rodando = True
produtos = [
    ["27300", "Rolamento de Rolos Cônicos", "3", "0"],
    ["13783", "Válvula Solenoide", "6", "1"],
    ["89243", "Engrenagem Helicoidal", "5", "2"],
]

def travar_tela():
    input("\nPressione <ENTER> para continuar...")

def adicionar_produto():
    id = input("Digite o ID da peça: ")
    nomedapeca = input("Digite o nome da peça: ")
    quantidade = input("Digite a quantidade presente no estoque: ")
    localizacao = input("Digite a localização da peça: ")
    novoproduto = [id, nomedapeca, quantidade, localizacao]
    produtos.append(novoproduto)
    print("Produto adicionado com sucesso.")
    travar_tela()

def listar_produtos():
    for i in range(len(produtos)):
        print(produtos[i])
    travar_tela()

def buscar_por_id():
    buscar = input("Buscar produto por ID: ")
    for i in range(len(produtos)):
        if buscar == produtos[i][0]:
            print(produtos[i])
    travar_tela()

def atualizar_estoque():
    global produtos
    buscar = input("Coloque o ID do produto: ")
    for i in range(len(produtos)):
        if buscar == produtos[i][0]:
            nova_quantidade = input("Atualize seu estoque: ")
            produtos[i][2] = nova_quantidade
    travar_tela()

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
    elif opcao == "5":
        rodando = False