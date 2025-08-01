# 2.16 
'''Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829)
como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.
'''
mapa_coordenadas = {
    (-8.0578, -34.8829): 'Recife',
    (-23.5505, -46.6333): 'São Paulo'
}

# 2.17 
'''A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla
(-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.
'''
mapa_coordenadas[(-22.9068, -43.1729)] = 'Rio de Janeiro'

# 2.18 
'''Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas.
A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas
(-23.5505, -46.6333) e (0, 0).
'''
def encontrar_local_por_coordenadas(mapa, coordenadas):
    return mapa.get(coordenadas, 'Local não encontrado.')
# Testando a função com as coordenadas fornecidas
print(encontrar_local_por_coordenadas(mapa_coordenadas, (-23.5505, -46.6333)))
print(encontrar_local_por_coordenadas(mapa_coordenadas, (0, 0)))

