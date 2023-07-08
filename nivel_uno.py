import pygame
from pygame.locals import *
from configuraciones import *
from niveles import Nivel
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_enemigo import Enemigo

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #TAMAÑO PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("backgrounds\\nuevo-fondo.jpeg")
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
        #mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)
        #PLATAFORMAS
        #piso
        #piso = pygame.Rect(0,0,W,20)
        # piso.top = mi_personaje.lados["main"].bottom
        # lados_piso = obtener_rectangulos(piso)

        #CRONOMETRO
        tiempo_inicial = pygame.time.get_ticks()
        tiempo_limite = 600000
        tipo_fuente = "Consolas"
        tamaño = 20
        fuente = pygame.font.SysFont(tipo_fuente, tamaño)

        piso = Plataforma("recursos\\vacio-png.png", W, 100, (0,490))
        #mi_personaje.lados["main"].bottom
        #PLATAFORMAS
        plataformas_1 = Plataforma("recursos\\plataforma.png", 180, 50, (330, 400))
        plataformas_2 = Plataforma("recursos\\0.png", 50, 50, (500, 200))
        plataformas_3 = Plataforma("recursos\\suelo.png", 210, 210, (750, 150))

        lista_plataformas = [piso, plataformas_1, plataformas_2, plataformas_3]

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo, tiempo_inicial, tiempo_limite, fuente)