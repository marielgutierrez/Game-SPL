import pygame
from niveles.configuraciones import *
from niveles.class_personaje import Personaje
from niveles.class_objeto_juego import Objeto_Juego

class Item(Objeto_Juego):
    def __init__(self,tamaño:tuple, imagen:pygame.Surface, animaciones:dict, posicion_inicial, es_llave):
        super().__init__(tamaño, imagen, posicion_inicial)
        #CARGA IMAGEN
        #self.image = pygame.image.load(imagen)
        #TAMAÑO IMAGEN
        #self.image = pygame.transform.scale(self.image, tamaño)
        self.animaciones = animaciones
        self.fotograma_actual = 0
        self.rectangulo = imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.es_llave = es_llave
        self.bandera_mensaje = True
        self.puede_colisionar = True
        self.tiempo_inicio = pygame.time.get_ticks()
        #self.lados = obtener_rectangulos(self.rectangulo)
        # group.add(self)
        # self.rect = self.image.get_rect()
        # self.rect.topleft = coordinate
        #self.rects.append(rect)
        # self._slave = None
        # self.slave_rect = None

    def animar(self, pantalla, que_animacion:str):
        lista_imagenes = self.animaciones[que_animacion]
        if self.fotograma_actual >= len(lista_imagenes):
            self.fotograma_actual = 0
        pantalla.blit(lista_imagenes[self.fotograma_actual], self.lados_rectangulo)
        self.fotograma_actual += 1

    def acumular_vidrios(self, pantalla, jugador):
        if self.puede_colisionar:
            if not self.rectangulo.colliderect(jugador.lados_rectangulo["main"]):
                #self.dibujar_en_pantalla(pantalla)
                self.animar(pantalla, "quieto")
            else:
                self.puede_colisionar = False
                if self.es_llave:
                    jugador.tiene_llave = True
                else:
                    jugador.puntaje += 50
                    jugador.proyectiles += 1

    def update(self):
        pass

    def draw(self, pantalla):
        lista_imagenes = self.animaciones["quieto"]
        if self.fotograma_actual >= len(lista_imagenes):
            self.fotograma_actual = 0
        pantalla.blit(lista_imagenes[self.fotograma_actual], (self.rectangulo.x, self.rectangulo.y))
        self.fotograma_actual += 1
        #pantalla.blit(self.animaciones[0], (self.rectangulo.x, self.rectangulo.y)) #VER PARAMETROS DE ESTA FUNCION

    # def sumar_puntos(self, cantidad):
    #     self.personaje.puntaje += cantidad