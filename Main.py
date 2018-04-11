""" Proyecto 2 Task 2 Inteligencia artificial """
import Funciones as fnc
import Graficar as gr

#cantidad de iteraciones
iteraciones = 1000
puntos = []
mu1 = []
desv1 = [[0,0], [0,0]]

lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']

#lectura del archivo, retorno de lista de listas [[],[]]
#ingreso = fnc.abrir_archivo_array()
#ingreso = fnc.abrir_archivo()
dataset = "dataset1.txt"
#inicio del programa

cant_gausianos = input("Ingrese la cantidad de clusters: ")
mu,desv,pi,puntos1,cluster1 = fnc.expectation_maximization(dataset, cant_gausianos, iteraciones)
"""
print "+----------------------------------------------------+"
print "         Punto perteneciente a un cluster"
print "+----------------------------------------------------+ \n"
x = float(input("    -> Coordenada x del punto: "))
y = float(input("    -> Coordenada y del punto: "))
"""
#gr.encontrar_punto(x,y)
mu1.append(mu[0])
mu1.append(mu[1])

desv1[0].append(desv[0])
desv1[0].append(0)
desv1[1].append(0)
desv1[1].append(desv[1])

#gr.pintar_puntos()
x1,y1 = gr.generateGrid(10,-10,10,-10, 0.025)
#mu array de dos puntos
#sigma matriz de 2x2
#n circulitos a dibujar
sigma = [[1.5,0],[0,0.6]]
sigma1 = [[3.1,0],[0,4.6]]
sigma2 = [[0.1,0],[0,3.1]]

gr.drawContour(x1, y1, [mu[0], mu[1]], [[desv[0], 0], [0, desv[1]]], 20, 'lightcoral')
#gr.drawContour(x, y, [4,0], sigma1, 10, "b")
#gr.drawContour(x, y, [2,1], sigma1, 10, "g")
#gr.showImage("salida.png", 200)
#print ingreso


