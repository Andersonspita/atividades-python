codigo = int(input('Digite o código funcional: '))
salario = float(input('Informe o salário: '))
nome = input('Digite o nome do funcionário: ')
ativo = True

tipo = type(salario)

print('Código: %d'% codigo)
print('Nome: %s'% nome)
print('Salário: %.2f'% salario)
print('Ativo: %r'% ativo)
