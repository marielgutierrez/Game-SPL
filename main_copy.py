import pygame, sys
from pygame.locals import *
from configuraciones import *
from class_enemigo import Enemigo
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from inicio_game import InicioJuego
from modo import *
'''
#Class = parte estatica, con atributos y variables, lo que me permite describir a un objeto
#Se define primero un constructor

# class Objeto_Juego():
#     def __init__(self, imagen, rectangulos:dict, posicion_inicial) -> None:
#         self.imagen = imagen
#         self.rectangulos = rectangulos

#Metodos: lo que puede hacer un objeto, parte dinamica de la clase 
'''

#PANTALLA
W, H = 1000,600 #1280 #686
FPS = 15
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Futurist Hero")
#PANTALLA.blit(fondo, (0,0))
pygame.init()

nivel_actual = NivelUno(PANTALLA)
#inicio_juego = InicioJuego(PANTALLA)

#MUSICA
# ruta_musica = "recursos\\music\\hero-80s-127027.mp3"
# musica_fondo = pygame.mixer.music.load(ruta_musica)
# pygame.mixer.music.play(-1)


while True:

    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    #PANTALLA.blit(texto, (10, 10))
    nivel_actual.update(eventos)
    #inicio_juego.update(eventos)
    pygame.display.update()