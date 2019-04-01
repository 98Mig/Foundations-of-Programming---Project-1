#Miguel Antonio Oliveira Rocha; 86482

letras=('A', 'B', 'C', 'D', 'E', 'F', 'G', \
        'H', 'I', 'J', ' ', 'L', 'M', 'N', \
        'O','P', 'Q', 'R', 'S', 'T', 'U', \
        'V', 'X', 'Z', '.')

def gera_chave1(letras):
    l1=letras[0:5] 
    l2=letras[5:10]
    l3=letras[10:15] 
    l4=letras[15:20]
    l5=letras[20:]
    return (l1,l2,l3,l4,l5)
#A funcao gera_chav1 devolve a matriz base da descodificacao., sendo que l1 corresponde a linha 1
#l2 corresponde a linha 2
#l3 corresponde a linha 3
#l4 corresponde a linha 4
#l5 corresponde a linha 5

def obtem_codigo1(car, chave):
    for i in range(len(chave)): 
        for j in range(len(chave)):
            if car==chave[i][j]:
                return str(i)+str(j)
#A funcao obtem_codigo1 corresponde a funcao que obtem, a partir da gera_chave1, o codigo de cada elemento da matriz
#sendo que i corresponde a linha da matriz, e j a coluna da matriz

def codifica1(cad,chave):
    codificado=''
    tuplo_cad=tuple(cad)
    for i in range(len(cad)):
        car=tuplo_cad[i]
        codificado=codificado+str(obtem_codigo1(car,chave))
    return codificado
#A funcao codifica1, a partir da chave de obtem_codigo1 (funcao invocada durante o codigo), faz a transformacao para um tuplo da string cad
#e devolve a string codificado, que corresponde a sequencia de caracteres, cada dois correspondendo ao car de obtem_codigo1.

def obtem_car1(cod,chave):
    i=eval(cod[0])
    j=eval(cod[1])
    car=chave[i][j]
    return car
#A funcao obtem_car1 corresponde a funcao que devolve o elemento da matriz corresponde a um i (linha da matriz) e
#um j (coluna da matriz).

def descodifica1(cad_codifica,chave):
    descodificado=''
    tuplo_descodificado=tuple(cad_codifica)
    for i in range(len(cad_codifica)//2):
        cod=tuplo_descodificado[i*2:(i+1)*2]
        descodificado=descodificado+str(obtem_car1(cod,chave))
    return descodificado
#A funcao descodifica1 corresponde a uma funcao que divide o tuplo em 2, que fazemos a conversao de cod para um tuplo.
#Para cada cod, ira existir dois indices que correspondem ao obtem_car1 de cod. No final, faz-se a conversao do tuplo
#para string.

#---------------------------Fim da versao simplificada--------------------------
letras=('A', 'B', 'C', 'D', 'E', 'F', 'G', \
        'H', 'I', 'J', 'L', 'M', 'N', \
        'O','P', 'Q', 'R', 'S', 'T', 'U', \
        'V', 'X', 'Z')


def gera_chave2(letras):
    from math import sqrt
    from math import ceil
    linhas = int(ceil(sqrt(len(letras))))
    colunas = int(round(sqrt(len(letras))))
    tuplofinal = ()
    for i in range(linhas):
        tuplofinal=tuplofinal+(letras[i*colunas:(i+1)*colunas],)
    return tuplofinal
#A funcao gera_chave2 devolve um tuplo que corresponde a um tuplo de tuplos, sendo que cada tuplo possui
#um numero determinado de elementos, obtidos a partir das linhas e colunas da matriz. O numero das linhas corresponde ao maior valor inteiro superior a raiz quadrada
#e o numero de colunas corresponde ao valor arredonado da raiz quadrada do numero de elementos de letras.

def obtem_codigo2(car,chave):
    for i in range(len(chave)):
        for j in range(len(chave[i])):
            if car==chave[i][j]:
                return str(i)+str(j)
    if car not in chave:
        return 'XX'
#A funcao obtem_codigo2 e bastante semelhante na maneira como a funcao obtem_codigo1 funciona. A unica diferenca corresponde se o car nao
#estiver na chave, devolve a string 'XX'.

def codifica2(cad,chave):
    codificado=''
    tuplo_cad=tuple(cad)
    for i in range(len(cad)):
        car=tuplo_cad[i]
        codificado=codificado+str(obtem_codigo2(car,chave))
    return codificado
#A funcao codifica2 funciona da mesma forma que a codifica 1. A unica diferenca envolve na funcao evocada: aqui, e
#invocada a funcao obtem_codigo2.

def obtem_car2(cod,chave):
    if cod!='XX':
        i=eval(cod[0])
        j=eval(cod[1])
        car=chave[i][j]
        return car        
    else:
        return '?'
#A funcao obtem_car2 a uma funcao que, se o caracter nao for 'XX', faz a mesma funcao que a obtem_car1. Se o caracter
#for 'XX', devolve '?'

def descodifica2(cad_codifica,chave):
    descodificado=''
    for i in range(len(cad_codifica)//2):
        descodificado=descodificado+(obtem_car2(cad_codifica[i*2:(i+1)*2],chave))
    return descodificado
#A funcao descodifica2 corresponde a funcao que, tal como a descodifica1, faz corresponder um cod a dois indices seguidos
#devolvendo depois o caracter respondente, atraves da invocacao da obtem_car2.