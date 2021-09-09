#Leandro Borba Barcelos
#DRE 120153604

#Eduardo de Aquino Menezes Soares
#DRE 120160148

from random import randint

def main():
    '''A função main executará o jogo da forca. A função sorteará uma palavra, dentro de um banco de 30 palavras
    e o usuário terá que inserir uma letra de cada vez até completar todas as letras da palavra. O jogador terá
    apenas 8 chances de errar. Caso o jogador ultrapasse esse número, ele receberá uma mensagem de que ele perdeu o jogo

    Dados de entrada -> none
    Dados de saída -> none'''
    
    print("Olá! Seja bem-vindo ao jogo da forca!\nVamos sortear uma palavra para você adivinhar as letras!\n\n")
    print("Aqui são as REGRAS do jogo:\n1) Cada jogador terá 8 chances de acertar a palavra escolhida\n")
    print("2) Insira uma letra por vez!\n\n")

    palavra = list(sorteio())
    palavraf = palavra[:]
    Q = len(palavra)

    palavra_tampada = palavra_escondida(Q)

    print("Começando...\n")
    print(str.format("Sua palavra tem {} letras. Veja: {}",Q,palavra_tampada))
    tentativas = 1

    while tentativas < 9:
        
        letrax = input("Insira a letra: ")

        letra = str.lower(letrax)
        if letra not in palavra:
            print(str.format("A letra     {}    não existe na palavra! Agora você tem {} tentativas", letra, 8-tentativas))
            tentativas += 1


        elif letra in palavra:

            destampando = descobrindopalavra(palavra,palavra_tampada,letra)

            print(str.format("A letra     {}    existe na palavra! Parabéns! Veja como ficou sua palavra agora: {}",letra,destampando))

            if '-' not in destampando:
                tentativas += 20
            
    if tentativas > 20:
        return "Você Venceu! Parabéns"

    else:    
        return print("Você Perdeu! A palavra do jogo era ",palavraf)

def sorteio():
    '''A função vai sortear uma palavra, dentro de um banco de 30 palavras diferentes
    Dados de entrada -> none
    Dados de saída -> string'''

    x = randint(0,29)

    banco = ['casa','cachorro','hotel','computador','professor','letras','musica','telhado','praia','cachoeira',
             'arma','borracha','amazonas','laranja','comida','programador','mesa','carro','moto','taxi',
             'jogo','arroz','calculadora','tomada','cama','tesoura','impressora','piso','relevo','matematica']

    return banco[x]


def palavra_escondida(Q):
    '''A função criar uma lista com Q traços, para esconder as letras de uma palavra do jogo da forca
    Dados de entrada -> int
    Dados de saída -> list'''

    palavra = []
    i = 0

    while i < Q:
        list.append(palavra,'-')
        i += 1
    
    return palavra


def descobrindopalavra(palavra,tampada,letra):
    '''A função vai destampar o caracter '-' de uma lista com a letra inserida.
    Exemplo: descobrindopalavra(['C','A','S','A'],['-','-','-','-',],'A')
    >>> ['-','A','-','A']
    Dados de entrada -> list, list, string
    Dados de saída -> list'''
    
    indices = []

    for i in palavra:
        if i == letra:
            indice = list.index(palavra,letra)
            list.append(indices,indice)
            palavra[indice] = '-'

    for j in indices:
        tampada[j] = letra

    return tampada
