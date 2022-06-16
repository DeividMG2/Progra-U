def invertirDigitos(numero,d1,d2):
    invertido = False
    cont = 0
    num=numero
    nuevoNumero=0
    while(num>0):
        cont+=1
        num = num//10
    while(not invertido):
        valor=10**(cont-1)
        digito=numero//valor
        numero = numero - (valor*digito)
        cont-=1
        if(digito==d1):
            nuevoNumero = nuevoNumero + (valor*d2)
        elif(digito==d2):
            nuevoNumero = nuevoNumero + (valor*d1)
        else:
            nuevoNumero = nuevoNumero + (valor*digito)
        if(cont==0):
            invertido=True
    return nuevoNumero
print(invertirDigitos(1230,2,3))