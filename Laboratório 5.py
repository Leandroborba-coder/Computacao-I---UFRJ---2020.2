def zodiaco(ano):
    '''A função zodiaco mostrará qual é o signo chinês que corresponde a um ano
    de nascimento.
    insira o ano de nascimento na função.

    Dado de entrada -> int
    Dado de saída -> string'''

    lista = ['Macaco' , 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

    resto = ano % 12
    
    return lista[resto]



def telefone(numero):
    '''A função verificará se um numero inserido corresponde a um numero de telefone
    válido no Brasil.

    Insira um numero entre aspas simples ou dupla com ou sem o DDD.
    A função retornará o DDD separado do telefone. Caso o número não seja
    válido, a função retornará uma tupla com duas strings vazias. Caso vocÊ
    não isira o DDD, o primeiro elemento da tupla será uma string vazia e o segundo
    com o numero inserido.

    OBS: Não é necessário colocar o DDI, pois a função apenas funcionará
    para número nos Brasil.

    Dado de entrada -> string
    Dado de saída -> tupla'''
    
    Q = len(numero) #Quantidade de caracteres

    #telefone com DDD
    if Q == 10:
        return (numero[0:2],numero[2:Q])
        
    #celular com DDD
    elif Q == 11 and numero[2] == "9":
        return (numero[0:2],numero[2:Q])

    #telefone sem DDD
    elif Q == 8:
        return (" ",numero)

    #celular sem DDD
    elif Q == 9 and numero[0] == "9":
        return (" ", numero)
    
    else:
        return (" ", " ")

            
    
