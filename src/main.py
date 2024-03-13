
import random
import time
from colorama import Back

def saudacao():
    """
    Função para exibir a saudação inicial e obter o nome do jogador.
    """
    print("------------------------------------------------------------------------")
    nome_jogador = input(Back.LIGHTBLACK_EX + "Olá! Bem-vindo(a) ao Advinhe o número!\nPor favor, digite seu nome: ")
    print(Back.LIGHTBLACK_EX + f"Olá, {nome_jogador}! Vamos testar suas habilidades em adivinhar números! 🎮🔮")
    print("-------------------------------------------------------------------------")
    return nome_jogador

def turno_jogador(nome_jogador):
    """
    Função para o turno do jogador humano.
    """
    print(Back.LIGHTWHITE_EX + f"\n====== {nome_jogador}, é a sua vez! ======")
    return int(input("Digite um número entre 1 e 100: "))

def turno_computador(baixo, alto):
    """
    Função para o turno do computador.
    """
    print(Back.LIGHTBLACK_EX + f"\n====== Vez do Computador! ======")
    palpite_computador = (baixo + alto) // 2
    print(f"O computador está palpitando: {palpite_computador}")
    return palpite_computador

def exibir_suposicoes(jogador, suposicoes):
    """
    Função para exibir as suposições do jogador.
    """
    print(Back.LIGHTBLACK_EX + f"Suposições do(a) {jogador}: {suposicoes}")

def verificar_vencedor(nome_jogador, numero_secreto, palpite, suposicoes):
    """
    Função para verificar o vencedor do jogo.
    """
    if palpite == numero_secreto:
        print(f"\nParabéns, {nome_jogador}! Você acertou! O número era: {numero_secreto}\n")
        time.sleep(0.5)
        return True
    elif palpite < numero_secreto:
        print(f"{nome_jogador}, seu palpite é menor que o número secreto. Tente novamente!")
        time.sleep(0.5)
    else:
        print(f"{nome_jogador}, seu palpite é maior que o número secreto. Tente novamente!")
        time.sleep(0.5)
    suposicoes.append(palpite)
    return False

def jogar_novamente():
    """
    Função para perguntar ao jogador se deseja jogar novamente.
    """
    return input("\nGostaria de jogar novamente? (s/n): ").lower() == 's'

def jogo_adivinhacao():
    """
    Função principal para iniciar o jogo de adivinhação.
    """
    nome_jogador = saudacao()

    while True:
        numero_secreto = random.randint(1, 100)

        suposicoes_jogador = []
        suposicoes_computador = []
        baixo, alto = 1, 100  # Intervalo inicial

        while True:
            palpite_jogador = turno_jogador(nome_jogador)
            if verificar_vencedor(nome_jogador, numero_secreto, palpite_jogador, suposicoes_jogador):
                break

            palpite_computador = turno_computador(baixo, alto)
            if verificar_vencedor("Computador", numero_secreto, palpite_computador, suposicoes_computador):
                break

            # Ajuste do intervalo com base no palpite do computador
            if palpite_computador < numero_secreto:
                baixo = palpite_computador + 1
            else:
                alto = palpite_computador - 1

        # Exibição das suposições dos jogadores
        exibir_suposicoes(nome_jogador, suposicoes_jogador)
        exibir_suposicoes("Computador", suposicoes_computador)

        # Finalizar o jogo
        if not jogar_novamente():
            print("\n-----------------------------------------------------------------------")
            print(f" Obrigado por jogar, {nome_jogador}! Esperamos que tenha se divertido. ")
            print(" Até a próxima!    ｡◕‿◕｡     🔮🎲🎮                      ")
            print("-----------------------------------------------------------------------")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
