# simulador/config.py

# --- Parâmetros Macroeconômicos da Simulação ---

# A inflação anual para o ano corrente da simulação.
INFLACAO_ANUAL = 0.04

# O salário mínimo inicial da simulação.
SALARIO_MINIMO = 1550.00

# --- Controle de Ciclos Econômicos ---
# O estado pode ser 'Crescimento', 'Estagnação' ou 'Recessão'.
ESTADO_ECONOMICO = 'Crescimento'
# Contador de anos dentro do ciclo atual.
ANOS_NO_ESTADO_ATUAL = 0
# Duração do ciclo atual em anos (será sorteado a cada novo ciclo).
DURACAO_DO_CICLO_ATUAL = 10