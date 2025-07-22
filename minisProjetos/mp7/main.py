# main.py

import datetime
import random
from simulador import io_handler, presentation, config
from simulador.agents import Pessoa, Empresa

def simular_um_mes(pessoas: list, empresas: list, categorias: dict, data_atual: datetime.date):
    """Executa a lógica de um ciclo completo da simulação."""
    for empresa in empresas:
        empresa.ajustar_para_proximo_mes(empresas, data_atual)
    for pessoa in pessoas:
        pessoa.simular_compras_do_mes(empresas, categorias)

def verificar_falencias_pessoais(pessoas: list) -> list:
    """Retorna uma nova lista contendo apenas as pessoas que não faliram."""
    return [p for p in pessoas if not (p.patrimonio < 0 and p.salario == 0)]

def reajustar_anualmente(pessoas: list):
    """Atualiza a inflação e reajusta salários uma vez por ano."""
    # A inflação do ano flutua com base no ano anterior
    variacao_inflacao = random.uniform(-0.015, 0.015)
    config.INFLACAO_ANUAL += variacao_inflacao
    config.INFLACAO_ANUAL = max(0.015, min(config.INFLACAO_ANUAL, 0.12)) # Limites de 1.5% a 12%

    # Salário mínimo é corrigido pela nova inflação
    config.SALARIO_MINIMO *= (1 + config.INFLACAO_ANUAL)
    
    # Salários das pessoas são corrigidos (inflação + ganho/perda de produtividade)
    for pessoa in pessoas:
        fator_ganho_real = random.uniform(-0.01, 0.02)
        pessoa.salario *= (1 + config.INFLACAO_ANUAL + fator_ganho_real)
    
    # Anuncia o evento no console
    inflacao_anunciada = f"Inflação para o ano: {config.INFLACAO_ANUAL * 100:.2f}%."
    salario_anunciado = f"Salário Mínimo atualizado para R$ {config.SALARIO_MINIMO:,.2f}."
    print(f"{presentation.COLORS['yellow']}[ECONOMIA] {inflacao_anunciada} {salario_anunciado}{presentation.COLORS['reset']}")

def main():
    """Função principal que carrega os dados e gerencia o loop da simulação."""
    # Carregamento inicial
    pessoas = io_handler.ler_pessoas()
    empresas = io_handler.ler_empresas()
    categorias = io_handler.ler_categorias()
    data_simulacao = datetime.date(2025, 1, 1)
    reajuste_anual_feito = {}

    # Loop principal da simulação
    while True:
        # 1. Exibe o estado atual
        presentation.clear()
        presentation.print_variaveis_economicas()
        presentation.print_grupos_sociais(pessoas, categorias)
        presentation.print_empresas(empresas)
        
        mes_atual_str = presentation.MESES_DO_ANO[data_simulacao.month - 1]
        print("\n" + "=" * 32)
        print(f"Data da Simulação: {presentation.COLORS['cyan']}{mes_atual_str} de {data_simulacao.year}{presentation.COLORS['reset']}")
        print("=" * 32)

        # 2. Obtém o input do usuário
        prompt = f"\nDigite um número para avançar N meses, 'enter' para 1 mês ou 'sair': "
        resposta = input(prompt)
        if resposta.lower() == "sair": break
        
        # 3. Processa e executa os meses
        meses_a_avancar = 1 if resposta == "" else int(resposta) if resposta.isdigit() else 0
        if meses_a_avancar > 0:
            for i in range(meses_a_avancar):
                # Calcula a data correta para a iteração atual
                mes_atual_loop = data_simulacao.month + i
                ano_atual_loop = data_simulacao.year + (mes_atual_loop - 1) // 12
                mes_final_loop = ((mes_atual_loop - 1) % 12) + 1
                data_iter = data_simulacao.replace(year=ano_atual_loop, month=mes_final_loop)
                
                # Verifica se é hora do reajuste anual
                if data_iter.month == 1 and not reajuste_anual_feito.get(data_iter.year, False):
                    reajustar_anualmente(