import pygame
import time
from classes import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_NAVE, PANTALLA
from classes.Proyectil import Proyectil

class Nave:
    def __init__(self):
        self.ancho = 50
        self.alto = 30
        self.x = ANCHO_PANTALLA // 2 - self.ancho // 2
        self.y = ALTO_PANTALLA - self.alto - 10
        self.salud = 100
        self.velocidad = 5
        self.disparando = False
        self.cantidad_metralleta = 100
        self.cantidad_misiles = 15
        self.ultimo_disparo_misil = 0
        self.cd_disparo_misil = 0.2 # Cooldown standard de disparo del misil
        self.contador_disparo = 0 # Contador de tiros de metralleta
        self.TICK_LIMITE_METRALLETA = 10 # Entre ticks de disparos de metralleta
        self.misiles = [] # Donde guardo los misiles que pertenecen a este objeto para su renderizado
        self.proyectiles = [] # Guardo los proyectiles de la metralleta para renderizar
        
    """
        self.contador_disparo se va sumando por tick, cuando estás disparando.
        Si disparas, se va sumando hasta chocar con self.TICK_LIMITE_METRALLETA
        para ralentizar el disparo
    """
        
    def dibujar(self):
        pygame.draw.rect(PANTALLA, COLOR_NAVE, (self.x, self.y, self.ancho, self.alto))
        for proyectil in self.proyectiles:
            proyectil.dibujar()
        
    def mover(self, direccion):
        if direccion == "izquierda" and self.x > 0:
            self.x -= self.velocidad
        if direccion == "derecha" and self.x < ANCHO_PANTALLA - self.ancho:
            self.x += self.velocidad
        if direccion == "arriba" and self.y > 0:
            self.y -= self.velocidad
        if direccion == "abajo" and self.y < ALTO_PANTALLA - self.alto:
            self.y += self.velocidad
            
    def manejar_input(self, eventos):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.mover("izquierda")
        elif teclas[pygame.K_RIGHT]:
            self.mover("derecha")
        elif teclas[pygame.K_UP]:
            self.mover("arriba")
        elif teclas[pygame.K_DOWN]:
            self.mover("abajo")
            
        if teclas[pygame.K_SPACE]:
            self.disparando = True
            self.disparar_metralleta()
                                    
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m and not self.disparando:
                    self.disparar_misil()
                    self.disparando = True                            
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_m or evento.key == pygame.K_SPACE and self.disparando:
                    self.disparando = False
        
    def manejar_colisiones(self):
        # A futuro
        pass
    
    def manejar_proyectiles(self):
        for proyectil in self.proyectiles:
            proyectil.mover()
            if proyectil.y < 0:
                self.proyectiles.remove(proyectil)
                
    def disparar_metralleta(self):
        if self.contador_disparo >= self.TICK_LIMITE_METRALLETA:
            if self.cantidad_metralleta >= 1:
                self.cantidad_metralleta -= 1
                proyectil = Proyectil(self.x + self.ancho // 2 - 2.5, self.y)
                self.proyectiles.append(proyectil)
                print("Metralleta: " + str(self.cantidad_metralleta))
            else:
                print("Sin municion de metralleta")
            self.contador_disparo = 0
        else:
            self.contador_disparo += 1
        
        
    def disparar_misil(self):
        momento_disparo = time.time()
        if momento_disparo - self.ultimo_disparo_misil > self.cd_disparo_misil:
            if self.cantidad_misiles >= 1:    
                self.ultimo_disparo_misil = momento_disparo
                self.cantidad_misiles -= 1
                misil = Proyectil(self.x + self.ancho // 2 - 2.5, self.y)
                self.proyectiles.append(misil)
                print("Misil: " + str(self.cantidad_misiles))
            else:
                print("Sin municion de misiles")
    
    def update(self, eventos): 
        self.dibujar()
        self.manejar_input(eventos)
        self.manejar_proyectiles()
        self.manejar_colisiones()
