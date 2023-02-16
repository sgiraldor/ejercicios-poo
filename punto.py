import math
class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mostrar(self):
        print(f"coordenadas de x: {self.x}coordenadas de y: {self.y}")

    def mover(self,nuevo_x,nuevo_y):
        self.x+=nuevo_x
        self.y+=nuevo_y

    def calcular_doistanncia(self,punto_2x,punto_2y,x,y):
        distancia=math.sqrt((punto_2x-x)**2+(punto_2y-y)**2)



