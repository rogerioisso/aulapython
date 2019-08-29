verificacao = True


while verificacao != False:
    numero = int(input("Digite um numero de 1 a 5"))

    if numero == 1:
        verificacao = False
        print("Um")
    elif numero == 2:
        verificacao = False
        print("Dois")
    elif numero == 3:
        verificacao = False
        print("Tres")
    elif numero == 4:
        verificacao = False
        print("Quatro")
    elif numero == 5:
        verificacao = False
        print("Cinco")
    else:

        print("Numero invalido")