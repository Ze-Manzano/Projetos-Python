print("---------- JOGO DA ADIVINHAÇÃO ----------")
print("O computador irá gerar um valor aleatório entre 1 e 100")
print("Sua missão será adivinhar qual é esse valor enquanto o computador te dará algumas dicas")
print("-----------------------------------------")

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um numero entre 1 e 100: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Erado! Tente um valor MAIOR!\n")

    elif palpite > numero_secreto:
        print("Erado! Tente um valor MENOR!\n")

    else:
        print(f"🎉PARABÉNS, VOCÊ ACERTOU🎉!")
        print(f"Você acertou em {tentativas} tentativas!")
        break
