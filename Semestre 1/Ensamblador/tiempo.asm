    INCLUDE 'emu8086.inc'

.model small
.stack

.data 
;VARIABLES DEL JUEGO--------------------------------------------------------
           
    sec db 0  
           
;---------------------------------------------------------------------------    
.code 

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
 

DEFINE_CLEAR_SCREEN