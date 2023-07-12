import pygame
from pygame.locals import *
from GUI_form_principal import *
from GUI_form import *
from GUI_button_image import *

class FormMenuInicio(Form):
    def __init__(self, pantalla: pygame.Surface, path_image):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), active=True)
        self.flag_play = True
        self._width = pantalla.get_width()
        self._height = pantalla.get_height()
        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (self._width, self._height))
        self._slave = imagen_aux
        self._btn_start = Button_Image(screen=self._slave, 
                            master_x = self._x,
                            master_y = self._y,
                            x = 440,
                            y = 369,
                            w = 120,
                            h = 50,
                            path_image = "Formularios\\recursos_form\\start_boton.png",
                            onclick= self.btn_start_click,
                            onclick_param = "")
        
        self.lista_widgets.append(self._btn_start)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                #self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_start_click(self, param):
        form_prueba = FormPrincipal(self._master,
                                250, 
                                25,
                                500,
                                550,
                                "Blue",
                                True,
                                "Formularios\\recursos_form\\menu.png")
        self.show_dialog(form_prueba)