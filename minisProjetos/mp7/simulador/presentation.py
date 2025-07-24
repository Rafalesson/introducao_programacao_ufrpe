import os
from collections import OrderedDict
from simulador import config

MESES_DO_ANO = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
COLORS = {"blue": "\033[94m", "green": "\033[92m", "purple": "\033[95m", "yellow": "\033[93m",
          "cyan": "\033[96m", "red": "\033[91m", "reset": "\033[0m", "grey": "\033[90m", "strikethrough": "\033[9m"}


def clear(): os.system('cls' if os.name == 'nt' else 'clear')


def print_variaveis_economicas():
    print(f"\n\n\n{COLORS['yellow']}[CENÁRIO ECONÔMICO]{COLORS['reset']}")
    inflacao_str = f"Inflação Anual: {config.INFLACAO_ANUAL * 100:.2f}%"
    salario_min_str = f"Salário Mínimo: R$ {config.SALARIO_MINIMO:,.2f}"
    # EXIBE O ESTADO ECONÔMICO ATUAL
    estado_str = f"Ciclo Econômico: {config.ESTADO_ECONOMICO}"

    print("-" * (len(inflacao_str) + len(salario_min_str) + len(estado_str) + 13))
    print(f"{inflacao_str:<25} | {salario_min_str:<30} | {estado_str}")
    print("-" * (len(inflacao_str) + len(salario_min_str) +
          len(estado_str) + 13) + "\n")


def print_grupos_sociais(pessoas: list, categorias: dict):
    print(f"{COLORS['yellow']}[GRUPOS SOCIAIS]{COLORS['reset']}")
    headers = ['Grupos', 'Qtd Pessoas', 'Salário Médio',
               'Patrimônio Médio', 'Conforto Médio']
    grupos_definidos = ["Classe A", "Classe B1", "Classe B2",
                        "Classe C1", "Classe C2", "Classe D", "Classe E"]
    stats = OrderedDict((grupo, {'salario': 0, 'patrimonio': 0,
                        'conforto': 0, 'count': 0}) for grupo in grupos_definidos)
    for p in pessoas:
        try:
            grupo_pessoa = p.nome.split(" #")[0]
            if grupo_pessoa in stats:
                stats[grupo_pessoa]['count'] += 1
                stats[grupo_pessoa]['salario'] += p.salario
                stats[grupo_pessoa]['patrimonio'] += p.patrimonio
                stats[grupo_pessoa]['conforto'] += p.conforto
        except IndexError:
            continue
    rows_data = []
    for nome, dados in stats.items():
        if dados['count'] > 0:
            rows_data.append([nome, str(dados['count']), f"R$ {dados['salario']/dados['count']:,.2f}",
                             f"R$ {dados['patrimonio']/dados['count']:,.2f}", f"{(dados['conforto']/dados['count'])/len(categorias) if categorias else 0:.1f}"])
    col_widths = [len(h) for h in headers]
    for row in rows_data:
        for i, cell in enumerate(row):
            if len(cell) > col_widths[i]:
                col_widths[i] = len(cell)
    header_line = " | ".join(
        [f"{h:<{col_widths[i]}}" for i, h in enumerate(headers)])
    separator_line = "-" * len(header_line)
    print(separator_line)
    print(header_line)
    print(separator_line)
    for row in rows_data:
        row_colored = [f"{row[0]:<{col_widths[0]}}", f"{row[1]:<{col_widths[1]}}", f"{COLORS['green']}{row[2]:<{col_widths[2]}}{COLORS['reset']}",
                       f"{COLORS['purple']}{row[3]:<{col_widths[3]}}{COLORS['reset']}", f"{COLORS['blue']}{row[4]:<{col_widths[4]}}{COLORS['reset']}"]
        print(" | ".join(row_colored))
    print(separator_line + "\n")


def print_empresas(empresas: list):
    print(f"{COLORS['yellow']}[EMPRESAS]{COLORS['reset']}")
    headers = ['Categoria', 'Empresa', 'Produto', 'Qualidade',
               'Margem', 'Custo', 'Preço', 'Lucro Total', 'Vendas']
    empresas_ativas = [e for e in empresas if not e.falida]
    col_widths = [len(h) for h in headers]
    for emp in empresas_ativas:
        row_str_data = [emp.categoria, emp.nome, emp.produto, str(
            emp.qualidade), f"{emp.margem*100:.1f} %", f"R$ {emp.custo:,.2f}", f"R$ {emp.preco_atual:,.2f}", f"R$ {emp.lucro_total:,.2f}", str(emp.vendas)]
        for i, cell in enumerate(row_str_data):
            if len(cell) > col_widths[i]:
                col_widths[i] = len(cell)
    header_line = " | ".join(
        [f"{h:<{col_widths[i]}}" for i, h in enumerate(headers)])
    separator_line = "-" * len(header_line)
    print(separator_line)
    print(header_line)
    print(separator_line)
    for emp in sorted(empresas, key=lambda e: (e.falida, e.categoria, e.custo)):
        if emp.falida:
            parte1 = f"{COLORS['strikethrough']}{COLORS['grey']}{emp.categoria:<{col_widths[0]}}{COLORS['reset']}"
            parte2 = f"{COLORS['strikethrough']}{COLORS['grey']}{emp.nome:<{col_widths[1]}}{COLORS['reset']}"
            parte3 = f"{COLORS['strikethrough']}{COLORS['grey']}{emp.produto:<{col_widths[2]}}{COLORS['reset']}"
            parte4 = f"{COLORS['strikethrough']}{COLORS['grey']}{str(emp.qualidade):<{col_widths[3]}}{COLORS['reset']}"
            mes_falencia = MESES_DO_ANO[emp.data_falencia.month - 1]
            ano_falencia = emp.data_falencia.year
            msg_falencia = f"Falência em: {mes_falencia} de {ano_falencia}"
            largura_restante = sum(col_widths[4:]) + (len(headers) - 5) * 3
            msg_formatada = f"{msg_falencia:^{largura_restante}}"
            print(
                f"{parte1} | {parte2} | {parte3} | {parte4} | {COLORS['grey']}{msg_formatada}{COLORS['reset']}")
        else:
            linha_formatada = " | ".join([f"{emp.categoria:<{col_widths[0]}}", f"{emp.nome:<{col_widths[1]}}", f"{emp.produto:<{col_widths[2]}}", f"{str(emp.qualidade):<{col_widths[3]}}", f"{COLORS['yellow']}{f'{emp.margem*100:.1f} %':<{col_widths[4]}}{COLORS['reset']}", f"{COLORS['red']}{f'R$ {emp.custo:,.2f}':<{
                                         col_widths[5]}}{COLORS['reset']}", f"{COLORS['blue']}{f'R$ {emp.preco_atual:,.2f}':<{col_widths[6]}}{COLORS['reset']}", f"{COLORS['green']}{f'R$ {emp.lucro_total:,.2f}':<{col_widths[7]}}{COLORS['reset']}", f"{COLORS['cyan']}{str(emp.vendas):<{col_widths[8]}}{COLORS['reset']}", ])
            print(linha_formatada)
    print(separator_line)
