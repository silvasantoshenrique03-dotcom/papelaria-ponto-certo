produtos = []

def mostrar_menu(qtd_produtos):
    print("\n--- Menu ---")
    print(f"Produtos cadastrados: {qtd_produtos}")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos")
    print("0 - Sair")


def listar_produtos(produtos):
    for produto in produtos:
        print(produto)
def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco_valido = False
    while not preco_valido:
        try:
            preco = float(input("Preço do produto (maior que zero): "))
            if preco > 0:
                preco_valido = True
            else:
                print("Preço inválido. Digite um valor maior que zero.")
        except ValueError:
            print("Digite um preço numérico válido.")
    produtos.insert(0,(nome, preco))
    print("Produto cadastrado com sucesso!")

def consultar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    encontrado = False
    i = 0
    while i < len(produtos):
        if produtos[i][0].lower () == nome_busca.lower ():
            print(
                f"Produto encontrado: "
                f"{produtos[i][0]} - R$ {produtos[i][1]:.2f}"
            )
            encontrado = True
        i += 1
    if not encontrado:
        print("Produto não encontrado.")

def listar_produtos(produtos):
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado.")
        return
    print("\n=== Produtos cadastrados ===\n")
    for i, produto in enumerate(produtos, start=1):
        nome = produto[0]
        preco = produto[1]
        preco_formatado = f"{preco:.2f}".replace(".", ",")
        print(f"{i}. {nome:.<20} R$ {preco_formatado}")
    print(f"\nTotal de produtos: {len(produtos)}")

continuar = True

while continuar:
    mostrar_menu(len(produtos))
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_produto(produtos)
    elif opcao == "2":
        consultar_produto(produtos)
    elif opcao == "3":
        listar_produtos(produtos)
    elif opcao == "0":
        continuar = False
        print("Programa encerrado.")
    else:
        print("Opção inválida.")

print("Lista de produtos cadastrados:")
print(produtos)