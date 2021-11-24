
def jogar():
    print("*********************************")
    print("******Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    # Enquanto o usuário nao "Enforcou" e não "Acertou"
    while(not enforcou and not acertou):
        # Solicita que o usuação digite a letra
        chute = input("Qual a letra? ")
        chute = chute.strip()

        # Contador de posição da letra na palavra
        index = 0

        # iteração em cada uma das letras da palavra secreta
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1


if(__name__ == "__main__"):
    jogar()
