consumo=int(input("Digite o kWh consumido: "))
instalacao=(input("Diga o tipo de instalação, R para residências, I para industria e C para comércios: "))
if instalacao=="R":
    if consumo<=500:
        preco=0.40
    else:
        preco=0.65
elif instalacao=="I":
    if consumo<=1000:
        preco=0.55
    else:
        preco=0.60
elif instalacao=="C":
    if consumo<=5000:
        preco=0.55
    else:
        preco=0.60
else:
    preco=0
    print("ERROR! Tipo de instalação desconhecido!")
custo=consumo*preco
print("Valor a pagar: R$ %7.2f" %custo)