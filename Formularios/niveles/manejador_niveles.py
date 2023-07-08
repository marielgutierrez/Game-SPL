import pygame
from pygame.locals import *
from niveles.nivel_uno import NivelUno
from niveles.nivel_dos import NivelDos

#Instanciar los niveles al momento de usar la interfaz grafica
class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno":  NivelUno, "nivel_dos": NivelDos}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)