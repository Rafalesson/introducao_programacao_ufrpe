import datetime
import random
from simulador import io_handler, presentation, config
from simulador.agents import Pessoa, Empresa

def simular_um_mes(pessoas: list, empresas: list, categorias: dict, data_atual: datetime.date):
    for empresa in empresas: empresa.ajustar_para_proximo_mes(empresas, data_atual)
    for pessoa in pessoas: pessoa.simular_compras_do_mes(empresas, categorias)

def verificar_falencias(pessoas: list) -> list:
    return [p for p in pessoas if not (p.patrimonio < 0 and p.salario == 0)]

def reajustar_anualmente(pessoas: list):
    """Atualiza a inflação e reajusta salários com base no ciclo econômico atual."""
    
    # 1. GERENCIA O CICLO ECONÔMICO
    config.ANOS_NO_ESTADO_ATUAL += 1
    if config.ANOS_NO_ESTADO_ATUAL > config.DURACAO_DO_CICLO_ATUAL:
        # Sorteia um novo estado e uma nova duração para o ciclo
        config.ESTADO_ECONOMICO = random.choice(['Crescimento', 'Estagnação', 'Recessão'])
        config.DURACAO_DO_CICLO_ATUAL = random.randint(5, 15) # Um ciclo dura de 5 a 15 anos
        config.ANOS_NO_ESTADO_ATUAL = 0
        print(f"{presentation.COLORS['cyan']}[MUDANÇA DE CICLO] A economia entrou em um período de {config.ESTADO_ECONOMICO}.{presentation.COLORS['reset']}")

    # 2. DEFINE OS PARÂMETROS COM BASE NO ESTADO ATUAL
    if config.ESTADO_ECONOMICO == 'Crescimento':
        inflacao_base = 0.03 # 3%
        variacao_inflacao = random.uniform(0, 0.04) # Flutua para cima, até 7%
        ganho_real_range = (0.005, 0.02) # Ganho real de 0.5% a 2%
    elif config.ESTADO_ECONOMICO == 'Estagnação':
        inflacao_base = 0.01 # 1%
        variacao_inflacao = random.uniform(0, 0.03) # Flutua para cima, até 4%
        ganho_real_range = (-0.005, 0.005) # Ganho real quase nulo
    else: # Recessão
        inflacao_base = 0.04 # 4%
        variacao_inflacao = random.uniform(0, 0.06) # Pode ir até 10% (estagflação)
        ganho_real_range = (-0.03, -0.01) # Perda real de 1% a 3%

    # 3. ATUALIZA A INFLAÇÃO E SALÁRIOS
    config.INFLACAO_ANUAL = inflacao_base + variacao_inflacao
    config.SALARIO_MINIMO *= (1 + config.INFLACAO_ANUAL)
    
    for pessoa in pessoas:
        fator_ganho_real = random.uniform(ganho_real_range[0], ganho_real_range[1])
        fator_reajuste = 1 + config.INFLACAO_ANUAL + fator_ganho_real
        pessoa.salario *= fator_reajuste
    
    inflacao_anunciada = f"Inflação para o ano: {config.INFLACAO_ANUAL * 100:.2f}%."
    salario_anunciado = f"Salário Mínimo: R$ {config.SALARIO_MINIMO:,.2f}."
    print(f"{presentation.COLORS['yellow']}[ECONOMIA] {inflacao_anunciada} {salario_anunciado}{presentation.COLORS['reset']}")

def main():
    pessoas = io_handler.ler_pessoas(); empresas = io_handler.ler_empresas(); categorias = io_handler.ler_categorias()
    data_simulacao = datetime.date(2025, 1, 1)
    reajuste_anual_feito = {}

    while True:
        presentation.clear()
        presentation.print_variaveis_economicas()
        presentation.print_grupos_sociais(pessoas, categorias)
        presentation.print_empresas(empresas)

        mes_atual_str = presentation.MESES_DO_ANO[data_simulacao.month - 1]
        ano_atual = data_simulacao.year
        print("\n" + "=" * 32); print(f"Data da Simulação: {presentation.COLORS['cyan']}{mes_atual_str} de {ano_atual}{presentation.COLORS['reset']}"); print("=" * 32)

        prompt = f"\nDigite um número para avançar N meses, 'enter' para 1 mês ou 'sair': "
        resposta = input(prompt)
        if resposta.lower() == "sair": break
        
        meses_a_avancar = 1 if resposta == "" else int(resposta) if resposta.isdigit() else 0
        if meses_a_avancar > 0:
            for i in range(meses_a_avancar):
                mes_atual_loop = data_simulacao.month + i
                ano_atual_loop = data_simulacao.year + (mes_atual_loop - 1) // 12
                mes_final_loop = ((mes_atual_loop - 1) % 12) + 1
                data_iter = data_simulacao.replace(year=ano_atual_loop, month=mes_final_loop)
                
                if data_iter.month == 1 and not reajuste_anual_feito.get(data_iter.year, False):
                    reajustar_anualmente(pessoas)
                    reajuste_anual_feito[data_iter.year] = True
                
                pessoas_antes = pessoas
                simular_um_mes(pessoas, empresas, categorias, data_iter)
                pessoas = verificar_falencias(pessoas)
                nomes_falidos = {p.nome for p in pessoas_antes} - {p.nome for p in pessoas}
                for nome in nomes_falidos: print(f"{presentation.COLORS['red']}[FALÊNCIA] {nome} foi removido(a) da simulação.{presentation.COLORS['reset']}")

            mes_atual = data_simulacao.month; ano_atual = data_simulacao.year; mes_final = mes_atual + meses_a_avancar
            ano_final = ano_atual + (mes_final - 1) // 12; mes_final = ((mes_final - 1) % 12) + 1
            data_simulacao = data_simulacao.replace(year=ano_final, month=mes_final)

    print(f"\n{presentation.COLORS['yellow']}Simulação encerrada!{presentation.COLORS['reset']}")

if __name__ == "__main__":
    main()