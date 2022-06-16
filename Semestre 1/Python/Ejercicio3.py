class plano:
    id=None
    finca=None
    plano=None
    area=None
    direccion=None
    iz=None
    der=None

    def __init__(self,plano) -> None:
        """Constructor de plano
        args:
        - plano : diccionario con las claves 'fid','finca','plano','area' y 'direccion'. Si el área no tiene un formato entero se asume un 0.
        """
        self.id=plano["fid"]
        self.finca=plano["finca"]
        self.plano=plano["plano"]
        try:
            self.area=int(plano["area"])
        except:
            self.area=0
        self.direccion=plano["direccion"]

    def insertar(self,nuevo_plano):
        """Inseración en el arbol
        args:
        - nuevo_plano : diccionario con las claves 'fid','finca','plano','area' y 'direccion'
        """
        self.__insertar(self,nuevo_plano)

    def __insertar(self,raiz,nuevo_plano):
        """Inseración recursiva en el arbol
        args:
        -raiz : puntero actual del nodo del arbol recorrido
        -nuevo_plano : diccionario con las claves 'fid','finca','plano','area' y 'direccion'
        """
        if raiz.finca==nuevo_plano['finca']:
            nuevo_plano=raiz.iz
            raiz.iz=nuevo_plano
        elif raiz.finca>=nuevo_plano['finca']:
            if raiz.iz==None:
                nuevo_nodo=plano(nuevo_plano)
                raiz.iz=nuevo_nodo
            else:
                self.__insertar(raiz.iz,nuevo_plano)
        else:
            if raiz.der==None:
                nuevo_nodo=plano(nuevo_plano)
                raiz.der=nuevo_nodo
            else:
                self.__insertar(raiz.der,nuevo_plano)
    
    def imprimirAtributosPlano(self,raiz,valor):
        if raiz!=None:
            if raiz.plano==valor:
                print(f"Id: {raiz.id} \nFinca: {raiz.finca} \nPlano:{raiz.plano} \nArea: {raiz.area} \nDireccion: {raiz.direccion}")
            self.imprimirAtributosPlano(raiz.iz,valor)
            self.imprimirAtributosPlano(raiz.der,valor)
        

    def totalArea(self,raiz,distrito):
        global total_area
        if raiz!=None:
            if distrito in raiz.direccion:
                total_area+=raiz.area
            else: 
                self.totalArea(raiz.iz,distrito)
                self.totalArea(raiz.der,distrito)
            return total_area
        
    # def reordenarXFinca():
        # Realice un método que reorganice el árbol de modo que quede ordenado por el atributo "finca" y no por el # de plano como originalmente está planteado. (5 pts)

#abre el archivo de datos de planos catastrados de la provincia de Alajuela
file=open('catastro.dat')

#Crea una lista de registros de datos de planos catastrados de la provincia de Alajuela leido del archivo
lista_datos=eval(file.read())

# Inicializa el nodo raiz del árbol con el primer elemento en la lista de planos
arbol_planos=plano(lista_datos[0])

#Inserta los planos en una estructura tipo árbol basado en el atributo Plano
for p in lista_datos[1:]:
    arbol_planos.insertar(p)

#Plano del tec:A_1743586_2014
total_area = 0
print("\n+++++++++++++++++\n")
arbol_planos.imprimirAtributosPlano(arbol_planos,"A_1743586_2014")
area = arbol_planos.totalArea(arbol_planos,"QUESADA")
print("\n+++++++++++++++++\n")
print(f"El total del area es de {area}")
print("\n+++++++++++++++++\n")