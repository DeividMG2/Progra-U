contador = 1
def profundidad(lista):
    """Funcion para ver la profundidad de lista
    args:
    lista (list): lista para ver la profundidad.
    """
    global contador
    try:
        if isinstance(lista[0],list):
            contador+=1
            profundidad(lista[0])
        else:
            profundidad(lista[1:])
        return contador
    except:
        return contador        
lista = [[1] , [ 2, 3, [4, [5], 6], 7], 8 ]
mayor = 1
for i in lista:
    if isinstance(i,list):
        cont = profundidad(i)
        print(i," tiene de profundidad ",cont)
        if cont > mayor: 
            mayor = cont+1
        cont = 0
print(f"La profundidad es de {mayor}")