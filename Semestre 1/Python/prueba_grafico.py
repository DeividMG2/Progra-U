from matplotlib.pyplot import fill
from tkinter import *
from tkinter import Canvas

ventana = Tk()

#Canvas
canvas=Canvas(ventana,width=650,height=400)
canvas.pack()

#Se crean las lineas (los costados) del grafico
canvas.create_line(100,50,100,300,fill="#222",width=3)
canvas.create_line(100,300,450,300,fill="#222",width=3)

#Porcentaje de la emoción presentada
canvas.create_text(50, 90, font=('Arial',10,'bold italic'), fill="#222", text="100%")
canvas.create_line(100,90,400,90,fill="#222",width=3)
canvas.create_text(50, 140, font=('Arial',10,'bold italic'), fill="#222", text="75%")
canvas.create_line(100,140,400,140,fill="#222",width=3)
canvas.create_text(50, 190, font=('Arial',10,'bold italic'), fill="#222", text="50%")
canvas.create_line(100,190,400,190,fill="#222",width=3)
canvas.create_text(50, 240, font=('Arial',10,'bold italic'), fill="#222", text="25%")
canvas.create_line(100,240,400,240,fill="#222",width=3)
canvas.create_text(50, 290, font=('Arial',10,'bold italic'), fill="#222", text="0%")

#Tiempos de registros de la actividad estimada
def imprimir_tiempos(m,s):
    """Imprime los valores de la recta horizontal del grafico

    Args:
        m (int): Numero de los minutos
        s (int): Numeros de los segundos registrados
    """
    if m==0:
        rango = int(1.5*s/10)
        aux = rango
        valor_x = 150
        valor_y = 320
        for i in range(1,(s+1)):
            if i==aux:
                aux+=rango
                canvas.create_text(valor_x, valor_y, font=('Arial',10,'bold italic'), fill="#222", text=i)
                # canvas.create_line(valor_x,300,valor_x,50,fill="#220de0",width=3)
                valor_x+=50        
    
imprimir_tiempos(0,180)

def crear_estructura():
    canvas.create_line(100,300,150,90,fill="#222",width=3)
    canvas.create_line(150,90,200,300,fill="#222",width=3)
    canvas.create_line(200,300,250,90,fill="#222",width=3)
    canvas.create_line(250,90,300,300,fill="#222",width=3)
    canvas.create_line(300,300,350,90,fill="#222",width=3)
    canvas.create_line(350,90,400,300,fill="#222",width=3)


crear_estructura()

def emocion_act(acti):
    try:
        with open("./Proyecto_Fase_3/datos/emociones_actividad.txt","tr") as lector:
            act=lector.readline()[:-1]
            emocion1=lector.readline()[:-1]
            nivel1=lector.readline()[:-1]
            emocion2=lector.readline()[:-1]
            nivel2=lector.readline()[:-1]
            emocion3=lector.readline()[:-1]
            nivel3=lector.readline()[:-1]
            aux = lector.readline()[:-1]
            if act==acti:                
                    return [nivel1,nivel2,nivel3]
            if aux == '':
                return "Nada"
            while (aux!=''):
                act=aux
                emocion1=lector.readline()[:-1]
                nivel1=lector.readline()[:-1]
                emocion2=lector.readline()[:-1]
                nivel2=lector.readline()[:-1]
                emocion3=lector.readline()[:-1]
                nivel3=lector.readline()[:-1]
                if act==acti:                
                    return [nivel1,nivel2,nivel3]
                if (lector.readline()[:-1]!=''):
                    return "Nada"
                
    except:
        print("Error")

# print(emocion_act("Dormir"))

ventana.mainloop()







# 0%: 
#     'UNKNOWN', 
#     'VERY_UNLIKELY', 
# 25%:
#     'UNLIKELY', 
# 50%:    
#     'POSSIBLE', 
# 75:    
#     'LIKELY', 
# 100%
#     'VERY_LIKELY'