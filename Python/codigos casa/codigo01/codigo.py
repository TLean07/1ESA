nome = input("Qual é o seu nome? ")
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