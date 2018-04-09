""" Proyecto 2 Task 2 Inteligencia artificial """
import Funciones as fnc
import Graficar as gr

#cantidad de iteraciones
iteraciones = 1000
puntos = []
lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']

#lectura del archivo, retorno de lista de listas [[],[]]
#ingreso = fnc.abrir_archivo_array()
#ingreso = fnc.abrir_archivo()
dataset = "dataset1.txt"
#inicio del programa

cant_gausianos = input("Ingrese la cantidad de clusters: ")
fnc.expectation_maximization(dataset, cant_gausianos, iteraciones)
print "+----------------------------------------------------+"
print "         Punto perteneciente a un cluster"
print "+----------------------------------------------------+ \n"
x = float(input("    -> Coordenada x del punto: "))
y = float(input("    -> Coordenada y del punto: "))

#gr.encontrar_punto(x,y)


#gr.pintar_puntos()
x1,y1 = gr.generateGrid(10,-10,10,-10, 0.025)
#mu array de dos puntos
#sigma matriz de 2x2
#n circulitos a dibujar
sigma = [[1.5,0],[0,0.6]]
sigma1 = [[3.1,0],[0,4.6]]
sigma2 = [[0.1,0],[0,3.1]]
gr.drawContour(x1, y1, [1,3], sigma, 20, "r")
gr.drawContour(x, y, [4,0], sigma1, 10, "b")
gr.drawContour(x, y, [2,1], sigma1, 10, "g")
gr.showImage("salida.png", 200)
#print ingreso


