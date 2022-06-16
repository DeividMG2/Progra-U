from turtle import width


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


class cursos(lista):
    nombre=None
    def __init__(self,nombre):
        self.nombre=nombre
    
    def __str__(self) -> str:
        return (f"Curso: {self.nombre}")

carreras=cursos("Matematica General")
carreras.insertar(cursos("Matematica Discreta"))
carreras.insertar(cursos("Ingles I"))
carreras.insertar(cursos("Artes Visuales"))
carreras.insertar(cursos("Comunicacion Escrita"))

if __name__=="__main__":
    carreras.imprimir()
    #Cambios de atributos por referencia de objetos
    carreras.obtener(1).nombre="Ing electrónica"
    # carreras.imprimir()
    pass


#Archivos

def leer_archivo():
    try:
        with open("cursos.txt","tr") as archivo: #usando with no es necesario el open
            lector = archivo.readline()[:-1]
            while(lector != ""):
                print(lector)
                lector = archivo.readline()[:-1]
    except FileNotFoundError:
        print("Archivo no encontrado")
        opcion = input("Desea crear este archivo? (s/n): ").lower()
        if opcion == "s":
            open("cursos.txt","ta")

# leer_archivo()


# Guardar datos de los cursos en el archivo
def guardar_archivo(texto):
    try:
        with open("cursos.txt","a") as archivo:
            archivo.write(texto)
            print("Cambios Guardados")
    except FileExistsError:
        print("El archivo no existe")
        op = input("Desea crearlo? s/n: ").lower()
        if op == "s":
            open("cursos.txt")
            print("Archivo Creado")
        
# guardar_archivo("Ingles I, Matematica Discreta, Matematica General, Comunicacion Escrita, Ingles II")


#Obtener datos de archivo para usar en memoria
lista = []
def obtener_datos(l):
    try:
        with open("cursos.txt","tr") as archivo:
            archivo.seek(0)
            reader = archivo.readline()
            while (reader != "") & (reader[:-1]!= "-"):
                l.append(reader[:-1])
                reader=archivo.readline()
    except FileNotFoundError:
        print("El archivo no existe")
        op = input("Desea crearlo? s/n: ").lower()
        if op == "s":
            open("cursos.txt")
            print("Archivo Creado")
        
obtener_datos(lista)
print(
    f"""
    Usuario: {lista[0]}
    Cursos: {lista[1:]}
    """)
#guardar en archivos cursos y cargar en memorias (2 funciones)
