from pickle import TRUE
import random
import time

x=[0,0,0,0,0]
y=[0,0,0,0,0]
Mejor=[0,0,0]
poblacion=[]
NewPoblacion=[]
Semilla=0


def seleccionInicial(aux): #genera valores entre 0 y 1 para x e y en la poblacion inicial.
    i=0
    aux1=aux[:]
    global Semilla
    while i<5:
        random.seed(Semilla)
        aux1.append(random.randint(0,1))
        Semilla=Semilla+1
        i=i+1
    return aux1
def PoblacionInicial(Cantidad):
    aux1=[]
    aux2=[]
    i=0
    global poblacion
    while i<Cantidad:
        poblacion.append((seleccionInicial(aux1[:]),seleccionInicial(aux2[:])))
        i=i+1

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
    global Semilla
    random.seed(Semilla)
    particion=random.randint(0,len(aux1)-1)
    Semilla=Semilla+1
    while i<len(aux1):
        if i<=particion:
            hijo1.append(aux1[i])
            hijo2.append(aux2[i])
        else:
            hijo1.append(aux2[i])
            hijo2.append(aux1[i])
        i=i+1
    mutacion(hijo1)
    mutacion(hijo2)
    return hijo1,hijo2

def mutacion(aux): #a veces cambia 1 bit
    global Semilla
    random.seed(Semilla)
    posicion=random.randint(0,len(aux)-1)
    Semilla=Semilla+1
    random.seed(Semilla)
    decision=random.randint(1,100)
    Semilla=Semilla+1
    if decision == 5:
        if aux[posicion]==1:
            aux[posicion]=0
        else:
            aux[posicion]=1

def ruleta(TamañoPoblacion): #Genera probabilidades segun el fitness de cada solucion, mejor fitness = mayor probabilidad, luego, elige 2 de los candidatos y realiza cruzamiento
    i=0
    global NewPoblacion
    global Semilla
    PosibleMejor=[0,0,0]
    probabilidad=[]
    while i<TamañoPoblacion:
        j=0
        while j<FO(poblacion[i][0],poblacion[i][1])/10:#Asigna probabilidades
            probabilidad.append(i)
            j=j+1
        i=i+1
    random.seed(Semilla)
    aux=random.randint(0,len(probabilidad)-1)
    Semilla=Semilla+1
    random.seed(Semilla)
    aux2=random.randint(0,len(probabilidad)-1)# Elige 2 
    Semilla=Semilla+1
    while TRUE:
        if probabilidad[aux]==probabilidad[aux2]:#Se asegura que no sea el mismo individuo
            random.seed(Semilla)
            aux2=random.randint(0,len(probabilidad)-1)
            Semilla=Semilla+1
        else:
            break
    poblador1X=poblacion[probabilidad[aux]][0]
    poblador1Y=poblacion[probabilidad[aux]][1]
    poblador2X=poblacion[probabilidad[aux2]][0]
    poblador2Y=poblacion[probabilidad[aux2]][1]
    aux=cruzamiento(poblador1X,poblador2X)
    aux2=cruzamiento(poblador1Y,poblador2Y)
    random.seed(Semilla)
    cruzan=random.randint(1,10)
    Semilla=Semilla+1
    if cruzan ==10:
        return [0,0,-10]
    NewPoblacion.append([aux[0],aux2[0]])
    NewPoblacion.append([aux[1],aux2[1]])
    fitness=FO(aux[0],aux2[0])
    if fitness>PosibleMejor[2]:
        PosibleMejor[0]=aux[0]
        PosibleMejor[1]=aux2[0]
        PosibleMejor[2]=fitness
    fitness=FO(aux[1],aux2[1])
    if fitness>PosibleMejor[2]:
        PosibleMejor[0]=aux[1]
        PosibleMejor[1]=aux2[1]
        PosibleMejor[2]=fitness
    return PosibleMejor




def solver(TamañoPoblacion):
    iteracion=0
    global NewPoblacion
    global Mejor
    global poblacion
    global Semilla
    PoblacionInicial(TamañoPoblacion)
    Posible=[0,0,0]
    while TRUE:
        if len(NewPoblacion) == TamañoPoblacion:
            poblacion=NewPoblacion[:]
            NewPoblacion=[]
        else:
            Posible=ruleta(TamañoPoblacion)
        if Posible[2]>Mejor[2]:
            Mejor=Posible[:]
            iteracion=0
        elif Posible[2]==Mejor[2]:
            iteracion=iteracion+1
        if iteracion ==6:
            print("Solucion con "+str(TamañoPoblacion)+" pobladores")
            print("Valor de X: "+str(Mejor[0]))
            print("Valor de Y: "+str(Mejor[1]))
            print("Valor de FO: "+str(Mejor[2]))
            Mejor=[0,0,0]
            poblacion=[]
            NewPoblacion=[]
            break

i=0
Tamaño=10   
while i<5:
    start=time.time()
    solver(Tamaño)
    end=time.time()
    print("Se demoro: "+str(end-start)+" segundos")
    i=i+1
    Tamaño=Tamaño+40