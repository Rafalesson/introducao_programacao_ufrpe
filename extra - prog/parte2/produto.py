# 2.2
'''Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 'estoque'
com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.
'''
produto = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}

# 2.4
''' Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio',
'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. 
Em seguida, atualize o preço para o valor promocional de 249.99.
'''
print(produto.get('preco'))
produto['preco'] = 249.99
print(produto.get('preco'))

# 2.8
'''Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'},
use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o
valor retornado (o nome do produto) e imprima uma mensagem de confirmação.
'''
catalogo_produtos = {
    'XYZ-001': 'Fone de Ouvido Sem Fio',
    'ABC-002': 'Teclado Mecânico'
}
produto_removido = catalogo_produtos.pop('XYZ-001', 'Produto não encontrado.')
print(f'Produto removido: {produto_removido}')

# 2.10 
'''Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50},
itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.
'''
catalogo_produtos_precos = {
    'Fone de Ouvido': 249.99,
    'Teclado Mecânico': 450.00,
    'Mouse Gamer': 120.50
}

# 2.11 
'''Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50},
itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.
'''
lista_compras = {
    'Tapioca': 18.99,
    'Queijo Manteiga': 45.00,
    'Ovos': 23.50
}

total = 0
for item, preco in lista_compras.items():
    print(f'Nome: {item}, Preço: R${preco:.2f}')
    total += preco
print(f'Total: R${total:.2f}')