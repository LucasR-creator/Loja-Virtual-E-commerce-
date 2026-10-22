
# NEXASHOP - SISTEMA DE LOJA VIRTUAL

produtos = []


# CADASTRAR PRODUTOS
def cadastrar_produto():
    print("\n===== CADASTRAR PRODUTO =====")

    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()
    descricao = input("Descrição: ").strip()

    if not nome or not categoria or not descricao:
        print("Preencha todos os campos!")
        return

    try:
        preco = float(input("Preço: R$ ").replace(",", "."))
        estoque = int(input("Quantidade em estoque: "))

    except ValueError:
        print("Preço ou estoque inválido!")
        return

    if preco <= 0 or estoque < 0:
        print("Preço ou estoque inválido!")
        return

    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "categoria": categoria,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque,
        "avaliacoes": []
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")


# MOSTRAR CATÁLOGO
def mostrar_catalogo():
    print("\n===== CATÁLOGO NEXASHOP =====")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("\n-------------------------")
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")


# AVALIAR PRODUTO
def avaliar_produto():
    print("\n===== AVALIAR PRODUTO =====")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    mostrar_catalogo()

    try:
        id_produto = int(input("\nDigite o ID do produto: "))

    except ValueError:
        print("ID inválido!")
        return

    produto_encontrado = None

    for produto in produtos:
        if produto["id"] == id_produto:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado!")
        return

    nome_cliente = input("Seu nome: ").strip()

    if not nome_cliente:
        print("Digite seu nome!")
        return

    try:
        nota = int(input("Sua nota (1 a 5): "))

    except ValueError:
        print("Digite uma nota válida!")
        return

    if nota < 1 or nota > 5:
        print("A nota precisa ser de 1 a 5!")
        return

    comentario = input("Seu comentário: ").strip()

    avaliacao = {
        "cliente": nome_cliente,
        "nota": nota,
        "comentario": comentario
    }

    produto_encontrado["avaliacoes"].append(avaliacao)

    print("\nAvaliação cadastrada com sucesso!")


# MOSTRAR AVALIAÇÕES
def mostrar_avaliacoes():
    print("\n===== AVALIAÇÕES DOS PRODUTOS =====")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"\nProduto: {produto['nome']}")

        avaliacoes = produto["avaliacoes"]

        if not avaliacoes:
            print("Ainda não possui avaliações.")
            continue

        soma = sum(
            avaliacao["nota"]
            for avaliacao in avaliacoes
        )

        media = soma / len(avaliacoes)

        print(f"Nota média: {media:.1f}/5")
        print(f"Total de avaliações: {len(avaliacoes)}")

        for avaliacao in avaliacoes:
            print(f"\nCliente: {avaliacao['cliente']}")
            print(f"Nota: {'★' * avaliacao['nota']}")
            print(f"Comentário: {avaliacao['comentario']}")


# MENU PRINCIPAL
def menu():
    while True:
        print("\n===== NEXASHOP =====")
        print("1 - Cadastrar produto")
        print("2 - Ver catálogo")
        print("3 - Avaliar produto")
        print("4 - Ver avaliações")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            mostrar_catalogo()

        elif opcao == "3":
            avaliar_produto()

        elif opcao == "4":
            mostrar_avaliacoes()

        elif opcao == "0":
            print("Encerrando NexaShop...")
            break

        else:
            print("Opção inválida!")


# INICIAR O SISTEMA
if __name__ == "__main__":
    menu()
