c1 = float(input("Digite o primeiro lado: "))
c2 = float(input("Digite o segundo lado: "))
c3 = float(input("Digite o terceiro lado: "))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print("Os lados acima FORMAM um triangulo!")
else:
    print("Os lados acima NÃO FORMAM um triângulo!")