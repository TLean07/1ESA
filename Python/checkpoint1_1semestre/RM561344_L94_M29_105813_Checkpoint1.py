nome = input("Qual é o seu nome?")
print(f"Olá {nome}, sejá bem-vindo a nossa vinheira!")

endereco = input("Qual é o seu endereço?")
nascimento = int(input("Qual é o seu ano de nascimento?"))

if nascimento >= 2008:
    print("Não é permitida a venda de bebidas alcoolicas")
else:
    print("Quais desse vinhos você quer comprar? (Apenas pode escolher um tipo de vinho)")
    print("1 - Vinho Branco - 80 R$")
    print("2 - Vinho Tradicional - 70 R$")
    print("3 - Vinho Rose - 85 R$")
    escolha = int(input("Escolha qual desses vinhos você quer pelo número: "))
    if escolha == 1:
        preco = 80
        print(f"Você escolheu o Vinho Branco que custa: R$ {preco}")
        quantidade = int(input("Quantas garrafas você quer comprar? "))
        valorfinal = quantidade * preco
        if valorfinal <= 100:
            print("Frete Gratis")
            frete = 0
        else:
            print("Você pagará frete de R$ 20")
            frete = 20
    elif escolha == 2:
        preco = 70
        print(f"Você escolheu o Vinho Tradicional que custa: R$ {preco}")
        quantidade = int(input("Quantas garrafas você quer comprar? "))
        valorfinal = quantidade * preco
        if valorfinal <= 100:
            print("Frete Gratis")
            frete = 0
        else:
            print("Você pagará frete de R$ 20")
            frete = 20
    elif escolha == 3:
        preco = 85
        print(f"Você escolheu o Vinho Rose que custa: R$ {preco}")
        quantidade = int(input("Quantas garrafas você quer comprar? "))
        valorfinal = quantidade * preco
        if valorfinal <= 100:
            print("Frete Gratis")
            frete = 0
        else:
            print("Você pagará frete de R$ 20")
            frete = 20
    else:
        print("Opção de vinho invalida")

    print(f"Sua compra tem um valor de R$ {valorfinal + frete}, muito obrigado por comprar em nossa vinheira!")










