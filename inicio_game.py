import pygame
from pygame.locals import *
from configuraciones import *

class InicioJuego:
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        self._slave = pantalla
        #FONDO
        fondo = pygame.image.load("backgrounds\\image.jpg")
        self.img_fondo = pygame.transform.scale(fondo, (W,H))

    def update(self, lista_eventos):
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        #PERSONAJE
        # posicion_inicial = (H/2 - 180, 444)
        # tamaño = (25,50)

        # diccionario_animaciones = {}
        # diccionario_animaciones["quieto"] = personaje_quieto
        # diccionario_animaciones["salta"] = personaje_salta
        # diccionario_animaciones["camina_derecha"] = personaje_camina
        # diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        # mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 5)


        # piso = Plataforma("recursos\\vacio-png.png", W, 100, (0,490))
        # #mi_personaje.lados["main"].bottom
        # #PLATAFORMAS
        # plataformas_1 = Plataforma("recursos\\plataforma.png", 180, 50, (330, 400))
        # plataformas_2 = Plataforma("recursos\\0.png", 50, 50, (500, 200))
        # plataformas_3 = Plataforma("recursos\\suelo.png", 210, 210, (750, 150))

        # lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3]

        #super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)