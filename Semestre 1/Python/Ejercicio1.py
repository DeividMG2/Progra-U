def ver_anterior(num):
    """Funcion para ver el numero fibonacci anterior a un numero N
    arg:
    num (int): Numero al que le quiero averiguar el numero fibonacci anterior
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    a = 0
    b = 1
    c = None
    while (a+b) < num:
        c = a+b
        b=a
        a=c
    return c
def imprimir_fibonacci(a,b):
    """Funcion recursiva para imprimir serie de numeros fibonacci entre 2 numeros
    args:
    a (int) Primer valor del rango (Inicio)
    b (int) Segundo valor del rango (Final)
    """
    numero = ver_anterior(a) + a
    if numero < b:
        print(numero,end=" ")
        imprimir_fibonacci(numero,b)
    
imprimir_fibonacci(5,40)