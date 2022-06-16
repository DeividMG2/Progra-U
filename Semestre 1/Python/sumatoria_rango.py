#Usando recursividad
# def sumatoria_rango(a,b):
#     if b == a:
#         return b
#     else:
#         return (b+(sumatoria_rango(a,b-1)))

# a = 5
# b = 15

# print(f"La suma de los numeros del rango de {a} hasta {b} es de {sumatoria_rango(a,b)}")

#Ver Pares

"""
19821
//

"""
# def ver_pares(n):
#     if n>0:
#         ver_pares(n//10)
#         if n%2==0:
#             print(n%10,end="")
# ver_pares(26353)





# def contar_elementos_lista(l):
#     try:
#         l[0]
#         return 1+ contar_elementos_lista(l[1:])
#     except:
#         return 0
    
# print(contar_elementos_lista([1,2,3,4,5,6,7]))
# def aplanar_lista(l):
#     if not l:
#         return []
#     if isinstance(l[0],list):
#         return(aplanar_lista(aplanar_lista(l[0])+aplanar_lista(l[1:])))
#     else:
#         return l[:1]+aplanar_lista(l[1:])

# print(aplanar_lista([1,2,3,[4,5,[6]],7]))


# def num_mayor(l):
#     if not l:
#         return 0
#     else: 
#         if l[0]>num_mayor(l[1:]):
#             return l[0]
#         else:
#             return num_mayor(l[1:])

# print(num_mayor([1,2,3,4,14,5,6,11,8,3]))

list=[]
def eliminar_numero(l,n):
    global list
    if not l:
        return 0
    else: 
        if l[0]!=n:
            list.append(l[0])
            eliminar_numero(l[1:],n)
        else:
            eliminar_numero(l[1:],n)
    return(list)
print(eliminar_numero([2,3,4,5,9,6,3],9))
        