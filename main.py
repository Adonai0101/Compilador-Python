import archivo
import tabsim
import Lectura

entrada = "archivo.txt"
salida = "archivo.dep"

archivo.depurador( entrada , salida)

tabsim.tabla(salida)
tabsim.imprimirTabla()

Lectura.lectura(salida)

#Creamos nuestro archivo ensamblador 
import ensamblador

# esta lista le pasara los valores a ensamblador
print(Lectura.listaAcciones)
print(Lectura.listaValor)



