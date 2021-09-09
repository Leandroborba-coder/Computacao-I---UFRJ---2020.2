#Leandro Borba Barcelos
#DRE: 120153604


#exercício 1
def produtomatriz(matriz,n):
    '''A função calculará o produto de duas matrizes.
    Dados de entrada -> lista, float
    Dados de saída -> lista'''

    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    resultado = []

    for i in range(nlinha):
        produto = []
        for j in matriz[i]:
            p = n * j
            list.append(produto,p)
        list.append(resultado,produto)
            
    return resultado



'''#exercício 2
#Esse código recebe a lista de telefones no seguinte formato: ["DDTELEFONE"]
def buscar_contatos_v2(lista, telefone):
    ''''''A função retornará os dados do telefone procurado.
    Dados de entrada -> lista, string
    Dados de saída -> lista''''''
    
    qcontatos = len(lista)
    resultado = []
    

    for i in range(qcontatos):
        
        qtelefones = len(lista[i][1])
        
        for k in range(qtelefones):
            for j in lista[i][1][k]:
                adicionado = []
                
                if telefone in j:
                    adicionado += [lista[i][0], lista[i][2], lista[i][3]]
                    list.append(resultado,adicionado)
                
    return resultado'''


#exercício 2
#Esse código recebe a lista de telefones no seguinte formato: ("DD","TELEFONE")
def buscar_contatos(lista, telefone):
    '''A função retornará os dados do telefone procurado.
    Dados de entrada -> lista, string
    Dados de saída -> lista'''
    
    qcontatos = len(lista)
    resultado = []
    

    for i in range(qcontatos):
        
        qtelefones = len(lista[i][1])
        
        for j in range(qtelefones):
            telefonejuntos = lista[i][1][j][0] + lista[i][1][j][1]
            adicionado = []
                
            if telefone in telefonejuntos:
                adicionado += [lista[i][0], lista[i][2], lista[i][3]]
                list.append(resultado,adicionado)
                
    return resultado


