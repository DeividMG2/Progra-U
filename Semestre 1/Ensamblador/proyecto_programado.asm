include "emu8086.inc"
org 100h
.model small
.stack
.data
    
;    matrizq db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
;           db 10 dup (0)
    matriz db 2 dup (0)
           db 2 dup (0)
.code                             
xor ax,ax
xor bx,bx
xor cx,cx
mov si,0     
mov ax,@data
mov ds, ax
 
;+++++++++++ Clic (der o izq) en lugar determinado +++++++++++



;+++++++++++ Reproducir sonido +++++++++++

;main proc
;    mov ah,2
;    mov dl,7        
;    int 21h
; 
;    exit:
;    mov ah,4ch
;    int 21h
;    main endp
;end main

;+++++++++++ Crear una matriz +++++++++++

llenado:
    ;print "Ingrese valor de la posicion "
    print "P "
    mov ax,bx
    call print_num
;    print " de la matriz: "
    print ": "
    inc bx
    call scan_num
    printn ""
    mov ax,cx
    mov matriz[si],al
    inc si
    cmp bx,2
    jne llenado
    mov bx,0
    mov si,0
    ret


;+++++++++++ Establecer tiempo +++++++++++



;+++++++++++ Numero aleatorio (posicion) +++++++++++

;RANDGEN:         ; generate a rand no using the system time
;RANDSTART:
;   MOV AH, 00h  ; interrupts to get system time        
;   INT 1AH      ; CX:DX now hold number of clock ticks since midnight      
;
;   mov  ax, dx                 
;   xor  dx, dx
;   mov  cx, 10    
;   div  cx       ; here dx contains the remainder of the division - from 0 to 9
;
;   add  dl, '0'  ; to ascii from '0' to '9'
;   mov ah, 2h   ; call interrupt to display a value in DL
;   int 21h    

;+++++++++++ Opcion de salir +++++++++++



;+++++++++++ Opcion de reiniciar +++++++++++



;+++++++++++ Mostrar EN TODO MOMENTO nickname con puntacion +++++++++++



;+++++++++++ Actualizar datos +++++++++++
                          
define_print_string 
define_print_num
define_print_num_uns
define_scan_num                   