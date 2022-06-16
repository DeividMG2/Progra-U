.model small
.stack
.data 
    msg db 'Hola Mundo ',13,10,'$' 
    msg2 db 'Adios',13,10,'$' 
    mayor db 'Mayor ',13,10,'$' 
    igual db 'Iguales',13,10,'$'
    msg3 db 'Ingrese un numero','$'    
    num db 0
    num2 db 0
    x db 2
    y db 3
.code

mov ax,@data  
mov ds,ax
    
    
      
;    ;interrupcion para imprimir
;    mov dx, offset msg
;    mov ah, 9
;    int 21h 
;    
;    lea dx, msg2
;    mov ah, 9
;    int 21h 
;    
;    xor ax,ax
;    mov ah,4 ; ah=4 
;    MOV BL,2
;    add ah,bl 
;    mov num,ah 
;    
;    mov dl,num 
;    add dl,30h
;    mov ah,02
;    int 21h 
;    
;    lea dx, msg3
;    mov ah, 9
;    int 21h   
;    
;    mov ah, 1
;	int 21h 
;	sub al,30h
;	mov num2, al    
	
	mov al,y
	mul x   
	
	cmp al,6
	je iguales
	jg mayores
	jmp salir
	
	
	iguales: 
	lea dx, igual
    mov ah, 9
    int 21h 
	
	jmp salir
	
	mayores: 
	lea dx, mayor
	mov ah, 9
    int 21h 
    
salir:
end     
    
    