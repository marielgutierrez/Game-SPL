import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_item import Item
from niveles.class_enemy import BossFinal
from niveles.class_objeto_juego import Objeto_Juego

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        w = pantalla.get_width()
        h = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds/nuevo_fondo_2.jpeg")
        fondo = pygame.transform.scale(fondo, (w,h))

        #PERSONAJE
        posicion_inicial = (211,419)
        tamaño = (25,50)

        #BOSS
        boss = BossFinal((150,300), boss_final[0], {"quieto": [boss_final[0]],"camina":boss_final}, (w/2, h/2), 10, proyectil_surface)
        
        #ENEMIGOS
        mi_personaje = Personaje(tamaño, diccionario_animaciones["quieto"][0], diccionario_animaciones, posicion_inicial, 5, proyectil_surface)
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)
        lista_enemigos = []
        #ITEM
        money = Item((24,20), item_dolar[0], {"quieto":item_dolar}, (205,86), False)
        money_2 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (400,86), False)
        money_3 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (600,86), False)
        money_4 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (502,220), False)
        money_5 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (129,221), False)

        lista_items = [money, money_2, money_3, money_4, money_5]

        #TRAMPAS
        pinches_1 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (500, 90), False)
        pinches_2 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (263, 91), False)
        pinches_3 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (287, 260), False)

        lista_traps = [pinches_1, pinches_2, pinches_3]

        #FUENTE
        fuente = pygame.font.SysFont("Consolas",20)

        #PORTAL
        portal = Objeto_Juego((90,80), portal_s, (890, 110))

        #LLAVE
        llave = Item((10,20), item_s[0], {"quieto": item_s}, (620,233), True)
        
        bala1 = Item((25,14), bala_item[0], {"quieto":bala_item}, (292, 486), False)
        bala2 = Item((25,14), bala_item[0], {"quieto":bala_item}, (330, 486), False)
        bala3 = Item((20,30), bala_item[0], {"quieto":bala_item}, (400, 90), False)

        lista_elemento = [llave, bala1, bala2]

        #PISO Y TECHO
        piso = Plataforma((w, 210), vacio_surface, (0,510))#490
        techo = Plataforma((w,50), vacio_surface, (0,0))
        #PLATAFORMAS
        plataformas_1 = Plataforma((180,50), plataforma_surface, (0, 409))
        plataformas_2 = Plataforma((180,50), plataforma_surface, (265, 358))
        plataformas_3 = Plataforma((180,50), plataforma_surface, (450, 303))
        plataformas_4 = Plataforma((180,50), plataforma_surface, (674, 257))
        plataformas_5 = Plataforma((180,50), plataforma_surface, (861, 183))
        #plataformas_6 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 120, 30, (540, 111))

        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3, plataformas_4, plataformas_5]
        
        lista_plataformas_rect = [piso.lados_rectangulo, plataformas_1.lados_rectangulo, plataformas_2.lados_rectangulo,
                        plataformas_3.lados_rectangulo, plataformas_4.lados_rectangulo, plataformas_5.lados_rectangulo]

        lista_paredes_rect = [piso.lados_rectangulo, techo.lados_rectangulo]

        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, lista_plataformas_rect, fondo, fuente, lista_items, lista_traps, llave, lista_elemento, portal, 2, False, lista_enemigos, boss, lista_paredes_rect)