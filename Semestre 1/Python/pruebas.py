# mi_diccionario = {'edad':12,'telefono':'87980985','cedula':'209760552'}

# i = 0
# for k,v in mi_diccionario.items():
#     if i==1:
#         mi_diccionario[k]="ROJO"
#     i+=1
# print(mi_diccionario)

# mi_lista = [12,"Deivid",True,"Matute",[1,2,3],7.77]
# print(mi_lista[:])

import random

def crear_lista(num):
    return ([[random.randrange(x+1) for y in range(1,x+1)] for x in range (1,num+1)])

print (crear_lista(5))