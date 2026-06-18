rodando = True
produtos = [
    [27300, "Rolamento de Rolos Cônicos", 3, "3, 0"],
    [13783, "Válvula Solenoide", 6, "3, 1"],
    [89243, "Engrenagem Helicoidal", 5, "3, 2"]
]

def adicionar_produto():
    global produtos
    produtos = input("Insira seu produto: ")

def listar_produtos():
    for i in range(len(produtos)):
        print(produtos[i][2])

while rodando == True:
    print("\nBem vindo ao Sistema de Controle de Estoque Simplificado (SCES). Selecione uma opção:")
    print("\n1 - Adicionar Produto\n2 - Listar Todos os Produtos\n3 - Buscar Produto por ID\n4 - Atualizar Estoque\n5 - Sair")
    opcao = input("\nEscolha: ")
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        listar_produtos()
    elif opcao == "4":
        listar_produtos()
    else:
        rodando = False