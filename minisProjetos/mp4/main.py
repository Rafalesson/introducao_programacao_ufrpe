# Propósito do arquivo:
# Ponto de entrada e orquestrador principal do Simulador de Investimentos.
# Gerencia o laço de interação com o usuário, o estado da simulação (lista de
# investimentos, data atual) e delega tarefas aos módulos específicos de cada "missão".

import time
from datetime import datetime

# Ajuste das importações para refletir a nova estrutura de pastas e nomes de arquivos
from missao1 import menu as ui_manager 
from missao2 import cadastro as cadastro_manager 
from missao3 import output_simulacao 
from constantes_base import constants

def main_loop():
    """
    Função principal que contém o laço de repetição (loop) da aplicação,
    controlando o fluxo da simulação e a interação com o usuário.
    """
    
    lista_de_investimentos_cadastrados = [] 
    
    data_hoje = datetime.now()
    indice_mes_corrente = data_hoje.month - 1 
    ano_corrente = data_hoje.year     

    ui_manager.limpar_console()
    ui_manager.exibir_boas_vindas()
    time.sleep(0.5)

    while True:
        acao_do_usuario = ui_manager.obter_acao_usuario()

        if acao_do_usuario == "novo":
            ui_manager.limpar_console()
            novo_investimento_criado = cadastro_manager.registrar_novo_investimento()
            
            if novo_investimento_criado:
                lista_de_investimentos_cadastrados.append(novo_investimento_criado)
                
                print(f"\n{constants.VERDE}Investimento adicionado com sucesso!{constants.RESET}")
                time.sleep(1.5)
                ui_manager.limpar_console()
                
        
        elif acao_do_usuario == "sair":
            ui_manager.exibir_mensagem_saida()
            break

        elif acao_do_usuario == "":
            ui_manager.limpar_console()
            
            if not lista_de_investimentos_cadastrados:
                print(f"\n{constants.AMARELO}Nenhum investimento cadastrado para simular.{constants.RESET} \n")
                
                proximo_mes_idx = indice_mes_corrente + 1
                proximo_ano = ano_corrente
                if proximo_mes_idx == 12:
                    proximo_mes_idx = 0
                    proximo_ano += 1
                
                indice_mes_corrente = proximo_mes_idx
                ano_corrente = proximo_ano
                
                print(f"Simulador avançou no tempo. \nPróximo período para avaliação: {constants.ROXO}{constants.MESES_NOMES[indice_mes_corrente]} de {ano_corrente}{constants.RESET}")
                time.sleep(0.5)
                continue

            for cada_investimento_obj in lista_de_investimentos_cadastrados: 
                cada_investimento_obj.avancar_mes() 
            
            output_simulacao.exibir_estado_simulacao(lista_de_investimentos_cadastrados, indice_mes_corrente, ano_corrente)
            
            indice_mes_corrente += 1
            if indice_mes_corrente == 12:
                indice_mes_corrente = 0
                ano_corrente += 1
        else:
            ui_manager.exibir_mensagem_opcao_invalida()

if __name__ == "__main__":
    main_loop()