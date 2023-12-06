import pygame
from pygame.locals import *
from niveles.class_item import Item

class Proyectil(Item):
    '''
    Clase que representa al proyectil/bala dentro del juego, maneja sus funciones.
    '''
    def __init__(self, tamaño: tuple, imagen: pygame.Surface, animaciones: dict, posicion_inicial: tuple, es_llave, direccion) -> None:
        super().__init__(tamaño, imagen, animaciones, posicion_inicial, es_llave)
        #self.cargas = jugador.proyectiles
        self.velocidad_x = 10
        self.velocidad_y = 10
        self.direccion = direccion
        self.x = posicion_inicial[0]
        self.colisiono = False
        #self.jugador = jugador
        self.eliminado = False

    def mover_proyectil(self, pantalla):
        '''
        Se encarga de mover el proyectil en el eje x
        '''
        if self.eliminado == False:
            self.rectangulo.x += self.velocidad_x * self.direccion
            pantalla.blit(self.imagen, self.rectangulo)
        
    def mover_proyectil_boss(self, pantalla):
        '''
        Se encarga de mover el proyectil en el eje y
        '''
        if self.eliminado == False:
            self.rectangulo.y -= self.velocidad_y
            pantalla.blit(self.imagen, self.rectangulo)

    def impactar_proyectil(self, pantalla, lista_enemigos):
        '''
        Se encarga de verificar si colisiona el proyectil con un enemigo en una lista.
        '''
        if self.colisiono == False:
            for enemigo in lista_enemigos:
                if not self.rectangulo.colliderect(enemigo.lados_rectangulo["main"]):
                    self.mover_proyectil(pantalla)
                else:
                    self.colisiono = True
        else:
            self.aplicar_daño(lista_enemigos)

    def colisionar_enemigo(self, enemigo)->bool:
        '''
        Se encarga de verificar si colisiona con un enemigo, retorna valor bool
        '''
        return self.rectangulo.colliderect(enemigo.lados_rectangulo["main"])

    def update(self, pantalla):
        self.mover_proyectil(pantalla)

