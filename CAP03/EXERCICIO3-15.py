cigarros=int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumante=int(input("Digite a quantidade de anos como fumante: "))
reducao_minutos=anos_fumante*365*cigarros*10
#um dia tem 24*60 minutos
reducao_dia=reducao_minutos/(24*60)
print("Redução de tempo de vida em dias: %8.2f"%reducao_dia)