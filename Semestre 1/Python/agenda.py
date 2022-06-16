"""
Mi agenda:
1) Nombre
2) Apellido1
3) Apellido2
4) Opcional listado de Telefonos (unicos - no se pueden repetir)
5) Opcional listado de Correos (unicos - no se pueden repetir)
6) Cedula inmutable (No se puede modificar)
7) usuario y contraseña (El usuario es inmutable clave esta cifrada)
8) Pueden agragarse multiples atributos adicionales
"""

import utils
clave1="Steph12345"
clave1=utils.cifrar(clave1)

clave2="Alex123G4?_"
clave2=utils.cifrar(clave2)


miAgenda=[{"nombre":"Stephanie","apellido1":"Matute","apellido2":"Guerrero","telefonos":{},"correos":{"stephanie07@gmail.com"},"cedula":tuple(('2876899')),"usuario":{"st2003"},"password":clave1},{"nombre":"Alejandro","apellido1":"Rodriguez","apellido2":"Navarro","telefonos":(85678345,87689087),"correos":{"stephanie07@gmail.com"},"cedula":tuple(("2876819")),"usuario":{"alex123"},"password":clave2}]

for e in miAgenda:
    for key,value in e.items():
        print(key,value)

