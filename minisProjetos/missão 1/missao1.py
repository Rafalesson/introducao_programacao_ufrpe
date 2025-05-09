# Dados pessoais
nome_completo = "Antonieta da Silva"
dia_nasc = 16
mes_nasc = 5
ano_nasc = 1998

# Data atual
dia_atual = 18
mes_atual = 5
ano_atual = 2025

#Calcula dias totais (cada ano = 365 dias, cada mês = 30 dias)
data_atual_em_dias = ano_atual * 365 + mes_atual * 30 + dia_atual
data_nasc_em_dias = ano_nasc * 365 + mes_nasc * 30 + dia_nasc
diasDeVida = data_atual_em_dias - data_nasc_em_dias

# Calcula a idade correta
ja_fez_aniversario = (mes_atual > mes_nasc) or (mes_atual == mes_nasc and dia_atual >= dia_nasc)
idade = ano_atual - ano_nasc - (not ja_fez_aniversario)

# Saída
print(f"{nome_completo}, nascida em {dia_nasc}/{mes_nasc}/{ano_nasc}.")
print(f"{nome_completo} tem {diasDeVida} dias de vida.")
print(f"{nome_completo} tem {idade} anos de vida.")