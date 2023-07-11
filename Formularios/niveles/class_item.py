import pygame
from niveles.configuraciones import *
from niveles.class_personaje import Personaje

class Item:
    def __init__(self, image_path, width, height, coordinate):
        #CARGA IMAGEN
        self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rectangulo = self.image.get_rect()
        self.rectangulo.x = coordinate[0]
        self.rectangulo.y = coordinate[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        # group.add(self)
        # self.rect = self.image.get_rect()
        # self.rect.topleft = coordinate
        #self.rects.append(rect)
        # self._slave = None
        # self.slave_rect = None


    def update(self):
        pass

    def draw(self, pantalla):
        pantalla.blit(self.image, (self.rectangulo.x, self.rectangulo.y)) #VER PARAMETROS DE ESTA FUNCION

    # def sumar_puntos(self, cantidad):
    #     self.personaje.puntaje += cantidad