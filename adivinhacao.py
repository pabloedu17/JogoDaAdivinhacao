import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(1, 101)
numero_de_tentativas = 0
pontos = 1000

print("*************NIVEL*************")
print("(1) Facil (2) Medio (3) Dificil")
nivel = int(input("Escolha o nivel: "))

if nivel == 1:
    numero_de_tentativas = 20
elif nivel == 2:
    numero_de_tentativas = 10
else:
    numero_de_tentativas = 5

for rodada in range(1, numero_de_tentativas+1):
    print(f'Tentativa {rodada} de {numero_de_tentativas}')
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Digite um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if acertou:
        print(f'Você acertou e fez {pontos} pontos Parabéns!')
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if menor:
            print("Você errou! Chute menor que o numero secreto")
            if rodada == numero_de_tentativas:
                print(f'O numero secreto era {numero_secreto}')
                print(f'Você fez {pontos} pontos')
        elif maior:
            print("Você errou! Chute maior que o numero secreto")
            if rodada == numero_de_tentativas:
                print(f'O numero secreto era {numero_secreto}')
                print(f'Você fez {pontos} pontos')

print("Fim de jogo!")
