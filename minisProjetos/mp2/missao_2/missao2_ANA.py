class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Gastos:
    def __init__(self, aluguel, feira, comida, transporte, outros):
        self.aluguel = aluguel
        self.feira = feira
        self.comida = comida
        self.transporte = transporte
        self.outros = outros

class Financas:
    def __init__(self, patrimonio, salario, gastos, investimento):
        self.patrimonio = patrimonio
        self.salario = salario
        self.gastos = gastos
        self.investimento = investimento

class Pessoa:
    def __init__(self, nome, nascimento, financas):
        self.nome = nome
        self.nasc = nascimento
        self.financas = financas

nome = input("Digite o nome: ")
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

aluguel = float(input("Digite o valor do aluguel: R$ "))
feira = float(input("Digite o valor da feira: R$ "))
comida = float(input("Digite o valor gasto com comida: R$ "))
transporte = float(input("Digite o valor do transporte: R$ "))
outros = float(input("Digite outros gastos: R$ "))

patrimonio = float(input("Digite o valor do patrimônio: R$ "))
salario = float(input("Digite o valor do salário: R$ "))
investimento = float(input("Digite o valor investido: R$ "))

# Instanciando objetos
nascimento = Data(dia, mes, ano)
gastos = Gastos(aluguel, feira, comida, transporte, outros)
financas = Financas(patrimonio, salario, gastos, investimento)
pessoa = Pessoa(nome, nascimento, financas)

# Cálculo dos gastos totais
gastos_totais = (
    pessoa.financas.gastos.aluguel +
    pessoa.financas.gastos.feira +
    pessoa.financas.gastos.comida +
    pessoa.financas.gastos.transporte +
    pessoa.financas.gastos.outros
)

print("\n---")
print(f"\nAgora organizei todos os seus dados de forma concentrada aqui no meu sistema")
print(f"Vou te mostrar como ficou:")
print(f"{pessoa.nome}, nascimento em {pessoa.nasc.dia}/{pessoa.nasc.mes}/{pessoa.nasc.ano}")
print(f"{pessoa.nome} tem R$ {pessoa.financas.patrimonio:.2f} de patrimônio")
print(f"{pessoa.nome} tem R$ {pessoa.financas.salario:.2f} de salário")
print(f"{pessoa.nome} tem R$ {gastos_totais:.2f} de gastos")
print(f"{pessoa.nome} tem R$ {pessoa.financas.investimento:.2f} de investimento")
