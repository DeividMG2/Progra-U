.model small
.data
    msj db 'Ingrese una cadena: $'
    string db 10 dup (?), '$'
.code
    mov ax,@data
    mov ds,ax
   
mov cx,10
mov di,0

leer: mov ah,1
      int 21h
      cmp al,13
      je imprimir
      mov string[di],al
      inc di
    loop leer
   
imprimir:
lea dx,string
mov ah,9
int 21h
.exit