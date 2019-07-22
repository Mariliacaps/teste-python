n=int(input("Tabuada de: "))
inicio=int(input("De: "))
fim=int(input("Até: "))
x=inicio
while x<=fim:
    print("%d x %d = %d" %(n,x,n*x))
    x=x+1