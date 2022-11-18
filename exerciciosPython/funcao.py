from random import randint
from time import sleep
from datetime import datetime
""" print("="*20 + "Quadrado" + "="*20)

def quadrado(largura, comprimento):
    return largura*comprimento


largura = int(input("Digite a largura:  "))
comprimento = int(input("Digite o comprimento:  "))

area = quadrado(largura, comprimento)
print(f"A área de um quadrade de {largura} x {comprimento} é de {area} metros quadrados!!") """

""" def especial(t):
    
    print("~" * (len(t)+4))
    print("  " + t)
    print("~" * (len(t)+4))

print("="*20 + "Texto especial" + "="*20)

texto = input("Digite o texto:  ")
especial(texto) """

""" def contador(i,f,p):
    if(i<f):
        while i <= f:

            print(i)
            i += p
    else:
        while i >= f:

            print(i)
            i -= p


print("="*20 + "Contador" + "="*20)
inicio = 1
fim = 10

while inicio <= fim:

    print(inicio, end=' - ')
    inicio += 1
print('')
inicio = 1
fim = 10

while fim >= inicio:

    print(fim, end=' - ')
    fim -= 1

print('')
ini = int(input("Digite o inicio:  "))
fi = int(input("Digite o Fim:  "))
pas = int(input("Digite o Passo:  "))

contador(ini,fi,pas) """

""" print("="*20 + "Maior valor" + "="*20)

def maior(* num):
    maior = 0
    cont = 0
    for valor in num:
        if(valor > maior):
            maior = valor
        cont += 1
        print(f'{valor} ', end='', flush=True)
        sleep(0.8)
    print()
    print(f"o maior valor foi o {maior} dentre  {cont} valores")

#maior(6,3,7,9,4,8)
#maior(5,4,1,7)
#maior(3,9,4,6)
#maior(7,5,9)
#maior(1) """


""" print("="*20 + "sortear e somar" + "="*20)

def sorteia():
    lista = []
    qtde = randint(0,10)
    while qtde >= 0:
        lista.append(randint(0,10))
        qtde -= 1
        
    return lista


def pares(l):
    soma = 0
    for item in l:
        if(item % 2 == 0):
            soma += item
    
    print(f"Somando os valores pares de {l} temos {soma} ")


lista = []
lista = sorteia()
pares(lista) """

""" print("="*20 + "Idade de votação" + "="*20)

def vota(i):
    if(i < 16):
        return('não vota')
    elif(i < 60):
        return('voto obrigatorio')
    else:
        return('voto opcional')

idade = datetime.now().year - (int(input("Digite o ano do seu nascimento:  ")))
print(vota(idade)) """

""" print("="*20 + "Fatorial com flag" + "="*20)

def fat(nunero, show=False): """
"""
    Calcula o Fatorial de um numero
    :param numero: o numero a ser calculado
    :param show: flag p mostrar o calculo
    :return: retorna o fatorial do numero
    """
""" f = 1

    for n in range(nunero, 0, -1):
        f *= n
        if(show == True):
            print(n, end=' x ')
    return f

print(f'= {fat(4, True)}')
help(fat) """


""" print("="*20 + "parametros opcionais" + "="*20)

def jogador(j='desconhecido', g=0):
    print(f'O jogador {j} fez {g} golsno campeonato!!')


nome = input("Nome do jogador:  ")
gols = int(input("Gols do jogador:  "))
jogador(nome,gols) """

""" print("="*20 + "funcao que valida numero" + "="*20) """

""" def valida():
    while True:
        numero = input("Digite um numero válido:  ")
        if(numero.isnumeric()):
            n = int(numero)
            print(f"O numero é o {n}")
            break
        else:
            print("Esse não é um numero válido, digite novamente:  ")
        
    return numero
    
valida() """

""" print("="*20 + "Situação do aluno" + "="*20)

def notas(*args, sit=False):
    resumo = dict()
    resumo['total'] = len(args)
    resumo['maior'] = max(args)
    resumo['menor'] = min(args)
    resumo['media'] = sum(args) / len(args)
    print(resumo['total'])
    if(sit):
    
        if(resumo['media'] < 5):
            resumo['situacao'] = "ruim"
        else:
            resumo['situacao'] = "boa"

    return resumo


resp = notas(5, 8, 4, 1, sit=True)
print(resp) """





























