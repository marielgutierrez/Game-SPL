from GUI_form import Form
import pygame
from pygame.locals import *
#from manejador_niveles import ManejadorNiveles
from GUI_button_image import Button_Image

class FormPerdedor(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        #self.manejador_niveles = ManejadorNiveles(self._master)#self._master
        path_image = "Formularios/recursos_forms/cartel_lose.jpg"
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w/2,h/2))
        self._slave = aux_image

        #self.btn_ranking = Button_Image(self._slave, x, y, w/2-75, 500, 200, 70, "recursos_form/BOTONES/3.png", self.btn_tabla_click, "lalala", "RANKING", font = "Consolas", font_size=30, font_color="White")
        #self.btn_niveles = Button_Image(self._slave, x, y, w/2-75, 400, 200, 70, "recursos_form/home.png", self.btn_niveles_click, "Nombre", "NIVELES", font = "Consolas", font_size=30, font_color="White")
        #self.lista_widgets.append(self.btn_ranking)
        #self.lista_widgets.append(self.btn_niveles)
        #pygame.mixer.init()
        efecto_sonid = pygame.mixer.Sound("Formularios/recursos/music/sonido_loser.mp3")
        efecto_sonid.set_volume(0.3)
        efecto_sonid.play(1)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()

    def btn_niveles_click(self, texto):
        self.end_dialog()
        #form_niveles = FormMenuPlay(self._master, 0, 0, 1400, 800, "Black", "White", -1, True, "Recursos_fondos/habitacion.jpg")
        #self.show_dialog(form_niveles)

    def btn_tabla_click(self, texto):
        pass
        #form_puntaje = FormMenuScore(self._master, 0, 0, 1400, 800, "Black", "White", -1, True, "Recursos_fondos/habitacion.jpg", dict_score, 100, 100,10)
        #self.show_dialog(form_puntaje)
