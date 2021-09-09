# Leandro Borba Barcelos
#DRE: 120153604

from math import *

def media(x,y,z):
    '''1b)Insira 3 número inteiros (x, y e z) para calcular
    a média aritmética entre eles.
    int, int, int -> float'''
    return (x + y + z)/3

def maior(x,y,z):
    '''Insira 3 números inteiros (x, y, z) para verificar
    qual é o maior entre eles
    int, int, int -> int'''
    return max(x,y,z)

def menor(x,y,z):
    '''Insira 3 números inteiros (x, y, z) para verificar
    qual é o menor entre eles
    int, int, int -> int'''
    return min(x,y,z)

def difMaiorMedia(x,y,z):
    '''1c)Insira 3 números inteiros (x, y ,z) para calcular
    a diferença entre o maior número com a média aritimética
    dos 3
    int, int, int -> float'''
    return maior(x,y,z) - media(x,y,z)

def somaMenorMedia(x,y,z):
    '''1d)Insira 3 números inteiros (x, y ,z) para calcular
    a somar entre o menor número com a média aritimética
    dos 3
    int, int, int -> float'''
    return menor(x,y,z) + media(x,y,z)

def discriminante(a,b,c):
    '''2a)Insira os coeficientes (a, b, c) de uma equação
    do segundo grau para calcular o discriminante (delta)
    int, int, int -> int'''
    return (b**2)-4*a*c

def raizum(a,b,c):
    '''2b)Insira os coeficientes (a, b, c) de uma equação
    do segundo grau para calcular a primeira raiz dessa
    equação.
    int, int, int -> float'''
    return (-b + sqrt(discriminante(a,b,c)))/(2*a)

def raizdois(a,b,c):
    '''2c)Insira os coeficientes (a, b, c) de uma equação
    do segundo grau para calcular a segunda raiz dessa
    equação.
    int, int, int -> float'''
    return (-b - sqrt(discriminante(a,b,c)))/(2*a)

def ntermos(a1,an,r):
    '''3b)Insira o valor do primeiro termo (a1), o valor
    do ultimo termo (an) e a razão (n) de uma progressão
    aritmética para calcular o numero de termos.
    int, int, int -> float'''
    return ((an - a1)/r) + 1

def somaPA(a1,an,r):
    '''3c)Insira o valor do primeiro termo (a1), o valor
    do ultimo termo (an) e a razão (n) de uma progressão
    aritmética para calcular a soma de todos os termos.
    int, int, int -> float'''
    return ((a1 + an)*ntermos(a1,an,r))/2

def hipotenusa(c1,c2):
    '''4a)Insira o primeiro cateto (c1) e o segundo cateto (c2)
    para calcular o valor da hipotenusa de um triângulo
    retângulo.
    int, int -> float'''
    return sqrt((c1**2) +(c2**2))

def distpontos(Xa,Ya,Xb,Yb):
    '''4b)Insira as coordenadas do ponto A (Xa, Ya) e depois as
    coordenadas do ponto B (Xb, Yb) para calcular a distância
    entre os pontos A e B.
    int, int -> float'''
    return hipotenusa((Xb - Xa),(Yb - Ya))

def perimetrotriangulo(c1,c2):
    '''4c)Insira o primeiro cateto (c1) e o segundo cateto (c2)
    para calcular o valor do perímetro de um triângulo
    retângulo.
    int, int -> float'''
    return hipotenusa(c1,c2) + c1 + c2

def leitrigonometria(a):
    '''4d)Insira o valor do ângulo (a) para calcular a soma do
    quadrado do seno com o quadrado do cosseno de (a).
    int -> float'''
    return (sin(a)**2) + (cos(a)**2)

def comprimentocirculo(r):
    '''4e)Insira o valor do raio (r) de um círculo para calcular
    o comprimento desse círculo.
    int -> float'''
    return 2*pi*r

def areaSetor(r,a=360):
    '''5)Insira o raio de uma circunferência (r) e o angulo (a)
    do setor circular para calcular a área desse setor.
    int -> float'''
    return pi*(r**2)*a/360

