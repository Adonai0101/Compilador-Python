archivo = open("archivo.txt", "r") 
linea1 = archivo.readline()
mas = archivo.read(archivo.tell() * 2)
 
if archivo.tell() > 50:
    archivo.seek(50)