import datetime
from missao1.dados import inicializar_dados
from missao3.resultados import print_pessoas, print_empresas
from util.util import clear, COLORS

MESES_DO_ANO = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

def main():
    """Função principal que orquestra a simulação."""
    pessoas, empresas, categorias, percentuais = inicializar_dados()
    data_simulacao = datetime.date.today()

    while True:
        clear()
        print(f"{COLORS['yellow']}[SIMULADOR DE RELAÇÕES DE MERCADO]{COLORS['reset']}\n")
        print_pessoas(pessoas, categorias)
        print_empresas(empresas)

        mes_atual_str = MESES_DO_ANO[data_simulacao.month - 1]
        ano_atual = data_simulacao.year
        print("\n" + "=" * 32)
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
        
        meses_a_avancar = 1 if resposta == "" else int(resposta) if resposta.isdigit() else 0

        if meses_a_avancar > 0:
            for _ in range(meses_a_avancar):
                for empresa in empresas:
                    empresa.ajustar_para_proximo_mes()
                for pessoa in pessoas:
                    pessoa.simular_compras_do_mes(empresas, categorias, percentuais)
            
            mes_atual = data_simulacao.month
            ano_atual = data_simulacao.year
            mes_final = mes_atual + meses_a_avancar
            ano_final = ano_atual + (mes_final - 1) // 12
            mes_final = ((mes_final - 1) % 12) + 1
            data_simulacao = data_simulacao.replace(year=ano_final, month=mes_final)

    print(f"\n{COLORS['yellow']}Simulação encerrada!{COLORS['reset']}")

if __name__ == "__main__":
    main()