# simulador/io_handler.py

import csv
import json
from simulador.agents import Pessoa, Empresa

def ler_categorias(caminho='data/categorias.json'):
    """Lê o arquivo JSON de categorias e retorna um dicionário."""
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def ler_pessoas(caminho='data/pessoas.txt'):
    """Lê o arquivo CSV de pessoas e retorna uma lista de objetos Pessoa."""
    pessoas = []
    with open(caminho, 'r', encoding='utf-8') as f:
        leitor_csv = csv.reader(f)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            nome, patrimonio, salario = linha
            pessoas.append(Pessoa(nome, float(patrimonio), float(salario)))
    return pessoas

def ler_empresas(caminho='data/empresas.csv'):
    """Lê o arquivo CSV de empresas e retorna uma lista de objetos Empresa."""
    empresas = []
    with open(caminho, 'r', encoding='utf-8') as f:
        leitor_csv = csv.reader(f)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            categoria, nome, produto, custo, qualidade = linha
            empresas.append(Empresa(categoria, nome, produto, float(custo), int(qualidade)))
    return empresas