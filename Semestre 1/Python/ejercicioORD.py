elementos = []
def cammelCase():
    cont = 65
    variablesCammelCase = {"miSaludo":"Hola","nombrePersona":"Leonardo"}
    for k,v in variablesCammelCase.items():
        for i in k:
            result = retornarSnakeCase(k,i,cont)
            if result!="":
                if not (result in elementos):
                    elementos.append(result)

resultado = ""
def retornarSnakeCase(v,e,cont):
    global resultado
    if cont<=90:
        if ord(e)!=cont:
            retornarSnakeCase(v,e,cont+1)
        else:
            v = v.replace(e,"_"+chr(cont+32))
            resultado = v
    return resultado

cammelCase()
print("Las variables que antes eran CammelCase ahora en SnakeCase son: ")
for i in elementos:
    print(i)