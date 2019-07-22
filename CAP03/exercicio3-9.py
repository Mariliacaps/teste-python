dias_trabalho=int(input("Digite os dias: "))
horas=int(input("Digite as horas: "))
minutos=int(input("Digite os minutos: "))
segundos=int(input("Digite os segundos: "))
#1 minuto tem 60 segundos
#1hora tem 3600(60*60)segundos
#1 dia tem 24hrs, logo 24*3600 segundos
total_em_segundos=dias_trabalho*24*3600+horas*3600+minutos*60+segundos
print("Convertido em segundos é igual a %10d segundos" %total_em_segundos)