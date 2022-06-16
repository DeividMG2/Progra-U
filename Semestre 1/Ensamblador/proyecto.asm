INCLUDE 'emu8086.inc'

.model small
.stack

.data 
;VARIABLES DEL JUEGO-------------------------------------------------------- 
    
    nombre_jugador db dup 20 (?),'$' ;No sabemos lo que vamos a recibir

    matriz db dup 10, '$'
    
    caracter db '','$'
              
    salto db 10,13, '$'    
    
    valor db '',10,13,'$' 
    
    nuevo_jugador db 0
    
           
;---------------------------------------------------------------------------    
.code
   
;AQUI SE DECLARAN LAS MACRO-------------------------------------------------         
            
    imp_men macro mensaje  
        mov dx, offset mensaje
        mov ah, 09h
        int 21h
    endm
    
    limpiar_datos macro ;DEVUELVE TODOS LOS VALORES DE LOS REGISTROS A CERO
        xor ax, ax
        xor cx, cx
        mov si, 00h 
    endm  
    
    pedir_dato macro;INTERRUPCION PARA PEDIR AL USUARIO 
        mov ah, 01h
        int 21h
    endm 
    
    numero_random macro
        MOV AH, 00h  
        INT 1AH          
        mov  ax, dx                 
        xor  dx, dx
        mov  cx, 10    
        div  cx       
        add  dl, '0'
        mov al,dl    
    endm
    
    
    
;---------------------------------------------------------------------------
    
    
    mov ax,@data    ;PARA EL AMACENAMIENTO DE DATOS        
    mov ds,ax
    mov nuevo_jugador,1
    
    call Principal  ;AQUI COMIENZA EL CODIGO 
    
    
    
        Principal proc ;FUNCION PRINCIPAL QUE LLAMA A LOS PROCEDIMIENTOS 
            
            mov ah,nuevo_jugador
            cmp ah,1
                jne imprimirJ2
            
            imprimirJ1:
                PRINT "JUGADOR 1:"
                jmp datosJugador              
                       
            imprimirJ2:           
                PRINT "JUGADOR 2:"        
                
            datosJugador:
                print 'Ingresa tu nickname: ' 
                call Obtener_nombre
                Principal endp 
                 
        
        Obtener_nombre proc ;FUNCION PARA OBTENER EL NOMBRE DEL JUGADOR
            leer:
                mov ah, 01h ;PIDE UN CARACTER QUE SIEMPRE SE GUARDA EN AL
                int 21h
                
                cmp al, 13
                 je terminar
                
                mov nombre_jugador[di], al;VAMOS FORMANDO UNA CADENA DE TEXTO
                inc di
                
                loop leer
                
            terminar:
                inc di
                mov al, 24h
                mov nombre_jugador[di],al

                loop imprimir:   
            
            imprimir:
                call clear_screen
                mov ah,nuevo_jugador
                cmp ah,1
                    jne imprimirJ2
                
                imprimirP1:
                    PRINT "JUGADOR 1:"
                    jmp mostrarJugador              
                           
                imprimirP2:           
                    PRINT "JUGADOR 2:"          
                                      
                mostrarJugador:                                      
                imp_men nombre_jugador
                                
                PRINT 10
                PRINT 13               

            print 'Ingresa tu simbolo: ' 
            mov ah,01
            int 21h                      
            mov caracter,al
            print 10
            print 13
            print 'Cargando datos del juego...'
            print 10
            print 13
            Obtener_nombre endp
        
                      
        Llenar_matriz proc
           
            mov al,31h
            
            llenado:
            
                ;METODO PARA OBTENER ELEMENTO RANDOM
                numero_random
                mov matriz[si],al
                inc si  
                cmp si,64H  
                jne llenado  
           
                     
                          
        Imprimir_matriz proc
            
            mov si,0
            mov bx,si
            PRINT 10
            PRINT 13
            impresion:          

                mov al,matriz[bx]
                mov ah,00h
                
                mov valor,al
                
                sub ax,30h
                
                cmp bl,10              
                    je imprimirSalto
                   
                cmp bl,20              
                    je imprimirSalto
                    
                cmp bl,30              
                    je imprimirSalto        
                        
                cmp bl,40              
                    je imprimirSalto
                    
                cmp bl,50              
                    je imprimirSalto
                     
               cmp bl,60              
                    je imprimirSalto
                    
                cmp bl,70              
                    je imprimirSalto
                    
                cmp bl,80              
                    je imprimirSalto
                    
                cmp bl,90              
                    je imprimirSalto
                               
                imprimirNormal: 
                    
                    add al,30H
                    mov ah,02h
                    mov dl,al
                    int 21h
                    
                               
                mov al,20h
                mov ah,02h
                mov dl,al 
                int 21h
                        
                                        
                inc bx
 
                cmp bx,100
                    jne impresion
                    
                salir:  
                    mov ah,nuevo_jugador
                    cmp ah,1
                        je volverInicio 
                    .exit
                
                volverInicio:
                    mov nuevo_jugador,2
                    call clear_screen
                    call principal
                
                imprimirSalto:
                    PRINT 10
                    PRINT 13
                    JMP imprimirNormal
              
;DEFINIR FUNCIONES DE LA LIBRERIA--------------------------------------------------- 

        DEFINE_CLEAR_SCREEN     
        DEFINE_PRINT_NUM
        DEFINE_PRINT_NUM_UNS