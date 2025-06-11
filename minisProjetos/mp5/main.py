import datetime
from missao1.dados import inicializar_dados
from missao2.simulador import simular_mercado
from missao3.resultados import print_pessoas, print_empresas
from util.util import clear, COLORS

MESES_DO_ANO = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

def main():
    """
    Função principal que inicializa e executa o loop da simulação de mercado,
    orquestrando os módulos de dados, simulação e exibição.
    """
    # 1. PREPARAÇÃO: Carrega os dados e inicializa a data da simulação.
    pessoas, empresas, categorias, percentuais = inicializar_dados()
    data_simulacao = datetime.date.today()

    while True:
        clear()
        print(f"\n\t\t{COLORS['blue']}[SIMULADOR DE RELAÇÕES DE MERCADO]{COLORS['reset']}\n")
        print_pessoas(pessoas, categorias)
        print_empresas(empresas)

        # Formata e exibe a data atual da simulação.
        mes_atual_str = MESES_DO_ANO[data_simulacao.month - 1]
        ano_atual = data_simulacao.year
        print("=" * 32)
        print(f"Data da Simulação: {COLORS['cyan']}{mes_atual_str} de {ano_atual}{COLORS['reset']}")
        print("=" * 32)

        prompt = (
            f"\nDigite um número para avançar N meses, "
            f"{COLORS['green']}'enter'{COLORS['reset']} para avançar 1 mês ou "
            f"{COLORS['red']}'sair'{COLORS['reset']} para encerrar: "
        )
        resposta = input(prompt)

        if resposta.lower() == "sair":
            break
        
        meses_a_avancar = 0
        if resposta.isdigit():
            meses_a_avancar = int(resposta)
        elif resposta == "":
            meses_a_avancar = 1

        if meses_a_avancar > 0:
            for _ in range(meses_a_avancar):
                simular_mercado(pessoas, empresas, categorias, percentuais)
            
            mes_atual = data_simulacao.month
            ano_atual = data_simulacao.year

            mes_final = mes_atual + meses_a_avancar
            ano_final = ano_atual + (mes_final - 1) // 12
            mes_final = ((mes_final - 1) % 12) + 1
            
            data_simulacao = data_simulacao.replace(year=ano_final, month=mes_final)

    print(f"\n{COLORS['yellow']}Simulação encerrada!{COLORS['reset']}")

if __name__ == "__main__":
    main()