def comprobarDigitos(numero1, numero2):
	resultado = True
	num = 0
	while ((numero1!=0) & (numero2!=0)):
		num = (numero1%10)+(numero2%10)
		numero1 = numero1 // 10
		numero2 = numero2 // 10
		if((numero1!=0)&(numero2!=0)&(num!=(numero1%10)+(numero2%10))):
			resultado = False
	return(resultado)
print(comprobarDigitos(13,31))