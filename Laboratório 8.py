#Leandro Borba Barcelos
# DRE: 120153604

#Exercício 1.a.
import math

def soma(n):
    '''A função calculará a soma dos (n) termos da equação: ((-1)^n)/(2n + 1)
    Dados de entrada -> int
    Dados de saída -> float'''

    seq = list(range(1,n+1)) #sequência de número de 1 até n
    x = 0 #indice dessa sequência
    soma = 1

    for i in seq:
        if x % 2 == 0 or x ==0:
            soma -= 1/((2*i)+1)


        else:
            soma += 1/((2*i)+1)

        x += 1

    return soma
        
#Exercício 1.b.
def somab():
    '''A função verificará quantos termos são necessários para que a soma de n termos da equação: ((-1)^n)/(2n + 1)
    possua um erro menor que 0.01 em relação a divisão (pi/4)
    Dados de entrada -> None
    Dados de saída-> tupla(float,int)'''
    seq = list(range(1,25))
    comparacao = math.pi/4

    for i in seq:
        s = soma(i)#soma dos i termos

        y = math.fabs(s-comparacao) #diferença entre a soma e o valor que 

        if y < 0.01:
            return (s,i)
        
    

#Exercícios 2
def buscar_contatos(lista, nome):
    '''A função retornará os dados do nome procurado. Insira a lista de contatos e o nome procurado
    Dados de entrada -> lista, string
    Dados de saída -> lista'''

   
    lista_nomes = [] #lista com os dados do nome procurado
    Q = len(lista) #quantidade de elementos dentro da lista

    for i in list(range(0,Q)):
        
        texto = str.lower(lista[i][0])
        nome_m = str.lower(nome)
        if nome_m in texto:
            lista_nomes += [lista[i]]

    return lista_nomes
