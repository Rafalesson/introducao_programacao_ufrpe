import time

# Importando as constantes e variáveis da missão 1
from missao1.missao1 import (
    CDI, red, green, blue, ciano, magenta, white, italic, regular
)

def missao_2(valor_investido, tipo_investimento):
    """
    Missão 2: Coleta do tempo, com validação de entrada do usuário.
    """
    taxas = {
        'A': CDI * 1.00,
        'B': CDI * 1.10,
        'C': CDI * 1.20,
        'D': CDI * 0.95
    }
    taxa_anual_selecionada = taxas[tipo_investimento]
    taxa_mensal = (1 + taxa_anual_selecionada / 100)**(1/12) - 1

    if tipo_investimento in ['A', 'B', 'C']:
        print(f"\nComo você escolheu um {blue}CDB{white} vou te lembrar as taxas regressivas de IR:") 
        time.sleep(.5)
        print(f"Até 6 meses.....: {magenta}22.50%{white}") 
        time.sleep(.5)
        print(f"Até 12 meses....: {magenta}20.00%{white}") 
        time.sleep(.5)
        print(f"Até 24 meses....: {magenta}17.50%{white}") 
        time.sleep(.5)
        print(f"Mais de 24 meses: {magenta}15.00%{white}") 
        time.sleep(.5)

    # --- TRATAMENTO DE ERRO PARA OS MESES ---
    while True:
        try:
            meses = int(input(f"\nQuanto tempo você gostaria de esperar para resgatar esse investimento? (em meses): "))
            if meses > 0:
                break # Sai do loop se o valor for um número inteiro positivo
            else:
                print(f"{red}O número de meses deve ser maior que zero.{white}")
        except ValueError:
            print(f"{red}Entrada inválida. Por favor, digite um número inteiro.{white}")

    time.sleep(.5)
    print(f"{italic}Ok, registrei o tempo para o resgate.{regular}")
    time.sleep(1) 

    valor_final_bruto = valor_investido * ((1 + taxa_mensal) ** meses)
    lucro = valor_final_bruto - valor_investido
    
    taxa_ir = 0
    valor_ir = 0
    
    if tipo_investimento in ['A', 'B', 'C']:
        if meses <= 6:
            taxa_ir = 0.225
        elif meses <= 12:
            taxa_ir = 0.20
        elif meses <= 24:
            taxa_ir = 0.175
        else: 
            taxa_ir = 0.15 
        valor_ir = lucro * taxa_ir
        
    valor_final_liquido = valor_final_bruto - valor_ir

    print(f"\n{green}---------------------------------{white}")
    print(f"\t{ciano}TAXAS UTILIZADAS{white}") 
    print(f"{green}---------------------------------{white}\n")
    time.sleep(.5)
    if tipo_investimento in ['A', 'B', 'C']:
        print(f"Taxa de IR aplicada......: {magenta}{taxa_ir * 100:.2f}%{white}") 
        time.sleep(.5)
    print(f"Taxa de rendimento anual.: {magenta}{taxa_anual_selecionada:.2f}%{white}") 
    time.sleep(.5)
    print(f"Taxa de rendimento mensal: {magenta}{taxa_mensal * 100:.2f}%{white}") 
    time.sleep(.5)
    
    print(f"\n{green}---------------------------------{white}")
    print(f"\t{ciano}RETORNO ESPERADO{white}")
    print(f"{green}---------------------------------{white}\n")
    time.sleep(.5)
    print(f"Valor investido.......: {green}R$ {valor_investido:.2f}{white}") 
    time.sleep(.5)
    print(f"Rendendo pelo tempo de: {blue}{meses} meses{white}") 
    time.sleep(.5)
    if tipo_investimento in ['A', 'B', 'C']:
        print(f"Dedução do IR (%).....: {red}{taxa_ir * 100:.2f}%{white}") 
        time.sleep(.5)
        print(f"Valor deduzido é de...: {red}R$ {valor_ir:.2f}{white}") 
        time.sleep(.5)
    
    print(f"O valor bruto será de.: {green}R$ {valor_final_bruto:.2f}{white}")
    time.sleep(.5)
    print(f"O resgate será de.....: {green}R$ {valor_final_liquido:.2f}{white}") 
    time.sleep(.5)
    print(f"O lucro total será de.: {green}R$ {valor_final_liquido - valor_investido:.2f}{white}") 
    time.sleep(.5)

    return valor_investido, meses, valor_final_liquido