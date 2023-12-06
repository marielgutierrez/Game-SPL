import pygame
from niveles.class_objeto_juego import ObjetoJuego

class Caja(ObjetoJuego):
    def __init__(self, tamaño: tuple, imagen: pygame.Surface, posicion_inicial) -> None:
        super().__init__(tamaño, imagen, posicion_inicial)
        self.velocidad_caida = 1
        self.esta_cayendo = False
        self.desplazamiento_y = 0
        self.gravedad = 1
        self.limite_velocidad_caida = 15
    
    def caer(self, lista_plat):
        if self.esta_cayendo:
            for lado in self.lados_rectangulo:
                self.lados_rectangulo[lado].y += self.desplazamiento_y - 1#por ahi lo tengo q poner 1

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        for piso in lista_plat:
            if self.lados_rectangulo["bottom"].colliderect(piso.lados_rectangulo["top"]):
                self.esta_cayendo = False
                self.desplazamiento_y = 0
                self.lados_rectangulo["main"].bottom = piso.lados_rectangulo["main"].top
                break
            else: 
                self.esta_cayendo = True 
    
    def empujar_caja(self, pantalla, jugador):
        for lado in self.lados_rectangulo:
            if jugador.lados_rectangulo["right"].colliderect(self.lados_rectangulo["left"]):
                #self.lados_rectangulo[lado].x += jugador.velocidad
                self.lados_rectangulo["main"].x += jugador.velocidad
                self.lados_rectangulo["bottom"].x += jugador.velocidad
                self.lados_rectangulo["top"].x += jugador.velocidad
                self.lados_rectangulo["right"].x += jugador.velocidad
                self.lados_rectangulo["left"].x += jugador.velocidad
            if jugador.lados_rectangulo["left"].colliderect(self.lados_rectangulo["right"]):
                self.lados_rectangulo[lado].x -= jugador.velocidad
                
            if self.esta_cayendo:
                self.lados_rectangulo[lado].y += self.velocidad_caida
        pantalla.blit(self.imagen, self.lados_rectangulo["main"])

    def colisionar_boss(self, boss):
        return self.lados_rectangulo["bottom"].colliderect(boss.lados_rectangulo["main"])

    
    def update_caja(self, pantalla, jugador, lista_plataformas):
        self.empujar_caja(pantalla, jugador)
        self.caer(lista_plataformas)