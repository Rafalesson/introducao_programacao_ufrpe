import numpy as np
import datetime

print("===========================================================================")
print("\t\t\tParte 1: Tuplas")
print("===========================================================================\n")

# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), 
# usando os valores 255 para vermelho, 102 para verde e 0 para azul.
# (Nota: O valor para azul foi inferido da questão 1.4)
cores_rgb = (255, 102, 0)
print(f"1.1: {cores_rgb}")
print('---')

# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude 
# e -34.8829 para longitude.
coordenadas_geo = (-8.0578, -34.8829)
print(f"1.2: {coordenadas_geo}")
print('---')

# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, 
# contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.
info_usuario = (101, 'ana_silva', '2023-01-15')
print(f"1.3: {info_usuario}")
print('---')

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 
# 'Verde' (o segundo elemento, de índice 1).
valor_verde = cores_rgb[1]
print(f"1.4: O valor do componente Verde é {valor_verde} ")
print('---')

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas 
# variáveis separadas chamadas latitude e longitude.
latitude, longitude = coordenadas_geo
print(f"1.5: Latitude: {latitude}, Longitude: {longitude}")
print('---')

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), 
# que representa (id, nome, email), desempacote-a em variáveis e use a variável 
# do nome para imprimir uma saudação.
usuario_info = (205, 'Carlos Pereira', 'carlos.p@email.com')
id_usuario, nome, email = usuario_info
print(f"1.6: Olá, {nome}! Bem-vindo!")
print('---')

# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), 
# itere sobre ela e imprima cada papel.
papeis_admin = ('moderador', 'editor', 'sysadmin')
print("1.7: Papéis de Administrador:")
for papel in papeis_admin:
    print(f"    - {papel}")
print('---')

# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.
print("1.8: Dados do Usuário:")
for dado in usuario_info:
    print(f"    - {dado}")
print('---')

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.
print("1.9: Componentes da cor RGB:")
componentes = ['R', 'G', 'B']
for i, valor in enumerate(cores_rgb):
    print(f"    - {componentes[i]}: {valor}")
print('---')

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de 
# papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com 
# os papéis 'editor' e 'usuario_comum'.
def verificar_papel(papel, tupla_papeis):
    if papel in tupla_papeis:
        return "Sim!"
    else:
        return "Não!"

papeis_admin = ('moderador', 'editor', 'sysadmin')
print(f"1.10: O papel 'editor' existe? {verificar_papel('editor', papeis_admin)}")
print(f"1.10: O papel 'usuario_comum' existe? {verificar_papel('usuario_comum', papeis_admin)}")
print('---')

# 1.11 Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 
# 'comentarista', 'editor'), escreva uma função que conta o número de vezes em que um papel 
# aparece, teste a função com os papíes 'editor', 'comentarista' e 'tradutor'.
def contar_ocorrencias(papel, tupla_atribuicoes):
    return tupla_atribuicoes.count(papel)

atribuicoes = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
print(f"1.11: Ocorrências de 'editor': {contar_ocorrencias('editor', atribuicoes)}")
print(f"1.11: Ocorrências de 'comentarista': {contar_ocorrencias('comentarista', atribuicoes)}")
print(f"1.11: Ocorrências de 'tradutor': {contar_ocorrencias('tradutor', atribuicoes)}")

print("\n=========================================================================")
print("\t\t\tParte 2: Dicionários")
print("===========================================================================\n")

# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', 
# a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.
usuario = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
print(f"2.1: {usuario}")
print("---")


# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 
# 'estoque' com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.
produto = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}
print(f"2.2: {produto}")
print("---")

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.
preferencias_usuario = {}
print(f"2.3: {preferencias_usuario}")
print("---")

# 2.4 Dado o dicionário de produto {...}, acesse e imprima o preço original. 
# Em seguida, atualize o preço para o valor promocional de 249.99.
print(f"2.4: Preço original: {produto['preco']}")
produto['preco'] = 249.99
print(f"2.4: Preço promocional: {produto['preco']}")
print("---")

# 2.5 Dado o perfil de usuário {...}, adicione uma nova informação: 
# a chave 'telefone' com o valor '98765-4321'.
usuario['telefone'] = '98765-4321'
print(f"2.5: {usuario}")
print("---")

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar 
# acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 
# 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir 
# a chave 'ultimo_login' com o valor '2024-05-22'.
perfil_bia = {'username': 'bia_costa'}
ultimo_login = perfil_bia.get('ultimo_login', 'Nunca logou')
print(f"2.6: Status inicial: {ultimo_login}")
perfil_bia['ultimo_login'] = '2024-05-22'
print(f"2.6: Status atualizado: {perfil_bia}")
print("---")

# 2.7 Dado o perfil de usuário {...}, use a instrução del ou a função pop() para 
# remover a chave 'telefone_fixo'.
perfil_com_fixo = {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}
del perfil_com_fixo['telefone_fixo']
print(f"2.7: {perfil_com_fixo}")
print("---")

# 2.8 Dado o catálogo de produtos {...}, use o método.pop() para remover o produto 
# com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima 
# uma mensagem de confirmação.
catalogo_produtos = {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}
produto_removido = catalogo_produtos.pop('XYZ-001')
print(f"2.8: Produto '{produto_removido}' foi removido. Catálogo atual: {catalogo_produtos}")
print("---")

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' 
# usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.
perfil_simples = {'username': 'bia_costa'}
resultado = perfil_simples.pop('email', 'Email não encontrado.')
print(f"2.9: Resultado da remoção: {resultado}")
print("---")

# 2.10 Dado o catálogo de produtos {...}, itere sobre seus itens e imprima o nome 
# e o preço de cada um no formato 'Nome: R$Preço'.
catalogo_precos = {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}
print("2.10: Catálogo de Produtos:")
for nome, preco in catalogo_precos.items():
    print(f"    - {nome}: R${preco:.2f}")
print("---")

# 2.11 Dado a lista de compras da feira {...}, itere sobre seus itens e imprima o nome e o 
# preço de cada um no formato 'Nome: R$Preço e depois imprima o total.
lista_feira = {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}
total_feira = 0
print("2.11: Compras da Feira:")
for item, preco in lista_feira.items():
    print(f"    - {item}: R${preco:.2f}")
    total_feira += preco
print(f"Total: R${total_feira:.2f}")
print("---")

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. 
# O valor associado a essa chave deve ser outro dicionário contendo: 
# 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.
perfil_usuario_2 = {'username': 'bia_costa'}
perfil_usuario_2['endereco'] = {
    'rua': 'Rua das Flores, 123',
    'cidade': 'São Paulo',
    'cep': '01000-000'
}
print(f"2.12: {perfil_usuario_2}")
print("---")

# 2.13 Dado o perfil de usuário da questão anterior, adicione uma nova chave 'profissao'. 
# O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 
# 'empresa': 'Tech Solutions'.
perfil_usuario_2['profissao'] = {
    'cargo': 'Desenvolvedora',
    'empresa': 'Tech Solutions'
}
print(f"2.13: {perfil_usuario_2}")
print("---")

# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, 
# acesse e imprima apenas o valor associado à chave 'cidade'.
cidade = perfil_usuario_2['endereco']['cidade']
print(f"2.14: A cidade do usuário é {cidade}")
print("---")

# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' 
# para 'Avenida Principal, 456'.
perfil_usuario_2['endereco']['rua'] = 'Avenida Principal, 456'
print(f"2.15: {perfil_usuario_2['endereco']}")
print("---")

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla 
# (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) 
# como chave para o valor 'São Paulo'.
mapa_locais = {
    (-8.0578, -34.8829): 'Recife',
    (-23.5505, -46.6333): 'São Paulo'
}
print(f"2.16: {mapa_locais}")
print("---")

# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser 
# a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.
mapa_locais[(-22.9068, -43.1729)] = 'Rio de Janeiro'
print(f"2.17: {mapa_locais}")
print("---")

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a 
# partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a 
# coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).
def encontrar_local(coordenadas, mapa):
    return mapa.get(coordenadas, "Local não encontrado.")

print(f"2.18: Buscando por (-23.5505, -46.6333): {encontrar_local((-23.5505, -46.6333), mapa_locais)}")
print(f"2.18: Buscando por (0, 0): {encontrar_local((0, 0), mapa_locais)}")

print("\n========================================================================")
print("\t\t\tParte 3: Vetores")
print("==========================================================================\n")

# 3.1 Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores 
# ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' 
# ao final da lista.
tags_post = ['#tecnologia', '#python', '#programacao']
tags_post.append('#dados')
print(f"3.1: {tags_post}")
print('---')

# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], 
# remova o elemento '#programacao'.
tags_post.remove('#programacao')
print(f"3.2: {tags_post}")
print('---')

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a 
# string '#importante' existe na lista.
existe = '#importante' in tags_post
print(f"3.3: A tag '#importante' existe? {existe}")
print('---')

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista 
# de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): 
# [('camiseta', 10), ('calça', 5), ('sapato', 2)].
itens_vendidos = [('camiseta', 10), ('calça', 5), ('sapato', 2)]
array_vendas = np.array(itens_vendidos)
print(f"3.4:\n{array_vendas}")
print('---')

# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno: 
# [0.85, 0.92, 0.78, 0.95, 0.88].
pontuacoes = np.array([0.85, 0.92, 0.78, 0.95, 0.88])
print(f"3.5: {pontuacoes}")
print('---')

# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].
temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])
print(f"3.6: {temperaturas_celsius}")
print('---')

# 3.7 Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), ...]), 
# crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).
# (Nota: O array foi corrigido para ser funcional, usando dtype=object para tipos mistos)
precos = np.array([("Sapato", 100.0), ("Calça", 250.0), ("Camiseta", 80.0), ("Tênis", 150.0)], dtype=object)
precos_com_desconto = np.array([(item, preco * 0.9) for item, preco in precos])
print(f"3.7:\n{precos_com_desconto}")
print('---')

# 3.8 Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais 
# e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.
print("3.8:")
for item, preco_original in precos:
    preco_com_desconto = preco_original * 0.85
    print(f"O {item} custava R${preco_original:.2f}, agora custa R${preco_com_desconto:.2f}.")
print('---')

# 3.9 Dados o array de quantidades ... e o array de preços unitários ..., calcule o valor 
# total por item multiplicando os dois arrays.
quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])
valor_total_item = quantidades * precos_unitarios
print(f"3.9: {valor_total_item}")
print('---')

# 3.10 Dado o array de temperaturas em Celsius ..., converta todas as temperaturas para 
# Fahrenheit usando a fórmula F = C * 1.8 + 32.
temperaturas_fahrenheit = temperaturas_celsius * 1.8 + 32
print(f"3.10: {temperaturas_fahrenheit}")


print("\n========================================================================")
print("\t\t\tParte 4: Matrizes")
print("\n========================================================================\n")

# 4.1 Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas.
# (Nota: Os dados do PDF foram organizados em uma matriz 3x4)
vendas_matriz = np.array([
    [0, 1, 3],
    [9, 7, 4],
    [2, 6, 6],
    [3, 3, 3],
])
print(f"4.1: Matriz de Vendas\n{vendas_matriz}")
print('---')

# 4.2 Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) 
# e sua transposta (atributo .T).
print(f"4.2: Shape: {vendas_matriz.shape}")
print(f"4.2: Transposta:\n{vendas_matriz.T}")
print('---')

# 4.3 Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).
matriz_zeros = np.zeros((3, 3), dtype=int)
print(f"4.3:\n{matriz_zeros}")
print('---')

# 4.4 Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados 
# para o segundo produto (linha de índice 1).
linha_produto_2 = vendas_matriz[1, :]
print(f"4.4: {linha_produto_2}")
print('---')

# 4.5 Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados 
# para o terceiro mês (coluna de índice 2).
coluna_mes_3 = vendas_matriz[:, 2]
print(f"4.5: {coluna_mes_3}")
print('---')

# 4.6 Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) 
# no mês 2 (coluna 1).
valor_especifico = vendas_matriz[2, 1]
print(f"4.6: {valor_especifico}")
print('---')

# 4.7 Dada a matriz de preços ..., crie uma nova matriz com todos os preços aumentados em 5%.
matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]])
precos_aumentados = matriz_precos * 1.05
print(f"4.7:\n{precos_aumentados}")
print('---')

# 4.8 Dadas as matrizes de vendas ..., some-as para criar uma matriz vendas_globais.
vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]])
vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]])
vendas_globais = vendas_eua + vendas_europa
print(f"4.8: Vendas Globais\n{vendas_globais}")
print('---')

# 4.9 Dada a matriz de vendas ... e o vetor de preços ..., calcule a receita total 
# por mês usando o produto escalar (np.dot).
vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) # (3 produtos x 2 meses)
precos = np.array([4.99, 5.25, 2.19]) # (3 produtos)
receita_mes = np.dot(precos, vendas_unidades)
print(f"4.9: {receita_mes}")
print('---')

# 4.10 Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas 
# em cada mês (soma ao longo do eixo 0).
total_unidades_mes = np.sum(vendas_matriz, axis=0)
print(f"4.10: {total_unidades_mes}")
print('---')

# 4.11 Usando a mesma matriz de vendas, calcule a média de vendas para cada produto 
# (média ao longo do eixo 1).
media_vendas_produto = np.mean(vendas_matriz, axis=1)
print(f"4.11: {media_vendas_produto}")
print('---')

# 4.12 A partir da matriz de vendas, encontre e imprima o valor máximo.
valor_maximo = np.max(vendas_matriz)
print(f"4.12: {valor_maximo}")

print("===========================================================================")
print("\t\t\tParte 5: Desafios Finais")
print("===========================================================================\n")

# Desafio 1: Crie uma lista chamada usuarios contendo um dicionário para um usuário. 
# Este dicionário deve ter: a chave 'id_usuario' com valor 101; a chave 'perfil' com um 
# dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'}; a chave 
# 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' com 
# uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função 
# registrar_login(usuario) que incremente o contador no mapa de calor do usuário 
# correspondente ao dia e hora atuais.
print("Desafio 1: Mapa de Calor de Logins\n")
usuarios = [
    {
        'id_usuario': 101,
        'perfil': {'nome': 'Ana Silva', 'email': 'ana.s@email.com'},
        'permissoes': ('leitura', 'escrita'),
        'mapa_calor_logins': np.zeros((7, 24), dtype=int)
    }
]

def registrar_login(usuario):
    """Incrementa o contador no mapa de calor para o dia da semana e hora atuais."""
    agora = datetime.datetime.now()
    dia_da_semana = agora.weekday()  # Segunda=0, Domingo=6
    hora = agora.hour
    usuario['mapa_calor_logins'][dia_da_semana, hora] += 1
    print(f"Login de {usuario['perfil']['nome']} registrado para o dia {dia_da_semana} às {hora}h.")

# Testando a função de login
registrar_login(usuarios[0])
print("Mapa de calor do usuário:\n")
print(usuarios[0]['mapa_calor_logins'])
print("---")

# Desafio 2: Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. 
# A função deve retornar uma tupla contendo: 1. valor total do inventário (soma de preco * estoque), 
# 2. O nome do produto mais caro, e 3. Uma lista de produtos sem estoque.
# Teste a função com o catálogo: {'Laptop Gamer':..., 'Mouse Vertical':..., 'Monitor 4k':..., 'Webcam HD':...}.
# (Nota: O catálogo do PDF foi corrigido para ser um dicionário válido)
print("\nDesafio 2: Análise de Inventário\n")
catalogo_desafio = {
    'Laptop Gamer': {'preco': 7500.00, 'estoque': 10},
    'Mouse Vertical': {'preco': 350.00, 'estoque': 50},
    'Monitor 4k': {'preco': 4200.00, 'estoque': 15},
    'Webcam HD': {'preco': 250.00, 'estoque': 0}
}

def analisar_inventario(catalogo):
    valor_total = 0
    produto_mais_caro = None
    preco_maximo = -1
    sem_estoque = []

    for produto, dados in catalogo.items():
        valor_total += dados['preco'] * dados['estoque']
        if dados['preco'] > preco_maximo:
            preco_maximo = dados['preco']
            produto_mais_caro = produto
        if dados['estoque'] == 0:
            sem_estoque.append(produto)
    
    return (valor_total, produto_mais_caro, sem_estoque)

# Testando a função de análise de inventário
resultado_analise = analisar_inventario(catalogo_desafio)
print(f"Valor total do inventário: R${resultado_analise[0]:.2f}")
print(f"Produto mais caro: {resultado_analise[1]}")
print(f"Produtos sem estoque: {resultado_analise[2]}")
print("---")

# Desafio 3: Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar 
# um dicionário self.conexoes. Implemente os métodos adicionar_amizade(id1, id2) para criar uma 
# amizade mútua e obter_amigos(id_usuario) para retornar a lista de amigos. Instancie a classe 
# e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). Teste o método 
# obter_amigos para os usuários 101, 205 e 999.
print("\nDesafio 3: Grafo Social\n")
class SocialGraph:
    def __init__(self):
        self.conexoes = {}

    def adicionar_amizade(self, id1, id2):
        self.conexoes.setdefault(id1, []).append(id2)
        self.conexoes.setdefault(id2, []).append(id1)

    def obter_amigos(self, id_usuario):
        return self.conexoes.get(id_usuario, [])

# Testando a classe SocialGraph
grafo = SocialGraph()
grafo.adicionar_amizade(101, 205)
grafo.adicionar_amizade(101, 308)
grafo.adicionar_amizade(205, 400)

print(f"Amigos de 101: {grafo.obter_amigos(101)}")
print(f"Amigos de 205: {grafo.obter_amigos(205)}")
print(f"Amigos de 999: {grafo.obter_amigos(999)}")