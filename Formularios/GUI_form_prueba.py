import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_menu_play import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True, path_image=""):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.1
        self.flag_play = True

        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (w,h))

        self._slave = imagen_aux
        pygame.mixer.init()
        ### CONTROLES
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White","Red", "Blue",2, font= "Comic Sans", font_size=15, font_color ="Black" )
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font = "Verdana", font_size=15,font_color="White")
        self.label_volumen = Label(self._slave, 370, 190, 100,50,"20%", "Comic Sans", 15,"White", "Formularios\\recursos_form\\Table.png")#FALTA imagen
        self.slider_volumen = Slider(self._slave, x, y,100,200,250,12,self.volumen,"Violet","White")
        
        self.btn_tabla = Button_Image(self._slave, x, y, 255,100,50,50,"Formularios\\recursos_form\\Menu_BTN.png",self.btn_tabla_click, "lalal")
        self.btn_jugar = Button_Image(self._slave, x, y, 300, 100, 50, 50, "Formularios\\recursos_form\\BOTONES\\0.png", self.btn_jugar_click, "a" )
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
                                    path_image = "Formularios\\recursos_form\\home.png")
        self.lista_widgets.append(self._btn_home)


        #Agrego los controles a la lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)        
        self.lista_widgets.append(self.slider_volumen)        
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        ########################


        pygame.mixer.music.load("Formularios\\recursos\\music\\hero-80s-127027.mp3") #poner musica path

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        #self.render()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                #self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)
    # def render(self):
    #     self._slave.fill(self._color_background)

    def btn_jugar_click(self, param):
        frm_jugar = FormMenuPlay(screen=self._master,
                                x = self._master.get_width() / 2 - 250,
                                y = self._master.get_height() / 2 - 250,
                                w = 500,
                                h = 550,
                                color_background = (220,0,220),
                                path_image="Formularios\\recursos_form\\Window.png",
                                color_border = (255,255,255),
                                active= True)
        self.show_dialog(frm_jugar)

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pausa")

        self.flag_play = not self.flag_play
        # nombre = self.txtbox.get_text()
        # print(nombre)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        dict_score = [{"Jugador": "Gio", "Score": 1000},
                    {"Jugador": "Fausto", "Score": 990},
                    {"Jugador": "Gonza", "Score": 800}                       
                    ]
        
        form_puntaje = FormMenuScore(self._master,
                                    250,
                                    25,
                                    500,
                                    550,
                                    (220,0,220),
                                    "White",
                                    True,
                                    "Formularios\\recursos_form\\Window.png",
                                    dict_score,
                                    100,
                                    10,
                                    10)
        
        self.show_dialog(form_puntaje)

    def btn_home_click(self, param):
        self.end_dialog()

        #formularios
        #crear controles
        #agregarlo a la lista de controles
        #desactivar, activar la musica
        #mostrar 

        #interfaz, menu de opciones