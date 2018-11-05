import archivo
import tabsim
import Lectura

entrada = "archivo.txt"
salida = "archivo.dep"

archivo.depurador( entrada , salida)

tabsim.tabla(salida)
tabsim.imprimirTabla()

Lectura.lectura(salida)