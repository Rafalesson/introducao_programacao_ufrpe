# Parte 3: Vetores (Listas e NumPy)

# 3.1 
'''Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' ao final da lista.
'''
tags_post = ['#tecnologia', '#python', '#programacao']
tags_post.append('#dados')
print(tags_post)

# 3.2
'''Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], remova o elemento '#programacao'.
'''
tags_post.remove('#programacao')
print(tags_post)

# 3.3
'''Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a string '#importante' existe na lista.
'''
tags_post = ['#tecnologia', '#python', '#dados']
existe_importante = '#importante' in tags_post
print(f"A tag '#importante' existe na lista? {existe_importante}")

# 3.4
'''Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): [('camiseta', 10), ('calça', 5), ('sapato', 2)].
'''
import numpy as np
itens_vendidos = [('camiseta', 10), ('calça', 5), ('sapato', 2)]
array_itens_vendidos = np.array(itens_vendidos, dtype=[('produto', 'U20'), ('quantidade', 'i4')])
print(array_itens_vendidos)

# 3.5
'''Crie um array NumPy para armazenar as seguintes pontuações de um aluno: [0.85, 0.92, 0.78, 0.95, 0.88].
'''
pontos_aluno = [0.85, 0.92, 0.78, 0.95, 0.88]
array_pontos_aluno = np.array(pontos_aluno)
print(array_pontos_aluno)

# 3.6
'''Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].
'''
temperaturas_celsius = [45.5, 46.0, 45.8, 47.1, 46.5]
array_temperaturas_celsius = np.array(temperaturas_celsius)
print(array_temperaturas_celsius)

# 3.7
'''Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0), (Tênis, 150.0)]), crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).
'''
precos = np.array([('Sapato', 100.0), ('Calça', 250.0), ('Camiseta', 80.0), ('Tênis', 150.0)], dtype=[('item', 'U20'), ('preco', 'f4')])
precos_com_desconto = precos.copy()
precos_com_desconto['preco'] *= 0.9
print(precos_com_desconto)

# 3.8
'''Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.
'''
precos_com_desconto_15 = precos.copy()
precos_com_desconto_15['preco'] *= 0.85
for item in precos:
    print(f"O {item['item']} custava {item['preco']}, agora custa {precos_com_desconto_15['preco'][np.where(precos['item'] == item['item'])][0]}.")

# 3.9
'''Dados os arrays de quantidades e preços unitários, calcule o valor total por item multiplicando os dois arrays.
'''
quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])
valores_totais = quantidades * precos_unitarios
print(valores_totais)

# 3.10
'''Dado o array de temperaturas em Celsius temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]), converta todas as temperaturas para Fahrenheit usando a fórmula F = C * 1.8 + 32.
'''
temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])
temperaturas_fahrenheit = temperaturas_celsius * 1.8 + 32
print(temperaturas_fahrenheit)
