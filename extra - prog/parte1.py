# Parte 1: Tuplas

# 1.1 
'''Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho,
102 para verde e 0 para azul.
'''
cores_rgb = (255, 102, 0)

# 1.2
'''Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.
'''
coordenadas_geo = (-8.0578, -34.8829)

# 1.3
'''Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101,
o username 'ana_silva' e a data de criação '2023-01-15'.
'''
usuario_info = (101, 'ana_silva', '2023-01-15')

# 1.4
'''Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).
'''
print(cores_rgb[1])

# 1.5
'''Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas
latitude e longitude.
'''
latitude, longitude = coordenadas_geo
print(f'Latitude: {latitude}, Longitude: {longitude}')

# 1.6
'''A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email),
desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.
'''
usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')
id_usuario, nome_usuario, email_usuario = usuario
print(f"Olá, {nome_usuario}!")

# 1.7
'''Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.
'''
papeis_admin = ('moderador', 'editor', 'sysadmin')
for papel in papeis_admin:
    print(f"Papel de administrador: {papel}")

# 1.8
'''Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.
'''
dados_usuarios = (id_usuario, nome_usuario, email_usuario)
for dado in dados_usuarios:
    print(f"Dado do usuário: {dado}")

# 1.9
'''Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.
'''
for cor in cores_rgb:
    print(f"Cor: {cor}")

# 1.10
'''Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.
'''

def verificar_papel(papel):
    papeis_admin = ('moderador', 'editor', 'sysadmin')
    return papel in papeis_admin

print(verificar_papel('editor'))
print(verificar_papel('usuario_comum'))

# 1.11
'''Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'),
escreva uma função que conta o número de vezes em que um papel aparece, teste a função com os papíes
'editor', 'comentarista' e 'tradutor'.
'''

def contar_ocorrencias(papel):
    atribuicoes = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
    return atribuicoes.count(papel)
print(contar_ocorrencias('editor'))
print(contar_ocorrencias('comentarista'))
print(contar_ocorrencias('tradutor'))