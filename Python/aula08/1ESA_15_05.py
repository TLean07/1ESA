'''
vogais = 0
for char in 'danilo':
    if char in ['a','e','i','o','u']:
        vogais += 1
print(vogais)
for i in range(1,10,3):
    print(i)
for i in range(20,10,2):
    print(i)

for i in range(10):
    print(i)
    i = 0
    print(i)

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
    print()

i = 1
j = 1
while i < 11:
    j = 1
    print(f"Tabuada do {i}:")
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j += 1
    i += 1
    print()

lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    print(elem)
print()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    print(elem)
print()
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")


lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    elem = 1
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)
'''
'''
profs = ['Danilo','André','Gabi','Yan','Lucas','Luís']
materias = ['Python','Historinha','Sw&TX','Matemática','Edge','Front','Web']
for i in range(len(profs)):
    print(f"O/A {profs[i]} dá a materia de {materias[i]}.")
'''
'''
alunos = ['Lucas Sena','Rhariel','Sara','Isabela','Lucas Zago']
notas = [8,8.5,6,4,1]

for i in range(len(alunos)):
    if notas[i] < 6:
        print(f"O/A {alunos[i]} foi reprovado com nota {notas[i]}")
    else:
        print(f"O/A {alunos[i]} foi aprovado com nota {notas[i]}")
'''

#Exercício 1 - Contar a quantidade de numeros pares na lista
#Exercício 2 - Calcular a soma dos elementos da lista
#Exercício 3 - Calcular media dos elementos da lista

'''
numeros = [9, 7, 3, 5, 2, 1, 8, 6, 0, 4]

# Exercício 1
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1

# Exercício 2
soma = 0
for num in numeros:
    soma += num

# Exercício 3
media = soma / len(numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Soma dos elementos: {soma}")
print(f"Média dos elementos: {media:.2f}")'''

'''lista = []
lista.append(349)
print(lista)
lista.append(67)
print(lista)
lista.append(765)
print(lista)'''

'''lista = []
for i in range(10):
    num = input(f"Digite o {i+1}º número: ")
    if not num.isnumeric():
        num = input(f"Digite o {i+1}º número: ")
        continue
    num = int(num)
    lista.append(num)
    print(lista)

lista = []
for i in range(10):
    num = input(f"Digite o {i+1}º número: ")
    while not num.isnumeric():
        num = input(f"Digite o {i+1}º número: ")
    num = int(num)
    lista.append(num)
    print(lista)'''

'''lista = [7,3,8,5,2,0,9,6,10,4]
maior = lista[0]
for num in lista:
    print(f"Vou testar se {num} > {maior}")
    if num > maior:
        print(f"Deu Certo, vou trocar {maior} por {num}")
        maior = num
print(f"O maior número em lista é o {maior}")'''

'''lista = [7, 3, 8, 5, 2, 0, 9, 6, 10, 4]
maior = lista[0]
posicao_maior = 0
for i in range(len(lista)):
    print(f"Vou testar se {lista[i]} > {maior}")
    if lista[i] > maior:
        print(f"Deu Certo, vou trocar {maior} por {lista[i]}")
        maior = lista[i]
        posicao_maior = i

print(f"O maior número em lista é o {maior} e está na posição {posicao_maior}")'''

preco = [600,50,80,1000000,5]
carros = ['Mustang','Up','Gol','POLINHO TURBÃO MANUAL 😈','Uno']
indice_maior = 0
maior = preco[0]

for i in range(len(preco)):
    # print(f"Vou testar se {preco[i]} > {maior}")
    if preco[i] > maior:
        # print(f"Deu Certo, vou trocar {maior} por {preco[i]}")
        maior = preco[i]
        indice_maior = i

print(f"O carro mais caro é o {carros[indice_maior]}")
