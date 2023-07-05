import pygame

class Personajes(pygame.sprite.Sprite):
    def __init__(self, path_imagen, tamaño, posicion_inicial, velocidad):
        super().__init__()
        #TAMAÑO IMAGEN
        self.imagen = pygame.image.load(path_imagen)
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        #RECTANGULOS
        self.listaDisparo = []
        self.rect = self.imagen.get_rect()
        self.rect.top = posicion_inicial[1]
        self.rect.left = posicion_inicial[0]
        # self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
