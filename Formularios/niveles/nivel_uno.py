import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_enemigo import Enemigo
from niveles.class_item import Item
from niveles.class_objeto_juego import Objeto_Juego

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        w = pantalla.get_width()
        h = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds/nuevo-fondo.jpeg")
        fondo = pygame.transform.scale(fondo, (w, h))

        #PERSONAJE
        #posicion_inicial = (h/2 - 180, 444)
        posicion_inicial = (28,55)
        tamaño = (25,50)
        
        mi_personaje = Personaje(tamaño, diccionario_animaciones["quieto"][0], diccionario_animaciones, posicion_inicial, 5)
        # ENEMIGOS  
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5, w/2)
        #lista_enemigos = []
        
        #ITEMS
        money = Item((24,20), item_dolar[0], {"quieto":item_dolar}, (205,86), False)
        money_2 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (400,86), False)
        money_3 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (600,86), False)
        money_4 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (502,220), False)
        money_5 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (129,221), False)

        lista_items = [money, money_2, money_3, money_4, money_5]

        #TRAMPAS
        pinches_1 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (500, 90), False)
        pinches_2 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (263, 91), False)
        pinches_3 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (287, 232), False)

        lista_traps = [pinches_1, pinches_2, pinches_3]
        
        #FUENTE
        fuente = pygame.font.SysFont("Consolas",20)

        #LLAVE
        llave = Item((10,20), item_s[0], {"quieto": item_s}, (180,105), True)

        #PORTAL
        portal = Objeto_Juego((80,70), portal_s, (918, 437))

        #PISO
        piso = Plataforma((w, 210), piso_surface, (0,490))

        #PLATAFORMAS
        plataformas_1 = Plataforma((180,50), plataforma_surface, (820, 111))
        plataformas_3 = Plataforma((180,50), plataforma_surface, (0, 111))
        plataformas_4 = Plataforma((180,50), plataforma_surface, (180, 111))
        plataformas_5 = Plataforma((180,50), plataforma_surface, (360, 111))
        plataformas_6 = Plataforma((180,50), plataforma_surface, (540, 111))

        plataformas_2 = Plataforma((50,50), miniplataforma_surface, (490, 250))
        plataformas_7 = Plataforma((180,50), plataforma_surface, (640, 250))
        plataformas_8 = Plataforma((180,50), plataforma_surface, (820, 250))
        plataformas_9 = Plataforma((180,50), plataforma_surface, (250, 250))
        plataformas_10 = Plataforma((50,50), miniplataforma_surface, (120, 250))

        #plataformas_3 = Plataforma("Formularios\\recursos\\suelo.png", 210, 210, (750, 150))

        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3, plataformas_4, plataformas_5, plataformas_6,
                            plataformas_7, plataformas_8, plataformas_9, plataformas_10]

        lista_plataformas_rect = [piso.lados_rectangulo, plataformas_1.lados_rectangulo, plataformas_2.lados_rectangulo,
                                plataformas_3.lados_rectangulo, plataformas_4.lados_rectangulo, plataformas_5.lados_rectangulo, plataformas_6.lados_rectangulo,
                                plataformas_7.lados_rectangulo, plataformas_8.lados_rectangulo, plataformas_9.lados_rectangulo, plataformas_10.lados_rectangulo] #techo.lados_rectangulo, index 1



        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, lista_plataformas_rect, fondo, fuente, lista_items, lista_traps, llave, portal)