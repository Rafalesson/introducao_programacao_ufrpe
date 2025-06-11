import sys

def clear():
    """
    Limpa o console de forma completa e definitiva.
    Esta implementação combina três comandos ANSI para garantir que
    tanto a tela visível quanto o histórico de scroll sejam limpos.
    """
    # \033[2J : Limpa a tela inteira (o viewport visível).
    # \033[3J : Limpa o histórico de scroll (scrollback buffer).
    # \033[H  : Move o cursor para a posição inicial (topo, esquerda).
    sys.stdout.write("\033[2J\033[3J\033[H")
    sys.stdout.flush()

# Dicionário de cores para facilitar o uso no projeto
COLORS = {
    "blue": "\033[94m",    # Azul 
    "green": "\033[92m",   # Verde 
    "purple": "\033[95m",  # Magenta/Roxo 
    "yellow": "\033[93m",  # Amarelo 
    "cyan": "\033[96m",    # Ciano 
    "white": "\033[97m",   # Branco 
    "red": "\033[91m",     # Vermelho 
    "reset": "\033[0m"     # Reseta a cor para o padrão do terminal
}