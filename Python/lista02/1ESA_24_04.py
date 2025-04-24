#Exercício 1
'''
num = input("Diga um número:")
while not num.isnumeric():
    num = input("Diga um número:")
num = int(num)
while num < 0 and num > 10:  # while not num > 0 and num <= 10
    print("Número inválido!")
    num = input("Diga um número:")
'''
#Exercício 2
'''
nome = input("Diga seu nome: ")
while len(nome) < 3:
    nome = input("Diga seu nome: ")

while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
salario = input("Diga seu salário: ")
while not salario.isnumeric():
    salario = input("Diga seu salário: ")
salario = int(salario)

sexo = ("Diga f ou m:")
while sexo != 'f' and sexo != 'm':
    sexo = input("Diga f ou m: ")

e_c = input("Diga s,c,v ou d: ")
while not (e_c == 's' or e_c == 'c' or e_c == 'v' or e_c == 'd'):
    e_c = input("Diga s,c,v ou d: ")
'''

#Exercício 3
'''
a = 80
b = 200
t = 0
while a > b:
    a *= 1.03
    b *= 1.015
    t += 1
print(t)
'''
#Exercício 4
'''
i = 0 
soma = 0
while i < 5:
    nota = input(f"Diga a {i+1} nota: ")
    while not nota.isnumeric():
        nota = input(f"Diga a {i + 1} nota: ")
    nota = int(nota)
    soma += nota
    i +=  1
media = soma/i
'''
#Exercício 5
'''
a = input(f"Diga o primeiro número: ")
while not a.isnumeric():
    a = input(f"Diga o primeiro número: ")
a = int(a)

b = input(f"Diga o primeiro número: ")
while not b.isnumeric():
    b = input(f"Diga o primeiro número: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1
'''
#Exercício 6
'''
senha_cadastrada = '1234'
senha_tentativa = input("Diga sua senha: ")
tentativas = 1
while senha_cadastrada != senha_tentativa and tentativas < 3:
    print(f"Senha invalida! só mais {3 - tentativas}")
    senha_tentativa = input("Diga sua senha: ")

    if senha_tentativa == senha_cadastrada:
        print(f"Acesso liberado! Você acertou em {tentativas - 3}")
    else:
        print("Acesso Bloqueado")

usuario = input("Diga seu nome de usuário: ")
senha = input("Diga sua senha: ")
while usuario == senha:
    print("Usuario não pode ser igual a senha!")
    usuario = input("Diga seu nome de usuário: ")
    senha = input("Diga sua senha: ")
'''
#Exercício 7
'''
num = 1
while num <= 10:
    print(f"Tabuada do {num}:")
    mult = 1
    while mult <= 10:
        print(f"{num}*{mult} = {num*mult}")
        mult += 1
    print()
    num += 1
'''
#Exercício 8
'''
a = 1
b = 1
print(a,b,end=' ')
i = 2
while i <= 100:
    c = a + b
    print(c/b)
    a = b
    b = c
    i += 1
'''
#Exercício 9
'''
i = 0
pares = 0
while i < 10:
    b = input(f"Diga o {i+1} número:")
    while not b.isnumeric():
        b = input(f"Diga o {i+1} número:")
    b = int(b)
    if b%2 == 0:
        pares += 1
    i += 1
print(f"Você digitou {pares} pares e {i - pares} ímpares")

#Explicação da soma

i = 0
soma = 0
while i < 10:
    i += 1
    soma += i
print(soma)

#Fatorial Exércicio 9

i = 1
fatorial = 1
while i < 5:
    i += 1
    fatorial *= i
print(fatorial)

#Outro Método

i = 1
fatorial = 1
num = 5
produto = f"{num}!*"
while i < num:
    produto += f"{i}*"
    i += 1
    fatorial *= i
produto += f"{i} = {fatorial}"
print(produto)
'''
#Exercício 10
'''
num = 7
i = 2

while True:
    print(f"{num}%{i} = {num%i}")
    if num %i == 0:
        print("Não é primo!")
        break
    elif i >= num**(1/2):
        print("É primo")
        break
    i += 1
'''
#Exercício 11

#Exercício 12 (Ver o exercício 5)

#Exercício 13
'''
salario = 1000
ano = 1995
taxa_inicial = 0.015
while ano < 2000:
    taxa = 1 + taxa_inicial
    taxa_inicial *= 2
    salario *= taxa
    ano += 1
print(f"{salario:.2f}")
'''
#Exercício 14
