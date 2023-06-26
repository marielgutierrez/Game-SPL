import pygame

class Plataforma:
    def __init__(self, image_path, width, height, coordinates):
        #Se carga la imagen de la plataforma
        self.image = pygame.image.load(image_path)
        #TAMAÑO IMAGEN
        self.image = pygame.transform.scale(self.image, (width, height))
        #Se crea una lista de rectángulos que representan las plataformas
        self.rects = []
        for coordinate in coordinates:
            rect = self.image.get_rect()
            rect.x = coordinate[0]
            rect.y = coordinate[1]
            self.rects.append(rect)

    def update(self):
        pass


# class Plataforma(pygame.sprite.Sprite):
#     def __init__(self, image_path, width, height, x, y):
#         super().__init__()
#         # Se carga la imagen de la plataforma
#         self.image = pygame.image.load(image_path)
#         # Se ajusta su tamaño
#         self.image = pygame.transform.scale(self.image, (width, height))
#         # Se obtiene el rectángulo de la plataforma
#         self.rect = self.image.get_rect()
#         # Se establecen las coordenadas
#         self.rect.x = x
#         self.rect.y = y

#     def update(self):
#         pass