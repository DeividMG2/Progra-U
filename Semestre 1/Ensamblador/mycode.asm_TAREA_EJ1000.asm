.model small
.stack
.data  
    msg1 db 'Ingrese numero 1: ','$'
    num1 db 0
    line db 13,10,'$'               
    msg2 db 'Ingrese numero 2: ','$'
    num2 db 0         
    msg3 db 13,10,'El resultado es: ','$'
    result db 0,'$'  
    numMayor db 13,10,'El resultado de la suma es mayor que 10','$'
.code         

mov ax,@DATA        
mov ds,ax

pedirNum macro
    mov ah, 1
	int 21h
endm        

    ;Solicito el numero 1
    lea dx, msg1
    mov ah, 9
    int 21h
    
pedirNum
mov num1,al
           
    ;Imprimo el salto de linea
    lea dx, line
        mov ah, 9
        int 21h
                         
    ;Solicito el numero 2                         
    lea dx, msg2
    mov ah, 9
    int 21h

pedirNum   
mov num2,al              
    xor ax,ax
    xor bx,bx
    ;Valido cual es mayor  
    mov al,num1
    mov bl,num2
    sub al,30h
    sub bl,30h
    cmp al,bl
    jg division
    je salir
    jmp suma
            

division:
    mov ah,00
    div bl      
    
    mov result,al
    
    lea dx,msg3 
    mov ah, 9
    int 21h      
            
    jmp imprimirResult
    
       
suma:   
          
    add al,bl
    mov result,al
    cmp result,0Ah
    jge mayor 
    jl imprimirResult
    
imprimirResult: 
lea dx,msg3 
mov ah, 9
int 21h
add result,48
lea dx,result 
mov ah, 9
int 21h
jmp salir

mayor:
lea dx,numMayor
mov ah, 9
int 21h

       
salir:
    end 
