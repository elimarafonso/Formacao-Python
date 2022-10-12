import random
def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')




    arquivo = open("palavras.txt", "r")

    palavras = [linha.strip() for linha in arquivo]

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (True):
        print("É UMA FRUTA")
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        if erros == 6:
            break
        elif "_" not in letras_acertadas:
            break

        print(letras_acertadas)
        print("Jogando...")

    if "_" not in letras_acertadas:
        print("VOCÊ VENCEU !!!")
        print(palavra_secreta)
    else:
        print("ENFORCADO !!! ")
        print("A FRUTA ERA: {}".format(palavra_secreta))
    print("Fim do jogo")


if (__name__ == '__main__'):
    jogar()
