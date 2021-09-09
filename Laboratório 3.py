#Laboratório 3
#Leandro Borba Barcelos
#DRE: 120153604

from Laboratório2 import discriminante

def absoluto(x):
    '''EX1: A função retornará o valor absoluto do valor (x).
    OBS: Essa função não admite números do tipo complexo.
    float -> float'''
    if x < 0:
        return x* (-1)
    
    else:
        return x

def qntraiz(a,b,c):
    '''EX2: Insira os 3 coeficientes (a, b, c) de uma equação do segundo grau
    para descobrir quantas raízes reais existem nessa equação.
    float, float, float -> string'''
    if discriminante(a,b,c) > 0:
        return 'A equação possui 2 (duas)raízes reais.'

    elif discriminante(a,b,c) == 0:
        return 'A equação possui 1 (uma) raiz real.'

    else:
        return 'A equação não possui nenhuma raiz real.'
    

def mensagem(texto, n):
    '''EX3: Insira o texto que você deseja repetir entre aspas simples ou
    duplas e o número de vezes (n) que deseja repetir esse texto.
    OBS: Essa função não admite, em (n), números do tipo float. Apenas insira
    numeros inteiros.
    string, int -> string'''
    return texto*n

def data(d,m,a):
    '''EX4: Insira o dia (d), o mês (m) - em números - e o ano (a) para
    que a função retorne a data no seguinte formato: DD/MM/AAAA.
    
    Obs: Para dia e/ou mês menores do que 10, não é necessário colocar o
    zero no início.
    
    int, int, int -> string.'''
    
    if d < 10 and m < 10 and 99 < a < 1000:
        return '0' + str(d) + '/' + '0' + str(m) + '/' + '0' + str(a)

    elif d < 10 and m < 10 and 9 < a < 100:
        return '0' + str(d) + '/' + '0' + str(m) + '/' + '00' + str(a)

    elif d < 10 and m < 10 and a < 10:
        return '0' + str(d) + '/' + '0' + str(m) + '/' + '000' + str(a)


    elif m < 10 and 99 < a < 1000:
        return str(d) + '/' + '0' + str(m) + '/' + '0' + str(a)

    elif m < 10 and 9 < a < 100:
        return str(d) + '/' + '0' + str(m) + '/' + '00' + str(a)

    elif m < 10 and a < 10:
        return str(d) + '/' + '0' + str(m) + '/' + '000' + str(a)




    elif d < 10 and 99 < a < 1000:
        return '0' + str(d) + '/' + str(m) + '/' + '0' + str(a)

    elif d < 10 and 9 < a < 100:
        return '0' + str(d) + '/' + str(m) + '/' + '00' + str(a)

    elif d < 10 and a < 10:
        return '0' + str(d) + '/' + str(m) + '/' + '000' + str(a)
    
    

    elif d < 10 and m < 10:
        return '0' + str(d) + '/' + '0' + str(m) + '/' + str(a)
    

    elif d < 10:
        return '0' + str(d) + '/' + str(m) + '/' + str(a)

    elif m < 10:
        return str(d) + '/' + '0' + str(m) + '/' + str(a)

    

    elif 99 < a < 1000:
        return str(d) + '/' + str(m) + '/' + '0' + str(a)
    
    elif 9 < a < 100:
        return str(d) + '/' + str(m) + '/' + '00' + str(a)
    
    elif a < 10:
        return str(d) + '/' + str(m) + '/' + '000' + str(a)
        
    else:
        return str(d) + '/' + str(m) + '/' + str(a)

def funcao(x):
    '''EX5: Insira o valor x de um função f(x) para descobrir o valor de y.
    float -> float'''
    if x < 0:
        return 0
    
    elif 0 <= x <=2:
        return x
    
    elif 2 < x <= 3.5:
        return 2
    
    elif 3.5 < x <= 5:
        return 3

    else:
        return (x**2) - (10*x) + 28

    
def INSS(salario):
    '''EX6a: Insira seu salário bruto para descobrir o valor do desconto
    do INSS em cima de seu salário.
    float -> float'''
    if salario <= 2000:
        return salario * (.06)
    
    elif 2000 < salario <= 3000:
        return salario * (.08)

    else:
        return salario * (.1)

def IR(salario):
    '''EX6b: Insira seu salário bruto para calcular o valor do desconto
    do Imposto de renda (IR) em cima de seu salário.
    float -> float'''
    if salario <= 2500:
        return salario * (.11)

    elif 2500 < salario <= 5000:
        return salario * (.15)
    
    else:
        return salario * (.22)

def descontoTotal(salario):
    '''EX6c: Insira seu salário bruto para calcular o valor do seu salário
    líquido (com descontos do INSS e do Imposto de Renda (IR)).
    float -> float'''
    return salario - INSS(salario) - IR(salario)


        

