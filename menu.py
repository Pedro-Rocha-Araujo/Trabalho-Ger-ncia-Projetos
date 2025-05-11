# É aqui onde serão armazenados os produtos
lista_produtos = []
# É aqui onde as compras dos clientes serão registradas
carrinho_de_compras = []
# Éssa é a classe do produto, como se fosse um molde que receberá suas características
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
# Esse é o menu de navegação que irá aparecer para o operador    
def menu():
    print('''[1] - Realizar compra
[2] - Cadastrar Novo Produto
[3] - Sair''')
# Essa é a função responsável pr cadastrar os produtos    
def CadastroProduto():
    nome_produto = str(input('Digite aqui o nome do produto que deseja cadastrar: '))
    preco_produto = float(input('Digite aqui o preço do produto que deseja cadastar: '))
    novo_produto = Produto(nome_produto, preco_produto)
    lista_produtos.append(novo_produto)
    print('---'*20)
    print(f'O produto: {nome_produto} que custa R${preco_produto} reais foi cadastrado com sucesso!')
# Essa é a função responsável por realizar as compras
def ComprarProduto():
    while True:
        print('---'*20)
        for i, item in enumerate(lista_produtos, 1):
            print(f"[{i}] - {item}")
        print('---'*20)
        resposta = int(input('Digite o número referente a opção que deseja comprar: '))
        print('---'*20)
        produto_escolhido = lista_produtos[resposta - 1]
        carrinho_de_compras.append(produto_escolhido)
        print(f'Por enquanto seu carrinho de compras está asim: ')
        for i in carrinho_de_compras:
            print(i)
        print('---'*20)
        repetir = str(input('Deseja realizar outra compra? [s/n]: ')).upper()
        if(repetir == 'N'):
            break
# Essses são os crodutos já previamente cadastrados
lista_produtos.append(Produto("Arroz 5kg", 25.90))
lista_produtos.append(Produto("Feijão 1kg", 8.50))
lista_produtos.append(Produto("Macarrão 500g", 4.20))
lista_produtos.append(Produto("Óleo de Soja 900ml", 6.80))
lista_produtos.append(Produto("Café 500g", 16.75))

while True:
    print('=-='*20)
    menu()
    print('=-='*20)
    resposta = int(input('Digite aqui sua Resposta: '))
    if (resposta == 1):
        carrinho_de_compras.clear()
        ComprarProduto()

    if (resposta == 2):
        CadastroProduto()

    if (resposta == 3):
        break
    else:
        print('---'*20)
        print('Digite uma opção Válida')