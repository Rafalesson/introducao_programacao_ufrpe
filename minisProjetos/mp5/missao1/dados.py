from missao2.classes import Pessoa, Empresa

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

_GRUPOS_A_CRIAR = [
    {"nome": GRUPOS_SOCIAIS[0], "n": 5, "pat": 20000000, "sal": 0, "var": 0},
    {"nome": GRUPOS_SOCIAIS[1], "n": 10, "pat": 200000, "sal": 100000, "var": -5000},
    {"nome": GRUPOS_SOCIAIS[2], "n": 25, "pat": 100000, "sal": 30000, "var": -1000},
    {"nome": GRUPOS_SOCIAIS[3], "n": 50, "pat": 10000, "sal": 5000, "var": -50},
    {"nome": GRUPOS_SOCIAIS[4], "n": 70, "pat": 10000, "sal": 1518, "var": 0},
]

def inicializar_dados():
    """Prepara e retorna todas as listas de entidades e configurações para a simulação."""
    def add_pessoas(grupo, num, patrimonio, salario, variacao=0.0):
        for i in range(num):
            pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao, grupo))

    pessoas = []
    for grupo_info in _GRUPOS_A_CRIAR:
        add_pessoas(grupo_info["nome"], grupo_info["n"], grupo_info["pat"], grupo_info["sal"], variacao=grupo_info["var"])

    empresas = [Empresa(*dados) for dados in _DADOS_EMPRESAS]
    categorias = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação"]
    percentuais = [0.35, 0.25, 0.10, 0.10, 0.10]
    
    return pessoas, empresas, categorias, percentuais