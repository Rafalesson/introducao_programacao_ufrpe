# Propósito do arquivo:
# Este arquivo centraliza todas as constantes usadas em diferentes partes da aplicação,
# facilitando a manutenção e a configuração de parâmetros globais.

# Códigos ANSI para formatação de texto no console (cores e estilos).
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AZUL = '\033[34m'
AMARELO = '\033[33m'
ROXO = '\033[35m'
CIANO = '\033[36m'
BRANCO = '\033[37m' 
ITALICO = '\033[3m'
RESET = '\033[0m' # Resetar formatação para o padrão do console

# TAXA CDI BASE MENSAL (PARA 100% DO CDI) - ASSUMIDA PARA ESTA SIMULAÇÃO
# --------------------------------------------------------------------------
# Este valor (0.01145, ou 1.145% ao mês) é a premissa fundamental para o cálculo
# dos rendimentos no simulador, quando o usuário não informa uma taxa CDI base.
# Derivado do primeiro exemplo do PDF (página 20): R$200 rendendo para R$202,29.
TAXA_CDI_BASE_MENSAL_SIMULACAO = 0.01145

# Número máximo de caracteres para a barra de cifrões no modo escalonado.
MAX_BAR_CHARACTERS = 40

MESES_NOMES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
               "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]