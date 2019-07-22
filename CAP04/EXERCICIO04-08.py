numero01=float(input("Digite o primeiro numero: "))
numero02=float(input("Digite o segundo numero: "))
operacao=input("Digite o numero da ação desejada: (+, -, * ou /): ")
if operacao=="+":
    resultado=numero01+numero02
elif operacao=="-":
    resultado=numero01-numero02
elif operacao=="*":
    resultado=numero01*numero02
elif operacao=="/":
    resultado=numero01/numero02
else:
    print("Ação invalida!")
    resultado=0
print("Resultado: ", resultado)