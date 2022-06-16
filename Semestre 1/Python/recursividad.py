#Determine si un String puede ser reconocido como un número entero (Recorre un string y determina si existen solo numeros en los dígitos que contiene)
"""
esConvertibles("12345") -> si "1" es digito? -> respuesta = esconvertibles ("2345")
                                si no respuesta= False


esConvertibles("2345") -> si "2" es digito? -> respuesta = esconvertibles ("345")
                                si no respuesta= False

esConvertibles("345") -> si "3" es digito? -> respuesta = esconvertibles ("45")
                                si no respuesta= False

esConvertibles("45") -> si "4" es digito? -> respuesta = esconvertibles ("5")
                                si no respuesta= False

esConvertibles("5") -> si "5" es digito and largo("5")==1 -> True
                                si no respuesta= False
"""

def esConvertible(numero_string):
    if len(numero_string)==1:
        if numero_string>="0" and numero_string<="9":
            return (True)
        else:
            return(False)
    else:
        digito=numero_string[0]
        if digito>="0" and digito<="9":
            return (esConvertible(numero_string[1:]))
        else:
            return(False)

print(esConvertible("123"))

print(esConvertible("12-3"))

#Ordenamiento de lista

def menorL(l):
    menor=l[0]
    for e in l[1:]:
        if (menor>e):
            menor=e 
    return(menor)

#print (menorL([10, 25, 5, 18]))

"""
[10, 25, 5, 18] => 5 + ordenarL([10,25,18])

[10, 25, 18] => 10 + ordenarL([25,18])

[25, 18] => 18 + ordenarL([25])

[18] => return(18)
"""


def ordenarL(l):
    if len(l)<=1:
        return (l)
    else:
        menor=menorL(l)
        l.remove(menor)
        return list((menor,))+ordenarL(l)

#print(ordenarL([101, 47, 83, 95,83, 4,17,25, -1]))

#Practica: Aplanar una lista

def aplanar (l):
    if len(l)==0:
        return([])
    elif len(l)==1:
        if type(l[0])==list:
            return(aplanar(l[0]))
        else:
            return (l)
    else:
        if type(l[0])==list:
            return (aplanar(l[0])+aplanar(l[1:]))
        else:
            return ([l[0]]+aplanar(l[1:]))

print (aplanar ([]))
print (aplanar ([[1],2]))
print (aplanar ([1,[2]]))
print (aplanar ([[[1]]]))


#Ordenamiento QuickSort
#Buscar elemento en una lista de punteros
#Unión de conjuntos con listas de punteros
#Intersección de listas de punteros
#Recorrer nveces los elementos de un alista de punteros circular

