from random import random, randrange
from tkinter import N

# mi_lista= [randrange (1000000) for e in range(1,10000)]
mi_lista= [20,4,2,5,7,8,5,4,3,7,8,11,43,24,64,112,432,56]
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

    def recorrer(self,raiz):
        if raiz!=None:
            print(raiz.valor)
            self.recorrer(raiz=raiz.iz)
            self.recorrer(raiz=raiz.der)
        
    def existe(self,raiz,valor,respuesta):
        if respuesta!="":
            return respuesta
        if raiz!=None:
            if valor==raiz.valor:
                self.existe(raiz=raiz.iz,valor=valor,respuesta="Si existe el numero "+str(valor))
                self.existe(raiz=raiz.der, valor=valor,respuesta="Si existe el numero "+str(valor))
            else:
                self.existe(raiz=raiz.iz,valor=valor,respuesta="")
                self.existe(raiz=raiz.der, valor=valor,respuesta="")
        
            
            
mi_arbol=arbol_b(mi_lista[0])

for e in mi_lista[1:]:
    mi_arbol.insertar(e)
    
print(mi_arbol.existe(raiz=mi_arbol,valor=4,respuesta=''))

pass