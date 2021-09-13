salario = float(input("Digite o salário do funcionário: "))

if salario > 1250.00:
    salarioNovo = (salario * 0.1) + salario
else:
    salarioNovo = (salario * 0.15) + salario


print("Seu novo salário é R$ {:.2f}" .format(salarioNovo))