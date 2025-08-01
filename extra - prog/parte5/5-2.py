'''Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. A função deve retornar uma 
tupla contendo: 1. O valor total do inventário (soma de preco * estoque), 2. O nome do produto mais caro, e 3. 
Uma lista de produtos sem estoque. Teste a função com o catálogo: {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 
'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': 
{'preco': 250.00, 'estoque': 0}}.
'''
def analisar_inventario(catalogo):
    valor_total = 0
    produto_mais_caro = ''
    preco_mais_caro = 0
    produtos_sem_estoque = []

    for produto, info in catalogo.items():
        valor_total += info['preco'] * info['estoque']
        
        if info['preco'] > preco_mais_caro:
            preco_mais_caro = info['preco']
            produto_mais_caro = produto
        
        if info['estoque'] == 0:
            produtos_sem_estoque.append(produto)

    return valor_total, produto_mais_caro, produtos_sem_estoque
# Testando a função com o catálogo fornecido
catalogo = {
    'Laptop Gamer': {'preco': 7500.00, 'estoque': 10},
    'Mouse Vertical': {'preco': 350.00, 'estoque': 50},
    'Monitor 4K': {'preco': 4200.00, 'estoque': 15},
    'Webcam HD': {'preco': 250.00, 'estoque': 0}
}
valor_total, produto_mais_caro, produtos_sem_estoque = analisar_inventario(catalogo)
print(f"Valor total do inventário: R${valor_total:.2f}")
print(f"Produto mais caro: {produto_mais_caro} (R${catalogo[produto_mais_caro]['preco']:.2f})")
print(f"Produtos sem estoque: {', '.join(produtos_sem_estoque) if produtos_sem_estoque else 'Nenhum'}")