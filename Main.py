""" Proyecto 2 Task 2 Inteligencia artificial """
import Funciones as fnc
import Graficar as gr


esto = fnc.abrir_archivo()
gr.pintar_puntos()
x,y = gr.generateGrid(10,-10,10,-10, 0.025)
#mu array de dos puntos
#sigma matriz de 2x2
#n circulitos a dibujar
sigma = [[1.5,0],[0,0.6]]
sigma1 = [[3.1,0],[0,4.6]]
sigma2 = [[0.1,0],[0,3.1]]
gr.drawContour(x, y, [1,3], sigma, 20, "r")
gr.drawContour(x, y, [4,0], sigma1, 10, "b")
gr.drawContour(x, y, [2,1], sigma1, 10, "g")
gr.showImage("salida.png", 200)
print esto


