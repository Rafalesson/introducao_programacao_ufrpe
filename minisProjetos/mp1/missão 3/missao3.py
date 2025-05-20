patrimonio_inicial = 2000
taxa_mensal = 0.005
meses = 12

patrimonio_final = patrimonio_inicial * (1 + taxa_mensal) ** meses
rendimento_obtido = patrimonio_final - patrimonio_inicial

print('Se Antonieta da Silva não investir nada, após 12 meses o seu patrimônio terá rendido R$'+str(rendimento_obtido),'e será R$'+str(patrimonio_final))
