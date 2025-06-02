# Propósito do arquivo:
# Responsável pela interface do usuário inicial (boas-vindas) e pelo menu principal
# de ações do simulador. (Missão 1)

import time
from datetime import datetime   
from constantes_base import constants 
import os

data_hoje = datetime.now()
dia_mes_corrente = data_hoje.day
indice_mes_corrente = data_hoje.month - 1 
ano_corrente = data_hoje.year   

def limpar_console():
    """
    Limpa a tela do console.
    Usa 'cls' para Windows (nt) e 'clear' para Linux/macOS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def exibir_boas_vindas():
    print(f"\n\t{constants.AZUL}[SIMULADOR DE INVESTIMENTOS RECORRENTES]{constants.RESET}\n")
    time.sleep(0.5) 
    print("Bem vindo(a)! Vamos simular seus investimentos recorrentes.")
    time.sleep(0.5) 
    print(f"{constants.ITALICO}Neste simulação vamos usar somente LCIs, sem cálculo de IR.{constants.RESET}")
    time.sleep(0.5) 
    print("\nIniciando as simulações...")
    time.sleep(0.5) 
    
    # Informa ao usuário a data de início da simulação.
    print(f"Simulação iniciando em {constants.CIANO}{dia_mes_corrente} de {constants.MESES_NOMES[indice_mes_corrente]} de {ano_corrente}{constants.RESET}")
    time.sleep(0.5) 

def obter_acao_usuario():
    """
    Exibe o menu principal e captura a escolha do usuário.
    Retorna: str: Ação do usuário em letras minúsculas.
    """
        
    acao = input(
        f"\nDigite [{constants.VERDE}novo{constants.RESET}] para adicionar investimento, "
        f"[{constants.VERMELHO}sair{constants.RESET}] para encerrar, ou "
        f"pressione [{constants.AZUL}ENTER{constants.RESET}] para avançar um mês: "
    ).lower()
    return acao

def exibir_mensagem_opcao_invalida():
    print(f"\n{constants.VERMELHO}Opção inválida. Por favor, tente novamente.{constants.RESET}")
    time.sleep(0.5) 

def exibir_mensagem_saida():
    print(f"\n{constants.ROXO}Simulador encerrado. Até a próxima!{constants.RESET}")
    time.sleep(0.5)