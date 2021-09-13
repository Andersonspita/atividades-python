from random import randint
print(" PEDRA - PAPEL - TESOURA ")

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)


print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print('-=' * 11)
print("O computador escolheu {}" .format(itens[comp]))
print("O jogador escolheu {}" .format(itens[jogador]))
print('-=' * 11)
if comp == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("O jogador ganhou!")
    elif jogador == 2:
        print("O computador ganhou!!")
    else:
        print("JOGADA INVÁLIDA")
elif comp == 1:
    if jogador == 0:
        print("O computador ganhou!!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("O jogador ganhou!!")
    else:
        print("JOGADA INVÁLIDA")
elif comp == 2:
    if jogador == 0:
        print("O jogador ganhou!!")
    elif jogador == 1:
        print("O computador ganhou!!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")



