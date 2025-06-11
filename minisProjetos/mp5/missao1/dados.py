# Constante com os dados estáticos das empresas.
# O "_" no início indica que é para uso interno deste módulo.
_DADOS_EMPRESAS = [
    ("Moradia", "República A", "Aluguel, Várzea", 300.0, 3), ("Moradia", "República B", "Aluguel, Várzea", 300.0, 3),
    ("Moradia", "CTI Imobiliária", "Aluguel, Centro", 1500.0, 7), ("Moradia", "Orla Smart Live", "Aluguel, Boa V.", 3000.0, 9),
    ("Alimentação", "CEASA", "Feira do Mês", 200.0, 3), ("Alimentação", "Mix Matheus", "Feira do Mês", 900.0, 5),
    ("Alimentação", "Pão de Açúcar", "Feira do Mês", 1500.0, 7), ("Alimentação", "Home Chef", "Chef em Casa", 6000.0, 9),
    ("Transporte", "Grande Recife", "VEM Ônibus", 150.0, 3), ("Transporte", "UBER", "Uber Moto", 200.0, 4),
    ("Transporte", "99", "99 Moto", 200.0, 4), ("Transporte", "BYD", "BYD Dolphin", 3000.0, 8),
    ("Saúde", "Health Coop", "Plano de Saúde", 200.0, 2), ("Saúde", "HapVida", "Plano de Saúde", 650.0, 5),
    ("Saúde", "Bradesco Saúde", "Plano de Saúde", 800.0, 5), ("Saúde", "Sulamérica", "Plano de Saúde", 850.0, 5),
    ("Educação", "Escolinha", "Mensalidade", 100.0, 1), ("Educação", "Mazzarello", "Mensalidade", 1200.0, 6),
    ("Educação", "Arco Íris", "Mensalidade", 1800.0, 8), ("Educação", "Escola do Porto", "Mensalidade", 5000.0, 9),
]

GRUPOS_SOCIAIS = ["Herdeiros", "Supersalários", "Faixa Média-Alta", "Faixa Baixa", "Salário Mínimo"]

class Pessoa:
    def __init__(self, patrimonio: float, salario: float, grupo: str):
        self.patrimonio = patrimonio
        self.salario = salario
        self.grupo = grupo
        self.conforto = 0.0
        self.compras_mes = {}

class Empresa:
    def __init__(self, categoria: str, nome: str, produto: str, custo: float, qualidade: int):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0
        self.lucro_total = 0.0

def inicializar_dados():
    """Prepara e retorna todas as listas de entidades e configurações para a simulação."""
    pessoas = []
    categorias = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação"]
    percentuais = [0.35, 0.25, 0.10, 0.10, 0.10]

    def add_pessoas(nome_grupo, num_pessoas, patrimonio, salario, variacao=0.0):
        for i in range(num_pessoas):
            pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao, nome_grupo))
    
    add_pessoas(GRUPOS_SOCIAIS[0], 5, patrimonio=20000000, salario=0)
    add_pessoas(GRUPOS_SOCIAIS[1], 10, patrimonio=200000, salario=100000, variacao=-5000)
    add_pessoas(GRUPOS_SOCIAIS[2], 25, patrimonio=100000, salario=30000, variacao=-1000)
    add_pessoas(GRUPOS_SOCIAIS[3], 50, patrimonio=10000, salario=5000, variacao=-50)
    add_pessoas(GRUPOS_SOCIAIS[4], 70, patrimonio=1000, salario=1518)

    empresas = [Empresa(*dados) for dados in _DADOS_EMPRESAS]

    return pessoas, empresas, categorias, percentuais