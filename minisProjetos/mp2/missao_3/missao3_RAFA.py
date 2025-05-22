import sys
import json
from pathlib import Path

# Adiciona a pasta raiz ao sys.path
sys.path.append(str(Path(__file__).parent.parent))

# Importa funções e variáveis de base.py
from base import colorir, azul, verde, ciano, vermelho, amarelo

# Importa as classes
from classes import Data, Gastos, Financas, Pessoa

# Carrega os dados do usuário
try:
    with open("dados_usuario.json", "r") as f:
        dados = json.load(f)

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

    # Cria objetos com os dados
    nascimento = Data(dia, mes, ano)
    gastos = Gastos(aluguel, feira, comida, transporte, outros)
    financas = Financas(patrimonio, salario, gastos, investimento)
    pessoa = Pessoa(nome, nascimento, financas)

    print("\n--------------------\n")
    print(f"Agora sim, vamos pensar no futuro!")
    print(f"Você tem um próximo objetivo financeiro?")
    print(f"Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?")
    print(f"Exemplos de objetivos assim são:")
    print(f"{colorir('Comprar um carro', azul)}, {colorir('fazer uma viagem', azul)}, {colorir('comprar uma casa', azul)}, {colorir('fazer um curso', azul)}, etc.")

    objetivo = input(f"\nQual seria esse seu próximo objetivo financeiro? ")
    valor_objetivo = float(input(f"Qual o valor do objetivo financeiro? R$ "))

    if investimento <= 0:
        print(colorir("⚠️ O investimento mensal deve ser maior que zero.", vermelho))
    else:
        meses_necessarios = (valor_objetivo - patrimonio) / investimento
        anos_necessarios = meses_necessarios / 12

        if meses_necessarios <= 0:
            print(f"\n{colorir('Parabéns!', verde)} Você já possui o suficiente para atingir o objetivo: '{objetivo}'.")
        else:
            print(f"\nEm uma conta simples que fiz aqui, sem considerar rendimentos ou inflação...")
            print(f"Com base na sua capacidade de investimento mensal de {colorir(f'R$ {investimento:.2f}', verde)}")
            print(f"E o seu patrimônio atual de {colorir(f'R$ {patrimonio:.2f}', verde)}")
            print(f"Você conseguiria atingir o valor de {colorir(f'R$ {valor_objetivo:.2f}', verde)} em:")
            print(f"{colorir(f'{meses_necessarios} meses', amarelo)} ou {colorir(f'{anos_necessarios:.1f} anos', amarelo)}.")
            print(f"\nPor hora, é isso que tenho para te ajudar.\nEspero que tenha sido útil!")

except FileNotFoundError:
    print(colorir("⚠️ Arquivo de dados não encontrado. Execute primeiro o 'missao1.py'", vermelho))