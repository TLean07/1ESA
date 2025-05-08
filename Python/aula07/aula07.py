'''canditato_1 = 'Lula'
canditato_2 = 'Bolsonaro'
canditato_3 = 'Dilma'
canditato_4 = 'Temer'
brancos = 'Brancos'
nulos = 'Nulos'

votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
votos_brancos = 0
votos_nulos = 0
total = 0

while True:
    votar = input(f"Escolha:\n{canditato_1}\n{canditato_2}"
                  f"\n{canditato_3}\n{canditato_4}\n{brancos}"
                  f"\n{nulos} \n-> ")
    if not (votar == canditato_1 or votar == canditato_2 or
            votar == canditato_3 or votar == canditato_4 or
            votar == brancos or votar == nulos):
        print("Inválido")
        continue

    if votar == canditato_1:
        votos_1 += 1
    elif votar == canditato_2:
        votos_2 += 1
    elif votar == canditato_3:
        votos_3 += 1
    elif votar == canditato_4:
        votos_4 += 1
    elif votar == brancos:
        votos_brancos += 1
    else:
        votos_nulos += 1
    total += 1
    proxima = input("Quer continuar? (s/n)\n-> ")
    while not (proxima == 's' or proxima == 'n'):
        proxima = input("Quer continuar? (s/n)\n-> ")
    if proxima == 'n':
        break

print(f"{canditato_1} - {votos_1}\n{canditato_2} - {votos_2}\n"
      f"{canditato_3} - {votos_3}\n{canditato_4} - {votos_4}\n"
      f"{brancos} - {votos_brancos}\n{nulos} - {votos_nulos}\n")
print(f"Porcentagem de nulos sobre o total: {votos_nulos * 100 / total:.2f}")
print(f"Porcentagem de brancos' sobre o total: {votos_brancos * 100 / total:.2f}")'''
'''
for i in range(10):
    print(i)
    i = 0
    print(i)
'''
'''
for i in range(1,10,2):
    print(i)
'''
'''
for i in range(20,0,-2):
    print(i)
'''
'''
a = 1 
b = 1
num = int(input("qt? "))
for i in range(num):
    c = a+b
    a = b
    b = c
    print(c)
'''
