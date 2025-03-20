'''
idoso = input("Você é idoso?")
cartao = input("Você possui o cartãozinho?")

if idoso == 'sim' and cartao == 'sim':
    print("Pode estacionar")
else:
    print("Não pode estacionar")
'''

'''
idoso = input("Você é idoso?")
deficiente = input("Você é deficiente?")

if idoso == 'sim' or deficiente == 'sim':
    print("Pode estacionar")
else:
    print("Não pode estacionar")
'''

'''
letra = input("Digite uma letra:")
if letra in 'aeiou':
    print("Essa letra é uma vogal")
elif letra.isalpha():
    print("Essa letra é uma consoante")
else:
    print("Não é uma letra válida")
'''

'''
letra = input("Digite uma letra:")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é vogal.")
else:
    print(f"{letra} não é vogal.")
'''

'''
time = input("Diga para que time você torce: ")
if time == 'São Paulo':
    print('Bambi, Rebaixados dos Paulista, Não caíram no tapetinho')
elif time == 'Palmeiras':
    print('Sem Mundial, Parabéns pelo Bi da série B, Titia Leila faz o PIX, 51 é pinga, Títulos no FAX, Como que ganha 2 brasileiros no mesmo ano?')
elif time == 'Corinthians':
    print('2005 foi justo, Maior Campeão Paulista, Bi Mundial')
else:
    print('Parabéns pela série B, Baixa taxa de Natalidade, o Pelé é dahora')
'''

'''
salario = float(input("Qual é o seu sálario?"))

if salario <= 1903.98:
    print("Você não possui taxa (Cuidado com o Leão)")
elif salario > 1903.98 and salario <= 2826.65:
    taxa = (salario * 7.5/100)
    valor_final = (salario - taxa)
    print("Sua taxa será de R$ {:.2f} esse é o seu salário após a taxação: R$ {}".format(taxa, salario))
elif salario > 2826.65 and salario <= 3751.05:
    taxa = (salario * 15/100)
    valor_final = (salario - taxa)
    print("Sua taxa será de R$ {:.2f} esse é o seu salário após a taxação: R$ {}".format(taxa, salario))
elif salario > 3751.05 and salario <= 4664.68:
    taxa = (salario * 22.5/100)
    valor_final = (salario - taxa)
    print("Sua taxa será de R$ {:.2f} esse é o seu salário após a taxação: R$ {}".format(taxa, salario))
else:
    taxa = (salario * 27.5/100)
    valor_final = (salario - taxa)
    print("Sua taxa será de R$ {:.2f} esse é o seu salário após a taxação: R$ {}".format(taxa, salario))
'''

'''
nome = input("Diga se nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a) a minha calculadora.")

num1 = float(input(f"{nome} diga um número:\n "))
print(num1)
num2 = float(input(f"{nome} diga outro número:\n "))
print(num2)

print(f"\n{nome} escolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Pontenciação")

opcao = input(f"{nome} escolha a operação desejada: ")

if opcao == "1":
    resultado = num1 + num2
    operador = "+"
elif opcao == "2":
    resultado = num1 - num2
    operador = "-"
elif opcao == "3":
    resultado = num1 * num2
    operador = "*"
elif opcao == "4":
    resultado = num1 / num2
    if num2 != 0:
        resultado = num1 / num2
        operador = "/"
    else:
        resultado = f"{nome} não é possivel dividir por 0"
        operador = "/"
elif opcao == "5":
    resultado = num1 ** num2
    operador = "**"
else:
    resultado = "Operação Invalida";
    operador = "?"

print(f"\n{nome} seu resultado é: {num1} {operador} {num2} = {resultado}")
'''

