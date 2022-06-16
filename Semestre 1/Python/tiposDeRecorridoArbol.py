# from tiempo import rendimiento
# r=rendimiento()


from random import random, randrange


mi_lista= [randrange (1000000) for e in range(1,20)]
mi_arbol=None

class arbol_b ():
    valor=None
    iz=None
    der=None

    def __init__(self,valor) -> None:
        self.valor=valor

    def insertar (self,valor):
        """Inserta un valor numérico dentro de un arbol binario
        Args
        -valor: (int) Valor a insertar
        """
        nn=arbol_b(valor)
        self.__insertar(self,nn)
    
    def __insertar(self,raiz,nn):
        """Inserta recursivamente sobre un arbol binario
        Args
        -raiz : (arbol_b) Raiz del arbol
        -nn: (arbol_b) nuevo nodo a insertar
        """
        if (raiz.valor>nn.valor):
            if raiz.iz==None:
                raiz.iz=nn
            else:
                self.__insertar(raiz.iz,nn)
        else:
            if raiz.der==None:
                raiz.der=nn
            else:
                self.__insertar(raiz.der,nn)

    def imprimir_en_orden(self):
        self.__imprimir_en_orden(self,'')

    def __imprimir_en_orden(self,raiz,separador):
        if raiz!=None:
            print(f'{separador}{raiz.valor}')
            separador+=".."
            self.__imprimir_en_orden(raiz.iz,separador)
            self.__imprimir_en_orden(raiz.der,separador)

    def imprimir_preorden(self):
        self.__imprimir_preorden(self)

    def __imprimir_preorden(self,raiz):
        if raiz!=None:
            self.__imprimir_preorden(raiz.iz)
            print(raiz.valor)
            self.__imprimir_preorden(raiz.der)

    def imprimir_posorden(self):
        self.__imprimir_posorden(self)

    def __imprimir_posorden(self,raiz):
        if raiz!=None:
            self.__imprimir_posorden(raiz.der)
            print(raiz.valor)
            self.__imprimir_posorden(raiz.iz)


mi_arbol=arbol_b(mi_lista[0])

for e in mi_lista[1:]:
    mi_arbol.insertar(e)

#mi_arbol.imprimir_en_orden()
#mi_arbol.imprimir_preorden()
mi_arbol.imprimir_posorden()
pass 