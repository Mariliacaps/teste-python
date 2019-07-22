deposito=float(input("Depósito inicial: "))
investimento=float(input("Depósito mensal: "))
taxa=float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês=1
saldo=deposito
while mês <=24:
    saldo=saldo+(saldo*(taxa/100))+investimento
    print ("Saldo do mês %d é de R$%5.2f." %(mês,saldo))
    mês=mês+1
    total_investido=deposito+investimento*24
print("O ganho obtido com os juros foi de R$%8.2f."% (saldo-total_investido))