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
    if tabsim.varlor[cont] == '--': # Separamos las variables que no tengan valor solo estas se pueden leer
        pass
        #print("NO DEBE SER VALIDO")
    else:
        var =  tabsim.nombreVar[cont] + " db '" + tabsim.varlor[cont] + "$'"
        ensamblador.write(var + "\n")
    cont =  cont + 1
#Declaramos las variables que se leen
cont = 0
while cont < len(Lectura.listaAcciones):
    if Lectura.listaAcciones[cont] == 'leer':
        #print("leer en ensamblador ")
        varlec = Lectura.listaValor[cont] + ' DB 10,?,10 DUP("$")'
        ensamblador.write(varlec + "\n")
    else:
        pass
        #print(Lectura.listaAcciones[cont])
    cont = cont + 1

ensamblador.write("SL DB 10,24H" + "\n") # en esta variable se guardara temporalmente el valor q se lee
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
        imp = 'imp ' + Lectura.listaValor[cont];
        ensamblador.write(imp + "\n")
        #Este codigo es para saltos de linea siempre debe de ir 
        ensamblador.write('mov dh,' + str(cont + 1) + "\n")
        ensamblador.write('mov ah,2' + "\n")
        ensamblador.write('mov bh,0' + "\n")
        ensamblador.write('int 10h' + "\n")

    elif Lectura.listaAcciones[cont] == 'leer':
        print("Codigo para leer")
        #LEA DX,ado
		#MOV AH,0AH
		#INT 21H

		#LEA DX,SL
		#MOV AH,9
		#INT 21H
						
		#LEA DX,ado+2
		#MOV AH,9
		#INT 21H
        ensamblador.write(';lectura' + "\n")
        ensamblador.write('LEA DX,' + Lectura.listaValor[cont] + "\n")
        ensamblador.write('MOV AH,0AH' + "\n")
        ensamblador.write('INT 21H' + "\n")
       
        ensamblador.write("""
        LEA DX,SL
		MOV AH,9
		INT 21H
        """)

        ensamblador.write('LEA DX,' + Lectura.listaValor[cont] + '+2' + "\n")
        ensamblador.write('MOV AH,9' + "\n")
        ensamblador.write('INT 21H' + "\n")
        

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