import json as js
import json as jso

# Funções para manipular o estoque
def salvar_estoque(estoque):
    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

def carregar_estoque():
    try:
        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'estoque.json' não encontrado. Criando um novo arquivo.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_estoque(estoque):
    if estoque:
        print("\nESTOQUE:")
        for i, item in enumerate(estoque, start=1):
            print(f"\nPRODUTO {i}:")
            print(f"Nome: {item['produto']}")
            print(f"Quantidade: {item['quantidade']}")
    else:
        print("Não há estoque registrado.")

def adicionar_estoque(estoque):
    nome_produto = input("Digite o nome do produto: ")

    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade de produtos: "))
            if quantidade_produto <= 0:
                print("A quantidade deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

    novo_item = {
        "produto": nome_produto,
        "quantidade": quantidade_produto
    }
    estoque.append(novo_item)
    salvar_estoque(estoque)
    print(f"Estoque de {quantidade_produto} unidades de {nome_produto} adicionado com sucesso!")

# Funções para manipular vendas
def salvar_vendas(vendas):
    with open('vendas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(vendas, arquivo, indent=4, ensure_ascii=False)

def carregar_vendas():
    try:
        with open('vendas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'vendas.json' não encontrado. Criando um novo arquivo.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_vendas(vendas):
    if vendas:
        print("\nVENDAS REALIZADAS:")
        for i, venda in enumerate(vendas, start=1):
            print(f"\nVENDA {i}:")
            print(f"Produto: {venda['produto']}")
            print(f"Preço: R$ {venda['preço']:.2f}")
            print(f"Quantidade vendida: {venda['quantidade']}")
            print(f"Total: R$ {venda['total']:.2f}")
    else:
        print("Não há vendas registradas.")

def adicionar_venda(vendas):
    estoque = carregar_estoque()
    exibir_estoque(estoque)

    if not estoque:
        print("Não há itens no estoque para vender.")
        return

    while True:
        try:
            numero_produto = int(input("\nDigite o número do produto do estoque: "))
            if numero_produto <= 0 or numero_produto > len(estoque):
                print("Produto não encontrado. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    produto_selecionado = estoque[numero_produto - 1]
    print(f"\nProduto selecionado: {produto_selecionado['produto']}")

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
            
            if quantidade_vendida > produto_selecionado['quantidade']:
                print("Quantidade em estoque insuficiente. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

    total_venda = preco_produto * quantidade_vendida
    produto_selecionado['quantidade'] -= quantidade_vendida
    salvar_estoque(estoque)

    venda = {
        "produto": produto_selecionado['produto'],
        "preço": preco_produto,
        "quantidade": quantidade_vendida,
        "total": total_venda
    }
    vendas.append(venda)
    salvar_vendas(vendas)

    print(f"\nVenda de {quantidade_vendida} unidades de {produto_selecionado['produto']} adicionada com sucesso!")
    print(f"Estoque atualizado: {produto_selecionado['quantidade']} unidades")

# Gerenciadores principais
def criar_estoque():
    estoque = carregar_estoque()
    while True:
        print("\n1. Adicionar estoque")
        print("2. Visualizar estoque")
        print("3. Sair")
        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            adicionar_estoque(estoque)
        elif escolha == "2":
            exibir_estoque(estoque)
        elif escolha == "3":
            print("Saindo do gerenciador de estoque...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def gerenciador_vendas():
    vendas = carregar_vendas()
    while True:
        print("\n1. Visualizar vendas")
        print("2. Visualizar estoque")
        print("3. Adicionar venda")
        print("4. Sair")
        opcao = input("\nDigite o número da opção desejada: ")
        if opcao == "1":
            exibir_vendas(vendas)
        elif opcao == "2":
            exibir_estoque(carregar_estoque())
        elif opcao == "3":
            adicionar_venda(vendas)
        elif opcao == "4":
            print("Saindo do sistema de vendas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
print("\nBem-vindo ao sistema de gerenciamento!")
while True:
    print("\n1. Gerenciar Estoque")
    print("2. Gerenciar Vendas")
    print("3. Sair")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        criar_estoque()
    elif escolha == "2":
        gerenciador_vendas()
    elif escolha == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")