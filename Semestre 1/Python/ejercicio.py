# Se desea crear un sistema para ofrecer servicios express en restaurantes, cafeterías y otros negocios aplicables a la entrega de pedidos en modalidad express.

# Para ello la aplicación debe registar un listado de negocios y las distintas opciones de menú. Esta lista de establecimientos puede ser implementada con listas "python" tradicionales, pero cada elemento dentro de ella deben ser un diccionario que almacene el nombre del comercio y el menú. Cada menú asociado a cada comercio deberá ser otra lista "python" que contenga elementos de menu disponibles para la venta. Cada elemento de menú deberá ser una instancia de la clase "opcion_menu", implementada por ustedes y que contenga las propiedades categoría, nombre del platillo, descripción y el precio.

# Cree una lista de almenos 3 restaurantes con sus respectivos menus con almenos 3 opciones, y realice una función que imprima el detalles del menú para cada restaurante existente.

from time import sleep

class opcion_menu():
    categoria = None
    nombre_platillo = None
    descripcion = None
    precio = None

    def set_opcion_menu(self,c,np,d,p):
        self.categoria = c
        self.nombre_platillo = np
        self.descripcion = d
        self.precio = p

    def get_opcion_menu(self):
        return [self.categoria,self.nombre_platillo,self.descripcion,self.precio]


#Negocio 1
menu1a = opcion_menu()
menu1a.set_opcion_menu("Comida Rapida","Pollo Frito","Pollo mediano","1600")
menu1b = opcion_menu()
menu1b.set_opcion_menu("Bebidas","Coca Cola","Botella de 800ml","1000")
menu1c = opcion_menu()
menu1c.set_opcion_menu("Comida Rapida","Papas Fritas","Bolsa mediana de papas fritas","700")

#Negocio 2
menu2a = opcion_menu()
menu2a.set_opcion_menu("Comida Rapida","Papas Fritas","Papas fritas jugosas","1200")
menu2b = opcion_menu()
menu2b.set_opcion_menu("Comida Rapida","Pollo Frito","3 Pedazos de pollo","2000")
menu2c = opcion_menu()
menu2c.set_opcion_menu("Comida Rapida","Hamburgesa","Hamburguesa grande de pollo","2200")

#Negocio 3
menu3a = opcion_menu()
menu3a.set_opcion_menu("Pan","Pan Blanco","Papas fritas jugosas","1200")
menu3b = opcion_menu()
menu3b.set_opcion_menu("Bebidas","Café negro","Vaso grande de café negro","1200")
menu3c = opcion_menu()
menu3c.set_opcion_menu("Bebidas","Capuccino","Vaso grande de capuccino","1200")



negocios_menu=[
    {"nombre_comercio": "KFC", "menu":[menu1a.get_opcion_menu(),menu1b.get_opcion_menu(),menu1c.get_opcion_menu()]},
    {"nombre_comercio": "Restaurante Dorado", "menu": [menu2a.get_opcion_menu(),menu2b.get_opcion_menu(),menu2c.get_opcion_menu()]},
    {"nombre_comercio": "Tía Panchita", "menu": [menu3a.get_opcion_menu(),menu3b.get_opcion_menu(),menu3c.get_opcion_menu()]}
]

def mostrar_menu(index):
    print("Menú Disponible")
    for i in negocios_menu[index]["menu"]:
        print(f"""
        Categoría: {i[0]}
        Platillo: {i[1]}
        Descripción: {i[2]}
        Precio: {i[3]}
        """)
        sleep(1)

def menu():
    opcion=int(input(
"""
**** A cual comercio desea ir? ****
        
        1. KFC
        2. Restaurante Dorado
        3. Tía Panchita 
"""
    ))
    print(f'\nBienvenido a "{negocios_menu[opcion-1]["nombre_comercio"]}" Abajo verás el menu\n')
    sleep(2)
    index = opcion-1
    mostrar_menu(index)
menu()

volver = int(input(
    """
**** Desea ir a otro negocio? ****
        
        1. Si
        2. No (salir) 
"""
    ))
while volver==1:
    menu()
    volver = int(input(
    """
**** Desea ir a otro negocio? ****
        
        1. Si
        2. No (salir) 
"""
    ))
    
