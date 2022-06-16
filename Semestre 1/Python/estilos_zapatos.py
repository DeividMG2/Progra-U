def combinaciones_estilos(t):
    """Esta funcion devuelve una lista con el total de combinaciones de estilos de zapatos
    
    args:
        t (tupla): Contiene los colores, materiales y tallas de los zapatos
    """
    combinaciones = []
    tam_colores = len(t['colores'])
    tam_material = len(t['material'])
    tam_tallas = len(t['tallas'])
    cont_color = 0
    cont_material = 0
    cont_talla = 0
    tam = tam_colores*tam_material*tam_tallas
    for i in range(tam):
        if not([t['colores'][cont_color],t['material'][cont_material],t['tallas'][cont_talla]] in combinaciones):
            combinaciones.append([t['colores'][cont_color],t['material'][cont_material],t['tallas'][cont_talla]])
        cont_color+=1
        if cont_color==tam_colores:
            cont_material+=1
            cont_color=0
        if cont_material==tam_material:
            cont_color=0
            cont_material=0
            cont_talla +=1
    return combinaciones
estilos=({'colores':['blanco', 'negro', 'Cafe','Rojo'],'material':['cuero','Vinilo'],'tallas':[29,32,35,42]})
for i in combinaciones_estilos(estilos):
    print(i)

