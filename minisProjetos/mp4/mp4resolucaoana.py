import os
import datetime

# --- Códigos de cores e formatação ---
R = '\033[31m'  # vermelho
G = '\033[32m'  # verde
B = '\033[34m'  # azul
Y = '\033[33m'  # amarelo
P = '\033[35m'  # roxo
C = '\033[36m'  # ciano
W = '\033[37m'  # branco
I = '\033[3m'   # itálico
N = '\033[7m'   # negativo
FX = '\033[0m'  # resetar (para voltar à formatação padrão)

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Investimento:
    def __init__(self, percentual, aporte_inicial, recorrente_str):
        self.percentual = float(percentual)
        self.aporte_inicial = float(aporte_inicial)
        self.recorrente = recorrente_str.lower() == 'sim'
        self.total_aportado = self.aporte_inicial
        self.saldo = self.aporte_inicial
        self.meses_passados = 0

    def simular_mes(self):
        cdi_mensal = 0.011458 #1.1458% ao mês

        # Se for investimento recorrente e não for o primeiro mês
        if self.recorrente and self.meses_passados > 0:
            self.saldo += self.aporte_inicial
            self.total_aportado += self.aporte_inicial

        # Calcula rendimento sobre o saldo atualizado
        rendimento_mes = self.saldo * (self.percentual / 100) * cdi_mensal
        self.saldo += rendimento_mes

        #Atualiza o número de meses:
        self.meses_passados += 1
        return rendimento_mes


def main():
    investimentos = [] # Lista que os investimentos são adicionados
    meses_simulados = 0
    mes_atual = datetime.datetime.now().month
    ano_atual = datetime.datetime.now().year

    print("[SIMULADOR DE INVESTIMENTOS RECORRENTES]")
    print(f"{I}Bem-vindo, vamos simular também investimentos recorrentes!{FX}")
    print(f"{I}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez.{FX}")
    print()

    while True:
        comando = input(f"Digite {B}[novo]{FX} investimento, {B}[sair]{FX} ou aperte {B}[enter]{FX} para avançar em um mês: ").strip().lower()

        if comando == "novo":
            print()
            try:
                percentual_str = input(f"Qual o percentual? ({B}% do CDI{FX}) ")
                aporte_str = input(f"Qual o valor do {B}aporte de entrada{FX}? ")
                recorrente_str = input(f"Serão depósitos mensalmente recorrentes? ({B}sim/não{FX}) ")

                novo_investimento = Investimento(percentual_str, aporte_str, recorrente_str)
                investimentos.append(novo_investimento)

                print()
                print(f"{I}Investimento adicionado com sucesso!{FX}")
                print()

            except ValueError:
                print()
                print(f"{R}{I}Erro: Percentual e aporte devem ser números. Tente novamente.{FX}")
                print()
            except Exception as e:
                print()
                print(f"{R}{I}Ocorreu um erro inesperado: {e}{FX}")
                print()

        elif comando == "sair":
            print()
            print(f"{I}Encerrando o simulador... Obrigado por usar!{FX}")
            break

        elif comando == "":
            print()
            if not investimentos:
                print(f"{I}Nenhum investimento cadastrado para simular.{FX}")
            else:
                meses_simulados += 1

                for investimento in investimentos:
                    investimento.simular_mes()
                    tipo_investimento = "R" if investimento.recorrente else "U"
                    barras = "$" * int(investimento.saldo // 1000)  # Uma barra por R$ 1.000
                    print(f"[{tipo_investimento}] LCI de {investimento.percentual:.2f}% do CDI | Total aportado: R${investimento.total_aportado:.2f} | Resgate: {G}R${investimento.saldo:.2f}{FX} {Y}{barras}{FX}")

                mes_simulado = (mes_atual + meses_simulados - 1) % 12
                ano_simulado = ano_atual + (mes_atual + meses_simulados - 1) // 12

                print()
                print(f"{I}Resumo da simulação em {P}{meses[mes_simulado]} de {ano_simulado}{FX}{FX}")

        else:
            print()
            print(f"{R}{I}Comando '{comando}' não reconhecido. Por favor, use [novo], [sair] ou [enter].{FX}")
            print()

if __name__ == "__main__":
    main()
