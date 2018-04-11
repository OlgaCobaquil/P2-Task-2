""" Proyecto 2 Task 2 Inteligencia artificial """
import Funciones as fnc
import Graficar as gr

#cantidad de iteraciones
iteraciones = 1000
puntos = []
mu1 = []
eval =[]
desv1 = [[0,0], [0,0]]

lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']

#lectura del archivo, retorno de lista de listas [[],[]]
#ingreso = fnc.abrir_archivo_array()
#ingreso = fnc.abrir_archivo()
dataset = "dataset1.txt"
#inicio del programa

cant_gausianos = input("Ingrese la cantidad de clusters: ")
#mu,desv,pi,puntos1,cluster1 = \
fnc.expectation_maximization(dataset, cant_gausianos, iteraciones)
"""
print "+----------------------------------------------------+"
print "         Punto perteneciente a un cluster"
print "+----------------------------------------------------+ \n"
x = float(input("    -> Coordenada x del punto: "))
y = float(input("    -> Coordenada y del punto: "))
"""

#gr.encontrar_punto(x,y)

