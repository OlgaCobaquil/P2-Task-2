import numpy as np

class Cluster:
    def __init__(self, puntos, puntos_totales):
        self.puntos = puntos
        #self.dimension = puntos[0].dimension
        print "Coordenadas Iniciales: ",puntos[0]

        #calcular media, desviacion estandar y probabilidad
        coordenadas_calculo = [p.coordenadas for p in self.puntos]
        self.mean = np.mean(coordenadas_calculo, axis=0)
        self.desv_estandar = np.array([1.0, 1.0])
        print self.desv_estandar
        self.pi = len(self.puntos) / float(puntos_totales)
        self.converge = False

    def __repr__(self):
        cluster = 'Media: ' + str(self.mean)
        for p in self.puntos:
            cluster += '\n' + str(p)

        return cluster + '\n\n'