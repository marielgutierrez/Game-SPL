import pygame
from pygame.locals import *
from configuraciones import *

class InicioJuego:
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        self._slave = pantalla
        #FONDO
        fondo = pygame.image.load("backgrounds\\image.jpg")
        self.img_fondo = pygame.transform.scale(fondo, (W,H))

    def update(self, lista_eventos):
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))