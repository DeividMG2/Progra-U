#Clase Perona
class persona():
    nombre = None
    telefonos = []

    def __init__(self, n, t):
        self.nombre = n
        self.telefonos = t
    
    def getter(self):
        return [self.nombre, self.telefonos]

    #Funcion Recursiva
    def imprimirPersona(self,l):
        try: 
            print(f"Nombre de la persona: {l[0].nombre}\n{len(l[0].telefonos)} teléfonos asociados: {l[0].telefonos}")
            self.imprimirPersona(l[1:])
        except:
            pass
#Personas
p1 = persona("Deivid",["87983402","78658890"])
p2 = persona("David",["88374402","82234190","81226300"])
p3 = persona("Daniela",["74435602"])
p4 = persona("Dennis",["81183402","72358890"])
p5 = persona("Dylan",["80983402","70658890","72126300","82738490"])
listaPersonas = [p1,p2,p3,p4,p5]

p1.imprimirPersona(listaPersonas)