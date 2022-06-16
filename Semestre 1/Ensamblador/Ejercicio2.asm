.model small
.stack
.data         
    num1 db 0
    num2 db 0
    num3 db 0
    msgN1 db 13,10,'Ingrese numero 1: ','$' 
    msgN2 db 13,10,'Ingrese numero 2: ','$'
    msgN3 db 13,10,'Ingrese numero 3: ','$'
    msgMayor1 db 13,10,'El numero mayor es el numero 1','$'
    msgMenor1 db 13,10,'El numero menor es el numero 1','$'
    msgMayor2 db 13,10,'El numero mayor es el numero 2','$'
    msgMenor2 db 13,10,'El numero menor es el numero 2','$'
    msgMayor3 db 13,10,'El numero mayor es el numero 3','$'
    msgMenor3 db 13,10,'El numero menor es el numero 3','$'
.code      

mov ax,@data
mov ds,ax

pedirNum1 macro
    mov ah,9
    lea dx,msgN1
    int 21h    
endm

pedirNum2 macro
    mov ah,9
    lea dx,msgN2
    int 21h
endm    
pedirNum3 macro            
    mov ah,9
    lea dx,msgN3
    int 21h
endm       
       
; Se crearon las macros donde lo que hace es pedir el numero y a continuacion se llaman     
pedirNum1
    
; Pasos para que el input realice su proceso de obtener un digito    
mov ah,1
int 21h                                          
mov num1,al
       
pedirNum2

mov ah,1
int 21h                                          
mov num2,al


pedirNum3

mov ah,1
int 21h                                          
mov num3,al


validacionMayor: ;Aqui se haran las validaciones para saber cual numero es el mayor

mov ch,num1 ;Se asigna num1 al ch para luego hacer las comparaciones
cmp ch,num2
jg validarMayor1

mov ch,num2
cmp ch,num3
jg validarMayor2          

mov ch,num3
cmp ch,num1
jg validarMayor3

validarMayor1: ;Esta funcion es para CONFIRMAR que el numero 1 es el mayor
cmp ch,num3
jg imprimirMayor1
jle imprimirMayor3

validarMayor2: ;Esta funcion es para CONFIRMAR que el numero 2 es el mayor
cmp ch,num1
jg imprimirMayor2
jle imprimirMayor1

validarMayor3: ;Esta funcion es para CONFIRMAR que el numero 3 es el mayor
cmp ch,num2
jg imprimirMayor3
jle imprimirMayor2

validacionMenor: ; Aqui se haran las validaciones para saber cual numero es el menor

mov ch,num1 ;Se asigna num1 al ch para luego hacer las comparaciones
cmp ch,num2
jle validarMenor1

mov ch,num2 ;
cmp ch,num3
jle validarMenor2          


validarMenor1: ;Esta funcion es para CONFIRMAR que el numero 1 es el menor
mov bh, num1
cmp bh,num3
jg imprimirMenor3
jle imprimirMenor1

validarMenor2: ;Esta funcion es para CONFIRMAR que el numero 2 es el menor
mov bh, num2
cmp bh,num1
jg imprimirMenor1
jle imprimirMenor2



     
; Impresion de los resultados
imprimirMayor1:                    
    mov ah,9
    lea dx,msgMayor1
    int 21h     
    jmp validacionMenor
             
imprimirMayor2:                    
    mov ah,9
    lea dx,msgMayor2
    int 21h     
    jmp validacionMenor
    
imprimirMayor3:                    
    mov ah,9
    lea dx,msgMayor3
    int 21h     
    jmp validacionMenor
    
imprimirMenor1:                    
    mov ah,9
    lea dx,msgMenor1
    int 21h     
    jmp salir
    
imprimirMenor2:                    
    mov ah,9
    lea dx,msgMenor2
    int 21h     
    jmp salir
    
imprimirMenor3:                    
    mov ah,9
    lea dx,msgMenor3
    int 21h     
    jmp salir
              
salir:
.exit                                                   
                                            