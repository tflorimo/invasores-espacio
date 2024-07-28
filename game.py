import pygame
import sys
from classes import FPS, TICKER, PANTALLA, COLOR_FONDO
from classes.Nave import Nave

pygame.init()

jugador = Nave()

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    PANTALLA.fill(COLOR_FONDO)
    
    jugador.dibujar()
    jugador.update(eventos)

    pygame.display.flip()
    TICKER.tick(FPS)
        