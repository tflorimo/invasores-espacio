from classes.Proyectil import Proyectil

class Metralla(Proyectil):
    def __init__(self, x, y):
        # La metralla es mas rápida que el misil.
        # Es mas pequeña, pero a la vez más rápida y con menos daño.
        self.velocidad = 10
        self.dmg = 8
        self.ancho = 3
        self.alto = 8
        super().__init__(x, y, self.velocidad, self.dmg, self.ancho, self.alto)