INCLUDE 'emu8086.inc'

.model small
.stack

.data 
;VARIABLES DEL JUEGO-------------------------------------------------------- 
    
    nombre_jugador db dup 20 (?),'$' ;No sabemos lo que vamos a recibir

    matriz db dup 10, '$'
    
    caracter db 0
              
    salto db 10,13, '$'    
    
    valor db '',10,13,'$' 
    
    nuevo_jugador db 0 
    
    posy db 0
    
    posx db 0
    
    puntaje db 0
    
           
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
    
    dejarEspacio macro;DEJA UN ESPACIO ENTRE LOS CARACTERES DE LA MATRIZ
        mov al,20h
        mov ah,02h
        mov dl,al 
        int 21h  
    endm
    
    saltarLinea macro;HACE UN SALTO DE LINEA
        PRINT 10
        PRINT 13
    endm
    
    hacerTab macro;PERMITE HACER UN TAB
        PRINT 09
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
                saltarLinea               

            
            menu_simbolos:;ESTA SECCION SOLIICTA EL SIMBOLO (GLOBO)
                print '1) '
                print 02h
                saltarLinea
                print '2) '
                print 03h
                saltarLinea 
                print '3) '
                print 04h
                saltarLinea
                print 'ESCRIBA EL NUMERO QUE CORRESPONDE AL GLOBO QUE DESEA: '
                pedir_dato
                
                saltarLinea
                sub al,30h
                mov caracter, al ;QUEDA EL GLOBO GUARDADO 
                
                call clear_screen          
                imp_men nombre_jugador

            saltarLinea
            print 'Cargando datos del juego...'
            saltarLinea
            Obtener_nombre endp
        
                      
        Llenar_matriz proc
           
            mov al,5fh
            
            llenado:
                mov matriz[si],al
                ;inc al 
                inc si
                cmp si,64H  
                    jne llenado  
                
                call MeterGlobo
            Llenar_matriz endp
                      
                      
        MeterGlobo proc
            numero_random
            xor cx, cx
            mov cl, al
            mov si, cx
            cmp caracter,01h
                je Caracter1
                
            cmp caracter,02h
                je caracter2
                
            cmp caracter,03h
                je caracter3
                
            
                
            caracter1:
                mov al, 01h
                jmp agregarGlobo    
            caracter2:
                mov al, 02h
                jmp agregarGlobo           
            caracter3:
                mov al, 03h
                jmp agregarGlobo
            agregarGlobo:
                mov matriz[si], al
                hacerTab
                call Imprimir_matriz
                
                     
                          
        Imprimir_matriz proc
            
            mov si,0
            mov bx,si

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
                     
                cmp bl, 60              
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
                    
                    dejarEspacio
                    dejarEspacio
                 
                inc bx
 
                cmp bx,100
                    jne impresion
                    
                salir: 
                    saltarLinea       
                    saltarLinea
                    PRINT "El juego empieza en 5 segundos... " 
                    contarSegundos: ;Esto se encarga de contar 5 segundos
                        MOV BL,30H ;Inicia valor (segundo) en 0
                        TOP:
                            MOV AH,2CH ;Obtiene la hora
                            INT 21H
                            MOV BH,DH ;Aqui en DH retorna los segundos
                            obtenerSegundos:
                                MOV AH,2CH
                                INT 21H  
                                CMP BH,DH ;Compara si los segundos son distintos (hubo cambio)
                                JNE imprimirSegundos
                                JMP obtenerSegundos
                            
                            imprimirSegundos:   
                                INC bl
                                CMP BL,36h
                                jne saltar
                                je segundosListo
                                
                            saltar:                                                                           
                                JMP TOP
                     
                    segundosListo:
                    call finalizacion
                    
                imprimirSalto:
                    saltarLinea
                    saltarLinea 
                    hacerTab
                    JMP imprimirNormal
                    
                    
                    call finalizacion
                    
            Imprimir_matriz endp                    
                     
                     
                     
       proc finalizacion 
            saltarLinea
            saltarLinea
            PRINT 'Puntaje: '
            finalizar:
                                         
                mov ah,08h
                int 10h
                mov ax, 03h
                int 33h
                
                cmp bl,01h
                    je guardarPosicion
                
                jmp finalizar
                
            guardarPosicion:
                xor ax,ax
                inc puntaje
                mov al, puntaje
                sub al,5fh
                call print_num
                mov posy, cl
                mov posx, dl
                
                loop finalizar 
                
                ;xor bh, bh
                ;mov ah, 02h 
                ;mov bh, posx
                ;mov dh, posy
                ;int 10h
                
            finalizacion endp
              
;DEFINIR FUNCIONES DE LA LIBRERIA--------------------------------------------------- 

        DEFINE_CLEAR_SCREEN     
        DEFINE_PRINT_NUM
        DEFINE_PRINT_NUM_UNS