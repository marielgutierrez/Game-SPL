import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba

pygame.init()
WIDTH = 1000
HEIGHT = 600
FPS = 15

pygame.display.set_caption("Futurist Hero")
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

form_prueba = FormPrueba(pantalla, 200, 100, 600, 350, "Blue", "Magenta", 5, True, "Formularios\\recursos_form\\interfaz_user.jpg")

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