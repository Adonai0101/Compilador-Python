import tabsim
import Lectura
ensamblador = open("com.asm", "w")

#Macro de Imprsion 
ensamblador.write("""
    ; Macro de Impresion de una Cadena 
    ; imp nombredelacad
    imp macro cadena
		push ax
		push dx
		lea dx,cadena
		mov ah,9
		int 21h
		pop dx
		pop ax
	endm
""")

#Macro de Lectura

#segmento de PILA
ensamblador.write("""
pila segment para stack  'stack'

pila ends
""")

#segmento de datos
ensamblador.write("""
datos segment para public 'data'
""")
#aqui declaramos nuestras variables en ensamblador
#cad db 'Hola Mundo$'
cont = 0
while cont < len(tabsim.varlor):
    var =  tabsim.nombreVar[cont] + " db '" + tabsim.varlor[cont] + "$'"
    ensamblador.write(var + "\n")
    cont =  cont + 1
#---------------------------------------
ensamblador.write("""
datos ends
""")

#Segmento Extra
ensamblador.write("""
extra segment para public 'data'

extra ends
""")

# 'asume' y public
ensamblador.write("""

assume cs:codigo,  ds:datos,    ss:pila,    es:extra
public p0 					;p0 es el nombre del procedimiento principal
							;solo assume y public pueden estar fuera de un inicio y fin de segmento

""")

# Segmento de Codigo
ensamblador.write("""
codigo segment para public 'code'
p0 proc far  				;inicia el procedimiento p0

   push ds    				;obligatoria      ;estas 3 instrucciones sirven para que cuando termine el programa regrese el control de la ucp al sistema operativo
   mov ax,0   				;obligatoria
   push ax    				;obligatoria

   mov ax,datos  			;obligatoria
   mov ds,ax     			;obligatoria
   mov ax,extra  			;obligatoria
   mov es,ax     			;obligatoria
   ; limpiamos la pantalla 
		mov ch,0	
		mov cl,0	
		mov dh,24	
		mov dl,79	; Limiamos pantalla
		mov ah,6	
		mov al,0	
		mov bh,7	
		int 10h	
        
        mov dh,0
		mov dl,0
		mov ah,2	
		mov bh,0
		int 10h

   ;enttre esto van nuestras instrucciones
   """)
#-------- Instruccciones en ensamblador------------
cont = 0
while cont < len(Lectura.listaAcciones):
    if Lectura.listaAcciones[cont] == 'imprimir':
        print("La vas a matar perro")
        imp = 'imp ' + Lectura.listaValor[cont];
        ensamblador.write(imp + "\n")

        ensamblador.write('mov dh,' + str(cont + 1) + "\n")
        ensamblador.write('mov ah,2' + "\n")
        ensamblador.write('mov bh,0' + "\n")
        ensamblador.write('int 10h' + "\n")

    cont =  cont + 1

#--------------------------------------------------
ensamblador.write("""
   ;-------------------------------------
   
   ret 						;es como return en otros programas, y debe estar antes de cerrar el procedimiento
p0 endp 					;termina el procedimiento p0
codigo ends 				;termina el segmento para codigo
       end p0 				;se define el procedimiento principal
""")


ensamblador.close()