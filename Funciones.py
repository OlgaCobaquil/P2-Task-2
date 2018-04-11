from Punto import Punto
import numpy as np
import random
import math
from Cluster import Cluster
import Graficar as gr
import imageio
imagenes = []
lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']
#Leer el archivo de entrada
def abrir_archivo():
    salida = []
    f = open("dataset1.txt", "r")
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

def abrir_archivo_array(data):
    puntos = list()
    with open(data, 'rt') as reader:
        for punto in reader:
            puntos.append(Punto(np.asarray(map(float, punto.split(",")))))
    return puntos

"""
calcular la probabilidad de que un punto pertenezca a un cluster
eij = exp(-0.5 (xj - ui)i-1 (xj - ui))

"""
def prob_punto_cluster(punto, cluster):

    media = cluster.mean
    desv = cluster.desv_estandar
    prob = 1.0

    for i in range(2):
        prob *= (math.exp(-0.5 * (
                math.pow((punto.coordenadas[i] - media[i]), 2) /
                math.pow(desv[i], 2))) / desv[i])

    #normalizar eij/R
    return cluster.pi * prob

"""
    Cluster con mayor probablidad
"""
def cluster_prob_mayor(clusters, punto):

    expectation = np.zeros(len(clusters))
    for i, c in enumerate(clusters):

        expectation[i] = prob_punto_cluster(punto, c)

    return np.argmax(expectation) #devuelve el indice maximo

def expectation_maximization( data, cant_clusters, iteraciones):

    puntos = abrir_archivo_array(data)
    """
     Inicializacion
     1. eleccion aleatoria de los puntos iniciales
    """
    inicial = random.sample(puntos, cant_clusters)

    #cant_clusters iniciales, generacion de kpi y demas
    clusters = [Cluster([p], len(inicial)) for p in inicial]

    #Crear una lista para guardar los puntos que vayan actualizando (inicial lista vacia)
    puntos_actualizados = [[] for i in range(cant_clusters)]
    converge = False
    limite_iteraciones = 0
    #While (los gaussianos se mueven o cambian de forma, o se alcanza el limite de iteraciones):
    while (not converge)and (limite_iteraciones <= iteraciones):
        for p in puntos:
            #paso e

            i_cluster = cluster_prob_mayor(clusters, p) #mayor probabilidad
            puntos_actualizados[i_cluster].append(p)

        # paso m
        for i, c in enumerate(clusters):
            c.actualizar(puntos_actualizados[i], len(puntos))

        #ver por probabilidad si converge
        converge = [c.converge for c in clusters].count(False) == 0

        #guardar puntos en clusters
        limite_iteraciones += 1
        puntos_actualizados = [[] for i in range(cant_clusters)]

        print '\nIteracion %d' % limite_iteraciones
        for i, c in enumerate(clusters):

            print 'Cluster %d:  \n \tProbabilidad = %s; \n \tMedia = %s; \n \tDesv. Estandar = %s; \n \tTotal Puntos Actuales = %s' % (
                i + 1, str(c.pi), str(c.mean), str(c.desv_estandar), str(len(c.puntos)))
            x1,y1 = gr.generateGrid(10,-10,10,-10,0.025)
            gr.drawContour(x1,y1,[c.mean[0], c.mean[1]], [[c.desv_estandar[0],0.2],[0.2, c.desv_estandar[1]]],10, color = 'k')
        gr.pintar_puntos(clusters, cant_clusters)

    return c.mean, c.desv_estandar, c.pi, c.puntos, clusters






