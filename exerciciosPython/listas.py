""" print('='*20 + '5 numeros em lista'+'='*20) """

""" lista=[]
menor = 0
maior = 0
for i in range(0,5):
    n = lista.append(int(input("Digite um numero:  ")))
    print(lista)
    print(i)
    if(i == 0):
        menor = lista[i]
    if(lista[i] < menor):
        menor = lista[i]
    if(lista[i] > maior):
        maior = lista[i]

print(f"O maior valor é {maior} e está ma posição {lista.index(maior)} e o menor valor é {menor} e está ma posição {lista.index(menor)}") """
    

""" print('='*20 + 'valores unicos'+'='*20)
lista = []
while True:
    numero = (int(input("Digite um valor:  ")))
    if(numero in lista):
        print("Não vpu adicionar!!")
    else:
        lista.append(numero)
        print("Valor adicionado com sucesso!!")
    resposta = input("Quer continuar?  ")
    if(resposta != 's'):
        break

print(sorted(lista)) """

""" print('='*20 + 'Lista ordenada sem repetições'+'='*20)

lista=[]
for indice in range(0,5):
    numero = int(input("Digite um valor:  "))
    if(indice == 0):
        lista.append(numero)
        print("Adicionado no final da lista")
        print(lista)
    else:
        for i, item in enumerate(lista):
            if(lista[i] > numero):
                lista.insert((i),numero)
                print(f"adicionado na posição {i}")
                print(lista)
                break
            elif(i == len(lista)-1):
                lista.insert(i+1,numero)
                print("Adicionado no final da lista")
                print(lista)
                break """



""" print('='*20 + 'Validando Expressões'+'='*20)

expressao = input("Digite a expressão:  ")

separadores_in = []
separadores_out = []
for letra in expressao:
    
    if letra in "([{" and len(separadores_out) == 0:
        separadores_in.append(letra)
        print(separadores_in)
    else:
        if letra == ")" and separadores_in[len(separadores_in)-1] == '(':
            separadores_in.pop()
            print(f"separador ) retirado  da lista {separadores_in}")
        else:
            if letra == ")" and separadores_in[len(separadores_in)-1] == '[':
                print("Expressão inválida")
            else:
                if letra == ")" and separadores_in[len(separadores_in)-1] == '{':
                    print("Expressão inválida")
                else:
                    if letra == "]" and separadores_in[len(separadores_in)-1] == '(':
                        print("Expressão inválida")
                    else:
                        if letra == "]" and separadores_in[len(separadores_in)-1] == '[':
                            separadores_in.pop()
                            print(f"separador ] retirado  da lista {separadores_in}")
                        else:
                            if letra == "]" and separadores_in[len(separadores_in)-1] == '{':
                                print("Expressão inválida")

                            else:
                                if letra == "}" and separadores_in[len(separadores_in)-1] == '(':
                                    print("Expressão inválida")
                                else:
                                    if letra == "}" and separadores_in[len(separadores_in)-1] == '[':
                                        print("Expressão inválida")
                                    else:
                                        if letra == "}" and separadores_in[len(separadores_in)-1] == '{':
                                            separadores_in.pop()
                                            print(f'separador chaves retirado  da lista {separadores_in}')
            
    print(separadores_in) """

lista = [1,3,4,6,9]

x = lista[:]
print(lista)
print(x)
x.insert(0,8)
print(lista)
print(x)




