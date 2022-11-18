""" lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
print (lanche[-3:-1])

for item in lanche:
    print(item)
    if(item == 'pizza'):
        break

a = ("marcelo", 2, {'rest0':'0',5:3})
b = (1,5,2)
c  =  b+a
print(len(c))
print(c.count(5))
print('index ' , c.index(5,2))
print(c)


print(len(lanche)) """




""" extenso= ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    numero = int(input("Digite um numero:  "))
    print(f'vc digitou o numero {numero} e por extenso {extenso[numero-1]}') """

""" print("-="*20 + "   bresileirao    "+"-="*20)

times = ('Corinthians','Flamengo','Palmeiras','Coritiba','Chapecoense')

for i, time in enumerate(times):
    if(i < 3):
        print(f'O {i+1} colocado é:  {time}')
for i, time in enumerate(times):
    if(i > len(time)-3):
        print(f'os ultimos colocados são: {i+1} {times[i]}')
print(sorted(times))
for i, time in enumerate(times):
    if(time == 'Chapecoense'):
        print(f'A Chapecoense está na {i+1} posição do campeonato')


print(f'os 3 primeiros colocados na tabela são: { times[:3]}')
print(f'os tre ultimos sao: {times[-3:]} ')
indice = times.index('Chapecoense')
print(f' a chp tá em : {indice}') """

from random import randrange


""" print("-="*20 + "   numeros aleatorios em tupla    "+"-="*20)

n = ( randrange(10), randrange(10), randrange(10), randrange(10), randrange(10) )
menor = min(n)
maior = max(n)

for i in n:
    print(f" {i}" , end='')
print(f"\no menor valor é {menor} e o maior valor é {maior}") """

""" print("-="*20 + "   numeros aleatorios em tupla    "+"-="*20)

tupla = (int(input("Digite um numero:  ")), int(input("Digite um numero:  ")), int(input("Digite um numero:  ")),int(input("Digite um numero:  ")))

print(f'o numero nove apareceu {tupla.count(9)}')
print(f'O primeiro numero 3 apareceu na posicao {tupla.index(3)} ')

print(tupla) """

""" print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
tupla = ('sabao', 2 ,'detergente', 98.5 , 'amaciante', 10.5 , 'bolacha', 2.5, 'pão', 0.5)

for indice in range(0, len(tupla)):
    if(indice%2 == 0):
        print(f'{tupla[indice]:.<30}', end='')
    else:
        print(f'R$ {tupla[indice]:>7.2f}')

print('-'*40) """

tupla = ('palavra', 'agosto', 'fevereiro', 'alex')

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais : ' , end='')
    for vogal in palavra:
        if(vogal in 'aeiou'):
            print(vogal, end=' ')














