# Se requiere determinar cual de de dos fechas recibidas es mayor

# Ejemplo: formato de función fecha_mayor(d1,m1,a1,d2,m2,a2) d1: día1, m1: mes1, a1: año1, d2: día2, m2: mes2, a2: año2,

# fecha_mayor(7,3,2021,25,3,2021) -> "25-3-2021"

def verificarFecha(d1,m1,a1,d2,m2,a2):
    if(a1==a2):
        if(m1>=m2):
            if(d1>=d2):
                print(d1,"-",m1,"-",a1)
            else:
                print(d2,"-",m2,"-",a2)
        else:
            print(d2,"-",m2,"-",a2)
        
    elif(a1>a2):
        print(d1,"-",m1,"-",a1)
    else:
        print(d2,"-",m2,"-",a2)
verificarFecha(26,3,2021,25,3,2021)