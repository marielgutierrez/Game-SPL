import pygame
from niveles.configuraciones import *
from niveles.class_objeto_juego import *

class Plataforma(ObjetoJuego):
    def __init__(self, tamaño:tuple, imagen:pygame.Surface, posicion_inicial):
        super().__init__(tamaño, imagen, posicion_inicial)
        #CARGA IMAGEN
        #self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        #self.image = pygame.transform.scale(self.image, tamaño)
        #self.rects = []
        #for coordinate in coordinates:
        # self.rectangulo = imagen.get_rect()
        # self.rectangulo.x = posicion_inicial[0]
        # self.rectangulo.y = posicion_inicial[1]
        # self.lados = self.obtener_rectangulos(self.rectangulo)
        #self.rects.append(rect)
        # self._slave = None
        # self.slave_rect = None


    def obtener_rectangulos(self, rectangulo):
        '''
        brief: Definir los rectangulos que voy a obtener a la izquierda, derecha, arriba y abajo
        esto tiene como fin definir los lados de un rectangulo (pasado por parametro)
        esto es necesario para que cuando colisionan dos rectangulos, por ej el personaje con la plataforma
        '''
        diccionario = {}
        #main - bottom - left - right
        diccionario["main"] = rectangulo
        diccionario["bottom"] = pygame.Rect(rectangulo.left, rectangulo.bottom - 10, rectangulo.width, 10)
        diccionario["right"] = pygame.Rect(rectangulo.right - 2, rectangulo.top, 2 , rectangulo.height)
        diccionario["left"] = pygame.Rect(rectangulo.left, rectangulo.top, 2, rectangulo.height)
        diccionario["top"] = pygame.Rect(rectangulo.left, rectangulo.top, rectangulo.width, 10)
        diccionario["top_left"] = pygame.Rect(rectangulo.left, rectangulo.top - 10, 10, 15)
        diccionario["top_right"] = pygame.Rect(rectangulo.right - 10, rectangulo.top - 10, 10, 15)
        return diccionario

    def update(self):
        pass
    
    # def draw(self, pantalla):
    #     pantalla.blit(self.image, (self.rectangulo.x, self.rectangulo.y)) #VER PARAMETROS DE ESTA FUNCION
        # for lado in self.lados:
        #     pygame.draw.rect(pantalla, "Blue", self.lados[lado])