'''
frase = "Hello World"
print(frase)
print("Hello World")
print("Hello World")
'''

'''
palavra_1 = "Olá";
palavra_2 = "Mundo";
frase = palavra_1 + " " + palavra_2;
print(frase);

frase = "Eu";
print(frase);
frase = frase + " " + "sou";
print(frase);
frase = frase + " " + "o";
print(frase);
frase = frase + " " + "Leandro";
print(frase);
'''

'''
frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("Diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("Diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("Diga a quinta palavra: ")
print(frase)

print(type("Olá Mundo"))
'''
'''
a = 2
b = 3
print(type(a))
soma = a + b
print(soma)
'''

num1 = float(input("Digite o primeiro número: "))
print(num1)
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Pontenciação")

opcao = input("Escolha a operação desejada: ")

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
        resultado = "Não é possivel dividir por 0"
        operador = "/"
elif opcao == "5":
    resultado = num1 ** num2
    operador = "**"
else:
    resultado = "Operação Invalida";
    operador = "?"

print(f"\nResultado: {num1} {operador} {num2} = {resultado}")