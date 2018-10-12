import archivo
import tabsim

entrada = "archivo.txt"
salida = "archivo.dep"

archivo.depurador( entrada , salida)

tabsim.tabla(salida)
tabsim.imprimirTabla()
