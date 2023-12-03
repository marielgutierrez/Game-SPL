import pygame
from pygame.locals import *
from base_datos import BaseDeDatos
from GUI_form import *
from GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height())
        self.nombre_jugador = ""
        self.nivel = nivel
        nivel._slave = self._slave
        self.database = BaseDeDatos()
        self.habilitar_nivel = False
        self.puntaje = None

        self._btn_home = Button_Image(screen=self._slave, 
                            master_x = self._x,
                            master_y = self._y,
                            x = self._w - 100,
                            y = self._h - 100,
                            w = 50,
                            h = 50,
                            path_image = "Formularios/recursos_form/home.png",
                            onclick= self.btn_home_click,
                            onclick_param = "")
        
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)

    def obtener_nombre(self, nombre):
        self.nombre_jugador = nombre

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.nivel.update(lista_eventos) 
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw() 
            self.game_over() #PROBANDO
        else:
            self.hijo.update(lista_eventos)#NO SE SI FUNCIONA

    def game_over(self):
        if self.nivel.verificar_victoria_game_over():
            print("entro en el verificar_victoria form contenedor")
            #self.habilitar_nivel = True
            self.puntaje = self.nivel.nivel_puntaje

    def cargar_db(self, nombre):
        if self.puntaje != None:
            self.database.insertar_datos(nombre, self.puntaje, self.nivel.nivel_actual)

    def btn_home_click(self, param):
        self.end_dialog()    
