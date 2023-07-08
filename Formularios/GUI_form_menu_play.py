import pygame
from pygame.locals import *

from GUI_form import *
from GUI_button_image import *
from GUI_form_contenedor_nivel import *
from niveles.manejador_niveles import Manejador_niveles


class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, path_image, color_border, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self._btn_level_1 = Button_Image(screen=self._slave,
                            master_x = x,
                            master_y = y,
                            x = 100,
                            y = 100,
                            w = 100,
                            h = 150,
                            path_image = "Formularios\\recursos_form\\NIVELES\\nivel_1.png",
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_uno")
        self._btn_level_2 = Button_Image(screen=self._slave,
                            master_x = x,
                            master_y = y,
                            x = 250,
                            y = 100,
                            w = 100,
                            h = 150,
                            path_image = "Formularios\\recursos_form\\NIVELES\\nivel_2.png",
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_dos")
        self._btn_home = Button_Image(screen=self._slave, 
                            master_x = x,
                            master_y = y,
                            x = w-70,
                            y = h-70,
                            w = 50,
                            h = 50,
                            color_background = (255,0,0),
                            color_border = (255,0,255),
                            onclick= self.btn_home_click,
                            onclick_param = "",
                            text = "",
                            font = "Verdana",
                            font_size = 15,
                            font_color = (0,255,0),
                            path_image = "Formularios\\recursos_form\\home.png")
        
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)

    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()