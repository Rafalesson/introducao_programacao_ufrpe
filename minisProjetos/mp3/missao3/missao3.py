import time

# Importando as constantes e variáveis necessárias
from missao1.missao1 import (
    POUPANCA, IPCA, red, green, blue, yellow, magenta, white
)

def missao_3(valor_investido, meses, valor_resgate):
    """
    Missão 3: Exibição das análises adicionais, com validação de entrada do usuário.
    """
    # --- TRATAMENTO DE ERRO PARA RESPOSTA S/N ---
    while True:
        ver_analise = input(f"\nVocê gostaria de ver algumas análises adicionais (S/N)? ").upper()
        if ver_analise in ['S', 'N']:
            break # Sai do loop se a resposta for S ou N
        else:
            print(f'{red}Resposta inválida. Por favor, digite S para sim ou N para não.{white}')
    
    time.sleep(.5)

    taxa_poupanca_mensal = (POUPANCA / 12) / 100
    resgate_poupanca = valor_investido * (1 + taxa_poupanca_mensal)**meses
    lucro_poupanca = resgate_poupanca - valor_investido

    taxa_ipca_mensal = (IPCA / 12) / 100
    valor_corrigido_inflacao = valor_investido * (1 + taxa_ipca_mensal)**meses
    
    inflacao_acumulada = (valor_corrigido_inflacao / valor_investido) * 100
    desvalorizacao = (valor_investido / valor_corrigido_inflacao) * 100

    if ver_analise == 'S':
        print(f"\n{green}---------------------------------{white}")
        print(f"{yellow}\tANÁLISES POUPANÇA{white}") 
        print(f"{green}---------------------------------{white}\n")
        time.sleep(.5)
        print(f"Se você tivesse investido: {green}R${valor_investido:.2f}{white}") 
        time.sleep(.5)
        print(f"na poupança, ao final dos: {blue}{meses} meses{white}") 
        time.sleep(.5)
        print(f"o valor resgatado seria..: {green}R${resgate_poupanca:.2f}{white}") 
        time.sleep(.5)
        print(f"e o lucro total..........: {green}R${lucro_poupanca:.2f}{white}") 
        time.sleep(.5)
        
        diferenca_lucro = (valor_resgate - valor_investido) - lucro_poupanca
        print(f"A diferença de lucro é de: {green}R${diferenca_lucro:.2f}{white}") 
        time.sleep(.5)
        
        print(f"\n{green}---------------------------------{white}")
        print(f"{yellow}\tANÁLISES INFLAÇÃO{white}") 
        print(f"{green}---------------------------------{white}\n")
        time.sleep(.5)
        
        print(f"A inflação acumulada foi de........................: {magenta}{inflacao_acumulada:.2f}%{white}") 
        time.sleep(.5)
        print(f"resultando em uma desvalorização de................: {magenta}{desvalorizacao:.2f}%{white}") 
        time.sleep(.5)
        print(f"Por exemplo, se você comprava algo por.............: {green}R$ {valor_investido:.2f}{white}") 
        time.sleep(.5)
        print(f"O mesmo item custaria corrigido pela inflação será.: {green}R$ {valor_corrigido_inflacao:.2f}{white}") 
        time.sleep(.5)

        resgate_proporcional = (valor_resgate / valor_corrigido_inflacao) * valor_investido
        poupanca_proporcional = (resgate_poupanca / valor_corrigido_inflacao) * valor_investido
        print(f"O resgate proporcionalmente ao valor corrigido fica: {green}R$ {resgate_proporcional:.2f}{white}") 
        time.sleep(.5)
        print(f"Já na poupança o proporcional a essa correção seria: {green}R$ {poupanca_proporcional:.2f}{white}") 
        time.sleep(.5)

    print(f"\n{green}---------------------------------{white}")
    print(f"{yellow}\tRESUMO GERAL{white}") 
    print(f"{green}---------------------------------{white}\n")
    time.sleep(.5)
    print(f"Valor investido.....: {green}R$ {valor_investido:.2f}{white}") 
    time.sleep(.5)
    print(f"Valor resgatado.....: {green}R$ {valor_resgate:.2f}{white}") 
    time.sleep(.5)
    print(f"Se fosse na poupança: {green}R$ {resgate_poupanca:.2f}{white}") 
    time.sleep(.5)
    print(f"Correção da inflação: {green}R$ {valor_corrigido_inflacao:.2f}{white}") 
    time.sleep(.5)
    
    print("\nEspero ter ajudado!")