nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print( f"Seu nome invertido é {nome[::-1]}:")
    if ' ' in nome:
        print("seu nome contem espaços: ")
    else:
        print("Seu nome NÃO contem espaços")

        print(f"Seu nome tem {len(nome)} letras ")
        print(f"A primeira letra do seu nome é {nome[0]}")
        print(f"A ultima letra do seu nome é {nome[-1]}")

else:
    print("Desculpe, voce deixou campos vazios.")