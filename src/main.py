
import random
import time
from colorama import  Back

# Saudação e entrada do nome do jogador
print("------------------------------------------------------------------------")
nome_jogador = input(Back.LIGHTBLACK_EX + "Olá! Bem-vindo(a) ao Advinhe o numero!\nPor favor, digite seu nome: ")
print(Back.LIGHTBLACK_EX + f"Olá, {nome_jogador}! Vamos testar suas habilidades em adivinhar números! 🎮🔮")
print("-------------------------------------------------------------------------")

# Função para a vez do jogador humano
def turno_jogador(nome_jogador):
    print(Back.LIGHTWHITE_EX + f"\n====== {nome_jogador}, é a sua vez! ======")
    return int(input("Digite um número entre 1 e 100: "))


def turno_computador(baixo, alto):
    print(Back.LIGHTBLACK_EX + f"\n====== Vez do Computador! ======")
    palpite_computador = (baixo + alto) // 2
    print(f"O computador está palpita: {palpite_computador}")
    return palpite_computador


# Função para exibir as suposições do jogador
def exibir_suposicoes(jogador, suposicoes):
    print(Back.LIGHTBLACK_EX + f"Suposições do(a) {jogador}: {suposicoes}")

    # Função para verificar o vencedor do jogo
def verificar_vencedor(nome_jogador, numero_secreto, palpite, suposicoes):
    if palpite == numero_secreto:
        print(f"\nParabéns, {nome_jogador}! Você acertou! O número era: {numero_secreto}\n")
        time.sleep(0.5)
        return True
    elif palpite < numero_secreto:
        print(f"{nome_jogador}, seu palpite é menor que o numero secreto. Tente novamente!")
        time.sleep(0.5)
    else:
        print(f"{nome_jogador}, seu palpite é maior que o numero secreto. Tente novamente!")
        time.sleep(0.5)
    suposicoes.append(palpite)
    return False

# Função para jogar novamente
def jogar_novamente():
    return input("\nGostaria de jogar novamente? (s/n): ").lower() == 's'

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
        print("\n")
        print(f" Obrigado por jogar, {nome_jogador}! Esperamos que tenha se divertido. ")
        print(" Até a próxima!   ◖ᵔᴥᵔ◗ ♪ ♫    (｡◕‿◕｡)                            ")
        print("")
        break
# def jogar_adivinhacao():
#     numero_secreto = random.randint(0, 100)
#     tentativas = 0

#     print("Bem-vindo ao jogo de Adivinhe o Número!")
#     print("Eu escolhi um número entre 0 e 100. Tente adivinhar.")

#     while True:
#         # Vez do jogador
#         tentativa_jogador = int(input("Digite um número entre 0 e 100: "))
#         tentativas += 1

#         if tentativa_jogador < numero_secreto:
#             print("Muito baixo! Tente um número maior.")
#         elif tentativa_jogador > numero_secreto:
#             print("Muito alto! Tente um número menor.")
#         else:
#             print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
#             break

#         # Vez da máquina
#         tentativa_maquina = random.randint(0, 100)
#         print(f"Agora é a minha vez. Eu escolho o número: {tentativa_maquina}")
#         tentativas += 1

#         if tentativa_maquina < numero_secreto:
#             print("Meu número é muito baixo!")
#         elif tentativa_maquina > numero_secreto:
#             print("Meu número é muito alto!")

# if __name__ == "__main__":
#     jogar_adivinhacao()
