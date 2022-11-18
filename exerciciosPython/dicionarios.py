from datetime import datetime
from random import randrange
from time import sleep
from operator import itemgetter

""" estado = dict()
brasil = list()

for i in range(0,3):
    estado['uf'] = input("Digite unidade federativa:  ")
    estado['sigla'] = input("Digite a sigla:  ")
    brasil.append(estado.copy())

print(brasil)"""

""" aluno = {} 

aluno['nome'] = input("Digite o nome:  ")
aluno['media'] = int(input("media  "))

print(f' nome = {aluno["nome"]}')
print(f' a media = {aluno["media"]}')
if(aluno['media'] >= 7):
    print("aprovado")
else:
    print("reprovado") """

""" print('='*20 + 'numeros aleatorios' +'='*20)

jogadores = {'jogador1': randrange(1,7), 'jogador2' : randrange(1,7), 'jogador3' : randrange(1,7), 'jogador4' : randrange(1,7)}
ranking = []
for k, v in jogadores.items():
    print(f"jogador {k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i} lugar : {v[0]} com {v[1]}')
    sleep(1) """

""" print('='*20 + 'Cadastro funcionario' +'='*20)

funcionario = {}
funcionario['nome'] = input("Digite o nome do funcionario:  ")
nascimento = int(input("Digite o ano de nascimento do funcionario:  "))
funcionario['idade'] = datetime.now().year - nascimento
resposta = input("Tem carteira de trabalho? : 0 não tem ")
if(resposta != '0'):
    funcionario['carteira'] = resposta
    funcionario['contratacao'] = int(input("Digite o ano de contratação:  "))
    funcionario['salario'] = float(input("digite o salario:   "))

for k, v in funcionario.items():
    print(f'{k} tem o valor de {v}') """

print('='*20 + 'Aproveitamento jogador' +'='*20)

aproveitamento = dict()

aproveitamento['nome'] = input("Digite o nome do jogador:  ")
aproveitamento['partidas'] = int(input("Digite o numero de partidas que jogou:  "))
gols = list()

for indice in range(0,aproveitamento['partidas']):
    gols.append(int(input(f"digite a quantidade de gols que marcou no jogo {indice}:  ")))

aproveitamento['gols'] = gols
total_gols = 0

for gol in gols:
    total_gols += gol
print(aproveitamento)
print(total_gols)






