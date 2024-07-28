from classes.Proyectil import Proyectil


class Misil(Proyectil):
    def __init__(self, x, y):
        # El misil se mueve mas lento que la metralla.
        # Es mas grande, y hace mas daño. Estos atributos son fijos
        self.velocidad = 5
        self.dmg = 25
        self.ancho = 5
        self.alto = 15
        super().__init__(x, y, self.velocidad, self.dmg, self.ancho, self.alto)