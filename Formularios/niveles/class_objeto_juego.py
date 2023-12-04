import pygame

class Objeto_Juego:
    def __init__(self, tamaño:tuple, imagen:pygame.Surface, posicion_inicial) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = self.reescalar_imagen(imagen)
        #self.imagen = pygame.image.load(imagen)
        self.nuevo_tamaño = False
        self.posicion_inicial = posicion_inicial
        if posicion_inicial is not None:
            rectangulo = self.imagen.get_rect()
            rectangulo.x = posicion_inicial[0]
            rectangulo.y = posicion_inicial[1]
            self.lados_rectangulo = self.obtener_rectangulos(rectangulo)
        
        # self.velocidad = [0, 0]
        # self.indice_animacion = 0  # Índice para animar movimientos
        # self.lista_imagenes = []  # Lista de imágenes para animar movimientos

    def obtener_rectangulos(self, rectangulo):
        diccionario = {}
        diccionario["main"] = rectangulo
        diccionario["bottom"] = pygame.Rect(rectangulo.left, rectangulo.bottom - 10, rectangulo.width, 10)
        diccionario["left"] = pygame.Rect(rectangulo.left, rectangulo.top, 10, rectangulo.height)
        diccionario["top"] = pygame.Rect(rectangulo.left, rectangulo.top, rectangulo.width, 10)
        diccionario["right"] = pygame.Rect(rectangulo.right - 10, rectangulo.top, 10, rectangulo.height)
        return diccionario
    
    def reescalar_imagen(self, imagen:pygame.Surface):
        imagen = pygame.transform.scale(imagen, (self.ancho, self.alto))

        # if self.nuevo_tamaño:
        #     imagen = pygame.transform.scale(imagen, (100,55))

        return imagen
        
    def draw(self, screen):
        screen.blit(self.imagen, self.posicion_inicial)
    
    # def mover(self, velocidad):
    #     for lado in self.lados_rectangulo:
    #         self.lados_rectangulo[lado].x += velocidad
        # self.velocidad = velocidad  # Establecer la velocidad del objeto
        # self.posicion[0] += self.velocidad[0]  # Mover en el eje X
        # self.posicion[1] += self.velocidad[1]
    
    # def animar_movimientos(self, screen, lista_imagenes):
    #     self.lista_imagenes = lista_imagenes
    #     if self.indice_animacion >= len(self.lista_imagenes):
    #         self.indice_animacion = 0  # Reiniciar la animación cuando se alcanza el final de la lista de imágenes
    #     imagen_actual = pygame.image.load(self.lista_imagenes[self.indice_animacion])
    #     screen.blit(imagen_actual, self.rectangulo)
    #     self.indice_animacion += 1  # Avanzar al siguiente frame de la animación en la siguiente llamada

    def update(self):
        pass