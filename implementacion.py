import random

x=[0,0,0,0,0]
y=[0,0,0,0,0]

poblacion=[]
TamañoPoblacion=10


def seleccionInicial(aux): #genera valores entre 0 y 1 para x e y en la poblacion inicial.
    i=0
    aux1=aux[:]
    while i<5:
        aux1.append(random.randint(0,1))
        i=i+1
    return aux1
def PoblacionInicial(Cantidad):
    aux1=[]
    aux2=[]
    i=0
    while i<Cantidad:
        poblacion.append((seleccionInicial(aux1[:]),seleccionInicial(aux2[:])))
        i=i+1
    print(poblacion[1][0])

def bin_dec(numero): #Conversor de binario a decimal
    i=0
    aux=0
    aux2=len(numero)-1
    while i<len(numero):
        aux=(numero[i]*2**aux2)+aux
        i=i+1
        aux2=aux2-1
    return aux

def FO(aux1,aux2): #Funcion objetivo o fitness
    val1=bin_dec(aux1)
    val2=bin_dec(aux2)
    fitness=(val1*val1*val2) - (val2*val2*val1)
    return fitness

def cruzamiento(aux1,aux2): # Cruzamiento en 1 punto
    hijo1=[]
    hijo2=[]
    i=0
    particion=random.randint(0,len(aux1)-1)
    while i<len(aux1):
        if i<=particion:
            hijo1.append(aux1[i])
            hijo2.append(aux2[i])
        else:
            hijo1.append(aux2[i])
            hijo2.append(aux1[i])
        i=i+1
    print(hijo1)
    print(hijo2)
    return hijo1,hijo2


print(FO([1,1,1,1,1],[0,1,0,1,0]))

print(cruzamiento([1,1,1,1,1],[0,1,0,1,0]))