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
    itera = 0
    for i, c in enumerate(clusters):
        x, y = zip(*[p.coordenadas for p in c.puntos])
        itera = itera + 1
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




def encontrar_punto(x,y):
    encuentra_x = False
    encuentra_y = False
    num_cluster = 0

    for i in range (len(puntos)):
        for j in range(0,len(puntos[0][i])):
            if (j%2 == 0):
                #x
                if (round(puntos[0][i][j], 2) == x):
                    encuentra_x = True
                    num_cluster = i
            else:
                if (round(puntos[0][i][j], 2) == y):
                    num_cluster = i
                    encuentra_y = True
    if (encuentra_x and encuentra_y):
            print "El punto (" + str(x) + ", " + str(y) + ") pertenece al cluster " + str(
                num_cluster + 1) + ", Color " + str(
                lista_colores[num_cluster])
    else:
            print "El punto (" + str(x) + ", " + str(y) + ") no pertenece a ningun cluster"



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