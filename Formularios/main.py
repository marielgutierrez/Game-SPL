import pygame
import sys
from pygame.locals import *
from GUI_form_menu_inicio import FormMenuInicio

pygame.init()
WIDTH = 1000
HEIGHT = 600
FPS = 15

pygame.display.set_caption("Futurist Hero")
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

#ICON
icon = pygame.image.load("backgrounds\\icono.png")
pygame.display.set_icon(icon)

#FORMULARIO INICIO
form_inicio = FormMenuInicio(pantalla, "backgrounds\\fondo_inicio.jpg")

#FONDO DETRAS DEL MENU
fondo_menu = pygame.image.load("backgrounds\\fondo_del_menu.jpg")
fondo_menu = pygame.transform.scale(fondo_menu, (WIDTH, HEIGHT))

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos: 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.blit(fondo_menu, (0,0))
    form_inicio.update(eventos)

    pygame.display.flip()