velocidade=float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa=(velocidade-80)*5
    print("Você sera multado em R$%7.2f!!!"%multa)
if velocidade <= 80:
    print("Continue sendo prudente!")