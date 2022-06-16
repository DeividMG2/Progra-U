.model small
.data 
;letra db ''
mens db 'El caracter ingresado es S.',10,13,'$'
.code 
mov ax, @data; Esto y lo de abajo es para que se ubique bien las variables
mov ds,ax

mov ah,1
int 21h
;mov letra al;Asigna el valor a la variable

cmp al,'S'
je seguir
jne salir

seguir:    
    mov ah,09; Para escribir
    lea dx,mens ;Leer mens
    int 21h; Interrupcion para escribir con servicio 09
    
salir:
.exit   
