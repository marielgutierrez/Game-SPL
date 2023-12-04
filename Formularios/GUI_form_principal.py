import pygame
from pygame.locals import *

from GUI_button import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_menu_play import *
from GUI_picture_box import *
from GUI_form_config import *

class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h, color_background, active=True, path_image=""):
        super().__init__(screen, x, y, w, h, color_background, active)

        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (w,h))

        self._slave = imagen_aux
        self.database = BaseDeDatos()
        self.diccionario_ranking = [{"jugador": "h", "score": 1000},
                    {"jugador": "x", "score": 900},
                    {"jugador": "z", "score": 750}]


        ### CONTROLES
        self.picturebox = PictureBox(self._slave, 85, 2, 320, 75, "Formularios/recursos_form/titulo_menu.png")
        self.btn_jugar = Button_Image(self._slave, x, y, 185, 150, 150, 60, "Formularios/recursos_form/boton_play.png", self.btn_jugar_click, "a" )
        self.btn_config = Button_Image(self._slave, x, y, 185,250,150,60,"Formularios/recursos_form/boton_opciones.png",self.btn_config_click, "lalal")
        self.btn_tabla = Button_Image(self._slave, x, y, 185,350,150,60,"Formularios/recursos_form/boton_rank.png",self.btn_tabla_click, "lalal")
        ###################
        #PARA SALIR DEL MENU PRINCIPAL E IR AL INICIO
        self._btn_home = Button_Image(screen=self._slave, 
                                    x = w-70,
                                    y = h-70,
                                    master_x = x,
                                    master_y = y,
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
                                    path_image = "Formularios/recursos_form/home.png")
        self.lista_widgets.append(self._btn_home)


        #Agrego los controles a la lista
        self.lista_widgets.append(self.picturebox)        
        self.lista_widgets.append(self.btn_config)      
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        ########################
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._master.blit(self._slave, (250,25))

    def btn_jugar_click(self, param):
        frm_jugar = FormMenuPlay(screen=self._master,
                                x = 250,
                                y = 25,
                                w = 500,
                                h = 550,
                                color_background = (220,0,220),
                                path_image="Formularios/recursos_form/menu.png",
                                active= True)
        self.show_dialog(frm_jugar)

    def btn_config_click(self, param):
        frm_config = FormMenuOptions(screen=self._master,
                                x = 250,
                                y = 25,
                                w = 500,
                                h = 550,
                                color_background = (220,0,220),
                                path_image="Formularios/recursos_form/menu.png",
                                active= True)
        self.show_dialog(frm_config)

    def btn_tabla_click(self, texto):
        self.diccionario_ranking = self.database.traer_datos()
        # dict_score = [{"Jugador": "Gio", "Score": 1000},
        #             {"Jugador": "Fausto", "Score": 990},
        #             {"Jugador": "Gonza", "Score": 800}                       
        #             ]
        form_puntaje = FormMenuScore(self._master,
                                    250,
                                    25,
                                    500,
                                    550,
                                    (220,0,220),
                                    "White",
                                    True,
                                    "Formularios/recursos_form/menu.png",
                                    self.diccionario_ranking,
                                    100,
                                    10,
                                    10)
        
        self.show_dialog(form_puntaje)

    def btn_home_click(self, param):
        self.end_dialog()

    def mostrar_datos_db(self):
        self.diccionario_ranking = self.database.traer_datos()
        #formularios
        #crear controles
        #agregarlo a la lista de controles
        #desactivar, activar la musica
        #mostrar 

        #interfaz, menu de opciones