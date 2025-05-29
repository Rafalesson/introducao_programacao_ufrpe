# Importa a função de cada arquivo de missão
from missao1.missao1 import missao_1
from missao2.missao2 import missao_2
from missao3.missao3 import missao_3
import sys
import os

# Adiciona o diretório raiz ao caminho de busca de módulos do Python
# para garantir que as importações entre as pastas funcionem corretamente.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def executar_simulador():
    """
    Função principal que executa todas as missões em sequência.
    """
    # Missão 1: Coleta os dados iniciais
    valor_inicial, tipo_investimento = missao_1()
    
    # Missão 2: Calcula o rendimento com base nos dados da missão 1
    valor_invest, meses, valor_final = missao_2(valor_inicial, tipo_investimento)
    
    # Missão 3: Mostra as análises finais com base nos resultados da missão 2
    missao_3(valor_invest, meses, valor_final)

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    executar_simulador()