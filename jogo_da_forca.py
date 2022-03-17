# criar lista dos caracteres do alfabeto
lista_alfabeto = ['a', 'b', 'c','ç', 'd', 'e', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u',
                  'v', 'w', 'x', 'y', 'z']
print('\n------------------------------JOGO DA FORCA------------------------------------' + 2*'\n' +
                          'Regras do jogo', 2*'\n' +
    'Dois competidores. O primeiro jogador deve escolher a palavra_chave, palavra a qual o jogador 02 deverá descobrir.\n'
    'Por padrão, o jogador2 pode errar apenas 5 vezes, se errar 6 vezes, vitória para o jogador 01.\n'
    'Se o jogador 02, conseguir completar a palavra_chave, vence o jogo.\n'
    'Observação: Não use acentos nas palavras, com exceção do caractere ç.' + 2*'\n', 'Bom jogo!' + 3*'\n')


jg01 = input('Nome do jogador01 --> ')
jg02 = input('Nome do jogador02 --> ')

palavra = ""# inicializar a variável palavra
#or (not palavra.isalnum())
while (not palavra.isalpha()): # verificar se o texto digitado não é número.

    palavra = input( '\n{} Digite uma palavra --> '.format( jg01 ) )# Receber palavra chave e criar lista

    if palavra.isalpha():
        print( 40 * '\n' + 'É hora da FORCA!\n' )

        palavra_chave = []
        for ch in palavra:  # percorrer cada caractere da palavra
            palavra_chave.append( ch )  # adicionar cada caracter na lista palavra_chave

        print( 'O texto secreto tem {} letras.'.format( len( palavra_chave ) ) )

        # Cria uma lista vazia para receber as letras certas.
        texto = []

        # Cópia da lista com a palavra chave para
        # limpar os caracteres e apresentar uma
        # lista vazia na tela
        texto = palavra_chave.copy()


        contador = 0  # Criar contador de erros
        qtd_erro = 6  # Definição da quantidade de erros

        # Altera todas as letra para campos vazios
        for item in texto:
            i = texto.index( item )
            texto[i] = '_'
        print(" ".join( map( str,texto)))#Imprimi a lista sem colchetes e vírgulas
        print( '\n' )

        # Entrada de caractere e verificação das posições dos caracteres
        # corretos
        while texto != palavra_chave:
            letra = input( 'Pense e digite uma letra: ' )
            print(5 * '---')
            if letra in lista_alfabeto:  # Verifica se o caractere inserido é válido

                if letra in palavra_chave:  # verifica se o caractere válido, existe na palavra chave
                    print( '\nMuito bem! Letra ({}) adicionada a palavra chave.'.format( letra ) )
                    lista_alfabeto.remove( letra )  # remove a letra da lista alfabeto
                    for pos, char in enumerate( palavra_chave ):  # Descobri a posição da letra
                        if (char == letra):
                            texto[pos] = letra  # Adiciona a letra dentro da posição encontrada
                    texto = texto
                    print(" ".join( map( str, texto)))
                    print('\n')

                else:  # Informa ao usuário que a letra não existe na palavra chave
                    print( '\nNão existe a letra {} na palavra chave'.format( letra ) )
                    contador += 1  # contabiliza o erro
                    print( 'Você falhou {} vez(es)\n'.format( contador ) )  # Apresenta a quantidade de erros
                    if qtd_erro == 6:
                        if contador == 0:
                            print( '| ------|\n - Forca vazia'
                                   '|\n'
                                   '|\n'
                                   '|\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 1:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|\n'
                                   '|\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 2:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|       | ' '--> Corpo\n'
                                   '|\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 3:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|      /| ' '--> Corpo e braço esquerdo\n'
                                   '|\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 4:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|      /|\ ' '--> Corpo, braço esquerdo e braço direito\n'
                                   '|\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 5:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|      /|\ ' '--> Corpo, braço esquerdo e braço direito\n'
                                   '|      /   ' '--> Perna esquerda\n'
                                   '|\n'
                                   '______________' )
                        elif contador == 6:
                            print( '| ------|\n'
                                   '|       O ' '--> Cabeça\n'
                                   '|      /|\ ' '--> Corpo, braço esquerdo e braço direito\n'
                                   '|      / \ ' '--> Perna esquerda e perna direita\n'
                                   '|\n'
                                   '______________' )
                if contador == qtd_erro:  # Verifica se o número de erros foi atingido
                    aux = palavra_chave
                    palavra_chave = "".join( map( str, aux ) )
                    print(
                        '\n Não foi dessa vez! \n Você errou {} vez(es). Vitória do(a) jogador(a) {}. \n A palavra chave é: {} \n FIM DO JOGO'.format(
                            contador, jg02, palavra_chave ) )
                    break
            else:  # Informa ao usuário que o caractere inserido não é válido
                print( '\nEste caracter não é válido.'.format( letra ) )
                print( 'Veja as letras, que você ainda pode usar.\n', lista_alfabeto, '\n' )
        else:  # Apresenta a vitória do usuário no jogo
            aux = palavra_chave
            palavra_chave = "".join( map( str, aux ) )
            print( 'Muito bem! Descobriu a palavra chave!\n Palavra Chave: {} \n '
                   '{} você venceu a partida!'.format( palavra_chave, jg02 ) )
            #" ".join( map( str, texto ) )
    else:
        print( 'Caractere(es) inválido. Digite somente texto.' )

