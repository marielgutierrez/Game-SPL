import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_item import Item

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        w = pantalla.get_width()
        h = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds\\mega-city-fondo.jpg")
        fondo = pygame.transform.scale(fondo, (w,h))

        #SCORE
        score = 0
        #VIDAS
        vidas = 3

        #PERSONAJE
        posicion_inicial = (28,55)
        # posicion_inicial = (H/2 - 180, 444)
        tamaño = (25,50)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 5, score, vidas)
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)

        #ITEM
        money = Item("Formularios\\recursos\\items\\money.png", 24, 20, (205,86))
        money_2 = Item("Formularios\\recursos\\items\\money.png", 24, 20, (400,86))
        money_3 = Item("Formularios\\recursos\\items\\money.png", 24, 20, (600,86))
        money_4 = Item("Formularios\\recursos\\items\\money.png", 24, 20, (502,220))
        money_5 = Item("Formularios\\recursos\\items\\money.png", 24, 20, (129,221))

        lista_items = [money, money_2, money_3, money_4, money_5]

        #TRAMPAS

        pinches_1 = Item("Formularios\\recursos\\items\\pinche.png", 90,28, (500, 90))
        pinches_2 = Item("Formularios\\recursos\\items\\pinche.png", 90,28, (263, 91))
        pinches_3 = Item("Formularios\\recursos\\items\\pinche.png", 90,28, (287, 232))

        lista_traps = [pinches_1, pinches_2, pinches_3]

        #CRONOMETRO
        tiempo_inicial = pygame.time.get_ticks()
        tiempo_limite = 600000
        fuente = pygame.font.SysFont("Consolas",20)

        #PISO
        piso = Plataforma("Formularios\\recursos\\pisos_2\\plataforma-final.png", w, 200, (0,490))
        #mi_personaje.lados["main"].bottom
        #PLATAFORMAS
        plataformas_1 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (820, 111))
        plataformas_3 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (0, 111))
        plataformas_4 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (180, 111))
        plataformas_5 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (360, 111))
        plataformas_6 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (540, 111))

        plataformas_2 = Plataforma("Formularios\\recursos\\pisos_2\\2.png", 60, 30, (490, 250))
        plataformas_7 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (640, 250))
        plataformas_8 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (820, 250))
        plataformas_9 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 180, 50, (250, 250))
        plataformas_10 = Plataforma("Formularios\\recursos\\pisos_2\\2.png", 60, 30, (120, 250))

        # plataformas_1 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (330, 400))
        # plataformas_2 = Plataforma("Formularios\\recursos\\0.png", 50, 50, (500, 200))
        # plataformas_3 = Plataforma("Formularios\\recursos\\suelo.png", 210, 210, (750, 150))

        # lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3]
        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3, plataformas_4, plataformas_5, plataformas_6,
                            plataformas_7, plataformas_8, plataformas_9, plataformas_10]

        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, fondo, tiempo_inicial, tiempo_limite, fuente, lista_items, lista_traps)