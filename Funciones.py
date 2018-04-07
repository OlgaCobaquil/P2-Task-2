import re

#Leer el archivo de entrada
def abrir_archivo():
    salida = []
    f = open("Input.txt", "r")
    lineas = [line for line in f]
    for i in range(len(lineas)):
        fila = []
        linea = lineas[i]
        linea = linea.replace("[","")
        linea = linea.replace("]", "")
        linea = linea.replace("\n","")
        linea = linea.replace(" ", "")

        #dividir los numero por coordenada x y coordenada y
        n1, n2 = linea.split(",")
        fila.append(float(n1))
        fila.append(float(n2))

        salida.append(fila)
    f.close()
    return salida

