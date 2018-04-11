import numpy as np

class Cluster:
    def __init__(self, puntos, puntos_totales):
        self.puntos = puntos
        self.dimension = puntos[0].dimension
        print "Coordenadas Iniciales: ",puntos[0]

        #calcular media, desviacion estandar y probabilidad
        coordenadas_calculo = [p.coordenadas for p in self.puntos]
        self.mean = np.mean(coordenadas_calculo, axis=0)
        self.desv_estandar = np.array([1.0, 1.0])
        print"p", len(self.puntos)
        print 'total', puntos_totales
        self.pi = len(self.puntos) / float(puntos_totales)
        self.converge = False

    #evaluacion si converge un cluster
    def actualizar(self, puntos, puntos_totales):
        prev_media = self.mean
        self.puntos = puntos
        coordenadas_ac = [p.coordenadas for p in self.puntos]
        self.mean = np.mean(coordenadas_ac, axis=0)
        self.desv_estandar = np.std(coordenadas_ac, axis=0)
        #self.desv_estandar = np.std(coordenadas_ac, axis=0, ddof=0)
        self.pi = len(puntos)/ float(puntos_totales)
        print "prob updateada ", self.pi
        self.converge = np.array_equal(prev_media, self.mean)

"""
    def __repr__(self):
        cluster = 'Media: ' + str(self.mean) + '\nDimension: ' + str(
            self.dimension)
        for p in self.puntos:
            cluster += '\n' + str(p)

        return cluster + '\n\n'"""