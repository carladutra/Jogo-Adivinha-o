import forca
import jogoadivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    #criando a condição
    if(jogo == 1):
        print("Jogando jogo Forca")
        forca.jogar_forca()
    else:
        print("Jogando jogo da Adivinhação")
        jogoadivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()