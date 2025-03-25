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
    if num1 < num3:  # Aqui foi corrigido o erro de sintaxe
        menor, meio, maior = num2, num1, num3
    else:
        menor, meio, maior = num2, num3, num1
else:
    if num1 < num2:
        menor, meio, maior = num3, num1, num2
    else:
        menor, meio, maior = num3, num2, num1

print(f"Ordem crescente é: {menor}, {meio}, {maior}")

#6
altura = float(input("Digite a altura (em metros): "))
sexo = int(input("Digite o sexo (1 para feminino, 2 para masculino): "))

if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
elif sexo == 2:
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Opção inválida! Digite 1 para feminino ou 2 para masculino.")

#7
import math

num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm): "))

if num_lados == 3:
    area = (math.sqrt(3) / 4) * (medida_lado ** 2)
    print(f"TRIÂNGULO - Área: {area:.2f} cm²")
elif num_lados == 4:
    area = medida_lado ** 2
    print(f"QUADRADO - Área: {area:.2f} cm²")
elif num_lados == 5:
    area = (5 * medida_lado ** 2)/(4 * math.tan(math.radians(36)))
    print(f"PENTÁGONO - Área: {area:.2f} cm²")

#8
import math

num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm): "))

if num_lados < 3:
    print("NÃO É UM POLÍGONO.")
elif num_lados == 3:
    area = (math.sqrt(3) / 4) * (medida_lado ** 2)
    print(f"TRIÂNGULO - Área: {area:.2f} cm²")
elif num_lados == 4:
    area = medida_lado ** 2
    print(f"QUADRADO - Área: {area:.2f} cm²")
elif num_lados == 5:
    print("PENTÁGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO.")

#9
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print(f"O maior número é: {maior}")

#10
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero: possui os 3 lados iguais.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles: possui 2 lados iguais.")
    else:
        print("Triângulo Escaleno: possui 3 lados diferentes.")
else:
    print("Os valores informados não formam um triângulo.")

#11
angulo1 = float(input("Digite o primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite o segundo ângulo do triângulo: "))
angulo3 = float(input("Digite o terceiro ângulo do triângulo: "))

if angulo1 + angulo2 + angulo3 == 180:
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Triângulo Retângulo: possui um ângulo reto (90°).")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Triângulo Obtusângulo: possui um ângulo obtuso (maior que 90°).")
    else:
        print("Triângulo Acutângulo: possui três ângulos agudos (menor que 90°).")