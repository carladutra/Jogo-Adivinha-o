print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = 38

#Definindo o número de tentativas
numeroTentativas = 3

while(numeroTentativas > 0):
    print('Ok')

#Recebendo o chute do jogador
    chuteString = input('Digite um número: ')
    print('Você digitou o número', chuteString)
    chute = int(chuteString)

#Declarando as condições
    if numeroSecreto == chute:
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')

#Aula Elif 26.02.24
