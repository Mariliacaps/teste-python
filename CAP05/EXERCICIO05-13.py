divida=float(input("Valor da dívida: "))
taxa=float(input("Taxa de juros mensal (Ex.: 3 para 3%):"))
pagamento=float(input("Valor a ser pago mensal: "))
mes=1
if (divida*(taxa/100)>= pagamento):
    print("O juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pago=0
    while saldo>pagamento:
        juros=saldo*taxa/100
        saldo=saldo+juros-pagamento
        juros_pago=juros_pago+juros
        print ("Saldo da dívida do mês %d é de R$%6.2f."%(mes,saldo))
        mes=mes+1
print("Para pagar a divida de R$%8.2f, a %5.2f %% de juros,"%(divida,taxa))
print("Você precisa de %d meses, pagando R$%8.2f de juros."%(mes-1, juros_pago))
print("No ultimo mês, você teria um saldo de R$%8.2f a pagar." %(saldo))