from itertools import count
from unicodedata import decimal


s = '        Curso em Vídeo Python     '
r= s.replace('python', 'C#')
r1 = s.lstrip()
print(r1)

print(s.split())

s1 = s.split()
print(s1)

nome = input("digite o nome:    ")

""" maiuscula = nome.upper()
print(maiuscula)
minuscula = nome.lower()
print(minuscula)
sem_espaco =(nome.split(' '))
junta = ''.join(sem_espaco)
print(len(junta))
m = []
m = nome.split(' ')
first_name = m[0]
print(len(first_name))

numero = input("digite um numero de 4 digitos:  ")



def unidades(n):
    i={
        0:'milhar',
        1:'centena',
        2:'dezena',
        3:'unidade'
    }
    s = 'milhar: ' + n[0] + '\n centena: '+ n[1] + '\n dezena: ' + n[2] + '\n unidade: ' + n[3]
    return s

print(unidades(numero)) """

s = nome.split(' ')
""" if(s[0] == 'SANTO'):
    print('começa com santo')
else:
    print('nao comeca com santo')
 """
""" if('SILVA' in nome):
    print('tem silva') """

print(nome.count('A'))
print(nome.rfind('A'))

print(s[0])
print(s[-1])


