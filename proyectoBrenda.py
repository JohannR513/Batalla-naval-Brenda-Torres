import random
import json

tablero = []
for m in range(10):
    a = []
    for x in range(10):
        a += [0]
    tablero.append(a)


Enemigo = []
for r in range (10):
    y = []
    for z in range (10):
        y += [0]
    Enemigo.append(y)

Disparos = []
for t in range (10):
    p = []
    for n in range (10):
        p += [0]
    Disparos.append(p)


print("Batalla Naval")
print("Vamos a iniciar poniendo los barcos")

def ImprimirTabla (Tableros):
    print("----------------------------------")
    print (*Tableros, sep="\n")
ImprimirTabla (tablero)

def posciónBarco(tablero):
    f = int(input("Indique la fila (del 1 al 10) inicial \n") ) - 1
    c = int(input("Indique la columna (del 1 al 10) inicial \n") ) - 1
    fc = [f, c]
    if f < 0 or f > 9 or c < 0 or c > 9:
        print ("Ingresa los valores bien")
        return posciónBarco (tablero)
    elif tablero[fc[0]][fc[1]] == 0:
            tablero[fc[0]][fc[1]] = 1
            return fc, tablero
    else:
        print ("Ya hay un barco aquí")
        return posciónBarco (tablero)

def Barco2(tablero,fc):
    direc = int(input("Direccion : \n1. Derecha -> \n2. Izquierda <- \n3. Arriba \n4. Abajo \n"))
    if (direc == 1) and (tablero[fc[0]][fc[1]+1] == 0) and ((fc[1] + 1) >= 0)  and ((fc[1] + 1) <= 9):
        tablero[fc[0]][fc[1]+1] = 1
        return tablero
    elif(direc == 2) and (tablero[fc[0]][fc[1]-1] == 0) and ((fc[1] - 1) >= 0)  and ((fc[1] - 1) <= 9):
        tablero[fc[0]][fc[1]-1] = 1
        return tablero
    elif direc == 3 and (tablero[fc[0]-1][fc[1]] == 0) and ((fc[0] - 1) >= 0)  and ((fc[0] - 1) <= 9):
        tablero[fc[0]-1][fc[1]] = 1
        return (tablero)
    elif (direc == 4) and (tablero[fc[0]+1][fc[1]] == 0) and ((fc[0] + 1) >= 0)  and ((fc[0] + 1) <= 9):
        tablero[fc[0]+1][fc[1]] = 1
        return tablero
    else:
        print("Posición Fuera del limite")
        return Barco2 (tablero,fc)
    ImprimirTabla (tablero)


def Barco3 (tablero,fc):
    direc = int(input("Direccion : \n1. Derecha -> \n2. Izquierda <- \n3. Arriba \n4. Abajo \n"))
    if (direc == 1) and (tablero[fc[0]][fc[1]+1] == 0) and ((fc[1] + 1) >= 0)  and ((fc[1] + 1) <= 9) and tablero[fc[0]][fc[1]+2] == 0:
        tablero[fc[0]][fc[1]+1] = 1
        tablero[fc[0]][fc[1]+2] = 1
        return tablero
    elif(direc == 2) and (tablero[fc[0]][fc[1]-1] == 0) and ((fc[1] - 1) >= 0)  and ((fc[1] - 1) <= 9) and tablero[fc[0]][fc[1]-2] == 0:
        tablero[fc[0]][fc[1]-1] = 1
        tablero[fc[0]][fc[1]-2] = 1
        return tablero
    elif direc == 3 and (tablero[fc[0]-1][fc[1]] == 0) and ((fc[0] - 1) >= 0)  and ((fc[0] - 1) <= 9) and tablero[fc[0]-2][fc[1]] == 0:
        tablero[fc[0]-1][fc[1]] = 1
        tablero[fc[0]-2][fc[1]] = 1
        return (tablero)
    elif (direc == 4) and (tablero[fc[0]+1][fc[1]] == 0) and ((fc[0] + 1) >= 0)  and ((fc[0] + 1) <= 9) and tablero[fc[0]+2][fc[1]] == 0:
        tablero[fc[0]+1][fc[1]] = 1
        tablero[fc[0]+2][fc[1]] = 1
        return tablero
    else:
        print("Posición Fuera del limite")
        return Barco3 (tablero,fc)


def Barco4 (tablero,fc):
    direc = int(input("Direccion : \n1. Derecha -> \n2. Izquierda <- \n3. Arriba \n4. Abajo \n"))
    if direc == 3 and (tablero[fc[0]-1][fc[1]] == 0) and (tablero[fc[0]-2][fc[1]] == 0) and (tablero[fc[0]-3][fc[1]] == 0) and ((fc[0] - 3) >= 0) and ((fc[0] - 3) <= 9):
        tablero[fc[0]-1][fc[1]] = 1
        tablero[fc[0]-2][fc[1]] = 1
        tablero[fc[0]-3][fc[1]] = 1
        return (tablero)
    elif(direc == 4) and (tablero[fc[0]+1][fc[1]] == 0) and (tablero[fc[0]+2][fc[1]] == 0) and (tablero[fc[0]+3][fc[1]] == 0) and ((fc[0] + 3) >= 0) and ((fc[0] + 3) <= 9):
        tablero[fc[0]+1][fc[1]] = 1
        tablero[fc[0]+2][fc[1]] = 1
        tablero[fc[0]+3][fc[1]] = 1
        return tablero
    elif (direc == 1) and (tablero[fc[0]][fc[1]+1] == 0) and (tablero[fc[0]][fc[1]+2] == 0) and (tablero[fc[0]][fc[1]+3] == 0) and ((fc[1] + 3) >= 0) and ((fc[1] + 3) <= 9):
        tablero[fc[0]][fc[1]+1] = 1
        tablero[fc[0]][fc[1]+2] = 1
        tablero[fc[0]][fc[1]+3] = 1
        return tablero
    elif (direc == 2) and (tablero[fc[0]][fc[1]-1] == 0) and (tablero[fc[0]][fc[1]-2] == 0) and (tablero[fc[0]][fc[1]-3] == 0) and ((fc[1] - 3) >= 0) and ((fc[1] - 3) <= 9):
        tablero[fc[0]][fc[1]-1] = 1
        tablero[fc[0]][fc[1]-2] = 1
        tablero[fc[0]][fc[1]-3] = 1
        return tablero
    else:
        print("Posición Fuera del limite")
        return Barco4 (tablero,fc)
    ImprimirTabla (tablero)

def Barco5 (tablero,fc):
    direc = int(input("Direccion : \n1. Derecha -> \n2. Izquierda <- \n3. Arriba \n4. Abajo \n"))
    if direc == 3 and (tablero[fc[0]-1][fc[1]] == 0) and (tablero[fc[0]-2][fc[1]] == 0) and (tablero[fc[0]-3][fc[1]] == 0) and (tablero[fc[0]-4][fc[1]] == 0) and ((fc[0] - 4)>= 0) and ((fc[0] - 4)<= 9):
        tablero[fc[0]-1][fc[1]] = 1
        tablero[fc[0]-2][fc[1]] = 1
        tablero[fc[0]-3][fc[1]] = 1
        tablero[fc[0]-4][fc[1]] = 1
        return (tablero)
    elif(direc == 4) and (tablero[fc[0]+1][fc[1]] == 0) and (tablero[fc[0]+2][fc[1]] == 0) and (tablero[fc[0]+3][fc[1]] == 0) and (tablero[fc[0]+4][fc[1]] == 0) and ((fc[0]+ 4) <= 9) and ((fc[0]+ 4) >= 0):
        tablero[fc[0]+1][fc[1]] = 1
        tablero[fc[0]+2][fc[1]] = 1
        tablero[fc[0]+3][fc[1]] = 1
        tablero[fc[0]+4][fc[1]] = 1
        return tablero
    elif (direc == 1) and (tablero[fc[0]][fc[1]+1] == 0) and (tablero[fc[0]][fc[1]+2] == 0) and (tablero[fc[0]][fc[1]+3] == 0) and (tablero[fc[0]][fc[1]+4] == 0) and ((fc[1] - 4) >= 0) and ((fc[1] - 4) <= 9):
        tablero[fc[0]][fc[1]+1] = 1
        tablero[fc[0]][fc[1]+2] = 1
        tablero[fc[0]][fc[1]+3] = 1
        tablero[fc[0]][fc[1]+4] = 1
        return tablero
    elif (direc == 2) and (tablero[fc[0]][fc[1]-1] == 0) and (tablero[fc[0]][fc[1]-2] == 0) and (tablero[fc[0]][fc[1]-3] == 0) and (tablero[fc[0]][fc[1]-4] == 0) and ((fc[1] - 4) >= 0) and ((fc[1] - 4) <= 9):
        tablero[fc[0]][fc[1]-1] = 1
        tablero[fc[0]][fc[1]-2] = 1
        tablero[fc[0]][fc[1]-3] = 1
        tablero[fc[0]][fc[1]-4] = 1
        return tablero
    else:
        print("Posición Fuera del limite")
        return Barco4 (tablero,fc)
    ImprimirTabla (tablero)

fc1, tablero =posciónBarco(tablero)
ImprimirTabla (tablero)
tablero = Barco2(tablero,fc1)
ImprimirTabla (tablero)
fc2, tablero =posciónBarco(tablero)
ImprimirTabla (tablero)
tablero = Barco3(tablero,fc2)
ImprimirTabla (tablero)
fc3, tablero =posciónBarco(tablero)
ImprimirTabla (tablero)
tablero = Barco4(tablero,fc3)
ImprimirTabla (tablero)
fc4, tablero =posciónBarco(tablero)
ImprimirTabla (tablero)
tablero = Barco5(tablero,fc4)
ImprimirTabla (tablero)


def posciónBarcoEnemigo (Enemigo):
    fe = random.randint(0,9)
    ce = random.randint(0,9)
    fcEnemiga = [fe, ce]
    if fe < 0 or fe > 9 or ce < 0 or ce > 9:
        return posciónBarcoEnemigo (Enemigo)
    elif Enemigo[fcEnemiga[0]][fcEnemiga[1]] == 0:
            Enemigo[fcEnemiga[0]][fcEnemiga[1]] = 1
            return fcEnemiga, Enemigo
    else:
        return posciónBarcoEnemigo (Enemigo)

   
def BarcoEnemigo1 (Enemigo,fcEnemiga):
    direc = random.randint(1,4)    
    try:
        if direc == 1 and (Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] == 0) and ((fcEnemiga[0] - 1) >= 0):
            Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] = 1
            return (Enemigo)
        elif(direc == 2) and (Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] == 0) and ((fcEnemiga[0] + 1) <= 9):
            Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] = 1
            return Enemigo
        elif (direc == 3) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] == 0) and ((fcEnemiga[1] + 1) <= 9):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] = 1
            return Enemigo
        elif (direc == 4) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] == 0) and ((fcEnemiga[1] - 1) >= 0):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] = 1
            return Enemigo
        else:
            return BarcoEnemigo1 (Enemigo,fcEnemiga)
    except:
        return BarcoEnemigo1 (Enemigo,fcEnemiga)


def BarcoEnemigo2 (Enemigo,fcEnemiga):
    direc = random.randint(1,4)    
    try:
        if direc == 1 and (Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] == 0) and ((fcEnemiga[0] - 2) >= 0):
            Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] = 1
           
            return (Enemigo)
        elif(direc == 2) and (Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] == 0) and ((fcEnemiga[0] + 2) <= 9):
            Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] = 1
           
            return Enemigo
        elif (direc == 3) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] == 0) and ((fcEnemiga[1] + 2) <= 9):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] = 1
           
            return Enemigo
        elif (direc == 4) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] == 0) and ((fcEnemiga[1] -2) >= 0):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] = 1
           
            return Enemigo
        else:
            return BarcoEnemigo2 (Enemigo,fcEnemiga)
    except:
        return BarcoEnemigo1 (Enemigo,fcEnemiga)


def BarcoEnemigo3 (Enemigo,fcEnemiga):
    direc = random.randint(1,4)    
    try:
        if direc == 1 and (Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-3][fcEnemiga[1]] == 0) and ((fcEnemiga[0] - 3) >= 0):
            Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-3][fcEnemiga[1]] = 1
            return (Enemigo)
        elif(direc == 2) and (Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+3][fcEnemiga[1]] == 0) and ((fcEnemiga[0] + 3) <= 9):
            Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+3][fcEnemiga[1]] = 1
            return Enemigo
        elif (direc == 3) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+3] == 0) and ((fcEnemiga[1] + 3) <= 9):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+3] = 1
            return Enemigo
        elif (direc == 4) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-3] == 0) and ((fcEnemiga[1] - 3) >= 0):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-3] = 1
            return Enemigo
        else:
            return BarcoEnemigo3 (Enemigo,fcEnemiga)
    except:
        return BarcoEnemigo3 (Enemigo,fcEnemiga)

def BarcoEnemigo4 (Enemigo,fcEnemiga):
    direc = random.randint(1,4)
    try:
        if direc == 1 and (Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-3][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]-4][fcEnemiga[1]] == 0) and ((fcEnemiga[0] - 4)>= 0):
            Enemigo[fcEnemiga[0]-1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-2][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-3][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]-4][fcEnemiga[1]] = 1
            return (Enemigo)
        elif(direc == 2) and (Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+3][fcEnemiga[1]] == 0) and (Enemigo[fcEnemiga[0]+4][fcEnemiga[1]] == 0) and ((fcEnemiga[0]+ 4) <= 9):
            Enemigo[fcEnemiga[0]+1][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+2][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+3][fcEnemiga[1]] = 1
            Enemigo[fcEnemiga[0]+4][fcEnemiga[1]] = 1
           
            return Enemigo
        elif (direc == 3) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+3] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]+4] == 0) and ((fcEnemiga[1] + 4) <= 9):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+2] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+3] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]+4] = 1
            fcEnemiga
            return Enemigo
        elif (direc == 4) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-3] == 0) and (Enemigo[fcEnemiga[0]][fcEnemiga[1]-4] == 0) and ((fcEnemiga[1] - 4) >= 0):
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-1] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-2] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-3] = 1
            Enemigo[fcEnemiga[0]][fcEnemiga[1]-4] = 1
            return Enemigo
        else:
            return BarcoEnemigo4 (Enemigo,fcEnemiga)
    except:
        return BarcoEnemigo4 (Enemigo, fcEnemiga)


fcEnemiga1, Enemigo =posciónBarcoEnemigo(Enemigo)
ImprimirTabla (Enemigo)
Enemigo = BarcoEnemigo1(Enemigo,fcEnemiga1)
ImprimirTabla (Enemigo)
fcEnemiga2, Enemigo =posciónBarcoEnemigo(Enemigo)
ImprimirTabla (Enemigo)
Enemigo = BarcoEnemigo2(Enemigo,fcEnemiga2)
ImprimirTabla (Enemigo)
fcEnemiga3, Enemigo =posciónBarcoEnemigo(Enemigo)
ImprimirTabla (Enemigo)
Enemigo = BarcoEnemigo3(Enemigo,fcEnemiga3)
ImprimirTabla (Enemigo)
fcEnemiga4, Enemigo =posciónBarcoEnemigo(Enemigo)
ImprimirTabla (Enemigo)
Enemigo = BarcoEnemigo4(Enemigo,fcEnemiga4)
ImprimirTabla (Enemigo)

print("Ahora vamos con los disparos")

def Disparo ():
    f = (int(input("Ingrese la fila (del 1 al 10) del disparo")) - 1)
    h = (int(input("Ingrese la hilera (del 1 al 10) del disparo")) - 1)
    if f >= 0 and f <= 9 and h >= 0 and h < 8:
        return [f, h]
    else:
        return Disparo()

def puntuarDisparo (tablero,tablero2, disparo):
    if tablero2[disparo[0]][disparo[1]] == 8:
        print (*tablero, sep="\n")
        print("Ahí ya has disparado, otra vez")
        return (puntuarDisparo(tablero,tablero2,Disparo()))
    elif tablero2[disparo[0]][disparo[1]] == 1:
        tablero[disparo[0]][disparo[1]] = 8
        tablero2[disparo[0]][disparo[1]] = 8
        print (*tablero, sep="\n")
        print ("Acertaste, Sigue así")
        return tablero,tablero2
    elif tablero2[disparo[0]][disparo[1]] == 0:
        tablero[disparo[0]][disparo[1]] = 8
        tablero2[disparo[0]][disparo[1]] = 8
        print (*tablero, sep="\n")
        print ("Intentalo después")
        return tablero,tablero2

def contarBarcos(tabla, contador):
    contador = 0
    for i in range (len(tabla)):
        for j in range(len(tabla[i])):
            if tabla[i][j] == 1:
                contador += 1
    return contador

def DisparoEnemigo (tablero):
    f = random.randint(0,9)
    h = random.randint(0,9)
    disparo = [f,h]
    if tablero[disparo[0]][disparo[1]] == 8:
        return DisparoEnemigo(tablero)
    elif tablero[disparo[0]][disparo[1]] == 1:
        tablero[disparo[0]][disparo[1]] = 8
        print ("Te han dado")
        return tablero
    elif tablero[disparo[0]][disparo[1]] == 0:
        tablero[disparo[0]][disparo[1]] = 8
        print ("El enemigo ha fallado")
        return tablero
numeroBarcos =0
numeroBarcosEnemigos = 0
Bandera = True
while Bandera:

    numeroBarcos = contarBarcos(tablero, numeroBarcos)
    numeroBarcosEnemigos = contarBarcos (tablero, numeroBarcosEnemigos)
    disparo = []
    disparo = Disparo()
    tableroDisparos,tableroEnemigo = puntuarDisparo(Disparos,Enemigo,disparo)
    tablero = DisparoEnemigo (tablero)
    if numeroBarcos == 0:
        print("Has perdido, tal vez la proxima.")
        Bandera = False
    if numeroBarcosEnemigos == 0:
        print ("Enhorabuena! Has ganado.")
        Bandera = False


with open ("proyecto.json","w") as file:
    (proyectoBrenda.json, file)
