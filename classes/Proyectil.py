import pygame
from classes import PANTALLA

class Proyectil:
    def __init__(self, x, y, velocidad, dmg, ancho, alto, color, sonido):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.dmg = dmg #  daño
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.sonido = sonido
        if self.sonido: self.sonido.play()
        
    def dibujar(self):
        pygame.draw.rect(PANTALLA, self.color, (self.x, self.y, self.ancho, self.alto))
    
    def mover(self):
        self.y -= self.velocidad
        
class Misil(Proyectil):
    def __init__(self, x, y):
        # El misil se mueve mas lento que la metralla.
        # Es mas grande, y hace mas daño. Estos atributos son fijos
        self.velocidad = 5
        self.dmg = 25
        self.ancho = 5
        self.alto = 15
        self.color = (252, 115, 3)
        self.sonido = pygame.mixer.Sound("assets/sounds/proyectiles/misil.wav")
        super().__init__(x, y, self.velocidad, self.dmg, self.ancho, self.alto, self.color, self.sonido)

class Metralla(Proyectil):
    def __init__(self, x, y):
        # La metralla es mas rápida que el misil.
        # Es mas pequeña, pero a la vez más rápida y con menos daño.
        self.velocidad = 10
        self.dmg = 8
        self.ancho = 3
        self.alto = 8
        self.color = (227, 252, 3)
        self.sonido = pygame.mixer.Sound("assets/sounds/proyectiles/metralla.mp3")
        super().__init__(x, y, self.velocidad, self.dmg, self.ancho, self.alto, self.color, self.sonido)