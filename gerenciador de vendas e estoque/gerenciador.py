import json as js
import json as jso

def salvar_estoque(estoque):
    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        js.dump(estoque, arquivo, indent=4, ensure_ascii=False)

def carregar_estoque():
    try:
        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            return js.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'estoque.json' não encontrado. Criando um novo arquivo.")
        return []
    except js.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_estoque(estoque):
    if estoque:
        print("\nESTOQUE:")
        for i, estoque in enumerate(estoque, start=1):
            print(f"\nPRODUTO {i}:")
            print(f"Nome: {estoque['produto']}")
            print(f"Quantidade: {estoque['quantidade']}")
    else:
        print("Não há estoque registrado.")

def adicionar_estoque(estoque):
    nome_produto = input("Digite o nome do produto: ")

    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade de produtos: "))
            if quantidade_produto <= 0:
                print("O preço deve ser maior que zero. Tente novamente.")
                break

        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
        break   

    _estoque_ = {
    "produto": nome_produto,
    "quantidade": quantidade_produto
    }

    estoque.append(_estoque_)

    salvar_estoque(estoque)

    print(f"Estoque de {quantidade_produto} unidades de {nome_produto} adicionada com sucesso!")


def criar_estoque():

    estoque = carregar_estoque()
    
    while True:

        print(
            "1. Adicionar estoque",
            "\n2. Vizualizar estoque",
            "\n3. Gerenciar vendas"
        )

        escolha = input("Escolha uma opção: ")

        if escolha == "3":
            print("Finalizando estoque...")
            break
        elif escolha == "2":
            exibir_estoque(estoque)
        elif escolha == "1":
            adicionar_estoque(estoque)
        else:
            print("Opção invalida tente novamente!")

criar_estoque()


def salvar_vendas(vendas):
    with open('vendas.json', 'w', encoding='utf-8') as arquivo:
        jso.dump(vendas, arquivo, indent=4, ensure_ascii=False)

def carregar_vendas():
    try:
        with open('vendas.json', 'r', encoding='utf-8') as arquivo:
            return jso.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'vendas.json' não encontrado. Criando um novo arquivo.")
        return []
    except jso.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_vendas(vendas):
    if vendas:
        print("\nVendas realizadas:")
        for i, venda in enumerate(vendas, start=1):
            print(f"\nPRODUTO {i}:")
            print(f"Nome: {venda['produto']}")
            print(f"Preço: R$ {venda['preço']:.2f}")
            print(f"Quantidade vendida: {venda['quantidade']}")
            print(f"Total: R$ {venda['total']:.2f}")
    else:
        print("Não há vendas registradas.")

def adicionar_venda(vendas):
    
    estoque = carregar_estoque()
    
    exibir_estoque(estoque)
    numero_produto = int(input("\nDigite o numero do produto do estoque: "))
    
    if numero_produto <= 0:
        print("O preço deve ser maior que zero. Tente novamente!")
    elif numero_produto > len(estoque):
        print("Produto não encontrado. Tente novamente!")
    else:
        print(f"\nProduto selecionado: {estoque[numero_produto - 1]['produto']}")

    while True:
        try:
            preco_produto = float(input("\nDigite o preço do produto: R$ "))
            if preco_produto <= 0:
                print("O preço deve ser maior que zero. Tente novamente.")
                continue
            quantidade_vendida = int(input("Digite a quantidade vendida: "))
            if quantidade_vendida <= 0:
                print("A quantidade deve ser maior que zero. Tente novamente.")
                continue
            break

        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

    total_venda = preco_produto * quantidade_vendida
    estoque_atualizado = estoque[numero_produto - 1]['quantidade'] - quantidade_vendida



    venda = {
        "produto": estoque[numero_produto - 1]['produto'],
        "preço": preco_produto,
        "quantidade": quantidade_vendida,
        "total": total_venda,
        "estoque": estoque_atualizado
    }

    vendas.append(venda)

    salvar_vendas(vendas)

    print(f"\nVenda de {quantidade_vendida} unidades de {estoque[numero_produto - 1]['produto']} adicionada com sucesso!")

    print(f"\nEstoque atualizado: {estoque_atualizado} unidades")

def gerenciador_vendas():
    
    vendas = carregar_vendas()
    estoque = carregar_estoque()

    while True:
        print("\nEscolha uma opção:")
        print("1. Visualizar vendas")
        print("2. Visualizar estoque")
        print("3. Adicionar venda")
        print("4. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == "1":
            exibir_vendas(vendas)
        elif opcao == "2":
            exibir_estoque(estoque)
        elif opcao == "3":
            adicionar_venda(vendas)
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

gerenciador_vendas()