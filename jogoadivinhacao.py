print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 38

chuteString = input('Digite um número: ')


print('Você digitou o número', chuteString)

chute = int(chuteString)

if numeroSecreto == chute:
    print('Você acertou!')
elif(chute>numeroSecreto):
    print('Você errou!! O número secreto é um número menor')
else:
    print('Você errou!! O número secreto é um número maior')

#Aula Elif 26.02.24
