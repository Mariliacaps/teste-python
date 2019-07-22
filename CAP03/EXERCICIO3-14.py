km_percorridos=float(input("Digite os kilometros percorridos: "))
dias_alugado=int(input("Quantidade de dias que o carro foi alugado: "))
aluguel=dias_alugado*60
valor_km=km_percorridos*0.15
total_aluguel=aluguel+valor_km
print("O valor a pagar por dias locado fica R$%5.2f e o valor pela quantidade de Km rodados fica R$%5.2f"%(aluguel,valor_km))
print("O total a pagar pelo aluguel do carro fica R$%5.2f" %total_aluguel)
print("Obrigada")