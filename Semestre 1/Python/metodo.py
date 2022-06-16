#ordenamiento por inserción
def insercion(lista):
    menor=0
    lista2=[]
    borrar=False
    while(len(lista)>0):
        for i in lista:
            if(i==menor):
                lista2.append(menor)
                borrar=True
        if(borrar):
            lista.remove(menor)
            borrar=False
        menor+=1
    print(lista2)
insercion([7,2,1,6,5,3]) 
# Hay varios metodos de ordenamiento pero quickSort es el que se ejecuta más rápido por ende el más optimo. 