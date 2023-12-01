import pygame
from pygame.locals import *

from GUI_form import *
from GUI_button_image import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_picture_box import *

class FormMenuOptions(Form):
    def __init__(self, screen, x, y, w, h, color_background, path_image, active):
        super().__init__(screen, x, y, w, h, color_background, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self.volumen = 0.1
        self.flag_play = True

        self.picturebox = PictureBox(self._slave, 90, 4, 320, 60, "Formularios\\recursos_form\\titulo_options.png")
        self.subtitulo = PictureBox(self._slave, 175, 150, 200, 20, "Formularios\\recursos_form\\music_titulo.png")        
        self.btn_play = Button(self._slave, x, y, 190, 250, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font = "Verdana", font_size=15,font_color="White")
        self.label_volumen = Label(self._slave, 370, 190, 100,50,"20%", "Comic Sans", 15,"White", "Formularios\\recursos_form\\Table.png")#FALTA imagen
        self.slider_volumen = Slider(self._slave, x, y,100,200,250,12,self.volumen,"Violet","White")
        
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
        
        pygame.mixer.music.set_volume(self.volumen)

        self.lista_widgets.append(self.picturebox)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.subtitulo)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)        
        self.lista_widgets.append(self.slider_volumen)        


    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)
    
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


    def btn_home_click(self, param):
        self.end_dialog()