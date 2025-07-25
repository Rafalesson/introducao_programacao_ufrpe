from collections import OrderedDict
from util.util import COLORS
from missao1.dados import GRUPOS_SOCIAIS

def _calcular_estatisticas_grupos(pessoas: list, categorias: list) -> OrderedDict:
    """Calcula os dados agregados dos grupos e retorna um dicionário com os resultados."""
    grupos = OrderedDict([(grupo, {'conforto': 0, 'salario': 0, 'patrimonio': 0, 'count': 0}) for grupo in GRUPOS_SOCIAIS])
    for p in pessoas:
        if p.grupo in grupos:
            grupos[p.grupo]['count'] += 1
            grupos[p.grupo]['conforto'] += p.conforto
            grupos[p.grupo]['salario'] += p.salario
            grupos[p.grupo]['patrimonio'] += p.patrimonio
    
    for dados in grupos.values():
        count = dados['count'] if dados['count'] > 0 else 1
        dados['conforto_medio'] = (dados['conforto'] / count) / len(categorias) if categorias else 0
        dados['salario_medio'] = dados['salario'] / count
        dados['patrimonio_medio'] = dados['patrimonio'] / count

    return grupos

def print_pessoas(pessoas: list, categorias: list):
    """Mostra os dados das pessoas em formato de tabela, com sua formatação."""
    print(f"{COLORS['yellow']}[PESSOAS]{COLORS['reset']}")
    divisao_renda = " | ".join(["Moradia 35.0%", "Alimentação 25.0%", "Transporte 10.0%", "Saúde 10.0%", "Educação 10.0%"])
    print(f"Divisão da renda mensal | {divisao_renda} | Totalizando 90.0% da renda mensal total.")
    print(f"\n{COLORS['yellow']}Exibindo média por grupo social{COLORS['reset']}")

    estatisticas = _calcular_estatisticas_grupos(pessoas, categorias)

    header = f"{'Grupo Social':<20} | {'Nº Pessoas':>10} | {'Conforto Médio':>15} | {'Salário Médio':>18} | {'Patrimônio Médio':>22}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for nome, dados in estatisticas.items():
        linha = (
            f"{nome:<20} | {dados['count']:>10} | "
            f"{COLORS['blue']}{dados['conforto_medio']:>15.1f}{COLORS['reset']} | "
            f"{COLORS['green']}{f'R$ {dados['salario_medio']:,.2f}':>18}{COLORS['reset']} | "
            f"{COLORS['purple']}{f'R$ {dados['patrimonio_medio']:,.2f}':>22}{COLORS['reset']}"
        )
        print(linha)
    
    print("-" * len(header) + "\n")

def print_empresas(empresas: list):
    """Mostra a tabela com o estado das empresas, com sua formatação e alinhamentos."""
    print(f"{COLORS['yellow']}[EMPRESAS]{COLORS['reset']}")

    header = f"{'Categoria':<12} | {'Empresa':<20} | {'Produto':<17} | {'Qualidade':<9} | {'Margem':<7} | {'Custo':<12} | {'Preço':<12} | {'Lucro Total':<15} | {'Vendas'}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for emp in sorted(empresas, key=lambda e: (e.categoria, e.custo)):
        vendas_str = (COLORS['cyan'] + '$' + COLORS['reset']) * (emp.vendas // 5)
        linha = (
            f"{emp.categoria:<12} | "
            f"{emp.nome:<20.20} | "
            f"{emp.produto:<17.17} | "
            f"{emp.qualidade:<9} | "
            f"{COLORS['yellow']}{emp.margem*100:<6.1f}%{COLORS['reset']} | "
            f"{COLORS['red']}{f'R$ {emp.custo:,.2f}':<12}{COLORS['reset']} | "
            f"{COLORS['blue']}{f'R$ {emp.preco_atual:,.2f}':<12}{COLORS['reset']} | "
            f"{COLORS['green']}{f'R$ {emp.lucro_total:,.2f}':<15}{COLORS['reset']} | "
            f"{vendas_str}"
        )
        print(linha)
    print("-" * len(header))