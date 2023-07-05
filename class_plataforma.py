import pygame

class Plataforma:
    def __init__(self, image_path, width, height, coordinate):
        #CARGA IMAGEN
        self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        self.image = pygame.transform.scale(self.image, (width, height))
        #Se crea una lista de rectángulos que representan las plataformas
        self.rects = []
        rect = self.image.get_rect()
        rect.x = coordinate[0]
        rect.y = coordinate[1]
        self.rects.append(rect)

    def update(self):
        pass
