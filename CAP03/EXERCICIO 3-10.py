salario=float(input("Digite seu salario: "))
p_aumento=float(input("Digite a porcentagem de aumento: "))
calc_aumento= salario*p_aumento/100
novo_salario=salario+calc_aumento
print("um aumento de %5.2f %% em um salario de R$ %7.2f" %(p_aumento,salario))
print("é igual a um aumento de R$ %7.2f" %calc_aumento)
print("Resultado em um novo salario é: R$ %7.2f" %novo_salario)