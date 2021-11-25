import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    # Abre o arquivo txt palavras e o armazena na variável arquivo
    arquivo = open("palavras.txt", "r")

    # Cria a lista vazia palavras
    palavras = []
    # Percorre todo o arquivo
    for linha in arquivo:
        # Remove o \n da linha
        linha = linha.strip()
        # e armazena cada linha em um índicie da lista
        palavras.append(linha)

    # Fecha o arquivo
    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def solicita_chute():
    chute = input("\nQual a letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    # Contador de posição da letra na palavra
    index = 0
    # iteração em cada uma das letras da palavra secreta
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto o usuário nao "Enforcou" e não "Acertou"
    while(not enforcou and not acertou):
        # Solicita que o usuação digite a letra
        chute = solicita_chute()

        # Verifica se a letra chute existe na palavra_secreta
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        # enforcou = true, se erros == 7
        enforcou = erros == 7
        # acertou = true, se não existir "_" em letras_acertadas
        acertou = "_" not in letras_acertadas

        print("\n", letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


if(__name__ == "__main__"):
    jogar()
