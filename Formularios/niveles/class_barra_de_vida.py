import pygame

class BarraDeVida:
    def __init__(self, posicion, largo, alto) -> None:
        self.posicion = posicion
        self.largo = largo
        self.alto = alto
        self.color = "Green"
        self.vida_actual = 100

    def actualizar_vida(self, nueva_vida):
        self.vida_actual = nueva_vida
    
    def dibujar(self, pantalla):
        ancho_vida = int(self.largo * (self.vida_actual / 100))
        rectangulo_vida = pygame.Rect(self.posicion, (ancho_vida, self.alto))
        rectangulo_fondo_barra = pygame.Rect(self.posicion, (self.largo, self.alto))

        pygame.draw.rect(pantalla, "Red", rectangulo_fondo_barra)
        pygame.draw.rect(pantalla, self.color, rectangulo_vida)

    def update_vida(self, pantalla, nueva_vida):
        self.actualizar_vida(nueva_vida)
        self.dibujar(pantalla)