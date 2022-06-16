
#Determine la profundidad de una lista de Pyhton. profundidad ([[1] , [ 2, 3, [4, [5], 6], 7], 8 ]) -> 4 (el 5 esta en la la sublista mas profunda de la lista, por ese se retorna un 4 dado que se esta a un nivel de 4 sublistas de profundidad.)
def profundidad (l):
    if not type(l)==list:
        return 0
    elif len(l)==0:
        return 1
    else:
        prof1=1+profundidad(l[0])
        profn=profundidad(l[1:])
        if prof1>profn:
            return prof1
        else:
            return profn

"""
print(profundidad (1))
print(profundidad ([]))
print(profundidad ([1]))
print(profundidad ([[[[[1]]]]]))
print(profundidad ( [[[[[1]]]], [[[[[[2]]]]]]] ))
print(profundidad ([[1] , [ 2, 3, [4, [5], 6], 7], 8, [[],[[]],[[["x"]]]] ]))
"""

class lista:
    sig=None

    def insertar (self,p):
        self.__insertar(self,p)
    
    def __insertar (self,l,p):
        if l.sig==None:
            l.sig=p
        else:
            self.__insertar(l.sig,p)

    def obtener (self,pos):
        return(self.__obtener(self,pos))
    
    def __obtener (self,l,pos):
        if pos==0:
            return (l)
        else:
            return (self.__obtener(l.sig,pos-1))

    def imprimir(self):
        self.__imprimir(self)
    
    def __imprimir (self,l):
        if l.sig==None:
            print (l.__str__())
        else:
            print (l.__str__())
            self.__imprimir(l.sig)


class cCarrera(lista):
    nombre=None
    def __init__(self,nombre):
        self.nombre=nombre
    
    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}")


carreras=cCarrera("Ingeniería en Computación")
carreras.insertar(cCarrera("Ingeniería en Electrónica"))

##Realice una clase "persona" que contenga nombre y un listado de números de telefonos de personas. 
# Cree una lista de personas con valores aleatorios y realice una función recursiva que recorra la lista de personas 
# e imprima para cada elemento el nombre y el total de sus teléfono 
#   (función interna en la lista que debe implementarse de igual manera de forma recursiva)
class persona (lista):

    nombre=None
    telefonos=None
    carrera=None

    def __init__(self,nombre,lt):
        self.nombre=nombre
        self.telefonos=lt

    def cant_telefonos (self):
        return self.__cant_telefonos(self.telefonos)

    def __cant_telefonos (self,l):
        if l==[]:
            return 0
        else:
            return 1+self.__cant_telefonos(l[1:])
    
    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} cantidad de telefonos: {self.cant_telefonos()}")


if __name__=="__main__":

    #Crea lista de personas
    personas=persona("Pedro",["2222-2222","2222-2223"])
    personas.insertar(persona("Maria", []))
    personas.insertar(persona("Ana", ["2222-1111","2222-1112","2222-1113"]))
    personas.insertar(persona("Raul", ["1111-1111","1111-1112"]))
    personas.insertar(persona("Rita", ["5555-5555"]))

    #La cambia nombre a un registro particular
    temp=personas.obtener(2)
    temp.nombre="Ana Maria"

    #Imprime listas de personas y cursos
    personas.imprimir()
    carreras.imprimir()

    #Relacionando instancias por referencia
    personas.carrera=carreras.obtener(1)
    personas.sig.carrera=carreras.obtener(0)

    #Cambios de atributos por referencia de objetos
    carreras.obtener(1).nombre="Ing electrónica"

    pass