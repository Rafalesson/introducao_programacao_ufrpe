'''Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar um dicionário self.conexoes. 
Implemente os métodos adicionar_amizade(id1, id2) para criar uma amizade mútua e obter_amigos(id_usuario) para 
retornar a lista de amigos. Instancie a classe e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). 
Teste o método obter_amigos para os usuários 101, 205 e 999.
'''
class SocialGraph:
    def __init__(self):
        self.conexoes = {}

    def adicionar_amizade(self, id1, id2):
        if id1 not in self.conexoes:
            self.conexoes[id1] = set()
        if id2 not in self.conexoes:
            self.conexoes[id2] = set()
        self.conexoes[id1].add(id2)
        self.conexoes[id2].add(id1)

    def obter_amigos(self, id_usuario):
        return list(self.conexoes.get(id_usuario, []))
# Instanciando a classe e adicionando amizades
social_graph = SocialGraph()
social_graph.adicionar_amizade(101, 205)
social_graph.adicionar_amizade(101, 308)
social_graph.adicionar_amizade(205, 400)
# Testando o método obter_amigos
print(social_graph.obter_amigos(101))
print(social_graph.obter_amigos(205))
print(social_graph.obter_amigos(999)) 