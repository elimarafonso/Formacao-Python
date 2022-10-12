import adivinhacao
import forca


def escolher_jogos():
    print("*********************************")
    print("**********SALA DE TESTES ALEATÓRIOS!*********")
    print("*********************************")


    #List Comprehension
    '''
        inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
        pares = [numero for numero in inteiros if numero % 2 == 0]
    
        impares = [numero for numero in inteiros if numero % 2 == 1]
    
        print("Inteiros: {}".format(inteiros))
        print("Pares: {}".format(pares))
        print("Impares: {}".format(impares))
    '''

    #ARQUIVOS

    arquivo = open("palavras.txt", "r")

    palavras = [linha.strip() for linha in arquivo]
    print(palavras)

    arquivo.close()

if (__name__ == "__main__"):
    escolher_jogos()
