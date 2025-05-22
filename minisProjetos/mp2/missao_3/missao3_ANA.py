class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def chatbot():

    print("Agora sim, vamos pensar no futuro! Você tem um próximo objetivo financeiro?")
    print("Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?")
    print("Exemplos de objetivos assim são:")
    print("Comprar uma moto ou um carro, fazer uma viagem, comprar uma casa, fazer um curso, etc.")

    objetivo = input("Qual seria esse seu próximo \033[93mobjetivo\033[0m financeiro: ")
    valor_objetivo = float(input("Qual o valor do \033[93mobjetivo\033[0m financeiro: R$ ").replace(',', '.'))

    investimento_mensal = 100.00
    patrimonio_atual = 2000.00
    restante = valor_objetivo - patrimonio_atual
    meses = 0 if restante <= 0 else restante / investimento_mensal
    anos = meses / 12

    print(f"Em uma conta simples que fiz aqui, sem considerar rendimentos ou inflação, com base na sua capacidade de investimento mensal de {bcolors.OKGREEN}R$ {investimento_mensal:.2f}{bcolors.ENDC}")
    print(f"e o seu patrimônio atual de {bcolors.OKGREEN}R$ {patrimonio_atual:.2f}{bcolors.ENDC}")
    print(f"Você conseguiria atingir o valor de {bcolors.OKGREEN}R$ {valor_objetivo:.2f}{bcolors.ENDC} em:")
    print(f"{meses:.2f} meses")
    print(f"Ou {anos:.2f} anos")
    print("Por hora, é isso que tenho para te ajudar")
    print("Espero que tenha sido útil.")

chatbot()
