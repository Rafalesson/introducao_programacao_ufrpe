# Propósito do arquivo:
# Contém toda a lógica para gerar a string da barra de cifrões ($$$$)
# incluindo o desafio do escalonamento para barras muito longas.

import math
from constantes_base import constants 

def gerar_string_barra(investimento_analisado, todos_os_investimentos):
    """
    Cria a string visual da barra de cifrões para um investimento.
    """
    string_barra_gerada = ""
    num_cifroes_para_exibir = 0
    
    if investimento_analisado.resgate < 1000:
        return "" 

    usar_barra_escalonada = False
    if todos_os_investimentos:
        if any(math.floor(inv.resgate / 1000) > constants.MAX_BAR_CHARACTERS 
               for inv in todos_os_investimentos if inv.resgate >= 1000):
            usar_barra_escalonada = True

    if usar_barra_escalonada:
        max_resgate_geral_na_simulacao = 0
        if todos_os_investimentos: 
            max_resgate_geral_na_simulacao = max(inv.resgate for inv in todos_os_investimentos)
        
        if max_resgate_geral_na_simulacao == 0: 
            max_resgate_geral_na_simulacao = 1.0 
        
        num_cifroes_para_exibir = int(math.floor(
            (investimento_analisado.resgate / max_resgate_geral_na_simulacao) * constants.MAX_BAR_CHARACTERS
        ))
    else:
        num_cifroes_para_exibir = int(math.floor(investimento_analisado.resgate / 1000))

    if num_cifroes_para_exibir > 0:
        string_barra_gerada = constants.AMARELO + '$' * num_cifroes_para_exibir + constants.RESET
    
    return string_barra_gerada