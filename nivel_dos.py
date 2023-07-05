import pygame
from pygame.locals import *
from configuraciones import *
from niveles import Nivel
from class_personaje import Personaje
from class_plataforma import Plataforma

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds\\mega-city-fondo.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))

        #PERSONAJE
        posicion_inicial = (H/2 - 180, 444)
        tamaño = (25,50)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 5)

        #PISO
        piso = Plataforma("recursos\\vacio-png.png",0, mi_personaje.lados["main"].bottom, (W,20))

        #PLATAFORMAS
        plataformas_1 = Plataforma("recursos\\plataforma.png", 180, 50, (330, 400))
        plataformas_2 = Plataforma("recursos\\0.png", 50, 50, (500, 200))
        plataformas_3 = Plataforma("recursos\\suelo.png", 210, 210, (750, 150))

        # lados_plataformas_1 = [obtener_rectangulos(coordinate) for coordinate in plataformas_1.rects]
        # lados_plataformas_2 = [obtener_rectangulos(coordinate) for coordinate in plataformas_2.rects]
        # lados_plataformas_3 = [obtener_rectangulos(coordinate) for coordinate in plataformas_3.rects]

        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3]

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)