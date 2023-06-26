import pygame
from pygame.locals import *

from GUI_form import *
from GUI_label import *
from GUI_button_image import *

class FormMenuScore(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image, score, margen_y, margen_x, espacio):
        super().__init__(screen, x,y,w,h,color_background,color_border, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self._score = score

        self.margen_y = margen_y

        lbl_jugador = Label(self._slave, x=margen_x + 10, y=20, w=w/2-margen_x-10, h=50, text="Jugador",
                       font="Verdana", font_size=30, font_color="White", path_image="bar.png")
        lbl_puntaje = Label(self._slave, x=margen_x + 10, y=20, w=w/2-margen_x-10, h=50, text="Jugador",
                       font="Verdana", font_size=30, font_color="White", path_image="bar.png")
        
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        pos_inicial_y = margen_y

        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2-margen_x, 100, cadena, "Verdana",
                                30, "White", "Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 + espacio

    def update(self,lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                pass
            #VER VIDEO CLASE 21 