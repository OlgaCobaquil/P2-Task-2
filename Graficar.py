import numpy as np
import matplotlib.pyplot as plt
import Funciones as fnc
from scipy.stats import multivariate_normal
lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']
puntos = []

#dibujar los puntos del archivo de entrada
def pintar_puntos(clusters, cant_cluster):
    plt.plot()
    puntos_nuevos = [[] for i in range(cant_cluster)]
    for i, c in enumerate(clusters):
        x, y = zip(*[p.coordenadas for p in c.puntos])

        for p in c.puntos:
            a = p.coordenadas[0]
            b = p.coordenadas[1]
            puntos_nuevos[i].append(a)
            puntos_nuevos[i].append(b)
        plt.plot(x, y, marker='o', color=lista_colores[i], ls='')
        plt.plot (c.mean[0], c.mean[1], 'x', color = lista_colores[i], markeredgecolor = 'k', markersize = 8)
    puntos.append(puntos_nuevos)
    #puntos = fnc.abrir_archivo_array()
    plt.show()

#dibujo de gausianos
def dibujar_gaus():
    print("dibujo del gausiano")
"""
    arange genera lista valores consecutivos con saltos delta desde x a y
    meshgrid genera un grid de los valores x y y para imprimir
"""
def generateGrid(maxx, minx, maxy, miny, delta):
    delta = 0.025
    x = np.arange(minx, maxx, delta)
    y = np.arange(miny, maxy, delta)
    X, Y = np.meshgrid(x, y)
    return X, Y
"""
    Bivariate Gaussian distribution for equal shape X, Y.
    x, y donde estara, sigma x, sigmay, mux, muy
"""
def drawContour(xgrid, ygrid, mu, sigma, n, color):

    pos = np.dstack((xgrid, ygrid))
    rv = multivariate_normal(mu, sigma)
    plt.contour(xgrid, ygrid, rv.pdf(pos), n, colors=color)
def showImage(name, dpi):
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig(name, bbox_inches='tight', dpi=dpi)