def devolver_cuadrados(l):
    """Esta funcion devuelve una lista con cada elemento de la lista dada pero elevada al cuadrado
    
    args:
        l (lista): Lista a la que se le asignará los elementos que esta tiene pero elevados al cuadrado
    """
    tam=len(l)
    cont=0
    for i in range(tam):
        l[cont] = l[cont]**2
        cont+=1
    return l
print(devolver_cuadrados([5,2,1,0]))