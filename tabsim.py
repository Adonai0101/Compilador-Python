import validar
# revisa si es una palabra reserbada
def esPalres(cad):
    palres = ["entero" , "cadena" , "caracter" ,"bol"]
    if cad in palres:
        return True
    else:
        return False

def esOtraPal(cad):
    otra = ["leer", "imprimir" , "si" , "mientras" , "repite"]
    if cad in otra:
        return True
    else:
        return False

# regresa un numero segun la palres esto para una desicion
def tipoPalres(cad):
    if cad == "entero":
        return 1
    elif cad == "cadena":
        return 2
    elif cad == "caracter":
        return 3
    elif cad == "bol":
        return 4
    elif cad == "lectura":
        return 5
    elif cad == "consola":
        return 6
    elif cad == "si":
        return 7
    elif cad == "mientras":
        return 8
    elif cad == "repite":
        return 9
    else:
        print("Erro No es Palabra reserbada")
        pass


## Variables Globales para las listas 
tipoDato = []
nombreVar = []
varlor = []
identi = [] # para lis 'id0.....idn'
tiposAsm = []

def existeVar(cad):
    if cad in nombreVar:
        return True
    else:
        return False

def buscarTabla(cad):
    if cad in nombreVar:
        return True
    else:
        return False
        
def tabla(cad):
    archivo = open(cad, "r")
    cont = 1
    noId = 0
    for linea in archivo.readlines():
        palabra = linea.split()
        if len(palabra) == 0: # Ignoramos los espacios en blanco
            pass
        elif len(palabra) < 2: # delimitamos nuestros pedos
            print("Error en la linea: " + str(cont))
        elif len(palabra) >= 2: # Para crear Variable
            if esPalres(palabra[0]):
                if existeVar(palabra[1]):
                    print("Error, Variable ya Existe, linea: " + str(cont))
                else:
                    if validar.var(palabra[1]):
                        tipoDato.append(palabra[0])
                        nombreVar.append(palabra[1])
                        varlor.append("--")
                        identi.append(crearId(noId))
                        noId =  noId + 1
                        tiposAsm.append("--")
                    else:
                        print("Error, no es un identificador valido, linea: " + str(cont))
            
            elif esOtraPal(palabra[0]):
                pass
            
            elif existeVar(palabra[0]):
                ## se ase aqui mismo la asignacion pero primero tenemos que ver de que tipo es 
                i = 0
                i = nombreVar.index(palabra[0])

                if tipoDato[i] == "entero":
                    if palabra[1] != '=':
                        print("Error en la linea: " +str(cont))
                    else:
                        try:
                            if validar.esNumero(palabra[2]):
                                i = nombreVar.index(palabra[0])
                                varlor.pop(i)
                                varlor.insert(i,palabra[2])
                            else:
                                print("Error de tipo en linea: " + str(cont))
                        except:
                            print("Sintaxis Error en la linea: " +  str(cont))

                elif tipoDato[i] == "cadena":
                   # print("Cadena")
                    if palabra[1] != '=':
                        print("Error en la linea: " +str(cont))
                    else:
                        try:

                            if palabra[2] == '<':
                                if palabra[4] == '>':
                                    #aqui registraos los datos
                                    i = nombreVar.index(palabra[0])
                                    varlor.pop(i)
                                    varlor.insert(i,palabra[3])
                                else:
                                    print("Error en la linea: "+ str(cont) + ' Tiene que terminar con una > ')
                            else:
                                print("Error en la linea: "+ str(cont) + ' Tiene que empesar con una < ')
                        except:
                            print("Sintaxis Error en la linea: " +  str(cont))

                elif tipoDato[i] == "caracter":
                    if palabra[1] != '=':
                        print("Error en la linea: " +str(cont))
                    else:
                        try:
                            if palabra[2] == "<":
                                if len(palabra[3]) == 1:
                                    if palabra[4] == ">":
                                        i = nombreVar.index(palabra[0])
                                        varlor.pop(i)
                                        varlor.insert(i,palabra[3])
                                    else:
                                        print("Error en la linea: " + str(cont) + " Tiene que terminar con >")
                                else:
                                    print("Error en la linea: " + str(cont) + " no es caracter")
                            else:
                                print("Error en la linea: " + str(cont) + " Tiene que empesar con <")
                        except:
                            print("Sintaxis Error en la linea: " +  str(cont))

                elif tipoDato[i] == "bol":
                    if palabra[1] != '=':
                        print("Error en la linea: " + str(cont) + "No es Asignacion valida")
                    else:
                        try:

                            if palabra[2] == 'verdad' or palabra[2] == 'falso':
                                i = nombreVar.index(palabra[0])
                                varlor.pop(i)
                                varlor.insert(i,palabra[2])
                            else:
                                print("Eroor de asignacion en la linea: " + str(cont))
                        except:
                            print("Sintaxis Error en la linea: " +  str(cont))
                else:
                    print("Error de declaracion en la linea: " + str(cont))
            else:
                pass
                print("Error, variable no declarada en linea: " + str(cont))
        cont = cont + 1
    archivo.close() 


def imprimirTabla():
    letrero = " Tabla de Simbolos "
    print("\n")
    print(letrero.center(72 ,"*"))
    print("Tipo de Dato \t\t Nombre de Variable \t\t varlor \t\t id \t\t Tipo-ASM")
    print(""); # Damos un espacio entreletrero
    x =  len(tipoDato)
    cont = 0
    while cont < x:
        print(tipoDato[cont] + "\t\t\t\t" + nombreVar[cont] + "\t\t\t  " + varlor[cont] + "\t\t\t" + identi[cont] + "\t\t\t\t" + tiposAsm[cont])
        cont = cont + 1
    print("")# Salto de Linea para separar letrero 

def crearId(numero): 
    id = "id" + str(numero)
    return id

## Ejecutamos todas la pruebas
#tabla()
#imprimirTabla()