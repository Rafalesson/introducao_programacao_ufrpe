import sys
import time
import json
from pathlib import Path

# Adiciona a pasta raiz ao sys.path
sys.path.append(str(Path(__file__).parent.parent))

from base import colorir, azul, verde, ciano, vermelho, amarelo

# Variáveis globais (sempre disponíveis)
nome = None
dia = None
mes = None
ano = None
patrimonio = None
salario = None
aluguel = None
feira = None
comida = None
transporte = None
outros = None
investimento = None

if __name__ == "__main__":
    # Introdução
    print(f"\nOi, pode me chamar de {colorir("Din", azul)}!") 
    print(f"Sou um assistente financeiro \ne vou tentar te ajudar com as {colorir("contas", azul)} e os {colorir("objetivos", azul)}.")
    time.sleep(1)

    # Dados Pessoais
    print(colorir("\n[DADOS PESSOAIS]", ciano)) 
    print("\nPrimeiro, preciso de algumas informações: ")

    nome = input(f"Me diz teu {colorir("nome", amarelo)}: ")
    dia = float(input(f"O {colorir("dia", amarelo)} que nasceu: "))
    mes = float(input(f"Agora o {colorir("mês", amarelo)}: "))
    ano = float(input(f"E o {colorir("ano", amarelo)}: "))

    # Confirmação de dados
    print("\nMuito bem! Confirmando seus dados, estou registrando aqui:" )
    print(f"{colorir(f"{nome}", verde)}, nascimento em {colorir(f"{dia}/{mes}/{ano}", verde)}")  

    print("\n--------------------\n")
    time.sleep(1)

    # Dados Financeiros
    print(colorir("[DADOS FINANCEIROS]\n", ciano))
    patrimonio = float(input(f"Se você somar o dinheiro que tem guardado, me diz o total desse {colorir("patrimônio", amarelo)}: R$ "))
    salario = float(input(f"Me diz teu {colorir("salário", amarelo)}: R$ "))

    print("\nSobre os seus gastos, me informa por partes por favor:")

    aluguel = float(input(f"Quanto custa teu {colorir("aluguel", amarelo)} (incluindo condomínio e outras taxas): R$ "))
    feira = float(input(f"Mais ou menos o quanto você gasta fazendo {colorir("feira", amarelo)} todo mês: R$ "))
    comida = float(input(f"Com {colorir("comida", amarelo)} fora de casa, em média dá quanto: R$ "))
    transporte = float(input(f"Na mobilidade, quanto que gasta com {colorir("transporte", amarelo)} (ônibus, uber, gasolina, etc): R$ "))
    outros = float(input(f"Pra terminar, quanto você gasta com {colorir("outros", amarelo)} (lazer, roupas, etc): R$ "))

    print("\n--------------------\n")
    time.sleep(1)

    # Cálculos
    gastos_totais = aluguel + feira + comida + transporte + outros
    saldo_mensal = salario - gastos_totais

    # Saída formatada
    print(f"Obrigado, {nome}, resumindo as informações financeiras até agora. \nOs seus gastos discriminados são:")
    print(f"{colorir("\nAluguel", verde)}: R$ {aluguel:.2f}")
    print(f"{colorir("Feira", verde)}: R$ {feira:.2f}")
    print(f"{colorir("Comida", verde)}: R$ {comida:.2f}")
    print(f"{colorir("Transporte", verde)}: R$ {transporte:.2f}")
    print(f"{colorir("Outros", verde)}: R$ {outros:.2f}")
    print(f"{colorir("GASTOS TOTAIS", vermelho)}: R$ {gastos_totais:.2f}")  

    print("\n--------------------\n")
    time.sleep(1)

    if saldo_mensal >= 0:
        print(f"Para terminar, calculando o seu saldo mensal, com base em todos os gastos e no teu salário, o valor resultante é de {colorir(f"R$ {saldo_mensal:.2f}", verde)}")
    else:
        print(f"Para terminar, calculando o seu saldo mensal, com base em todos os gastos e no teu salário, o valor resultante é de {colorir(f"R$ {saldo_mensal:.2f}", vermelho)}")

    investimento = float(input(f"Desse valor, considerando que qualquer investimento é válido, o quanto você conseguiria investir todo mês: R$ "))

    print(f"\nOk, anotado! O valor do investimento mensal é {colorir(f"R$ {investimento:.2f}", verde)}")
    print("Acredito que coletei todas as informações necessárias para te ajudar com os objetivos financeiros.")
    
     # Salva os dados em um arquivo JSON
    dados_usuario = {
        "nome": nome,
        "dia": dia,
        "mes": mes,
        "ano": ano,
        "patrimonio": patrimonio,
        "salario": salario,
        "aluguel": aluguel,
        "feira": feira,
        "comida": comida,
        "transporte": transporte,
        "outros": outros,
        "investimento": investimento
    }

    with open(os.path.join(projeto_raiz, "dados_usuario.json"), "w") as f:
        json.dump(dados_usuario, f, indent=4)

    print("\nDados salvos em 'dados_usuario.json'.")