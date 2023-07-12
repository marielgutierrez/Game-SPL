import pygame
import random
from niveles.configuraciones import *
from niveles.class_personaje import Personaje

class Enemy:
    def __init__(self, image_path, width, height, coordinate):
        #CARGA IMAGEN
        self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rectangulo = self.image.get_rect()
        self.rectangulo.x = coordinate[0]
        self.rectangulo.y = coordinate[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = random.randrange(10, 20, 1)
        # group.add(self)
        # self.rect = self.image.get_rect()
        # self.rect.topleft = coordinate
        #self.rects.append(rect)
        # self._slave = None
        # self.slave_rect = None

    # def crear_lista_donas(cantidad):
    #     lista_donas = []
    #     for i in range(cantidad):
    #         x = random.randrange(0,740,60)
    #         y = random.randrange(-1000,0,60)
    #         diccionario = crear(x,y,60,60, "dona.png")
    #         lista_donas.append(diccionario)
    #     return lista_donas

    def update(self):
        pass

    def draw(self, pantalla):
        pantalla.blit(self.image, (self.rectangulo.x, self.rectangulo.y)) #VER PARAMETROS DE ESTA FUNCION

    # def sumar_puntos(self, cantidad):
    #     self.personaje.puntaje += cantidad