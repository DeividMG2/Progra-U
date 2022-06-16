clave=0
original = 0
valor=0
def cifrar(num):
    global clave
    global original
    global valor
    suma=0
    original = num
    n=num
    while(n>0):
        suma+=(n%10)
        n//=10
        print(suma)
    clave=suma%10
    nuevoNum=0
    numero=num
    exponente=0
    while(numero>0):
        ultimo=numero%10
        numero//=10
        nuevoNum+=((ultimo+clave)%10)*(10**exponente)
        exponente+=1
    descifrado=nuevoNum*10+clave
    divisor=1*10**(exponente+1)
    resultado=descifrado/divisor
    valor=exponente
    return(resultado)
print(cifrar(77635245))

def descifrar(numCifrado): # return factorial
    global clave
    global valor
    descifrando=True
    n = numCifrado%10
    nuevoNum=0
    ex=valor
    while(descifrando):
    	print(nuevoNum)
    	n=n*10
    	nuevoNum+=(clave-int(n%10))*10**ex
    	ex-=1
    	if(ex==10):
    		break
descifrar(0.665241349)




# Por ejemplo si recibimos el número 77635245 -> la clave de cifrado sería 7+7+6+3+5+2+4+5=39 donde 9 por ser la última cifra se toma como clave de cifrado.
# Conociendo la clave se procede a cifrar el número, procedimiento que consiste en sumarle la clave de cifrado a cada dígito, si esta suma es mayor o igual que 10 se mantiene únicamente la última cifra.
# Por ejemplo: 
# Número a cifrar = 77635245
# clave de cifrado = 9
# pPor ejemplo: 
# Número a cifrar = 77635245
# clave de cifrado = 9
# Ejemplo final: 

# cifrar(77635245)=0.665241349 donde la parte azúl representa el número cifrado y la parte en rojo es la clave de cifrado, y en negro el "0." es utilizado para evitar que el cifrado deje 0's a la izquierda que produzcan pérdidas de datos.
# descifrar(0.665241349)=77635245 donde la parte azúl representa el número cifrado y la parte en rojo es la clave de cifrado

# Supuestos y restricciones:

# Los parámetros de entrada debe ser únicamente un valor numérico
# Debe aparecer todos los métodos que le permitiesen llegar a la solución planteada.
# No se permite transformar el número recibido a cadenas de caracteres, listas u otro tipo de datos.
# El retorno del algoritmo de cifrado debe ser un número fraccionado y el resultado del algoritmo de descrifrado debe ser unnúmero entero positivo.