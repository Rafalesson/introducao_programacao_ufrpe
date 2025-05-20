# Função para imprimir com cor
def colored(text, color_code):
    resultado = f"\033[{color_code}m{text}\033[0m"
    return resultado
 
# Códigos de cores ANSI 
azul = 94
verde = 92
ciano = 96
vermelho = 91
magenta = 95
amarelo = 93
branco = 97
preto = 90