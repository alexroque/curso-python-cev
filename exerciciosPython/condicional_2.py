from datetime import datetime
from random import random, randrange
from time import sleep
from xmlrpc.client import DateTime

""" salario = float(input('Digite seu salario:  '))
valor_casa = float(input('Digite o valor da casa:   '))
parcelas = int(input('Digite o valor das parcelas:  '))

prestacao = valor_casa / parcelas
pagamento = salario * 0.3

if(prestacao>pagamento):
    print('O valor da parcela excede o salario')
else: 
    print('pode comprar tranquilo') """

""" n = int(input('Digite um numero:  '))
base = input('escolha a base para a conversão  ')

if(base == 'b'):
    print(str(bin(n)))
elif(base == 'o'):
    print(str(oct(n)))
else:
    print(str(hex(n)))

 """

""" ano = int(input('digite o ano do seu nascimento:   '))
data_hoje = datetime.date.today()
dif = (data_hoje.year) - ano
print(dif)
 """
""" ano = int(input('Digite o ano de nascimento:  '))
hoje = datetime.date.today()
dif = hoje.year - ano

if(dif < 10):
    print('mirim')
elif(dif < 15):
    print('infantil')
elif(dif < 20):
    print('junior')
elif(dif < 21):
    print('senior')
else:
    print('master') """
resp = 's'
while(resp == 's'):
    
    """  print("="*20+" Triangulo "+"="*20)

    seg1 = int(input("Digite o primeiro segmento: "))
    seg2 = int(input("Digite o segundo segmento:  "))
    seg3 = int(input("Digite o terceiro segmento:  "))

    if(seg1<(seg2+seg3)):
        print("1")
        if(seg2<(seg1+seg3)):
            print("2")
            if(seg3<(seg1+seg2)):
                print("entrou no print")
                if(seg1 == seg2 == seg3):
                    print('equilatero')
                elif(seg1 == seg2 or seg2 == seg3 or seg1 == seg3):
                    print('isosceles')
                else:
                    print('escaleno')

    """
    """ peso = int(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    imc = peso/(altura**2)
    print(imc)
    """
    """ jokempo = input("Escolha pedra papel ou tesoura: 1 2 ou 3:   ")

    computador = randrange(1,3)
    """
    """ indice = int(input("digite o tempo do loop:   "))
    comeco = -1
    for i in range(indice,comeco, -1):
        sleep(1)
        print(i)

    print("dkdskjkdfkgjjfkdljkgfdkl")
    """
    """ for n in range(2,51, 2):
        print(n) """
    """ soma = 0
    for n in range(1,500,2):

        if((n%3) == 0):
            soma += n

    print(soma) """
    """ soma = 0
    for n in range(6):
        m = int(input("Digite um numero:   "))
        if(m%2 == 0):
            soma += m

    print(soma) """

    """print("-="*20 + "   progressao aritmetica    "+"-="*20)

     p = int(input("digite o primeiro termo:  "))
    r = int(input("Digite a razão:  "))

    soma = p
    print(soma)
    for n in range(9):
        soma += r
        print(soma) """

    """  print("-="*20 + "   primo    "+"-="*20)

    n = int(input("Digite um numero:  "))
    flag = True
    for i in range(2, n):
        print(str(i)+'----'+str(n))
        if(n%i == 0):
            flag = False
            break

    if(flag == True):
        print("É primo")
    else:
        print(" Não é primo") """

    """ print("-="*20 + "   Palíndromo    "+"-="*20)

    frase = input("digite a frase:    ")
    p = frase.split()
    refeito = ''.join(p)
    soma = refeito[::-1]

    for i in range(len(refeito)-1,-1,-1):
        soma += refeito[i]
    if(refeito == soma):
        print("é um palindromo")
    else:
        print("Não é um palindromo")
    print(soma) """

    """ print("-="*20 + "   Maioridade    "+"-="*20)

    idades = []
    for i in range(5):
        idades.append(int(input("Digite a idade")))
    
    hoje = datetime.today().year
    
    print(hoje)

    for i in range(len(idades)):
        print(hoje-idades[i]) """

    """  print("-="*20 + "   Maior e menor da sequencia    "+"-="*20)

    maior_valor= 0.0
    menor_valor= 0.0
    for i in range(5):
        peso = float(input("Digite o Peso:  "))
        if(i==0.0):
            menor_valor = maior_valor = peso
        if(peso < menor_valor):
            menor_valor = peso
        if(peso > maior_valor):
            maior_valor = peso

    print("O maior peso é {} e o menor peso é {}" .format(maior_valor, menor_valor))"""
    
    print("-="*20 + "   Analisador completo    "+"-="*20)

    media = 0
    homem_velho = ""
    idade_velho = 0
    mulheres = 0
    soma = 0
    for p in range(4):
        nome = input("Nome:  ") 
        idade = int(input("Idade: "))
        sexo = input("Sexo:  ")
        soma += idade
        if(sexo == "F" and idade < 20):
            mulheres += 1

        if(idade > idade_velho and sexo == "M"):
            idade_velho = idade
            homem_velho = nome
        
    media = soma/4
    print("A média de idade do grupo é {} " .format(media))
    print("O homem mais velho tem {} anos e se chama {} " .format(idade_velho, homem_velho))
    print("Ao todo são {} mulheres com menos de 20 anos" .format(mulheres))

    resp = input("Quer continuar?: ")
    