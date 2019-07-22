mercadoria=float(input("Digite o preço da mercadoria: "))
desconto=float(input("Digite o desconto: "))
valor_desconto=mercadoria*desconto/100
novo_preco_mercadoria=mercadoria-valor_desconto
print("O desconto é de %5.2f no valor da mercadoria, entao pagasse %5.2f" %(valor_desconto,novo_preco_mercadoria))