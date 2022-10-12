import adivinhacao
import forca

def escolher_jogos():

    print("*********************************")
    print("**********SALA DE JOGOS!*********")
    print("*********************************")

    print("Escolha um jogo: ")
    print("(1) Adivinhação / (2) Forca")

    jogo = int(input("Qual jogo você quer? "))

    if(jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()

if(__name__ == "__main__"):
    escolher_jogos()

