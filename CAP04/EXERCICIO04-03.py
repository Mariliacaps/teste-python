numero01=int(input("Digite o primeiro valor:"))
numero02=int(input("Digite o segundo valor:"))
numero03=int(input("Digite o terceiro valor:"))
maior = numero01
if numero02 > numero01 and numero02 > numero03:
    maior = numero02
if numero03 > numero01 and numero03 > numero02:
    maior = numero03
menor = numero01
if numero02 < numero03 and numero02 < numero01:
    menor = numero02
if numero03 < numero02 and numero03 < numero01:
    menor = numero03
print("O menor número digitado foi %d" % menor)
print("O maior número digitado foi %d" % maior)