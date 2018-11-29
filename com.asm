
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

pila segment para stack  'stack'

pila ends

datos segment para public 'data'
x db '10$'
var db '--$'
cad db 'ado$'
car db 'L$'
let db 'Hola_compilador$'

datos ends

extra segment para public 'data'

extra ends


assume cs:codigo,  ds:datos,    ss:pila,    es:extra
public p0 					;p0 es el nombre del procedimiento principal
							;solo assume y public pueden estar fuera de un inicio y fin de segmento


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
   imp let
mov dh,1
mov ah,2
mov bh,0
int 10h
imp x
mov dh,2
mov ah,2
mov bh,0
int 10h
imp x
mov dh,3
mov ah,2
mov bh,0
int 10h
imp x
mov dh,4
mov ah,2
mov bh,0
int 10h
imp x
mov dh,5
mov ah,2
mov bh,0
int 10h
imp x
mov dh,6
mov ah,2
mov bh,0
int 10h
imp x
mov dh,7
mov ah,2
mov bh,0
int 10h
imp x
mov dh,8
mov ah,2
mov bh,0
int 10h

   ;-------------------------------------
   
   ret 						;es como return en otros programas, y debe estar antes de cerrar el procedimiento
p0 endp 					;termina el procedimiento p0
codigo ends 				;termina el segmento para codigo
       end p0 				;se define el procedimiento principal
