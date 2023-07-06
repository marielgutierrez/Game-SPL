import pygame
from configuraciones import *

class Plataforma():
    def __init__(self, image_path, width, height, coordinate):
        #CARGA IMAGEN
        self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        self.image = pygame.transform.scale(self.image, (width, height))
        #self.rects = []
        #for coordinate in coordinates:
        rectangulo = self.image.get_rect()
        rectangulo.x = coordinate[0]
        rectangulo.y = coordinate[1]
        self.lados = obtener_rectangulos(rectangulo)
        #self.rects.append(rect)
        # self._slave = None
        # self.slave_rect = None


    def update(self):
        pass
    
    def draw(self,pantalla):
        pantalla.blit(self.image, (self.rect.x, self.rect.y)) #VER PARAMETROS DE ESTA FUNCION
        pygame.draw.rect(pantalla, "Green", self.rect)