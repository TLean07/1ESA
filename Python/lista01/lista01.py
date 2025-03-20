#1
valor1 = float(input("Digite o Primero Valor: "))
valor2 = float(input("Digite o Segundo Valor: "))

if valor1 == valor2:
    print("Valores são iguais, tente novamente.")
else:
    if valor1 > valor2:
        print(f"O primeiro valor: {valor1} é maior que o segundo valor: {valor2}")
    else:
        print(f"O segundo valor: {valor2} é maior que o primeiro valor: {valor1}")

#2
ano = int(input("Qual ano você nasceu? "))

if ano <= 2009:
    print("Você pode votar esse ano.")
else:
    print("Você não pode votar esse ano.")

#3
senha = float(input("Digite a senha: "))
senha1 = 1234

if senha == senha1:
    print("Senha certa, acesso liberado")
else:
    print("Senha errada, acesso negado ")

#4
quantidade = int(input("Digite a quantidade de maçãs compradas: "))

if quantidade < 12:
    preco = 0.30
else:
    preco = 0.25

total = quantidade * preco
print(f"O Preço total da compra é: R$ {total:.2f}")

#5
num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva um número: "))
num3 = int(input("Escreva um número: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        menor, meio, maior = num1, num2, num3
    else:
        menor, meio, maior = num1, num3, num2
elif num2 < num1 and num2 < num3:
    if num1 < num3
        menor, meio, maior = num2, num1, num3
    else:
        menor, meio, maior = num2, num3, num1
else:
    if num1 < num2:
        menor, meio, maior = num3, num1, num2
    else:
        menor, meio, maior = num3, num2, num1
print(f"Ordem crescente é: {menor}, {meio}, {maior}")