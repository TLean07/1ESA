'''nome = input("Qual é o seu nome? ")
print(f"Seja bem-vindo/a {nome} à Vinheria Agnello!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2025 - ano

if idade < 18:
    print("QUE FEIO!!! VÔ CONTA P SUA MÃE")
else:
    endereco = input("Diga seu endereço: ")
    vinho1 = 'Pérgola'
    vinho2 = 'Sangue de Boi'
    vinho3 = 'Cantinho do Vale'
    preco1 = 50
    preco2 = 30
    preco3 = 10
    escolha = input(f"Esses são nossos vinhos: \n{vinho1} - {preco1}"
                    f"\n{vinho2} - {preco2} \n{vinho3} - {preco3}"
                    f"\nQual você quer? ")
    qtd = int(input(f"Quantas garrafas de {escolha} você quer? "))
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco1 = preco2
    else:
        preco = preco3
    total = preco*qtd
    if total > 100:
        frete = 0
        print("Frete grátis!")
        valorfinal = total+frete
    else:
        frete = 10
        print("Frete de 10 reais")
        valorfinal = total+frete
    print(f"Olá {nome}, seu preço final é R$ {valorfinal}")
'''
'''i = 0
pares = 0

while i < 5:
    num - int(input(f"Diga o {i+1}° número: "))
    if num%2 == 0:
        pares = pares + 1
    print(i)
    i = i + 1
print(f"Você digitou {pares} números pares e {i} números ímpare")
'''
'''
senha_certa = '0703'
senha_fornecida = input("Digite a senha: ")
tentativas = 1

while senha_fornecida != senha_certa and tentativas < 3:
    print(f"Acesso Negado, você possui {3-tentativas} tentativas restantes")
    senha_fornecida = input("Digite a senha: ")
    tentativas = tentativas + 1

if senha_fornecida == senha_certa:
    print("Acesso Liberado")
else:
    print("Número de tentativa excedidas")
'''
'''
sexo = input("Qual é o seu sexo?(masculino/feminino)\n-> ")

while sexo != "masculino" and sexo != "feminino":
    print("Erro, escolha entre masculino ou feminino")
    sexo = input("Qual é o seu sexo?(masculino/feminino)\n-> ")
altura = float(input("Agora, qual é a sua altura?(em metros)\n-> "))
if sexo == 'masculino':
    peso = (72.7  * altura) - 58
    print(f"Esse é o seu peso ideal: {peso} KG")
else:
    peso = (62.1  * altura) - 44.7
    print(f"Esse é o seu peso ideal: {peso} KG")
'''
'''
sexo = input("Qual é o seu sexo?(masculino/feminino)\n-> ")

while not (sexo != "masculino" or sexo != "feminino"):
    print("Erro, escolha entre masculino ou feminino")
    sexo = input("Qual é o seu sexo?(masculino/feminino)\n-> ")
altura = float(input("Agora, qual é a sua altura?(em metros)\n-> "))
if sexo == 'masculino':
    peso = (72.7  * altura) - 58
    print(f"Esse é o seu peso ideal: {peso} KG")
else:
    peso = (62.1  * altura) - 44.7
    print(f"Esse é o seu peso ideal: {peso} KG")
'''
'''
numero = input("Escreva um número: ")
while not numero.isnumeric():
    print("Erro, coloque apenas números")
    numero = input("Escreva um número: ")
    numero = int(numero)
else:
    print(f"Seu número é {numero}!")
'''


