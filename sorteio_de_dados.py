import random
print('Este programa sorteia dois números de 1 a 6 simulando dois dados.\n')
resposta = input('Você quer jogar? Digite S para jogar ou N para não jogar.\n ----> ')

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]


while resposta == 'S' or resposta == 's':

    jgdado1 = random.choice(dado1)
    jgdado2 = random.choice(dado2)

    print('Dado verde: {}'.format(jgdado1))
    print('Dado vermelho: {}'.format(jgdado2))
    resposta = input('Quer jogar novamente? S ou N: ')

if resposta == 'N' or resposta == 'n':
    print('Quem sabe mais tarde, até a próxima!')
    exit()
else:
    print('Digite S para jogar ou N para sair.')