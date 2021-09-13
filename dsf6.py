print("{:=^40}" .format(" LOJAS PITA "))

preco = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco - (preco * 0.1)
    print("O valor total será R$ {:.2f}" .format(total))
elif opcao == 2:
    total = preco - (preco * 0.05)
    print("O valor total será R$ {:.2f}" .format(total))
elif opcao == 3:
    print("O valor total será R$ {:.2f}" .format(preco))
elif opcao == 4:
    total = preco + (preco * 0.1)
else:
    total = 0
    print("OPÇÃO INVÁLIDA - Tente novamente")