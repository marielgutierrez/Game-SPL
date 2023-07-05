import pygame
from pygame.locals import *
from nivel_uno import NivelUno
from nivel_dos import NivelDos

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno":  NivelUno, "nivel_dos": NivelDos}

    def get_nivel(self, nombre_nivel):
        pass