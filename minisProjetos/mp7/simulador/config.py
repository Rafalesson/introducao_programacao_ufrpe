# simulador/config.py

# --- Parâmetros Macroeconômicos da Simulação ---

# A inflação anual para o ano corrente da simulação.
# Este valor é inicializado com 4% e flutua a cada ano no main.py.
INFLACAO_ANUAL = 0.04

# O salário mínimo inicial da simulação.
# Ele serve como piso para a geração de pessoas e é reajustado anualmente pela inflação.
SALARIO_MINIMO = 1550.00