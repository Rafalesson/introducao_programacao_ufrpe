import sys
import json
from pathlib import Path

# Adiciona a pasta raiz ao sys.path
sys.path.append(str(Path(__file__).parent.parent))

from classes import Data, Gastos, Financas, Pessoa
from base import colorir, verde, ciano, vermelho, amarelo

# Carrega os dados do arquivo JSON
try:
    with open("dados_usuario.json", "r") as f:
        dados = json.load(f)

    # Atribui os dados às variáveis
    nome = dados["nome"]
    dia = dados["dia"]
    mes = dados["mes"]
    ano = dados["ano"]
    patrimonio = dados["patrimonio"]
    salario = dados["salario"]
    aluguel = dados["aluguel"]
    feira = dados["feira"]
    comida = dados["comida"]
    transporte = dados["transporte"]
    outros = dados["outros"]
    investimento = dados["investimento"]

    # Criação dos objetos conforme Missão 2
    nascimento = Data(dia, mes, ano)
    gastos = Gastos(aluguel, feira, comida, transporte, outros)
    financas = Financas(patrimonio, salario, gastos, investimento)
    antonieta = Pessoa(nome, nascimento, financas)

    gastos_totais = (
        antonieta.financas.gastos.aluguel +
        antonieta.financas.gastos.feira +
        antonieta.financas.gastos.comida +
        antonieta.financas.gastos.transporte +
        antonieta.financas.gastos.outros
    )

    print(f"\nAgora organizei todos os seus dados de forma concentrada aqui no meu sistema. \nVou te mostrar como ficou:")
    print(f"\n{colorir(antonieta.nome, ciano)}, nascido(a) em {colorir(f"{antonieta.nasc.dia}/{antonieta.nasc.mes}/{antonieta.nasc.ano}", verde)}.")
    print(f"{colorir(antonieta.nome, ciano)} tem R$ {colorir(f"{antonieta.financas.patrimonio:.2f}", verde)} de {colorir("patrimônio", amarelo)}.")
    print(f"{colorir(antonieta.nome, ciano)} tem R$ {colorir(f"{antonieta.financas.salario:.2f}", verde)} de {colorir("salário", amarelo)}.")
    print(f"{colorir(antonieta.nome, ciano)} tem R$ {colorir(f"{gastos_totais:.2f}", vermelho)} de {colorir("gastos", amarelo)}.")
    print(f"{colorir(antonieta.nome, ciano)} tem R$ {colorir(f"{antonieta.financas.investimento:.2f}", verde)} de {colorir("investimento", amarelo)}.")

except FileNotFoundError:
    print(f"\n⚠️\tArquivo de dados não encontrado. Execute primeiro o {colorir('missao1.py', vermelho)} para gerar o arquivo.")