"""
Un punto tiene coordenadas x,y con dimension 2
"""
class Punto:
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
        self.dimension = len(coordenadas)
