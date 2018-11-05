import tabsim

def lectura(fuente):
    cont = 0
    archivo = open(fuente, "r")
    for linea in archivo.readlines():
            cont = cont + 1   
            palabra = linea.split()
            if len(palabra)  >= 1:
                    if palabra[0] == 'leer' or palabra[0] == 'imprimir':
                            try:
                                    if tabsim.existeVar(palabra[1]):
                                            if palabra[0] == 'leer':
                                                    pass
                                            else:
                                                    pass
                                    else:
                                            print("Error de sintaxis en la linea " +  str(cont))
                            except:
                                    print("Falta atributo a expresion  en la linea:  " +  str(cont))

#lectura("archivo.txt")