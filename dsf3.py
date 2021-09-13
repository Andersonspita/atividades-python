from datetime import date 

atual = date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc

if idade < 18:
    print("Ainda vai se alistar")
elif idade == 18:
    print("Hora de se alistar")
else:
    print("Passou do tempo de alistamento")