from GUI_form import Form
import pygame
from pygame.locals import *
from GUI_button_image import Button_Image

class FormGanador(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        #self.manejador_niveles = ManejadorNiveles(self._master)#self._master
        path_image = "recursos_form/cartel_win.jpg"
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w/2,h/2))
        self._slave = aux_image

        #self.ganaste = Label(self._slave, w/4 -200, 150, 400, 200, "", "Arial", 1, "Black", "fuentes/ganaste.png")
        self.btn_ranking = Button_Image(self._slave, x, y, w/2-75, 500, 200, 70, "recursos_form/BOTONES/3.png", self.btn_tabla_click, "lalala", "RANKING", font = "Consolas", font_size=30, font_color="White")
        self.btn_niveles = Button_Image(self._slave, x, y, w/2-75, 400, 200, 70, "recursos_form/home.png", self.btn_niveles_click, "Nombre", "NIVELES", font = "Consolas", font_size=30, font_color="White")
        #self.lista_widgets.append(self.ganaste)
        self.lista_widgets.append(self.btn_niveles)
        sonido = pygame.mixer.Sound("recursos/music/sonido_winner.mp3")
        sonido.set_volume(0.3)
        sonido.play()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()

    def btn_niveles_click(self, texto):
        self.end_dialog()        

    def btn_tabla_click(self, texto):
        pass    
