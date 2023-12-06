import pygame
from pygame.locals import *
from niveles.configuraciones import *
from niveles.niveles import Nivel
from niveles.class_personaje import Personaje
from niveles.class_plataforma import Plataforma
from niveles.class_enemy import BossFinal
from niveles.class_enemy import FlyBot
from niveles.class_item import Item
from niveles.class_caja import Caja
from niveles.class_objeto_juego import ObjetoJuego
import random
class NivelTres(Nivel):
    '''
    Clase derivada, declara los elementos necesarios para el nivel 3 del juego.
    '''
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        w = pantalla.get_width()
        h = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds/mega-city-fondo.jpg")
        fondo = pygame.transform.scale(fondo, (w,h))
        #PERSONAJE
        posicion_inicial = (105,433)
        tamaño = (25,50)

        mi_personaje = Personaje(tamaño, diccionario_animaciones["quieto"][0], diccionario_animaciones,
                                posicion_inicial, 5, proyectil_surface)
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)
        #ENEMIGOS
        flybot1 = FlyBot((70, 90), flybot_d[0], {"camina_d": flybot_d, "camina_i":flybot_i}, (random.randrange(10, 1000, 60),random.randrange(10, 500, 60)), 5, proyectil_surface)
        flybot2 = FlyBot((70, 90), flybot_d[0], {"camina_d": flybot_d, "camina_i":flybot_i}, (random.randrange(10, 1000, 60),random.randrange(10, 500, 60)), 5, proyectil_surface)
        flybot3 = FlyBot((70, 90), flybot_d[0], {"camina_d": flybot_d, "camina_i":flybot_i}, (random.randrange(0, 1000, 60),random.randrange(10, 500, 60)), 5, proyectil_surface)
        
        lista_enemigos = [flybot1, flybot2, flybot3]
        #BOSS
        boss = BossFinal((110,195), boss_final[0], {"quieto": [boss_final[0]],"camina":boss_final, "muerte" : boss_muerte}, (W/2, H/2), 10, proyectil_surface)
        #ITEM                                                                                                                               PROYECTIL DEL BOSS!!
        money = Item((24,20), item_dolar[0], {"quieto":item_dolar}, (205,250), False)
        money_2 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (400,300), False)
        money_3 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (400,220), False)
        money_4 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (502,220), False)
        money_5 = Item((24,20),item_dolar[0], {"quieto":item_dolar}, (129,221), False)

        lista_items = [money, money_2, money_3, money_4, money_5]
        #TRAMPAS
        pinches_1 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (200, 487), False)
        pinches_2 = Item((90,28),item_pinche[0], {"quieto":item_pinche}, (661, 487), False)
        lista_traps = [pinches_1, pinches_2]

        #FUENTE
        fuente = pygame.font.SysFont("Consolas",20)
        #PORTAL
        portal = ObjetoJuego((90,80), portal_s, (890, 110))

        #LLAVE
        llave = Item((10,20), item_s[0], {"quieto": item_s}, (620,233), True)
        
        bala1 = Item((25,14), bala_item[0], {"quieto":bala_item}, (292, 486), False)
        bala2 = Item((25,14), bala_item[0], {"quieto":bala_item}, (330, 486), False)
        bala3 = Item((25,14), bala_item[0], {"quieto":bala_item}, (31, 377), False)
        bala4 = Item((25,14), bala_item[0], {"quieto":bala_item}, (99, 377), False)
        bala5 = Item((25,14), bala_item[0], {"quieto":bala_item}, (14, 462), False)
        bala6 = Item((25,14), bala_item[0], {"quieto":bala_item}, (24, 462), False)
        lista_elemento = [llave, bala1, bala2,bala3,bala4,bala5,bala6]

        #PISO Y TECHO
        piso = Plataforma((w, 200), plataforma_final, (0,490))#490 #510
        techo = Plataforma((w,20), vacio_surface, (0,50))
        pared_d = ObjetoJuego((20, H), vacio_surface, (W - 30, 0))
        pared_i = ObjetoJuego((20, H), vacio_surface, (0, 0))
        #PLATAFORMAS
        plataformas_1 = Plataforma((120, 30),plataforma3_s, (880, 187))
        plataformas_2 = Plataforma((60, 20),miniplataforma3_s, (429, 250))
        plataformas_3 = Plataforma((120, 30),plataforma3_s,  (0, 385))
        #plataformas_4 = Plataforma(plataforma3_s, 120, 30, (120, 111))
        plataformas_5 = Plataforma((120, 30),plataforma3_s,(873, 394))
        # plataformas_6 = Plataforma((120, 30),plataforma3_s,  (540, 111))
        plataformas_7 = Plataforma((120, 30),plataforma3_s, (561, 248))
        plataformas_8 = Plataforma((120, 30),plataforma3_s, (749, 245))
        plataformas_9 = Plataforma((120, 30),plataforma3_s, (250, 250))
        plataformas_10 = Plataforma((60, 20),miniplataforma3_s,  (120, 280))
        #CAJAS
        caja_1 = Caja((30,30), caja_s, (326, 214))
        caja_2 = Caja((30,30), caja_s, (437, 214))
        caja_3 = Caja((30,30), caja_s, (572, 210))

        lista_plataformas = [piso, techo, pared_i, pared_d, plataformas_1, plataformas_2, plataformas_3, plataformas_5, 
                            plataformas_7, plataformas_8, plataformas_9, plataformas_10]
        

        lista_paredes_rect = [piso.lados_rectangulo, techo.lados_rectangulo, 
                            pared_i.lados_rectangulo, pared_d.lados_rectangulo]

        lista_plataformas_rect = [piso.lados_rectangulo, techo.lados_rectangulo, plataformas_1.lados_rectangulo, plataformas_2.lados_rectangulo,
                            plataformas_3.lados_rectangulo, plataformas_5.lados_rectangulo,
                            plataformas_7.lados_rectangulo, plataformas_8.lados_rectangulo, plataformas_9.lados_rectangulo,
                            plataformas_10.lados_rectangulo,pared_d.lados_rectangulo, pared_i.lados_rectangulo, 
                            caja_1.lados_rectangulo, caja_2.lados_rectangulo, caja_3.lados_rectangulo]
        
        lista_cajas = [caja_1,caja_2,caja_3]
        super().__init__(pantalla, w, h, mi_personaje, lista_plataformas, lista_plataformas_rect, fondo, 
                        fuente, lista_items, lista_traps, llave, lista_elemento, portal, 3, True,
                        lista_enemigos, boss, lista_paredes_rect, lista_cajas)