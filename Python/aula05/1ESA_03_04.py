# Maior, Meio, Menor
'''a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a

if b < menor:
    menor = b
if c < menor:
    menor = c

meio = a + b + c - maior - menor

print(maior, meio, menor)'''

# Resolução
'''a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
print(a,b,c)
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)
if b > c:
    aux = b
    b = c
    c = aux
print(a,b,c)
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)'''
'''
#7 & 8
numlados = int(input("Escreva o número de lados: "))
medida = int(input("medida do lado (em cm): "))

if numlados < 3:
    print("Isso não é um polígono")
elif numlados == 3:
    perimetro = medida * numlados
    area = medida * medida / 2
    print(f"Triângulo - Perímetro: {perimetro:.2f} cm - Área: {area:.2f} cm²")
elif numlados == 4:
    perimetro = medida * numlados
    area = medida * medida
    print(f"Quadrado - Perímetro: {perimetro:.2f} cm - Área: {area:.2f} cm²")
elif numlados == 5:
    perimetro = medida * numlados
    area = (medida * medida / 2) * 5
    print(f"Pentágono - Perímetro: {perimetro:.2f} cm Área: {area:.2f} cm²")
else:
    print("Polígono não identificado")
'''
'''
#9
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c

print(maior)'''

numlados = int(input("Escreva o número de lados: "))
medida = int(input("Medida do lado (em cm): "))
perimetro = numlados * medida

if numlados < 3:
    print("Isso não é um polígono")
elif numlados == 3:
    area = (medida ** 2) / 2
    poligono = "Triângulo"
elif numlados == 4:
    area = medida ** 2
    poligono = "Quadrado"
elif numlados == 5:
    area = (medida ** 2 / 2) * 5
    poligono = "Pentágono"
else:
    print("Polígono não identificado")
    poligono = None
    area = None

if poligono:
    print(f"Seu polígono é um {poligono}, seu perímetro é: {perimetro:.2f} cm e sua área é: {area:.2f} cm²")

