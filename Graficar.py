import numpy as np
import matplotlib.pyplot as plt
import imageio
from matplotlib.patches import Ellipse
import Funciones as fnc
from scipy.stats import multivariate_normal
lista_colores = ['lightcoral', 'yellowgreen', 'darkorange', 'turquoise', 'gold','mediumorchid', 'mediumvioletred']
puntos = []
imagenes = []

#dibujar los puntos del archivo de entrada
def pintar_puntos(clusters, cant_cluster):
    x1, y1 = generateGrid(10, -10, 10, -10, 0.025)
    mu1 = []
    desv1 = [[0, 0], [0, 0]]
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
        plt.plot(x, y, marker='.', color=lista_colores[i], ls='', markersize = 2)
        plt.plot (c.mean[0], c.mean[1], 'x', color = lista_colores[i], markeredgecolor = 'k', markersize = 4)
        mu1.append(c.mean[0])
        mu1.append(c.mean[1])

        desv1[0].append(c.desv_estandar[0])
        desv1[0].append(0)
        desv1[1].append(0)
        desv1[1].append(c.desv_estandar[1])
        #plot_ellipse(c.mean, [p.coordenadas for p in c.puntos], 0.5, color = 'k')
        # puntos = fnc.abrir_archivo_array()
        drawContour(x1, y1, [mu1[0], mu1[1]], [[desv1[0][2], 0.2], [0.2, desv1[1][3]]], 10, color='k')
        #drawContour(x1, y1, [mu1[0], mu1[1]], [[desv1[0][2], 0.2], [0.2, desv1[1][3]]], 10, color='k')
    showImage("salida.png", 200)
    imagenes.append(imageio.imread('salida.png'))
    puntos.append(puntos_nuevos)
    imageio.mimsave('salida.gif', imagenes, duration=0.3)
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


