import numpy as np
import matplotlib.pyplot as plt
import Funciones as fnc
from scipy.stats import multivariate_normal

#dibujar los puntos del archivo de entrada
def pintar_puntos():
    puntos = fnc.abrir_archivo_array()
    plt.plot(*zip(*puntos), marker='o', color='g', ls='')
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