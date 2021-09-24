
def num_bombons(d,p):
    '''Insira o valor (d) referente ao dinheiro e o valor (p) referente
    ao preço unitário do bombom para a função calcular a quantidade
    máxima de bombons que podem ser comprados'''
    return d//p

from math import *
def carros(p,c=5):
    '''Função calcula a quantidade de carros, com capacidade (c),
    para transportar uma quantidade (p) de pessoas'''
    return ceil(p/c)

def PosNegZero(x):
    '''Função que verifica se um número inteiro (x) é positivo,
    negativo ou igual a zero
    int -> string'''
    if x > 0:
        return str(x) + ' e positivo'
    
    elif x < 0:
        return str(x) + ' e negativo'
    
    else:
        return str(x) + ' e zero'

def classificacao(cv, ce, cs, fv, fe, fs):
    '''Essa função verificará qual dos times (Cormengo ou Flaminthians)
    foi vitorioso no campeonato de futebol ou se houve empate entre os dois.
    Para isso, serão verificados várias variáveis, como o número de vitórias
    (cv e fv), o número de empates (ce e fe) e o saldo de gols (cs e fs) de 
    cada time, sendo as variáveis que começam com a letra (c) referentes ao time
    Cormengo e as com letra (f) referentes ao time flaminthians.'''
    
    if (cv*3 + ce*1) > (fv*3 + fe*1):
        return 'Cormengo'
    
    elif (fv*3 + fe*1) > (cv*3 + ce*1):
        return 'Flaminthians'

    elif (fv*3 + fe*1) == (cv*3 + ce*1):
        if cs > fs:
            return 'Cormengo'
        elif fs > cs:
            return 'Flaminthians'
        else:
            return 'Empate'

def avioes(c, p_compr, p_compet):
    '''A função verificará se a quantidade de papel comprada pela diretora
    é suficiente para distribuir igualmente entre os competidores de acordo com
    a quantidade de papel por competidor. Sendo (c) o número de competidores,
    (p_compr) a quantidade total de papel comprada e (p_compet) a quantidade
    de papel por competidor.
    int, int, int -> string'''
    if (p_compet * c) <= p_compr:
        return 'Suficiente'
    else:
        return 'Insuficiente'

def bolos(A,B,C):
    '''Função calcula a quantidade máxima de bolos que podem ser feitos
    em função da quantidade mínima de cada ingredientes, sendo (A) a 
    quantidade de xícaras de farinha de trigo, (B) a quantidade de ovos
    e (C) a quantidade de colheres de sopa de leite. As quantidades
    mínimas são: 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de
    sopa de leite
    int, int, int -> int'''
    return min(A//2,B//3,C//5)

def diff_datas(data1,data2):
    '''A função calcula a quantidade de dias entre duas datas. Insira as duas datas
    no formato "DD/MM/AAAA". Ao inserir as datas, coloque em aspas simples '' ou aspas 
    duplas " "
    
    Obs.: A quantidade de dias será uma aproximação e não a quantidade de dias exata,
    pois foram considerados meses de 30 dias e anos de 365 dias.
    
    string, string -> int'''
    
    #Cortando as strings
    dia2x = data2[0:2]
    mes2x = data2[3:5]
    ano2x = data2[6:10]
    
    dia1x = data1[0:2]
    mes1x = data1[3:5]
    ano1x = data1[6:10]

    #convertendo as strings para inteiros
    dia2 = int(dia2x)
    mes2 = int(mes2x)
    ano2 = int(ano2x) 
    
    dia1 = int(dia1x)
    mes1 = int(mes1x)
    ano1 = int(ano1x)
    
  
    
    difano = abs((ano2 - ano1)*365)
    
    difmes = abs(mes2 - mes1)*30
    
    difdias = abs(dia2 - dia1)
    
    Soma = difano + difmes + difdias
    
    if mes2 < mes1:
        return ((ano2-ano1-1)*365) + (((12 - (mes1 - mes2))*30)+5) + (dia2 - dia1)
    
    elif dia2 < dia1:
        return ((ano2 - ano1)*365) + (((mes2 - mes1)-1)*30) + (30 - (dia1 - dia2))
   
    elif mes2 < mes1 and dia2 < dia1:
        return ((ano2-ano1-1)*365) + ((12 - (mes1 - mes2))*30) + (dia1 - dia2 - 1)
    
    else:
	return  Soma

def hashtag(s):
    '''A função colocará 3 hashtags nos caracteres inseridos: No início,
    no meio e no final no texto inserido.
    string -> string'''
    Qs = len(s)
    m = Qs//2
    metade1 = s[0:m]
    metade2 = s[m:Qs]
    
    return '#' + metade1 + '#' + metade2 + '#'

def concatenacao(a, b):
    '''A função realizará a concatenação de duas string (a) e (b) no seguinte
    formato: (abba)
    string, stirng -> string'''
    return a + b*2 +a

def substitui(s,x,i):
    '''A função colocará o caracter (x) na posição (i) da string (s).
    string, string, int -> string'''
    Qs = len(s)
    parte1 = s[0:i]
    parte2 = s[i+1:Qs]
    return parte1 + x + parte2]

def recursiva(s):
    Qs = len(s)
    m = Qs//2
    parte1 = s[0:m]
    parte2 = s[m:Qs]
    return parte1 + s + parte2

def sorte(nome, n, ano):
    produto = n*2
    soma = produto + 5
    produto2 = soma * 50
    soma2 = produto2 + 1767
    diferenca = soma2 - ano
    
    return 'Parabéns ' + nome + '! Seu número da sorte é ' + str(diferenca) + '!'

def rotacione(s,i):
    '''A função vai rotacionar uma conjunto de caracteres (s)
    a partir da posição (i). 
    Exemplo: ("LeandroBorba", 5)
    >>> BorbaLeandro
    
    string, int -> string'''
    Qs = len(s)
    
    parte1 = s[0:Qs-i]
    parte2 = s[-i:Qs]
    
    if i == 0:
        return s
    else:
    	return parte2 + parte1

def concatenacao(a, b):
    '''A função concatenará a string (a) sem os cinco primeiros caracteres com a 
    string (b) sem os ultimos dez caracteres.
    Obs: Caso a string (tanto a (a) quanto a (b)) devem possuir no mínimo 15 caracteres
    string, string -> string'''
    
    Qa = len(a)
    Qb = len(b)
    
    stringA = a[5:Qa]
    stringB = b[0:Qb-10]
    
    if Qa <15 or Qb <15:
        return 'String inválida'
    
    else:
        return stringA + stringB

def colisao(ret1x1,ret1y1,ret1x2,ret1y2,ret2x1,ret2y1,ret2x2,ret2y2):
    '''A função colisao verificará, através das coordenadas cartesianas, a existência ou não de colisão entre dois retângulos.
    Caso a função retorne "Verdadeiro" (True), significa que os dois retângulos colidem! Caso o contrário, não haverá colisão (False)
    
    float, float, float, float, float, float, float, float -> Bool'''

    resultado = not (ret2x2 < ret1x1 or ret1x2 < ret2x1) and not (ret2y2 < ret1y1 or ret1y2 < ret2y1)
    
    return resultado

def rotaciona3(s):
    '''A função vai rotacionar uma string em 3 posições para a esquerda.
    string -> string'''
    
    Qs = len(s)
    
    parte1 = s[0:Qs-3]
    parte2 = s[-3:Qs]
    
    return parte2 + parte1

def rotacione(s,i):
    '''A função vai rotacionar uma conjunto de caracteres (s)
    a partir da posição (i). 
    Exemplo: ("LeandroBorba", 5)
    >>> BorbaLeandro
    
    string, int -> string'''
    
    Qs = len(s)          #Quantidade de caracteres da string
    x = i % Qs           #Quantidade de vezes que a contagem vai "rodar" pela palavra
    
    parte1 = s[0:Qs-x]
    parte2 = s[Qs-x:Qs]

 
    return parte2 + parte1

def SIGA(tupla):
    '''A função calculará a média aritmética de 3 notas (nota1, nota2 e nota3)
    de um aluno (nome).
    Ao inserir seu nome, coloque entre aspas simples ('   ') ou duplas ("  ")
    tupla(string, float, float, float) -> tupla (string, float, string, string)'''
    
    nome = tupla[0]
    nota1 = tupla[1]
    nota2 = tupla[2]
    nota3 = tupla[3]

    media = round((nota1 + nota2 + nota3)/3,1)


    if media >= 7:
        return nome, media, 'aprovado', 'Parabéns!'

    elif 5 <= media < 7:
        return nome, media, 'aprovado'

    else:
        return nome, media, 'reprovado'

def quant_palavras(frase):
    '''A função calculará a quantidade de palavras escritas em uma frase.
    parâmetros de entrada -> string
    parâmetros de saída -> int
    '''
    x = str.split(frase," ")
    y = len(x)
    
    return y

def intercala(lista1, lista2):
    """A função irá intercalar os dados de duas lista (lista1 e lista2) em uma terceira lista.
    Cada lista poderá admitir apenas 3 elementos
    
    Exemplo: lista1 = [1,3,5] e lista2 = [2,4,6] gera lista3 = [1,2,3,4,5,6]
    
    dados de entrada -> list, list
    dados de saída -> list"""
    
    L1_1 = lista1[0]
    L1_2 = lista1[1]
    L1_3 = lista1[2]
    
    L2_1 = lista2[0]
    L2_2 = lista2[1]
    L2_3 = lista2[2]
    
    lista3 = [L1_1, L2_1, L1_2, L2_2, L1_3, L2_3]
    
    return lista3

def colchao(medidas,H,L):
    '''A função verificará se um colção será capaz de passar por um porta.
    Insira as medidas, em centímetro, do colção na lista [medidas] e a altura (H) e a
    largura da porta (L) também em centímetros.
    
    Obs: A primeira medida da lista deve ser referente a altura do colchão,
    	 A segunda deve ser ferente a altura ou o comprimento
         A terceira deve ser ferente a altura ou o comprimento
         
   	Dados de entrada -> list, float, float
    Dados de saída -> Boolean'''
    
    
    A = medidas[0] #altura
    B = medidas[1] #largura ou comprimento
    C = medidas[2] #comprimento ou comprimento
    
    if A <= L and B <= 	H or B <= L and A <= H:
        return True
    
    else:
        return False

def piramide_num(n1,n2):
    '''A função criará uma pirâmide de números, em que, ao inserir
    doi números (n1) e (n2), ela retornará a seguência de (n1) até
    (n2) e, depois, de (n2) até (n1), sendo que o maior número (n2)
    só vai aparecer uma vez!
    
    dados de entrada -> int, int
    dados de saída -> list'''
    
    
    if n1 > n2:
        
        parte1 = list(range(n1,n2,-1))
    	parte2 = list(range(n2,n1))
    	fim = list(range(n1,n1+1))
        
        return parte1 + parte2 + fim
    
    else:
        parte1 = list(range(n1,n2))
        parte2 = list(range(n2,n1,-1))
        fim = list(range(n1,n1+1))
        
        return parte1 + parte2 + fim

def conta_frases(frase):
    '''A função contará a quantidade de frases na string inserida pelo usuário.
    
    dados de entrada -> string
    dados de saída -> int'''
    
    x = str.count(frase, ".")
    y = str.count(frase, "!")
    z = str.count(frase, "?")
    i = str.count(frase, "...")
    
    if x != 0 and i != 0:
        return (x - 3*i) + y + z + i
    
    else: 
    	return x + y + z + i

def retira_pontuacao(frase):
    '''A função vai retirar todos os tipos de pontuação de uma frase inserida pelo usuário.
    
    dados de entrada -> string
    dados de saída -> string'''
        
    x = str.count(frase, "-")
    y = str.count(frase, ",")
    z = str.count(frase, ":")
    i = str.count(frase, ";")
    i = str.count(frase, ".")
    j = str.count(frase, "!")
    k = str.count(frase, "?")
        
    if x != 0 or y != 0 or z != 0 or i != 0 or j != 0 or k != 0:
    	x1 = str.replace(frase,"-"," ")
        x2 = str.replace(x1,","," ")
        x3 = str.replace(x2,":"," ")
        x4 = str.replace(x3,";"," ")
        x5 = str.replace(x4,"."," ")
        x6 = str.replace(x5,"!"," ")
        final = str.replace(x6,"?"," ")
            
        return final
        
	else:
    	return frase

def inverte(frase):
	'''A função vai inverter a ordem das palavras de uma frase
        
    dados de entrada -> string
    dados de saída -> string'''
        
    x = retira_pontuacao(frase) #retirando a pontuação da string
    lista = str.split(x," ") #separando as palavras da string em uma lista
    Q = len(lista) #Quantidade de palavras que existem na lista
        
    juncao = str.join(" ",lista[Q-1:-Q-1:-1]) #Juntou as strings da lista de ordem inversa com um espaço entre elas
    minusculo = str.lower(juncao) # colocou todas as letras da string em minúsculo
        
    return minusculo

def faltas(lista):
    '''A função somará a quantidade total de faltas que ocorreram em um campeonato.
    Insira as informações na seguinte formatação:
    [  ['Brasil', 'Itália', [10,9] ] ,  ['Brasil', 'Espanha', [5,7] ],  ['Itália', 'Espanha', [7,8] ]  ]
    
    dados de entrada -> lista
    dados de saída -> int'''
    
    jogo1 = lista[0][2][0] + lista[0][2][1] 
    jogo2 = lista[1][2][0] + lista[1][2][1]
    jogo3 = lista[2][2][0] + lista[2][2][1]
    
        
	soma = jogo1 + jogo2 + jogo3
    
    return soma

def insere(lista_numero,n):
    '''A função colocará um número (n) em uma lista (lista_numero) e ordernará 
    os numeros desta lista em ordem crescente.
    
    dados de entrada -> lista, float
    dados de saída -> lista'''
    
    list.append(lista_numero,n) #inserindo o numero (n) no final da lista
    list.sort(lista_numero) #ordenando a lista em ordem crescente
    
    return lista_numero

def maiores(lista, n):
    '''A função retornará uma lista com apenas os números maiores que (n).
    
    dados de entrada -> lista, int
    dados de saída -> lista'''
    
    list.append(lista,n) #inserindo o numero (n) no final da lista
    list.sort(lista) #colocando os números em ordem crescente
    posicao = list.index(lista,n) #descobrindo a posição do numero n na lista ordenada
    
    return lista[posicao+1:] #fatiamento da lista com os números maiores que n

def acima_da_media(lista):
    '''A função retornará as notas dos alunos que obtiveram grau superior a média
    da turma.
    
    dados de entrada -> lista
    dados de saída -. lista'''
    Q = len(lista) #Quantidade de numeros que existem na lista
    Soma = sum(lista) #Soma todos os numeros da lista
    Media = Soma/Q #Calcula a média artimética da lista
    Maiores = maiores(lista,Media) #executa a função maiores, para colocar apenas os números maiores que a média em uma lista
	
    if Media in Maiores: #Caso a média seja igual a um valor dentro da lista, vamos retirar o valor da média
        list.remove(Maiores,Media)
        return Maiores
    
    else:
	return Maiores

def eh_ordenada(lista):
    '''A função indicará se uma lista está ordenada ou não. Caso esteja,
    a função retornará 'True' e indicará se o ordenamento é crescente ou decrescente.
    Caso não exista ordenamento, a função retornará 'False' e a palavra 'desordenada'
    
    dados de entrada -> lista
    dados de sída -> tupla(booleano,string)'''
    
    listacresce = lista[:] #copiando a lista
    listadecresce = lista[:] #copiando a lista
    
    list.sort(listacresce) #ordenando os numeros da lista em ordem crescente
    list.sort(listadecresce,reverse=True) #ordenando os numeros da lista em ordem decrescente
    
    if listacresce == lista:
        return (True,'crescente')
    
    elif listadecresce == lista:
        return (True,'decrescente')
    
    else:
        return (False,'desordenada')

def altera_frase(frase,palavra,posicao):
    '''A função colocará a palavra em uma posição na frase informada.
    Caso a palavra informada já exista na frase, a palavra ficará no formato maiúsculo
    apenas na primeira ocorrência.
    
    dados de entrada -> string, string, int
    dados de saída -> string'''
    
    frase_separada = str.split(frase) #separando cada palavra da string (frase) em uma lista
    
    if palavra not in frase_separada:
        
        list.insert(frase_separada,posicao,palavra)
        
        frase_costurada = str.join(" ",frase_separada)
        
        return frase_costurada
   
    else: 
        palavraM = str.upper(palavra)
        
        frase_separada = str.split(frase)

        Q =  len(frase_separada)


        if posicao <= Q:
            posicao2 = list.index(frase_separada,palavra)
            
            frase_separada[posicao2] = palavraM 
            
            substituicao = str.replace(frase,palavra,palavraM,1)
            
            return substituicao

        else:
            list.append(frase_separada,palavra)
            substituicao = str.replace(frase,palavra,palavraM,1)
            
            return substituicao

def filtraMultiplos(lista,n):
    '''A função receberá como entrar uma lista de numeros e retornará apenas os números multiplos de (n).
    Dados de entrada -> list, int
    Dados de saída -> list'''
    Q = len(lista)
    i = 0
    multiplos = []
    
    while i < Q:
        if lista[i] % n == 0:
            list.append(multiplos,lista[i])
        i = i +1
        
    return multiplos

def uppCons(frase):
    '''A função retornará a frase inserida com todas as consoantes em maiúsculo. As outras letras retornarão
    conforme elas foram inseridas
    dados de entrada -> string
    dados de saída -> string'''
    
    Q = len(frase)
    novafrase = ''
    i = 0
    
    while i < Q:
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
            novafrase = novafrase + str.upper(frase[i])
        else:
            novafrase = novafrase + frase[i]
        i = i + 1
    return novafrase

def repetidos(lista):
    '''A função retornará a quantidade de vezes que um número é igual ao seu número seguinte.
    Dados de entrada -> list
    Dados de saída -> int'''
    Q = len(lista)
    i = 0
    repeticoes = 0
    
    while i < Q:
        if lista[i-1] == lista[i]:
            repeticoes = repeticoes + 1
        i = i +1
        
    return repeticoes

def fatorial(n):
    '''A função retornará o fatorial do número inserido.
    Dados de entrada -> int
    Dados de saída -> int'''
    
    i = 1
    fatorial = n
    
    while n-i != 0:
        fatorial = fatorial * (n-i)
        i = i +1
        
    return fatorial

def faltante(lista):
    '''A função verificará qual é a numeração da peça que está faltando de um quebra-cabeça.
    Será inserida em uma lista os numeros da peças em ordem crescente e, caso ocorra uma quebra na sequência,
    a função retornará esse número.
    Dados de entrada -> list
    Dados de saída -> int'''
    
    Q = len(lista)
    i = 0
    
	if lista[0] != 1:
    	return lista[0] - 1
    
    while i < Q-1:
        if Q == 1 and lista[0] == 1:
            return lista[0] + 1
        
        elif Q > 1:
            if lista[i] != lista[i+1] - 1:
                return lista[i + 1] - 1
            
            i = i + 1
            
    return lista[-1] + 1

def posLetra(palavra,letra,n):
    '''A função retornará qual o indice da (n)ézima ocorrência da (letra) na (palavra)
    Dados de entrada -> string, string, int
    Dados de saída -> int'''   
    
    Q = len(palavra) #quantidade de caracteres
    p = str.index(palavra,letra) # indice da primeira ocorrência
    c = str.count(palavra,letra) #contando a quantidade de ocorrência
    i = 0 #contador e indice
    acu = 0 #acumulador
    
    #Quando o indice inserido corresponde a primeira ocorrência
    if n == p:
        return p
    
    #Quando existem menos ocorrência do que o usuário indica em (n)
    elif c < n:
        return -1
    
    while i <= Q-1:
        if acu == n:
            return i-1
        
        elif palavra[i] == letra:
            acu = acu + 1
        i = i + 1

def soma_fatorial(n):
    '''A função vai calcular a soma dos fatorias de 1 até n
    dados de entrada ->int
    dados de saída -> int'''
    soma = 0
    
    for i in list(range(n+1)):
        fat = fatorial(i)
        soma += fat
        
    return soma

def qtd_divisores(n):
    '''A função calculará a quantidade de divisores que um numero (n) possui
    dados de entrada -> int
    dados de saída -> int'''
    
    c = 0 #contador
    
    if n < 0:
        return 0
    
    for i in list(range(1,n+1)):
        if n % i == 0:
            c += +1
    return c

def qtd_divisores(n):
    '''A função calculará a quantidade de divisores que um numero (n) possui
    dados de entrada -> int
    dados de saída -> int'''
    
    c = 0 #contador
    
    if n < 0:
        return 0
    
    for i in list(range(1,n+1)):
        if n % i == 0:
            c += +1
    return c

def primo(n):
    '''A função verificará se um determinado numero (n) é primo ou não.
    Dados de entrada -> int
    Dados de saída -> booleano'''
    
    qtd = qtd_divisores(n)
    
    if qtd != 2:
        return False
    
    else:
        return True

def soma_h(n):
    '''A função retornará a soma das divisões de por (n) termos
    Dados de entrada -> int
    Dados de saída -> float'''
    
    soma = 1
    
    for i in list(range(1,n)):
        soma += + (1/(i+1))
        
    return round(soma,2)

def lingua_p(palavra):
    '''A função traduzirá a palavra para a lingua do P, em que toda vez que ocorre uma vogal,
    será inserido a letra (p)
    dados de entrada -> string
    dados de saída -> string'''
    
    palavram = str.lower(palavra)
    letras = list(palavram)
    i = 0  #indice da lista
    Q = len(letras)
    
    while i < Q:
        if letras[i] in ['a','e','i','o','u','é','ú','á','à','í','ó']:
            list.insert(letras,i+1,'p')
            list.insert(letras,i+2,letras[i])
            Q = len(letras)
            i += +2
       
        i += +1
        
               
    junta_letras = "".join(letras)
    return junta_letras

def soma():
    n = 10
    s = 0 #soma
    seq = list(range(1,n+1))
    x = 0
    for i in seq:
        numerador = seq[-1-x]
        fat = fatorial(i)
        
        
        if numerador % 2 != 0: 
        	s += numerador/fat
            x += +1
            
        else:
            s -= numerador/fat
            x += +1
    
    s = s*(-1)
	return round(s,2)


def eh_quadrada(lista):
    '''A função reberá uma lista e a função verificará se a lista é quadrada.
    Dados de entrada -> lista
    Dados de saída -> booleano'''
    
    nlinha = len(lista)
    
    if nlinha != 0:
    	ncoluna = len(lista[0])
    
    	if nlinha == 0:
        	return True
    
    	elif nlinha == ncoluna:
        	return True
    
    	else:
        	return False
    else:
        return True

def busca(setor,matriz):
    '''A função buscará as informações dos funcionários de um determinado setor
    Dados de entrada -> string, lista
    Dados de saída -> lista'''
    
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    resultado = []
    
    for i in range(nlinha):
        if setor == matriz[i][2]:
            resultado += [[matriz[i][0],matriz[i][1],matriz[i][3]]]
            
    return resultado

def ordena_por_insercao(lista):
    '''A função ordenará os numeros de uma lista em ordem crescente
    Dados de entrada -> lista
    Dados de saída -> lista'''
    
    copia_lista = lista[:]
    lista_ordenada = []
    
    for i in lista:
    	menor = min(copia_lista)
        lista_ordenada += [menor]
        list.remove(copia_lista,menor)
        
    return lista_ordenada

def melhor_volta(matriz):
    '''A função retornará qual foi o corredor com o menor tempo (1 à 6), qual esse menor tempo
    e em qual volta isso ocorreu
    Dados de entrada -> lista
    Dados de saída -> tupla (int, int, int)'''
    
    lista_menor = []
    
    for i in range(6):
        menor = min(matriz[i])
        lista_menor += [menor]
        
    menor_todos = min(lista_menor)
    
    indice_menor = list.index(lista_menor,menor_todos)
    indice_menor1 = list.index(lista_menor,menor_todos) + 1
    
    volta_menor = list.index(matriz[indice_menor],menor_todos) + 1
    
    return (indice_menor1,menor_todos,volta_menor)






	
