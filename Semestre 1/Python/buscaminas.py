import random

matriz_juego=[]


def colocar_bombas(l,b):
    filas=len(l)    
    columnas=len(l[0])
    while b>0:
        nueva_fila=random.randint(0, filas-1)
        nueva_columna=random.randint(0, columnas-1)
        if l[nueva_fila][nueva_columna]!="*":
            l[nueva_fila][nueva_columna]="*"
            b-=1
def colocar_numeros(l):
    tam=len(l)
    for x in range(tam):
        tam2=len(l[x])
        for y in range(tam2):
            if(l[x][y]!="*"):
                    x1=x-1
                    x2=x+2
                    y1=y-1
                    y2=y+2
                    cont=0
                
                # No me sirve la primer fila y la primera columna

                    for i in range(x1,x2):
                        for j in range(y1,y2):
                            if(i>=tam)|(j>=tam2):
                                continue
                            if(i<1):
                                i=0
                            if(l[i][j]=="*"):
                                cont+=1
                    l[x][y]=cont            
            
def imprimir_juego(l):
    print("\x1b[2J\x1b[1;1H")
    for x in l:
        print ("\t", end='')
        for y in x:
            print (" {0} ".format(y), end='')
        print ("")
    print ("\n")

def inicio_juego ():
    print("\x1b[2J\x1b[1;1H")
    print ("************")
    print ("*Buscaminas*")
    print ("************\n\n")

    filas=int(input ("Número de filas: "))
    columnas=int(input ("Número de Columnas: "))

    bombas=(filas*columnas)*10//100

    print ("\nEl juego tiene {0} bombas ocultas, indique las celdas a descubrir sin pisar una bomba, buena suerte!\n\n".format(bombas))
    input ("Toca cualquier tecla para continuar...")    
    lista=[["□" for y in range(columnas)] for i in range(filas)]
    colocar_bombas(lista,bombas)
    colocar_numeros(lista)
    imprimir_juego (lista)
inicio_juego()

