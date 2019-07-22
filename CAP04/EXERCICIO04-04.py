salario=float(input("Digite o salario do funcionario: "))
pc_aumento= 0.15
if salario >1250:
    pc_aumento=0.10
aumento=salario*pc_aumento
print("seu novo aumento é: R$%7.2f" %aumento)