import pygame
import time
from classes import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_NAVE, PANTALLA

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
        self.cd_disparo_misil = 0.2
        
    def dibujar(self):
        pygame.draw.rect(PANTALLA, COLOR_NAVE, (self.x, self.y, self.ancho, self.alto))
        
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
            if self.cantidad_metralleta >= 100:
                self.disparar_metralleta()
            else:
                print("sin municion de metralleta")
                        
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m and not self.disparando:
                    if self.cantidad_misiles >= 1:
                        self.disparar_misil()
                        self.disparando = True
                    else:
                        print("sin municion de misiles")
                                                
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_m or evento.key == pygame.K_SPACE and self.disparando:
                    self.disparando = False
        
    def manejar_colisiones(self):
        # aqui
        pass
        
    def disparar_metralleta(self):
        self.cantidad_metralleta -= 1
        print("Metralleta: " + str(self.cantidad_metralleta))
        
    def disparar_misil(self):
        momento_disparo = time.time()
        if momento_disparo - self.ultimo_disparo_misil > self.cd_disparo_misil:
            self.ultimo_disparo_misil = momento_disparo
            self.cantidad_misiles -= 1
            print("Misil: " + str(self.cantidad_misiles))
    
    def update(self, eventos): 
        self.dibujar()
        self.manejar_input(eventos)
        self.manejar_colisiones()
