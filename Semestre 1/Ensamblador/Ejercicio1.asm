.model small
.stack
.data
    msg db 'Ingrese un numero (Presione Enter Para Ver El Resultado): ','$' 
    msgImpar db 13,10,'El numero es impar','$'
    msgPar db 13,10,'El numero es par','$'
    num1 dw 0    
.code
mov ax,@data
mov ds,ax

;Interrupcion para solicitar el numero
       
imprimirInput:
lea dx, msg
mov ah,9
int 21h

pedirNum:
mov bl,al ;Guardo el ultimo digito en BL para luego hacerle la operacion a este digito.
mov ah,1
int 21h    
             
cmp al,0Dh
jne pedirNum


;Asigno el valor obtenido a la variable y a ax
mov ah,00h
mov num1,bx ;Le asigno a la variable el ultimo digito
sub num1,30h;Le resto los 30 para obtener el valor numerico
mov ax,num1


;Uso el 2 para ver si el residuo es 1 o 0
mov bl,2
div bl   

;Comparo el residuo                    
cmp ah,01h
je impares
cmp ah,00h
je pares
jmp salir
        
;Imprimo que es impar        
impares:
lea dx, msgImpar		
mov ah,9
int 21h
jmp salir                

;Imprimo que es Par
pares:
lea dx,msgPar
mov ah,9
int 21h 
jmp salir

salir:
.exit
