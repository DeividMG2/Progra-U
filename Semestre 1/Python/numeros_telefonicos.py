def devolver_telefonos(l):
    """Esta funcion devuelve una lista con los telefonso de las personas que se encuentren la lista dada que cumplan tener edades entre 20 y 30 años
    
    args:
        l (lista): Lista que contiene a todas las personas con sus datos
    """
    l2 = []
    for i in l:
        if 20<=i[3]<=30:
            l2.append(i[4])
    return l2
lista = [
["Leonardo", "Víquez", "Acuña", 40, "8895-3002"] , 
["Ana", "Rodríguez","Castro",23,"1111-1111"] ,
["Marcos", "Rodríguez","Saens",17,"2222-2222"] ,
["Pedro", "Mendez","Acuña",30,"3333-3333"] ,
["Xinia", "Arce","durán",32,"4444-4444"]
] 
print(devolver_telefonos(lista))