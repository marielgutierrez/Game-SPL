import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba

pygame.init()
WIDTH = 1200
HEIGHT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

#Como puedo hacer que esta clase pase una ruta a una imagen en vez de un color?

form_prueba = FormPrueba(pantalla, 200, 100, 900, 350, "Blue", "Magenta", 5, True)
while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos: 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("Black")

    form_prueba.update(eventos)

    pygame.display.flip()