from random import random, randrange

""" 
aleatorio = randrange(1,11)
print(aleatorio)
n = int(input("adivinhe o numero:  "))
if(n == aleatorio):
    print("vc acertou")
else:
    print("vc errou") """

km = int(input("km por hora:  "))

if(km > 80):
    aumento = km + (km*0.10)
    multa = (km-80) * 7
    print("sua multa é: R${}" .format(multa))
else:
    print("tranquilo")

if((km%2) == 0):
    print("é par")
else:
    print("é impar")


print(aumento)