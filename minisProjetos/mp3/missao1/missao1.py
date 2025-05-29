import time

# Cores e constantes que serão usadas em todo o projeto
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
yellow = '\033[33m'
ciano = '\033[36m'
magenta = '\033[35m'
white = '\033[0m'
italic = '\033[3m'
bold = '\033[1m'
regular = '\033[0m'

IPCA = 5.53
CDI = 14.65
POUPANCA = 6.00

def missao_1():
    """
    Missão 1: Interação inicial, com validação de entradas do usuário.
    """
    print(f"\n{ciano}----------------------------------------------------")
    print(f"\t{green}💰 SIMULADOR DE INVESTIMENTOS 💰")
    print(f"{ciano}----------------------------------------------------{white}\n")
    time.sleep(.5)
    
    print(f"{italic}Olá, vou te ajudar a simular as possibilidades de investimentos.{regular}")
    time.sleep(.5)
    print(f"{italic}Pra começar, quero te dizer que as taxas anuais que estou utilizando são:{regular}")
    time.sleep(.5)
    print(f"\nIPCA (inflação): {magenta}{IPCA}%{white}") 
    time.sleep(.5)
    print(f"CDI (juros)....: {magenta}{CDI}%{white}") 
    time.sleep(.5)
    print(f"Poupança.......: {magenta}{POUPANCA}%{white}") 
    time.sleep(.5)

    # --- TRATAMENTO DE ERRO PARA VALOR DO INVESTIMENTO ---
    while True:
        try:
            valor_investido = float(input(f"\nAgora me informa o valor em reais que você quer investir: {green}R$ "))
            if valor_investido > 0:
                break # Sai do loop se o valor for um número positivo
            else:
                print(f"{red}Por favor, digite um valor maior que zero.{white}")
        except ValueError:
            print(f"{red}Entrada inválida. Por favor, digite apenas números.{white}")

    time.sleep(.5)
    print(f"{white}{italic}Ok, registrei o valor de seu investimento.{regular}")
    time.sleep(.5)
    
    print("\nEssas são as opções de investimento que tenho disponíveis para você:")
    time.sleep(.5)
    
    print(f"{italic}\t[A] {blue}CDB{white} valendo 100% do CDI, taxa final de {magenta}{CDI * 1.00:.2f}%{white}") 
    time.sleep(.5)
    print(f"{italic}\t[B] {blue}CDB{white} valendo 110% do CDI, taxa final de {magenta}{CDI * 1.10:.2f}%{white}") 
    time.sleep(.5)
    print(f"{italic}\t[C] {blue}CDB{white} valendo 120% do CDI, taxa final de {magenta}{CDI * 1.20:.2f}%{white}") 
    time.sleep(.5)
    print(f"{italic}\t[D] {blue}LCA{white} valendo 95%  do CDI, taxa final de {magenta}{CDI * 0.95:.2f}%{white}") 
    time.sleep(.5)
    
    print(f"{italic}Obs.: Lembre que o {red}CDB retém IR na fonte{white}, enquanto a LCA não.{white}{regular}") 
    time.sleep(.5)
    
    # --- TRATAMENTO DE ERRO PARA TIPO DE INVESTIMENTO ---
    while True:
        tipo_investimento = input("\nQual o investimento que você quer fazer? (A, B, C ou D): ").upper()
        if tipo_investimento in ['A', 'B', 'C', 'D']:
            break # Sai do loop se a opção for válida
        else:
            print(f"{red}Opção inválida. Por favor, digite A, B, C ou D.{white}")

    time.sleep(.5)
    print(f"{italic}Ok, registrei sua opção de investimento.{regular}")
    time.sleep(.5)

    return valor_investido, tipo_investimento