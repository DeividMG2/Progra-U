codigosAnsi=("\033[1;33m", "\033[94m", chr(27)+"[2J")
print(codigosAnsi[2])
print(codigosAnsi[0]+"Juan\n"+codigosAnsi[1])


#Más combinaciones de colores: 

# print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo") 
# print("\033[4;35m"+"Texto en negrita y subrayado de color morado\n") 
# print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
# print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m') 
# print("\033[;36m"+"Texto normal de color cian")
# print("\033[4;35;47m"+"Texto subr morado sobre blanco"+'\033[0;m') 
# print("\033[4;35m"+"Texto normal subr color morado"+'\033[0;m')

print("Titulo")
#Abajo se ejemplifica el uso de subtitulo identado.
print("\t1) Subtitulo Identado")
