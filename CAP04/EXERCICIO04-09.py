#Programa que calcula a aprovação de financiamento de casa
salario=float(input("Digite seu salario: "))
anos=float(input("Digite a quantidade de anos que deseja pagar: "))
preco_casa=float(input("Digite o valor da casa que deseja financiar: "))
meses=anos*12
prestacao=preco_casa/meses
if prestacao>salario*0.3:
    print("Seu financiamento foi negado!")
else:
    print("Seu financiamento foi aprovado!")