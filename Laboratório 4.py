#Laboratório 4
#Leandro Borba Barcelos
#DRE:120153604

def SIGA(tupla):
    '''A função calculará a média aritmética de 3 notas (nota1, nota2 e nota3)
    de um aluno (nome) e retornará a situação do aluno.

    
    OBS: Ao inserir seu nome, coloque entre aspas simples ('   ') ou duplas ("  ")
    
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

def formato_data(data):
    '''A função receberá uma data - com apenas:
    dois caracteres para o dia
    dois caracteres para o mês
    dois caracteres para o ano
    formato: 'XX/YY/ZZ'
    sendo cada um separado com uma barra ( / ) - e retornará qual é/são o(s)
    possível(eis) formato(s) dessa data

    string -> tupla'''
    
    primeiro = int(data[0:2])     #Referente aos dois primeiros caracteres da data
    meio = int(data[3:5])         #Referente aos dois caracteres do meio da data
    ultimo = int(data[6:8])       #Referente aos ultimos caracteres da data
 

    modelo1 = 'dd/mm/yy'
    modelo2 = 'mm/dd/yy'
    modelo3 = 'yy/mm/dd'

#OS 3 EM COMUM
    if 1 <= primeiro <= 12 and 1 <= meio <=12 and 1 <= ultimo <= 31:
        return modelo1, modelo2, modelo3

#2 EM COMUM
    #1 & 2 em comum
    elif 1 <= primeiro <= 12 and 1 <= meio <= 12:
        return modelo1, modelo2

    #1 & 3 em comum
    elif 1 <= primeiro <= 31 and 1 <= meio <= 12 and 1 <= ultimo <= 31:
        return modelo1, modelo3

    #2 e 3 em comum = #OS 3 EM COMUM, POIS SEMPRE PEGAM TODOS OS MÍNIMOS
    #elif 1 <= primeiro <= 12 and 1 <= meio <= 12 and 1 <= ultimo <= 31:
    #    return modelo2, modelo3



#ÚNICAS 
    elif   1 <= primeiro > 31 and 1 <= meio <= 12 and 1 <= ultimo <= 31:
        return modelo3

    elif 1 <= primeiro <= 12 and 1 <= meio <= 31:
        return modelo2

    elif 1 <= primeiro <= 31 and 1 <= meio <= 12:
        return modelo1
    
    else:
        return ()


    

    


    
    


