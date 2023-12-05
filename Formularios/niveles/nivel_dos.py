import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_item import Item
from niveles.class_enemy import BossFinal
from niveles.class_enemy import MiniBot
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
        mi_personaje = Personaje(tamaño, diccionario_animaciones["quieto"][0], diccionario_animaciones, posicion_inicial, 5, proyectil_surface)

        #BOSS
        boss = BossFinal((150,300), boss_final[0], {"quieto": [boss_final[0]],"camina":boss_final}, (w/2, h/2), 10, proyectil_surface)
        
        #ENEMIGOS
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)
        minibot_techo_1 = MiniBot((40,60), minibot_techo, {"quieto_d":[minibot_techo]}, (350,50), 5, False, proyectil_surface)
        minibot_techo_2 = MiniBot((40,60), minibot_techo, {"quieto_d":[minibot_techo]}, (760,232), 5, False, proyectil_surface)
        minibot_techo_3 = MiniBot((40,60), minibot_techo, {"quieto_d":[minibot_techo]}, (500,30), 5, False, proyectil_surface)
        robot_caminante_1 = MiniBot((40,42), robot_camina[0], {"camina_d":robot_camina_d, "camina_i":robot_camina}, (533, 222), 2, True, proyectil_surface)
        robot_caminante_2 = MiniBot((40,42), robot_camina[0], {"camina_d":robot_camina_d, "camina_i":robot_camina}, (710, 525), 2, True, proyectil_surface)
        robot_caminante_3 = MiniBot((40,42), robot_camina[0], {"camina_d":robot_camina_d, "camina_i":robot_camina}, (861, 190), 2, True, proyectil_surface)
        
        lista_enemigos = [robot_caminante_1, robot_caminante_2, robot_caminante_3, minibot_techo_1, minibot_techo_2, minibot_techo_3]
        #ITEM
        money = Item((24,20), item_dolar[0], {"quieto":item_dolar}, (205,250), False)
        money_2 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (400,300), False)
        money_3 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (600,350), False)
        money_4 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (502,220), False)
        money_5 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (129,221), False)

        lista_items = [money, money_2, money_3, money_4, money_5]

        #TRAMPAS
        pinches_1 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (403, 487), False)
        pinches_2 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (661, 487), False)
        #pinches_3 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (287, 260), False)

        lista_traps = [pinches_1, pinches_2]

        #FUENTE
        fuente = pygame.font.SysFont("Consolas",20)

        #PORTAL
        portal = Objeto_Juego((90,80), portal_s, (890, 110))

        #LLAVE
        llave = Item((10,20), item_s[0], {"quieto": item_s}, (620,233), True)
        
        bala1 = Item((25,14), bala_item[0], {"quieto":bala_item}, (292, 486), False)
        bala2 = Item((25,14), bala_item[0], {"quieto":bala_item}, (330, 486), False)
        bala3 = Item((25,14), bala_item[0], {"quieto":bala_item}, (31, 377), False)

        lista_elemento = [llave, bala1, bala2,bala3]

        #PISO Y TECHO
        piso = Plataforma((w, 210), vacio_surface, (0,510))#490
        techo = Plataforma((w,40), vacio_surface, (0,50))
        pared_d = Objeto_Juego((20, H), vacio_surface, (W - 30, 0))
        pared_i = Objeto_Juego((20, H), vacio_surface, (0, 0))
        #PLATAFORMAS
        plataformas_1 = Plataforma((180,50), plataforma_surface, (0, 409))
        plataformas_2 = Plataforma((180,50), plataforma_surface, (265, 358))
        plataformas_3 = Plataforma((180,50), plataforma_surface, (450, 303))
        plataformas_4 = Plataforma((180,50), plataforma_surface, (674, 257))
        plataformas_5 = Plataforma((180,50), plataforma_surface, (861, 183))
        #plataformas_6 = Plataforma("Formularios\\recursos\\pisos_2\\1.png", 120, 30, (540, 111))

        lista_plataformas = [piso,techo, pared_d, pared_i, plataformas_1, plataformas_2, plataformas_3, plataformas_4, plataformas_5]
        
        lista_plataformas_rect = [piso.lados_rectangulo, techo.lados_rectangulo, plataformas_1.lados_rectangulo, plataformas_2.lados_rectangulo,
                        plataformas_3.lados_rectangulo, plataformas_4.lados_rectangulo, plataformas_5.lados_rectangulo]

        lista_paredes_rect = [piso.lados_rectangulo, techo.lados_rectangulo, pared_d.lados_rectangulo, pared_i.lados_rectangulo]

        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, lista_plataformas_rect, fondo, fuente, lista_items, lista_traps, llave, lista_elemento, portal, 2, False, lista_enemigos, boss, lista_paredes_rect)