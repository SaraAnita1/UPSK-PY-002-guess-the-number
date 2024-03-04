#print("hello World")

#msg = "Hello World"
#print(msg)

import random

def jogar_adivinhacao():
    numero_secreto = random.randint(0, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de Adivinhe o Número!")
    print("Eu escolhi um número entre 0 e 100. Tente adivinhar.")

    while True:
        # Vez do jogador
        tentativa_jogador = int(input("Digite um número entre 0 e 100: "))
        tentativas += 1

        if tentativa_jogador < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif tentativa_jogador > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

        # Vez da máquina
        tentativa_maquina = random.randint(0, 100)
        print(f"Agora é a minha vez. Eu escolho o número: {tentativa_maquina}")
        tentativas += 1

        if tentativa_maquina < numero_secreto:
            print("Meu número é muito baixo!")
        elif tentativa_maquina > numero_secreto:
            print("Meu número é muito alto!")

if __name__ == "__main__":
    jogar_adivinhacao()