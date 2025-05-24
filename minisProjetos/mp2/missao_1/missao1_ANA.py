#Cores: Verde: \033[32m, Azul: \033[34m, Amarelo: \033[33m
print("Oi, pode me chamar de \033[34mDin!\033[0m \nSou um assistente financeiro \ne vou tentar te ajudar com as \033[34mcontas\033[0m e os \033[34mobjetivos\033[0m.")

print("\n[DADOS PESSOAIS]")
print("\nPrimeiro, preciso de algumas informações")
nome = input("Me diz teu \033[33mnome\033[0m: ")
dia_nasc = input("O \033[33mdia\033[0m em que tu nasceu: ")
mes_nasc = input("Agora o \033[33mmês\033[0m: ")
ano_nasc = input("E o \033[33mano\033[0m: ")

print("\n---")
print("\nMuito bem, então conferindo seus dados, estou registrando aqui.")
print(f"\033[32m{nome}\033[0m, nascimento em \033[32m{dia_nasc}/{mes_nasc}/{ano_nasc}\033[0m")

print("\n[DADOS FINANCEIROS]")
print("\nAgora me informa por favor alguns dados financeiros")
patrimonio = float(input("Se você somar o dinheiro que tem guardado, me diz o total desse \033[33mpatrimônio\033[0m: R$ "))
salario = float(input("Me diz teu \033[33msalário\033[0m: R$ "))

print("\nSobre os seus gastos, me informa por partes por favor.")
aluguel = float(input("Quanto custa teu \033[33maluguel\033[0m, (incluindo condomínio e outras taxas): R$ "))
feira = float(input("Mais ou menos o quanto você gasta fazendo \033[33mfeira\033[0m todo mês: R$ "))
comida = float(input("E com \033[33mcomida\033[0m fora de casa, em média dá quanto: R$ "))
transporte = float(input("Na mobilidade, quanto que gasta com \033[33mtransporte\033[0m (ônibus, uber, gasolina, etc): R$ "))
outros = float(input("Pra terminar, quanto você gasta com \033[33moutros\033[0m (lazer, roupas, etc): R$ "))

# Soma total dos gastos
gastos_totais = aluguel + feira + comida + transporte + outros

print("\n---")
print(f"\nObrigado! \033[32m{nome}\033[0m, resumindo as informações financeiras até agora.")
print("Os seus gastos discriminados são:")
print(f"\033[32mAluguel\033[0m: R$ {aluguel:.2f}")
print(f"\033[32mFeira\033[0m: R$ {feira:.2f}")
print(f"\033[32mComida\033[0m: R$ {comida:.2f}")
print(f"\033[32mTransporte\033[0m: R$ {transporte:.2f}")
print(f"\033[32mOutros\033[0m: R$ {outros:.2f}")
print(f"\033[32mGASTOS TOTAIS\033[0m: R$ {gastos_totais:.2f}")

resultado = salario - gastos_totais
print("\n---")
print("\nPra terminar, calculando o seu saldo mensal, com base em todos os gastos") 
print(f"e no teu salário, o valor resultante é de \033[32mR$ {resultado:.2f}\033[0m")
print("Desse valor, considerando que qualquer investimento é valido,")
investimento = float(input("o quanto você conseguiria \033[33minvestir\033[0m todo mês: R$ "))
print(f"Ok, anotado, o valor do investimento mensal é \033[32mR$ {investimento:.2f}\033[0m ")
print("Acredito que coletei todas as informações necessárias")
