import random

def jogar():

    print("*********************************")
    print("Bem vindo a jogo de adivinhação !")
    print("*********************************")

    numero_secreto = random.randrange(1,51)
    numero_tentativa = 0
    pontos = 1000

    print("ESCOLHA O NÍVEL DE DIFICULDADE")
    print("1: Fácil 2: Intermediário 3: Difícil")

    level = int(input("Digite o nível: "))

    if(level == 1):
        numero_tentativa = 15
    elif(level ==2):
        numero_tentativa = 10
    else:
        numero_tentativa = 5



    for rodada in range(1, numero_tentativa + 1):

        print("rodada {} de {}".format(rodada, numero_tentativa))
        chute = input("Tente adivinhar o número entre 1 e 50: ")


        chute_int = int(chute)

        if((chute_int > 100) or (chute_int < 1)):
                print("DIGITE UM VALOR ENTRE 1 E 100")
                continue

        acertou     = chute_int == numero_secreto
        errou_maior = chute_int > numero_secreto
        errou_menor = chute_int < numero_secreto

        if (acertou):
            print("################")
            print("você acertou !!")
            print("################")
            break
        else:
            if(errou_maior):
                print("------------------")
                print("ERROOOUUU")
                print("------É MENOR -------")
            elif(errou_menor):
                print("------------------")
                print("ERROOOUUU")
                print("------É MAIOR -------")

            pontos = round(pontos - numero_secreto)


    print("fim do jogo.")
    print("PONTUAÇÃO FINAL: {}".format(pontos))
    print("o número éra: {}".format(numero_secreto))


if( __name__ == "__main__" ):
    jogar()