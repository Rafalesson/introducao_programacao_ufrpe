nome_completo = "Antonieta da Silva"
salario_minimo = 1518

# Dados financeiros da pessoa
patrimonio_inicial = 2000
recebimentos_mensais = 1518
gastos_mensais = 1077
investimentos_mensais = 150

# Cálculo de quantos salários mínimos equivalem a renda e patrimônio
salarios_minimos_renda = recebimentos_mensais / salario_minimo
salarios_minimos_patrimonio = patrimonio_inicial / salario_minimo

# Cálculo do percentual dos recebimentos que é gasto
percentual_gasto = (gastos_mensais / recebimentos_mensais) * 100

# Simulação dos resultados financeiros após 1 mês
# Rendimento do patrimônio (0.5% ao mês)
rendimento_patrimonio = patrimonio_inicial * 0.005
patrimonio_resultante = patrimonio_inicial + rendimento_patrimonio + investimentos_mensais
salarios_minimos_patrimonio_resultante = patrimonio_resultante / salario_minimo

# Dinheiro livre no final do mês
dinheiro_livre = recebimentos_mensais - gastos_mensais - investimentos_mensais

# Imprimir os resultados na tela
print()
print(f"1°) {nome_completo} recebe mensalmente R${recebimentos_mensais:.2f}.")
print(f"2°) Os recebimentos equivalem a {salarios_minimos_renda} salário(s) mínimo(s).")
print(f"3°) {nome_completo} tem um patrimônio de R${patrimonio_inicial:.2f}.")
print(f"4°) O patrimônio equivale a {salarios_minimos_patrimonio:.1f} salários mínimos.")
print(f"5°) {nome_completo} gasta R${gastos_mensais:.2f} por mês.")
print(f"6°) Os gastos equivalem a {percentual_gasto:.2f}% da sua renda.")
print(f"7°) {nome_completo} investe mensalmente R${investimentos_mensais:.2f}.")
print(f"8°) {nome_completo} após 1 mês está com o patrimônio de R${patrimonio_resultante:.2f}.")
print(f"9°) O patrimônio resultante equivale a {salarios_minimos_patrimonio_resultante:.1f} salários mínimos.")
print(f"10°) O saldo de dinheiro livre no mês foi de R${dinheiro_livre:.2f}.")