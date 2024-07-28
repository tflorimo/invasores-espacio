import pygame
import sys
from classes import FPS, TICKER, PANTALLA, COLOR_FONDO
from classes.Nave import Nave


class Juego():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Invasores del espacio") # Texto en ventana
        self.jugador = Nave()
        self.correr()
        
    def correr(self):
        corriendo = True
        while corriendo:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    corriendo = False
                    pygame.quit()
                    sys.exit(0)
                    
            PANTALLA.fill(COLOR_FONDO)
            
            self.jugador.update(eventos)

            pygame.display.flip()
            TICKER.tick(FPS)
        
Juego()