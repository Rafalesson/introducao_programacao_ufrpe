# scripts/gerar_populacao.py

import csv
import random
import sys
import os

# Permite que o script importe o módulo 'config' da pasta 'simulador'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulador import config

# Blueprint da população, definindo a quantidade e os parâmetros de cada classe
GRUPOS_SOCIAIS = [
    {"nome": "Classe A", "quantidade": 30, "salario": (35000, 15000), "patrimonio": (2500000, 800000)},
    {"nome": "Classe B1", "quantidade": 70, "salario": (15000, 5000), "patrimonio": (500000, 150000)},
    {"nome": "Classe B2", "quantidade": 130, "salario": (7500, 2000), "patrimonio": (150000, 50000)},
    {"nome": "Classe C1", "quantidade": 250, "salario": (4000, 1000), "patrimonio": (40000, 12000)},
    {"nome": "Classe C2", "quantidade": 250, "salario": (2500, 500), "patrimonio": (10000, 3000)},
    {"nome": "Classe D", "quantidade": 170, "salario": (1800, 400), "patrimonio": (5000, 1500)},
    {"nome": "Classe E", "quantidade": 100, "salario": (1500, 250), "patrimonio": (1500, 500)},
]

def gerar_populacao():
    """Gera a lista de pessoas para o arquivo de dados."""
    populacao = [['nome', 'patrimonio', 'salario']]
    for grupo in GRUPOS_SOCIAIS:
        for i in range(grupo["quantidade"]):
            salario_medio, salario_desvio = grupo["salario"]
            salario = random.normalvariate(salario_medio, salario_desvio)
            salario = max(config.SALARIO_MINIMO, salario) # Usa o salário mínimo como piso

            patrimonio_medio, patrimonio_desvio = grupo["patrimonio"]
            patrimonio = max(0, random.normalvariate(patrimonio_medio, patrimonio_desvio)) # Evita patrimônio negativo inicial
            
            nome_pessoa = f"{grupo['nome']} #{i+1}"
            populacao.append([nome_pessoa, f"{patrimonio:.2f}", f"{salario:.2f}"])
    return populacao

if __name__ == "__main__":
    # Função principal que executa a geração e salva o arquivo.
    dados_populacao = gerar_populacao()
    caminho_saida = 'data/pessoas.txt'
    with open(caminho_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dados_populacao)
    print(f"Arquivo '{caminho_saida}' com {len(dados_populacao) - 1} pessoas foi gerado com sucesso!")