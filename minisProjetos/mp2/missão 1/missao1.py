import time
from base import colored, azul, verde, ciano, vermelho, amarelo

# Introdução
print(f"\nOi, pode me chamar de {colored("Din!", azul)}") 
print(f"Sou um assistente financeiro \ne vou tentar te ajudar com as {colored("contas", azul)} e os {colored("objetivos", azul)}.")
time.sleep(1)

# Dados Pessoais
print(colored("\n[DADOS PESSOAIS]", ciano) ) 
print("\nPrimeiro, preciso de algumas informações: ")

nome = input(f"Me diz teu {colored("nome", 93)}: ")
dia = int(input(f"O {colored("dia", amarelo)} que nasceu: "))
mes = int(input(f"Agora o {colored("mês", amarelo)}: "))
ano = int(input(f"E o {colored("ano", amarelo)}: "))

# Confirmação de dados
print("\nMuito bem! Confirmando seus dados, estou registrando aqui:" )
print(f"{colored(f"{nome}", verde)}, nascimento em {colored(f"{dia}/{mes}/{ano}", verde)}")  

print("\n--------------------\n")
time.sleep(1)

# Dados Financeiros
print(colored("[DADOS FINANCEIROS]\n", ciano))
patrimonio = float(input(f"Se você somar o dinheiro que tem guardado, me diz o total desse {colored("patrimônio", amarelo)}: R$ "))
salario = float(input(f"Me diz teu {colored("salário", amarelo)}: R$ "))

print("\nSobre os seus gastos, me informa por partes por favor:")

aluguel = float(input(f"Quanto custa teu {colored("aluguel", amarelo)} (incluindo condomínio e outras taxas): R$ "))
feira = float(input(f"Mais ou menos o quanto você gasta fazendo {colored("feira", amarelo)} todo mês: R$ "))
comida = float(input(f"Com {colored("comida", amarelo)} fora de casa, em média dá quanto: R$ "))
transporte = float(input(f"Na mobilidade, quanto que gasta com {colored("transporte", amarelo)} (ônibus, uber, gasolina, etc): R$ "))
outros = float(input(f"Pra terminar, quanto você gasta com {colored("outros", amarelo)} (lazer, roupas, etc): R$ "))

print("\n--------------------\n")
time.sleep(1)

# Cálculos
gastos_totais = aluguel + feira + comida + transporte + outros
saldo_mensal = salario - gastos_totais

# Saída formatada
print(f"Obrigado, {nome}, resumindo as informações financeiras até agora. \nOs seus gastos discriminados são:")
print(f"{colored("\nAluguel", verde)}: R$ {aluguel:.2f}")
print(f"{colored("Feira", verde)}: R$ {feira:.2f}")
print(f"{colored("Comida", verde)}: R$ {comida:.2f}")
print(f"{colored("Transporte", verde)}: R$ {transporte:.2f}")
print(f"{colored("Outros", verde)}: R$ {outros:.2f}")
print(f"{colored("GASTOS TOTAIS", vermelho)}: R$ {gastos_totais:.2f}")  

print("\n--------------------\n")
time.sleep(1)

print(f"Para terminar, calculando o seu saldo mensal, com base em todos os gastos e no teu salário, o valor resultante é de {colored(f"R$ {saldo_mensal:.2f}", verde)}")

investimento = float(input(f"Desse valor, considerando que qualquer investimento é válido, o quanto você conseguiria investir todo mês: R$ "))

print(f"\nOk, anotado! O valor do investimento mensal é {colored(f"R$ {investimento:.2f}", verde)}")
print("Acredito que coletei todas as informações necessárias para te ajudar com os objetivos financeiros.")