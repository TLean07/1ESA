'''
alunos = ['Luigi','Guilherme','Leandro','Vinicius']
notas = [2,6,8,5]
for i in range(len(notas)):
    if not [i]>=6:
        print(f'Os {alunos[i]} passou com {notas[i]}')
'''

# <!--------------------------------------!>

'''
def verfica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

qtd = verfica_numero("Quantos números vc vai colocar na lista?\n-> ")
print(qtd)
# ano = verfica_numero("Diga seu ano de nascimento:\n-> ")

lista = []
while len(lista) < qtd:
    num = input(f"Diga o {len(lista)+1}º número: ")
    while not num.isnumeric():
        num = input(f"Diga o {len(lista) + 1}º número: ")
    num = int(num)
    lista.append(num)
    print(lista)'''

# <!--------------------------------------!>

'''
import random

def verfica_numero(msg):
    print(msg, end='')
    numero = input(msg)
    print(numero)
    return int(numero)

qtd = verfica_numero("Quantos números você vai colocar na lista?\n-> ")
print(f"Quantidade escolhida: {qtd}")

lista = []

while len(lista) < qtd:
    num = str(random.randint(1, 1000))
    print(f"Diga o {len(lista) + 1}º número: {num}")
    lista.append(int(num))
    print(lista)'''

# <!--------------------------------------!>

'''def fora_opcao(msg,lista_opcoes):
    escolha = input(msg)
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha

vinhos = ['Pérgola','Sangue de Boi','Salton']
print('-> Nós possuimos o seguintes vinhos: Pérgola, Sangue de Boi e Salton')
vinho = fora_opcao("Qual Vinho você quer?\n-> ", vinhos)
print(f"Você escolheu o {vinho}")
opcoes = ['sim','não']
continuar = fora_opcao("Você quer continuar? [sim/não]\n-> ",opcoes)
print(f"Você disse {continuar}")'''

# <!--------------------------------------!>

'''
def acha_media(lista_numeros):
    soma = 0
    for num in lista_numeros:
        soma += num
    media = soma/len(lista_numeros)
    return media

def conta_pares(lista):
    pares = 0
    for num in lista:
        if num%2 == 0:
            pares += 1
    return pares

lista = [5,1,8,7,2,3]
print(conta_pares(lista))'''

# <!--------------------------------------!>

'''def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior
carros = ['Mustang','Up','Gol','POLINHO TURBÃO MANUAL 😈','Uno']
preco = [600,50,80,1000000,5]
local_maior = acha_maior(preco)
print(local_maior)'''

# <!--------------------------------------!>

'''def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

def acha_index(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = ['Mustang','Up','Gol','POLINHO TURBÃO MANUAL 😈','Uno']
preco = [600,50,80,1000000,5]

escolha = forca_opcao("Qual carro te interessa?", carros)
indice_escolha = acha_index(carros,escolha)
print(f"O {escolha} custa {preco[indice_escolha]}")'''

# <!--------------------------------------!>

def join(lista_str,sep):
    ajuntado = lista_str[0]
    for i in range(1,len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado

def forca_opcao(msg, lista_opcoes):
    #opcoes = '\n'.join(lista_opcoes)
    opcoes = join(lista_opcoes, '\n')
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

def acha_index(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = ['Mustang','Up','Gol','POLINHO TURBÃO MANUAL 😈','Uno']
preco = [600,50,80,1000000,5]

escolha = forca_opcao("Qual carro te interessa?", carros)
indice_escolha = acha_index(carros,escolha)
print(f"O {escolha} custa {preco[indice_escolha]}")