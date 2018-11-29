import tabsim

listaAcciones = []
listaValor = []

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
                                                    print("Soy leer")
                                                    listaAcciones.append(palabra[0])
                                                    listaValor.append(palabra[1])

                                            elif palabra[0] == 'imprimir':
                                                    #print("Soy Imprimir")
                                                    listaAcciones.append(palabra[0])
                                                    listaValor.append(palabra[1])

                                            else:
                                                    pass
                                    else:
                                            print("Error de sintaxis en la linea9 " +  str(cont))
                            except:
                                    print("Falta atributo a expresion  en la linea:  " +  str(cont))

#lectura("archivo.txt")