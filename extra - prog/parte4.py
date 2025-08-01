# Parte 4: Matrizes (NumPy)

# 4.1 
'''Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas com os dados: 
[0, 1, 3]
[9, 7, 4]
[2, 6, 6]
[3, 3, 3]. '''
import numpy as np
vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
print(vendas)

# 4.2 
'''Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) e sua transposta (atributo .T).
'''
print(vendas.shape)
print(vendas.T)
# 4.3
'''Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).
'''
matriz_zeros = np.zeros((3, 3), dtype=int)
print(matriz_zeros)

# 4.4
'''Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados para o segundo produto (linha de índice 1).
'''
linha_produto_2 = vendas[1, :]
print(linha_produto_2)

# 4.5
'''Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados para o terceiro mês (coluna de índice 2).
'''
coluna_mes_3 = vendas[:, 2]
print(coluna_mes_3)

# 4.6
'''Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) no mês 2 (coluna 1).
'''
valor_produto_3_mes_2 = vendas[2, 1]
print(valor_produto_3_mes_2)

# 4.7
'''Dada a matriz de preços matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]]), crie uma nova matriz com todos os preços aumentados em 5%.
'''
matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]])
matriz_precos_aumentada = matriz_precos * 1.05
print(matriz_precos_aumentada)

# 4.8
'''Dadas as matrizes de vendas com a quantidade de vendas de 4 produtos nos primeiros 3 meses do ano,
vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]]) e vendas_europa = np.array([[90, 140, 190], [70, 110, 150],
[80, 100, 120], [60, 90, 130]]), some-as para criar uma matriz vendas_globais.
'''
vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]])
vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]])
vendas_globais = vendas_eua + vendas_europa
print(vendas_globais)

# 4.9
'''Dada a matriz de vendas vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) (3 produtos x 2 meses) e o vetor de preços precos = np.array([4.99, 5.25, 2.19]), calcule a receita total por mês usando o produto escalar (np.dot).
'''
vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]])
precos = np.array([4.99, 5.25, 2.19])
receita_total = np.dot(vendas_unidades, precos)
print(receita_total)

# 4.10
'''Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas em cada mês (soma ao longo do eixo 0).
'''
total_unidades_mes = vendas.sum(axis=0)
print(total_unidades_mes)

# 4.11
'''Usando a mesma matriz de vendas, calcule a média de vendas para cada produto (média ao longo do eixo 1).
'''
media_vendas_produto = vendas.mean(axis=1)
print(media_vendas_produto)
# 4.12
'''A partir da matriz de vendas, encontre e imprima o valor máximo.
'''
valor_maximo_vendas = vendas.max()
print(valor_maximo_vendas)