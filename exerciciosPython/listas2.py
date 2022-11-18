from random import randrange
from time import sleep
""" print('='*20 + 'Pessoas mais pesadas' +'='*20)

pessoas = []
qtde_pessoas = 0
while True:
    pessoa = []
    pessoa.append(input("Digite o nome:  "))
    pessoa.append(int(input("Digite o peso:  ")))
    qtde_pessoas += 1
    pessoas.append(pessoa)

    if(input("Quer continuar:  ") != 's'):
        break
print(f"Ao todo vc cadastrou {len(pessoas)} pessoas.")
pesada = []
leve = []
for p in pessoas:
    if(p[1] > 70):
        pesada.append(p[0])
    else:
        leve.append(p[0])
print(pesada)
print(leve) """

""" print('='*20 + 'Lista de numeros pares e impares' +'='*20)

numeros = []
for n in range(0,7):
    numeros.append(int(input("Digite o numero:  ")))

par = list()
impar = list()

for numero in numeros:
    if(numero%2 == 0):
        par.append(numero)
    else:
        impar.append(numero)

print(sorted(par))
print(sorted(impar)) """

""" print('='*20 + 'Matriz 3x3' +'='*20) """
""" matriz1 = []
matriz2 = []
matriz3 = []
for x in range(0,3):
    matriz1.append(int(input("Digite os numeros da primeira linha:  ")))
print(matriz1)
for x in range(0,3):
    matriz2.append(int(input("Digite os numeros da segunda linha:  ")))
print(matriz2)
for x in range(0,3):
    matriz3.append(int(input("Digite os numeros da terceira linha:  ")))
print(matriz3)

for elemento in matriz1:
    print(elemento, end='')

for elemento in matriz2:
    print(elemento, end='')

for elemento in matriz3:
    print(elemento, end='') """

""" matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (input(f"Digite um valor para: [{l}] [{c}]:   "))

for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end='')
    print() """

""" matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}] [{c}]:  "))
soma = 0
terceira_coluna = 0
segunda_linha = 0
for l in range(0,3):
    for c in range(0,3):
        if(matriz[l][c]%2 == 0):
            soma += matriz[l][c]
        if(c == 2 ):
            terceira_coluna += matriz[l][c]
        if(l == 1):
            segunda_linha += matriz[l][c]

print(f'A soma dos valores pares é {soma}')
print(f'A soma da terceira coluna é {terceira_coluna}')
print(f'A soma da seguna linha é {segunda_linha}') """
    
""" print('='*20 + 'megasena' +'='*20)

numero = int(input("Digite quantos jogos irá fazer:  "))
jogos = []
for indice in range(0,numero):
    jogo = []
    for i in range(0,6):
        
        while True:
            n = randrange(1,61)
            if(n not in jogo):
                jogo.append(n)
                break
    sleep(3)
    print(jogo) """

print('='*20 + 'lista composta' +'='*20)


sala = []

while True:
    pessoa = []
    pessoa.append(input("Digite o nome:  "))
    notas = []
    for indice in range(0,2):
        notas.append(int(input("Digite a nota:  ")))
    pessoa.append(notas)
    sala.append(pessoa)
    if(input("quer continuar") != 's'):
        break 
for p in sala:
    print(p, end='')
while True:
    n = int(input('Quer mostras as notas de qual aluno?   '))
    print(sala[n])
    s = input('quer continuar:  ')
    if(s != 's'):
        break
