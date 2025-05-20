nome_completo = 'Antonieta da Silva'
dia_nascimento = 16
mes_nascimento = 5
ano_nascimento = 1998

print(nome_completo + ', nascida em ' + str(dia_nascimento) + '/' + str(mes_nascimento) + '/' + str(ano_nascimento))

dia_atual = 15
mes_atual = 5
ano_atual = 2025

diferenca_de_anos = ano_atual - ano_nascimento
quantidade_de_dias = diferenca_de_anos * 365 - (dia_nascimento - dia_atual)
idade = diferenca_de_anos - ((mes_atual, dia_atual) < (mes_nascimento, dia_nascimento))

print(nome_completo + ' tem', str(quantidade_de_dias), 'dias de vida')

print(nome_completo + ' tem', str(idade), 'anos de vida')
