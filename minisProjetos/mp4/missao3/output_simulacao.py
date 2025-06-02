# Propósito do arquivo:
# Este módulo é o principal da Missão 3. Ele é responsável por formatar e exibir
# o estado da simulação a cada mês, incluindo os dados de cada investimento
# e o resumo do período. Ele utiliza o `gerador_barra` da Missão 4 para a parte visual.

import time 
from constantes_base import constants 
from missao4 import gerador_barra   

def exibir_estado_simulacao(lista_de_investimentos, indice_do_mes_atual, ano_corrente_simulacao):
    """
    Imprime o status atual de todos os investimentos e o resumo do mês/ano.
    Args:
        lista_de_investimentos (list): Lista dos objetos Investimento.
        indice_do_mes_atual (int): Índice do mês (0-11).
        ano_corrente_simulacao (int): O ano atual da simulação.
    """
    print(f"\n\t\t{constants.CIANO}[SIMULAÇÃO]{constants.RESET}\n")
    
    for i, cada_investimento in enumerate(lista_de_investimentos):
        linha_de_texto_investimento = (
            f"{cada_investimento.get_tipo_str()}"
            f"[LCI de {cada_investimento.percentual:.2f}% do CDI a "
            f"{constants.VERDE}R${cada_investimento.total_investido:.2f}{constants.RESET}, rende {constants.VERDE}R${cada_investimento.resgate:.2f}{constants.RESET}]"
        )
        
        string_visual_barra = gerador_barra.gerar_string_barra(cada_investimento, lista_de_investimentos)
        
        print(f"{linha_de_texto_investimento}\t{string_visual_barra}")
        if len(lista_de_investimentos) > 1 and i < len(lista_de_investimentos) -1: 
             time.sleep(0.15) 

    print(f"\nResumo da simulação em {constants.ROXO}{constants.MESES_NOMES[indice_do_mes_atual]} de {ano_corrente_simulacao}{constants.RESET}")