import pygame

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Negro
COLOR_FONDO = (0, 0, 0)

# Blanco
COLOR_NAVE = (255, 255, 255)

# Blanco
COLOR_MISIL = (255, 255, 255)

# Rojo
COLOR_ENEMIGO = (255, 0, 0)

# Handle de la pantalla
PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Handle del responsable de tirar el tick del juego
TICKER = pygame.time.Clock()
pygame.display.set_caption("Invasores del espacio")
FPS = 60
# FUENTE_TEXTO = pygame.freetype.SysFont()