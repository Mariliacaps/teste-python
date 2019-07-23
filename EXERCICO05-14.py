s=0
digitados=0
while True:
    numero=int(input("Digite um número inteiro a somar e depois digite 0 para sair: "))
    if numero==0:
        break;
    s+=numero
    digitados=digitados+1
print("Quantidade de números digitados: %d " %digitados)
print(f"soma: {s}")
print("Média: %6.2f" %(s/digitados))