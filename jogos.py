import forca
import jogoadivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")



jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar_forca()
else:
    print("Jogando Adivinhação")
    jogoadivinhacao.jogar_adivinhacao()