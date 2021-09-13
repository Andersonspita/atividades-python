valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
parcelas = int(input("Qual quantidade de parcelas deseja? "))

prestacaoExata = valorCasa/parcelas
prestacaoEmprestimo = salario * 0.3

if prestacaoExata <= prestacaoEmprestimo:
    print("Seu empréstimo terá parcela de valor R$ {:.2f}" .format(prestacaoExata))
else: 
    print("Seu empréstimo foi \033[1;31;42m NEGADO \033[m")
