def ajustar(s):
    return s[ 0:len(s) - 1]

def quitaEspacios(cad):
    cad = cad.split()
    cadena = ""
    for x in cad:
        cadena = cadena + x +" "
    return cadena 

def quitarComentario(cad):
    x = cad
    y = x.find("#")
    return x[:y]


# ---- Metodo depurador Genera el archivo.dep
def depurador(fuente , depurado):
    cont = 0
    archivo = open(fuente, "r")
    a = open(depurado , "w")
    for linea in archivo.readlines():
        cont =  cont + 1
        linea = quitarComentario(linea)
        linea = quitaEspacios(linea)
        a.write(linea + "\n")
