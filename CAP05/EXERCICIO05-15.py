#programa que controla uma maquina registradora
pagar=0
while True:
    produto=int(input("Digite o código do produto desejado (0 para sair): "))
    preco=0
    if produto==0:
        break;
    elif produto==1:
        preco=0.50
    elif produto==2:
        preco=1.00
    elif produto==3:
        preco=4.00
    elif produto==5:
        preco=7.00
    elif produto==9:
        preco=8.00
    else:
        print("Código Inválido!")
    if preco!=0:
        quantidade=int(input("Digite a quantidade comprada: "))
        pagar=pagar+(preco*quantidade)
print("Total R$%8.2f" %pagar)