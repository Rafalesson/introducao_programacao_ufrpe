import numpy as np
import os
import time

# --- Funções de Utilitários ---

def limpar_tela():
    """Limpa a tela do terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo: str):
    """Exibe um cabeçalho estilizado."""
    print("\n" + "=" * 50)
    print(f"--- {titulo.upper()} ---".center(50))
    print("=" * 50 + "\n")

# --- Funções de Configuração (Menu) ---

def definir_jogador(simbolo: str, jogadores: dict, placar: dict):
    """Permite ao usuário definir o nome de um jogador."""
    nome_antigo = jogadores[simbolo]
    novo_nome = input(f"Digite o nome do Jogador {simbolo}: ").strip()
    if not novo_nome:
        print("\nNome não pode ser vazio. Mantendo nome atual.")
        return
        
    jogadores[simbolo] = novo_nome
    
    if nome_antigo in placar:
        pontuacao = placar.pop(nome_antigo)
        placar[novo_nome] = pontuacao
    else:
        placar[novo_nome] = 0
        
    print(f"\nJogador {simbolo} definido como: {novo_nome}")

def definir_tamanho_tabuleiro() -> int:
    """Solicita e valida o tamanho do tabuleiro."""
    while True:
        try:
            tamanho = int(input("Digite o tamanho do tabuleiro (ex: 3 para 3x3, mínimo 2): "))
            if tamanho >= 2:
                return tamanho
            else:
                print("\n*Erro: O tamanho mínimo do tabuleiro é 2.*")
        except ValueError:
            print("\n*Erro: Por favor, digite um número inteiro válido.*")

def definir_tamanho_sequencia(tamanho_tabuleiro: int) -> int:
    """Solicita e valida o tamanho da sequência para vitória."""
    while True:
        try:
            sequencia = int(input(f"Digite o tamanho da sequência para vencer (mínimo 2): "))
            if sequencia >= 2:
                return sequencia
            else:
                print(f"\n*Erro: A sequência deve ser de no mínimo 2.*")
        except ValueError:
            print("\n*Erro: Por favor, digite um número inteiro válido.*")

# --- Funções do Jogo ---

def exibir_placar(placar: dict):
    """Mostra o placar atual do jogo."""
    exibir_cabecalho("Placar")
    if not placar:
        print("Nenhum jogador definido ainda.")
    else:
        for jogador, vitorias in placar.items():
            print(f"  {jogador}: {vitorias} vitórias")
    print("\n" + "-"*50)
    input("\nPressione Enter para continuar...")

def inicializar_tabuleiro(tamanho: int) -> np.ndarray:
    """Cria a matriz NumPy que representa o tabuleiro."""
    return np.full((tamanho, tamanho), ' ', dtype=str)

def exibir_tabuleiro(tabuleiro: np.ndarray):
    """Exibe o tabuleiro do jogo com índices de letra e número."""
    tamanho = tabuleiro.shape[0]
    
    print("    " + "   ".join([f"{i}" for i in range(tamanho)]))
    print("  " + "----" * tamanho)

    for i in range(tamanho):
        letra_linha = chr(ord('A') + i)
        print(f"{letra_linha} |", end="")
        for j in range(tamanho):
            print(f" {tabuleiro[i, j]} ", end="|")
        print()
    print("\n")

def solicitar_jogada(jogador: str, tabuleiro: np.ndarray) -> tuple:
    """Solicita a jogada, valida e retorna como uma tupla."""
    tamanho = tabuleiro.shape[0]
    limite_letra = chr(ord('A') + tamanho - 1)

    while True:
        jogada_str = input(f"{jogador}, escolha sua jogada (letra e número, ex: A 0): ").strip().upper()
        try:
            partes = jogada_str.split()
            if len(partes) != 2:
                raise ValueError("Formato incorreto. Use letra e número.")

            letra, numero_str = partes
            if len(letra) != 1 or not 'A' <= letra <= limite_letra:
                raise ValueError(f"Letra da linha inválida. Use de 'A' a '{limite_letra}'.")

            linha = ord(letra) - ord('A')
            coluna = int(numero_str)

            if not (0 <= coluna < tamanho):
                raise ValueError(f"Número da coluna inválido. Use de 0 a {tamanho - 1}.")
            
            jogada_tupla = (linha, coluna)

            if tabuleiro[jogada_tupla] != ' ':
                print("\n*Erro: Posição já ocupada! Tente outra.*\n")
            else:
                return jogada_tupla
        except ValueError as e:
            print(f"\n*Erro: {e} Tente novamente.*\n")


def verificar_vitoria(tabuleiro: np.ndarray, simbolo: str, sequencia: int) -> bool:
    """Verifica se existe uma sequência do tamanho definido em qualquer direção."""
    tamanho = tabuleiro.shape[0]
    for r in range(tamanho):
        for c in range(tamanho):
            if tabuleiro[r, c] == simbolo:
                # Horizontal
                if c + sequencia <= tamanho and all(tabuleiro[r, c+i] == simbolo for i in range(sequencia)):
                    return True
                # Vertical
                if r + sequencia <= tamanho and all(tabuleiro[r+i, c] == simbolo for i in range(sequencia)):
                    return True
                # Diagonal (principal \)
                if r + sequencia <= tamanho and c + sequencia <= tamanho and all(tabuleiro[r+i, c+i] == simbolo for i in range(sequencia)):
                    return True
                # Diagonal (secundária /)
                if r + sequencia <= tamanho and c - sequencia + 1 >= 0 and all(tabuleiro[r+i, c-i] == simbolo for i in range(sequencia)):
                    return True
    return False

def verificar_empate(tabuleiro: np.ndarray) -> bool:
    """Verifica se o jogo empatou."""
    return not np.any(tabuleiro == ' ')

def iniciar_partida(jogadores: dict, placar: dict, tamanho: int, sequencia: int):
    """Gerencia o fluxo de uma única partida."""
    limpar_tela()
    exibir_cabecalho("Nova Partida")
    
    tabuleiro_jogo = inicializar_tabuleiro(tamanho)
    simbolos = {'X': jogadores['X'], 'O': jogadores['O']}
    jogador_atual_simbolo = 'X'
    
    while True:
        exibir_tabuleiro(tabuleiro_jogo)
        
        jogador_atual_nome = simbolos[jogador_atual_simbolo]
        
        jogada = solicitar_jogada(jogador_atual_nome, tabuleiro_jogo)
        tabuleiro_jogo[jogada] = jogador_atual_simbolo
        
        limpar_tela()
        exibir_cabecalho(f"Partida - {tamanho}x{tamanho}")

        if verificar_vitoria(tabuleiro_jogo, jogador_atual_simbolo, sequencia):
            exibir_tabuleiro(tabuleiro_jogo)
            print(f"🎉 {jogador_atual_nome} venceu! 🎉\n")
            placar[jogador_atual_nome] += 1
            break
            
        if verificar_empate(tabuleiro_jogo):
            exibir_tabuleiro(tabuleiro_jogo)
            print("🤝 DEU VELHA! O jogo terminou em empate. 🤝\n")
            break
            
        jogador_atual_simbolo = 'O' if jogador_atual_simbolo == 'X' else 'X'
        
    input("Pressione Enter para continuar...")

def main():
    """Função principal que gerencia o menu e o estado do jogo."""
    jogadores = {'X': 'Jogador 1', 'O': 'Jogador 2'}
    placar = {'Jogador 1': 0, 'Jogador 2': 0}
    tamanho_tabuleiro = 3 
    tamanho_sequencia = 3
    
    while True:
        limpar_tela()
        exibir_cabecalho("Jogo da Velha Configurável")
        print(f"Configurações Atuais: Tabuleiro {tamanho_tabuleiro}x{tamanho_tabuleiro}, Sequência para vencer: {tamanho_sequencia}")
        print("-" * 50)
        print("Menu:")
        print(f"1. Definir jogador X (Atual: {jogadores['X']})")
        print(f"2. Definir jogador O (Atual: {jogadores['O']})")
        print("3. Definir tamanho do tabuleiro")
        print("4. Definir tamanho da sequência")
        print("5. Mostrar placar")
        print("6. Iniciar novo jogo")
        print("7. Sair do jogo")
        
        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == '1':
            definir_jogador('X', jogadores, placar)
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == '2':
            definir_jogador('O', jogadores, placar)
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == '3':
            tamanho_tabuleiro = definir_tamanho_tabuleiro()
            # Aviso: agora a sequência pode ser maior que o tabuleiro, tornando o jogo impossível de ganhar.
            # O usuário precisará redefinir a sequência manualmente se quiser uma partida jogável.
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == '4':
            tamanho_sequencia = definir_tamanho_sequencia(tamanho_tabuleiro)
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == '5':
            exibir_placar(placar)
        elif escolha == '6':
            iniciar_partida(jogadores, placar, tamanho_tabuleiro, tamanho_sequencia)
        elif escolha == '7':
            limpar_tela()
            print("\nObrigado por jogar! 👋\n")
            break
        else:
            print("\n*Opção inválida. Por favor, tente novamente.*")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
