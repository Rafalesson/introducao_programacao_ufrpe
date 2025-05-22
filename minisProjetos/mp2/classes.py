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
