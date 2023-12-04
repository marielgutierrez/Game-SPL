import pygame
import sys
from pygame.locals import *
from GUI_form_menu_inicio import FormMenuInicio

pygame.init()
WIDTH = 1000
HEIGHT = 600
FPS = 10

pygame.display.set_caption("Futurist Hero")
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

#ICON
icon = pygame.image.load("backgrounds/icon_game.ico")
pygame.display.set_icon(icon)

#FORMULARIO INICIO
form_inicio = FormMenuInicio(pantalla, "backgrounds/fondo_inicio.jpg")

#MUSICA
pygame.mixer.init()
pygame.mixer.music.load("Formularios/recursos/music/hero-80s-127027.mp3") #poner musica path
pygame.mixer.music.play(-1)

#FONDO DETRAS DEL MENU
fondo_menu = pygame.image.load("backgrounds/fondo_del_menu.jpg")
fondo_menu = pygame.transform.scale(fondo_menu, (WIDTH, HEIGHT))


def mostrar_coordenadas(pos):
    print("Coordenadas: ({}, {})".format(pos[0], pos[1]))

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos: 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # mouse_pos = pygame.mouse.get_pos()
    
    # #Verificar si el mouse ha tocado los lados de la ventana
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             mostrar_coordenadas(mouse_pos)
    
    pantalla.blit(fondo_menu, (0,0))
    form_inicio.update(eventos)

    pygame.display.flip()