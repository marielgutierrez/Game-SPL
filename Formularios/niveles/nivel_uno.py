import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_enemigo import Enemigo
from niveles.class_item import Item

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        w = pantalla.get_width()
        h = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds\\nuevo-fondo.jpeg")
        fondo = pygame.transform.scale(fondo, (w, h))

        #SCORE
        score = 0

        #PERSONAJE
        #posicion_inicial = (h/2 - 180, 444)
        posicion_inicial = (28,55)
        tamaño = (25,50)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
        #grupo_items = pygame.sprite.Group()
        
        # ENEMIGOS  
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5, w/2)
        #lista_enemigos = []
        
        #ITEMS
        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 5, score)

        money = Item("Formularios\\recursos\\items\\money.png", 24, 20, (205,86))
        money_2 = Item("Formularios\\recursos\\items\\money.png", 24, 20, (400,86))
        
        lista_items = [money, money_2]

        #grupo_items.add(money)
        #grupo_items.add(mi_personaje)
        
        #CRONOMETRO
        tiempo_inicial = pygame.time.get_ticks()
        tiempo_limite = 600000
        fuente = pygame.font.SysFont("Consolas",20)

        #PISO
        piso = Plataforma("Formularios\\recursos\\vacio-png.png", w, 200, (0,490))
        #mi_personaje.lados["main"].bottom
        #PLATAFORMAS
        '''
        Coordenadas: (132, 106)
        Coordenadas: (127, 90)


        Coordenadas: (363, 118)
        '''
        plataformas_1 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (820, 111))
        plataformas_3 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (0, 111))
        plataformas_4 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (180, 111))
        plataformas_5 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (360, 111))
        plataformas_6 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (540, 111))

        plataformas_2 = Plataforma("Formularios\\recursos\\0.png", 50, 50, (490, 250))
        plataformas_7 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (640, 250))
        plataformas_8 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (820, 250))
        plataformas_9 = Plataforma("Formularios\\recursos\\plataforma.png", 180, 50, (250, 250))
        plataformas_10 = Plataforma("Formularios\\recursos\\0.png", 50, 50, (120, 250))

        #plataformas_3 = Plataforma("Formularios\\recursos\\suelo.png", 210, 210, (750, 150))

        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3, plataformas_4, plataformas_5, plataformas_6,
                            plataformas_7, plataformas_8, plataformas_9, plataformas_10]

        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, fondo, tiempo_inicial, tiempo_limite, fuente, lista_items)