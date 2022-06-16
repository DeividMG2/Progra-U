class personas ():
    nombre=None
    apellido1 = None
    apellido2 = None
    cedula = None
    iz=None
    der=None

    def __init__(self,nombre,apellido1, apellido2, cedula) -> None:
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.cedula = cedula

    def insertar (self,n,a1,a2,c):
        """Insertar datos al arbol
        Args
        -n: (string) Nombre a insertar
        -a1: (string) Primer apellido a insertar
        -a2: (string) Segundo apellido a insertar
        -c: (string) Nombre a insertar
        """
        nn=personas(n,a1,a2,c)
        self.__insertar(self,nn)
    
    def __insertar(self,raiz,nn):
        """Metodo para insertar los datos
        Args
        -raiz : (clase personas) Raiz
        -nn: (clase personas) Nuevo nodo
        """
        if (raiz.nombre>nn.nombre):
            if raiz.iz==None:
                raiz.iz=nn
            else:
                self.__insertar(raiz.iz,nn)
                
        elif (raiz.nombre==nn.nombre):
            if (raiz.apellido1>nn.apellido1):
                if raiz.iz==None:
                    raiz.iz=nn
                else:
                    self.__insertar(raiz.iz,nn)
            elif (raiz.apellido1==nn.apellido1):
                if (raiz.apellido2>nn.apellido2):
                    if raiz.iz==None:
                        raiz.iz=nn
                    else:
                        self.__insertar(raiz.iz,nn)
            else:
                if raiz.der==None:
                    raiz.der=nn
                else:
                    self.__insertar(raiz.der,nn)
        else:
            if raiz.der==None:
                raiz.der=nn
            else:
                self.__insertar(raiz.der,nn)

    def imprimir_ascendiente(self):
        self.__imprimir_ascendiente(self)

    def __imprimir_ascendiente(self,raiz):
        """Metodo para imprimir nombres de forma ascendente

        Args:
            raiz (clase persona): Raiz para ver los datos
        """
        if raiz!=None:
            self.__imprimir_ascendiente(raiz.iz)
            print(f'{raiz.nombre} {raiz.apellido1} {raiz.apellido2}')
            self.__imprimir_ascendiente(raiz.der)
                    
    def imprimir_descendiente(self):
        """Metodo para imprimir nombres de forma descendiente

        Args:
            raiz (clase persona): Raiz para ver los datos
        """
        self.__imprimir_descendiente(self)

    def __imprimir_descendiente(self,raiz):
        if raiz!=None:
            self.__imprimir_descendiente(raiz.der)
            print(f'{raiz.nombre} {raiz.apellido1} {raiz.apellido2}')
            self.__imprimir_descendiente(raiz.iz)



    def busqueda(self,e):
        """Metodo para buscar persona en el arbol

        Args:
            e (string): Nombre que se buscará
        """
        tupla = ()
        if self.__busqueda(self,e,tupla)[0]:
            return self.__busqueda(self,e,tupla)[1]
        else:
            return "No Encontramos los datos"

    def __busqueda(self,raiz,e,t):
        if raiz!=None:
            if raiz.nombre==e:
                t = (raiz.cedula,raiz.nombre,raiz.apellido1,raiz.apellido2)
                return [True,t]
            else:
                if raiz.nombre>e:
                    return self.__busqueda(raiz.iz,e,t)
                else:
                    return self.__busqueda(raiz.der,e,t)
        else:
            return [False]

# +++ Agrego los datos +++
persona=personas("Deivid","Perez","Rojas","202830401")
persona.insertar("Lucas","Acuña","Lopez","208170293")
persona.insertar("Pedro","Jimenez","Mora","201170194")
persona.insertar("Sofia","Araya","Guevara","209890130")
persona.insertar("Carlos","Soto","Solis","208370281")
persona.insertar("Emilio","Juarez","Hernández","208390129")
persona.insertar("Ana","Zuñiga","Salazar","208370293")
persona.insertar("Ana","Lopez","Salazar","208370293")
persona.insertar("Rodrigo","Fernández","Duarte","203980993")
persona.insertar("Berny","Artavia","Montero","201820901")

# +++ Impresion de forma ascendiente +++
print("Nombres Ordenados Descendientes\n")
persona.imprimir_ascendiente()
print("")
# +++ Impresion de forma descendiente +++
print("Nombres Ordenados Ascendientes\n")
persona.imprimir_descendiente()
print("")

# +++ Busqueda de persona +++
nombre = input("Ingrese el nombre del la persona que desea buscar: ")

print(f"""\n
Resultados de la busqueda: 
    {persona.busqueda(nombre)}
      """)

