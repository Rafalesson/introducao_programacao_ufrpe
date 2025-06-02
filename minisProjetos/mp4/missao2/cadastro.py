# Propósito do arquivo:
# Gerencia a interação com o usuário para cadastrar um novo investimento,
# solicitando os dados e validando-os.

import time
from .investimentos_defs import Investimento 
from constantes_base import constants  

def registrar_novo_investimento():
    """
    Conduz o diálogo de cadastro de um novo investimento com o usuário.
    Retorna: Investimento ou None.
    """
    print(f"\n\t{constants.CIANO}[Cadastro de Novo Investimento]{constants.RESET}")
    time.sleep(0.5) 
    try:
        percentual_str = input(f"\nDigite o percentual do {constants.AZUL}CDI{constants.RESET} para este investimento (%): ")
        while True:
            try:
                percentual = float(percentual_str)
                if percentual >= 0:
                    break
                else:
                    print(f"{constants.VERMELHO}O percentual não pode ser negativo. Tente novamente.{constants.RESET}")
            except ValueError:
                print(f"{constants.VERMELHO}Entrada inválida. Por favor, digite um número para o percentual (use '.' como separador decimal).{constants.RESET}")
            time.sleep(0.5) 
            percentual_str = input(f"\nDigite o percentual do {constants.AZUL}CDI{constants.RESET} para este investimento (%): ")
        time.sleep(0.5) 
        
        aporte_str = input(f"Digite o valor do aporte de entrada: {constants.VERDE}R$")
        while True:
            try:
                aporte = float(aporte_str)
                if aporte > 0:
                    break
                else:
                    print(f"{constants.VERMELHO}O valor do aporte deve ser positivo. Tente novamente.{constants.RESET}")
            except ValueError:
                print(f"{constants.VERMELHO}Entrada inválida. Por favor, digite um número para o aporte.{constants.RESET}")
            time.sleep(0.5) 
            aporte_str = input(f"Digite o valor do aporte de entrada: {constants.VERDE}R$")
        time.sleep(0.5) 

        recorrente_str = input(f"{constants.RESET}Este investimento terá depósitos mensais recorrentes no mesmo valor do aporte inicial? ({constants.VERDE}sim/s{constants.RESET}/{constants.VERMELHO}não/n{constants.RESET}) ").lower()
        while recorrente_str not in ['sim', 's', 'não', 'nao', 'n']: # Adicionado 's'
            print(f"{constants.VERMELHO}Resposta inválida. Por favor, digite 'sim/s' ou 'não/n'.{constants.RESET}")
            time.sleep(0.5) 
            recorrente_str = input(f"Depósitos mensais recorrentes? ({constants.VERDE}sim/s{constants.RESET}/{constants.VERMELHO}não/n{constants.RESET}) ").lower()
        
        # Normaliza 's', 'nao', 'n' para a lógica interna
        if recorrente_str == 'nao' or recorrente_str == 'n':
            eh_recorrente_param = 'não'
        elif recorrente_str == 's':
            eh_recorrente_param = 'sim'
        else: 
            eh_recorrente_param = recorrente_str 
            
        print(f"{constants.CIANO}------------------------------------{constants.RESET}")
        return Investimento(percentual, aporte, eh_recorrente_param)

    except Exception as e:
        print(f"{constants.VERMELHO}Ocorreu um erro inesperado durante o cadastro: {e}{constants.RESET}")
        time.sleep(0.5) 
        return None