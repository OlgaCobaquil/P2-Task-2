import numpy as np

class Cluster:
    def __init__(self, puntos, puntos_totales):
        self.puntos = puntos
        #self.dimension = puntos[0].dimension

        print "Coordenadas Iniciales: "
        print puntos[0]