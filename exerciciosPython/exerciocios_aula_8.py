


from math import trunc,sqrt, cos, sin,tan
from random import random, randint, shuffle
import random

#n =  trunc(float(input("digite um numero real ")))
#print(n)

#co = float(input("didite o cateto oposto"))
#ca = float(input("Digite o cateto adjacente"))

#hip = sqrt((co**2)+(ca**2))
#print(hip)

""" angulo = int(input("digite o angulo  "))
cosseno = cos(angulo) 
seno = sin(angulo)
tangente = tan(angulo)
print(tangente) """
alunos = []
alunos.append('alex')
alunos.append('pedro')
alunos.append('tatiana')
alunos.append('alfredo')
n = random.choice(alunos)
print(n)

listar = shuffle(alunos)
print(alunos)



