# 2.1
'''Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', 
a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.
'''
usuario = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}

# 2.3
'''Crie um dicionário vazio chamado preferencias_usuario.
'''
preferencias_usuario = {}

# 2.5
'''Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com',
'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.
'''
usuario['telefone'] = '98765-4321'

# 2.6
''' Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get()
para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe,
forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login,
então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.
'''
ultimo_login = usuario.get('ultimo_login', 'Nunca logou')
usuario['ultimo_login'] = '2024-05-22'

# 2.7
'''Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com',
'telefone_fixo': '98765-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.
'''
del usuario['telefone_fixo']

# 2.9
'''Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop().
Forneça o valor padrão 'Email não encontrado.' para evitar um erro.
'''
email = usuario.pop('email', 'Email não encontrado.')

# 2.12
'''Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'.
O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123',
'cidade': 'São Paulo' e 'cep': '01000-000'.
'''
usuario['endereco'] = {
    'rua': 'Rua das Flores, 123',
    'cidade': 'São Paulo',
    'cep': '01000-000'
}

# 2.13 
'''Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'.
O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora',
'empresa': 'Tech Solutions'.
'''
usuario['profissao'] = {
    'cargo': 'Desenvolvedora',
    'empresa': 'Tech Solutions'
}

# 2.14
'''A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas
o valor associado à chave 'cidade'.
'''
print(usuario['endereco']['cidade'])

# 2.15
'''Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.
'''
usuario['endereco']['rua'] = 'Avenida Principal, 456'
