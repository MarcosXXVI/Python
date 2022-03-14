import random

#inserir os clubes
lista_clubes = []
contador = 1
while contador <= 4:
    clube = input('Insira o {} competidor: '.format(contador))
    lista_clubes.append(clube)
    contador += 1
else:
    print('Clubes cadastrados \n')
    #print(lista_clubes)

#Criar uma nova lista para os competidores
lista_competidores = []

while lista_clubes != []:
    #Sortear os clubes
    s = random.choice(lista_clubes)
    ##print('O clube sorteado foi: {}'.format(s))

    #Inserir o sorteado na lista_competidores
    lista_competidores.append(s)

    #Remover o clube da lista_clubes sorteado
    lista_clubes.remove(s)
    ##print(lista_clubes)
else:
    print('O sorteio foi feito.\n')
    ##print(lista_competidores)

#Apresentar duelos
comp1 = lista_competidores [0]
comp2 = lista_competidores [1]
comp3 = lista_competidores [2]
comp4 = lista_competidores [3]

print('Jogos definidos Semi-final \n')
print('{} _VS_ {}'.format(comp1, comp2))
print('{} _VS_ {}\n'.format(comp3, comp4))

#Entrar com resultados
#Verificar se os valores são iguais

pts1 = int(input('{} fez quantos pontos? '.format(comp1)))
pts2 = int(input('{} fez quantos pontos? '.format(comp2)))
pts3 = int(input('{} fez quantos pontos? '.format(comp3)))
pts4 = int(input('{} fez quantos pontos? '.format(comp4)))
print('\n')

#Comparar as pontuações
#remover da lista os derrotados
if pts1 > pts2:
    print( '{} {}_VS_{} {}'.format(comp1, pts1, pts2, comp2 ) )
    print('Vitória da equipe {} \n'.format(comp1))
    lista_competidores.remove(comp2)
else:
    print( '{} {}_VS_{} {}'.format( comp1, pts1, pts2, comp2 ) )
    print( 'Vitória da equipe {} \n'.format( comp2 ) )
    lista_competidores.remove( comp1 )
if pts3 > pts4:
    print( '{} {}_VS_{} {}'.format( comp3, pts3, pts4, comp4 ) )
    print( 'Vitória da equipe {} \n'.format( comp3 ) )
    lista_competidores.remove( comp4 )
else:
    print( '{} {}_VS_{} {}'.format( comp3, pts3, pts4, comp4 ) )
    print( 'Vitória da equipe {} \n'.format( comp4 ) )
    lista_competidores.remove( comp3 )

#Apresentar a próxima chave

comp1 = lista_competidores[0]
comp2 = lista_competidores[1]

print('Jogos definidos - Final \n')
print('{} _VS_ {}'.format(comp1, comp2))

#Entrar com a pontuação

pts1 = input('Quantos pontos o {} fez? '.format(comp1))
pts2 = input('Quantos pontos p {} fez? \n'.format(comp2))

#Verificar o vencedor
if pts1 > pts2:
    print( '{} {}_VS_{} {}'.format(comp1, pts1, pts2, comp2 ) )
    print('Vitória da equipe {} \n'.format(comp1))
    lista_competidores.remove(comp2)
    # Apresentar Campeão
    print( 'Campeão do Torneio' )
    print( '************************' )
    print( 'Equipe {}'.format(comp1) )
elif pts2 > pts1:
    print( '{} {}_VS_{} {}'.format( comp1, pts1, pts2, comp2 ) )
    print( 'Vitória da equipe {} \n'.format( comp2) )
    lista_competidores.remove( comp1 )
    # Apresentar Campeão

    print( 'Campeão do Torneio' )
    print( '************************' )
    print( 'Equipe {}'.format(comp2) )
else:
    print('Valor inválido')

