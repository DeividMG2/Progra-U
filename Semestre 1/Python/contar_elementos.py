class elemento_persona:
    nombre:None
    siguiente:None

    def __init__(self,nombre):
        self.nombre=nombre
        self.siguiente=None
    def adjuntar (self,nombre):
        np=elemento_persona(nombre)
        np.siguiente=None
        actual=self

        while actual.siguiente!=None:
            actual=actual.siguiente

        actual.siguiente=np  
        pass      

    def push(self,nombre):
        np=elemento_persona(self.nombre)
        self.nombre=nombre
        np.siguiente=self.siguiente
        self.siguiente=np
        pass

    def contar(self):
        cont=1
        actual=self
        while actual.siguiente!=None:
            actual=actual.siguiente
            cont+=1
        return(cont)

    def index (self,nombre):
        cont = 0
        actual=self
        while actual.siguiente!=None:
            if (actual.nombre == nombre):
                return(cont)
            else:
                actual = actual.siguiente
                cont += 1
        pass

    def get (self,pos):
        """Extrae el nombre de la lista en una determinada posición
        Argumentos:
            pos (int) : Posición de la lista a extraer
        returns:
        - (String) Nombre de la persona extraído de la lista
        """
        cont = 0
        actual=self
        while actual.siguiente!=None:
            if (cont == pos):
                return(actual.nombre)
            else:
                actual = actual.siguiente
                cont += 1
        pass



mi_lista_personas=elemento_persona("Karina")
mi_lista_personas.adjuntar("Maria José")
mi_lista_personas.adjuntar("Fabian")
mi_lista_personas.adjuntar("Brithanny")
mi_lista_personas.adjuntar("Yindra")
mi_lista_personas.adjuntar("Kevin")
mi_lista_personas.adjuntar("jose Armando")
mi_lista_personas.push("Deivid")

print(mi_lista_personas.index("Deivid"))

print(mi_lista_personas.get(7))


#print (f"Cantidad de elementos en la lista :{mi_lista_personas.contar()}")

pass