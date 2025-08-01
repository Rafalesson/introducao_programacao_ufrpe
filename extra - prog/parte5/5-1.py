'''Crie uma lista chamada usuarios contendo um dicionário para um usuário. Este dicionário deve ter: 
a chave 'id_usuario' com valor 101; a chave 'perfil' com um dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'};
a chave 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' 
com uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função registrar_login(usuario) 
que incremente o contador no mapa de calor do usuário 
'''

import numpy as np
usuarios = [
    {
        'id_usuario': 101,
        'perfil': {
            'nome': 'Ana Silva',
            'email': 'ana.s@email.com'
        },
        'permissoes': ('leitura', 'escrita'),
        'mapa_calor_logins': np.zeros((7, 24))
    }
]

def registrar_login(usuario):
    usuario['mapa_calor_logins'][0, 0] += 1
    print(f"Login registrado para {usuario['perfil']['nome']}.")
    print(usuario['mapa_calor_logins'])
# Testando a função registrar_login
registrar_login(usuarios[0])