distancia=float(input("Digite a distancia que deseja percorrer em Km: "))
if distancia <=200:
    passagem=0.5*distancia
else:
    passagem=0.45*distancia
print("O valor da sua passagem será: R$%7.2f"%passagem)