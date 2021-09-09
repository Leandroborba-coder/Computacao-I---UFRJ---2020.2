#Leandro Borba Barcelos
#DRE 120153604

from random import randint

#Exercício 1
def dados():
    '''A função contará a quantidade de vezes que dois dados foram
    jogados até que os dois números desses dois dados foram iguais.
    
    Não existe dado de entrada, apenas chame a função
    Dados de saída -> int'''

    d1 = randint(1,6) #Dado 1
    d2 = randint(1,6) #Dado 2

    i = 1

    while d1 != d2:
        i = i + 1
        d1 = randint(1,6) 
        d2 = randint(1,6)
        
        
    return i


#Exercício 2
def buscar_contatos(lista, nome):
    '''A função retornará a posição dos nomes dentro de uma lista.
    Dados de entrada -> lista, string
    Dados de saída -> lista'''

    i = 0
    lista_nomes = [] #lista com os índices de cada nome
    Q = len(lista) #quantidade de elementos dentro da lista

    while i < Q:
        nome_da_lista = str.lower(lista[i][0]) #nome extraído das lista

        if nome in nome_da_lista:
            lista_nomes = lista_nomes + [i]

        i = i + 1

    return lista_nomes
