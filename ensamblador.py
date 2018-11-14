import tabsim
ensamblador = open("com.asm", "w")



#segmento de PILA
ensamblador.write("""
pila segment para stack  'stack'

pila ends
""")

#segmento de datos
ensamblador.write("""
datos segment para public 'data'

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

   ;enttre esto van nuestras instrucciones

   ;-------------------------------------
   

   ret 						;es como return en otros programas, y debe estar antes de cerrar el procedimiento
p0 endp 					;termina el procedimiento p0
codigo ends 				;termina el segmento para codigo
       end p0 				;se define el procedimiento principal
""")


ensamblador.close()