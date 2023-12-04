import pygame
from pygame.locals import *

from GUI_form import *
from GUI_button_image import *
from GUI_picture_box import *
from GUI_form_contenedor_nivel import *
from GUI_textbox import *
from niveles.manejador_niveles import Manejador_niveles


class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, path_image, active):
        super().__init__(screen, x, y, w, h, color_background, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self.nombre_jugador = "jugador1"
        self.guardado = False
        self.habilitado_guardar = False


        self.picturebox = PictureBox(self._slave, 95, 2, 315, 70, "Formularios/recursos_form/titulo_levels.png")
        self.subtitulo = PictureBox(self._slave, 150, 300, 200, 20, "Formularios/recursos_form/name_titulo.png")        
        self.txtbox = TextBox(self._slave, x, y, 185,350, 150, 30, "Gray", "White","Magenta", "Blue",2, font= "Consolas", font_size=15, font_color ="Black" )


        self._btn_level_1 = Button_Image(screen=self._slave,
                            master_x = x,
                            master_y = y,
                            x = 80,
                            y = 100,
                            w = 100,
                            h = 150,
                            path_image = "Formularios/recursos_form/NIVELES/nivel_1.png",
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_uno")
        self._btn_level_2 = Button_Image(screen=self._slave,
                            master_x = x,
                            master_y = y,
                            x = 195,
                            y = 100,
                            w = 100,
                            h = 150,
                            path_image = "Formularios/recursos_form/NIVELES/nivel_2.png",
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_dos")
        self._btn_level_3 = Button_Image(screen=self._slave,
                            master_x = x,
                            master_y = y,
                            x = 308,
                            y = 100,
                            w = 100,
                            h = 150,
                            path_image = "Formularios/recursos_form/NIVELES/nivel_3.png",
                            onclick = self.entrar_nivel,
                            onclick_param = "nivel_tres")
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
                            path_image = "Formularios/recursos_form/home.png")
        self._btn_guardar = Button(screen=self._slave,
                            master_x= x,
                            master_y= y,
                            x= 148,
                            y= 400,
                            w=240,
                            h=30,
                            color_background="Magenta",
                            color_border="Black",
                            onclick= self.btn_guardar_click,
                            onclick_param= "Guardar",
                            text="Guardar partida",
                            font="Consolas",
                            font_size= 20,
                            font_color="White"
                            )

        self.lista_widgets.append(self.picturebox)
        self.lista_widgets.append(self.subtitulo)
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_guardar)


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
        self.nombre_jugador = self.txtbox.get_text()
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        if nivel != False:
            self.habilitado_guardar = True
            self.frm_contenedor_nivel = FormContenedorNivel(self._master, nivel)
            self.show_dialog(self.frm_contenedor_nivel)
    
    def btn_guardar_click(self, param):
        if self.habilitado_guardar:# and self.form_contenedor_nivel.puntaje != None:
            if not self.guardado:
                self.frm_contenedor_nivel.cargar_db(self.nombre_jugador)
                self._btn_guardar._color_background = "Black"
                self._btn_guardar._font_color = "White"
                self._btn_guardar.set_text("Guardado")
                self.guardado = True

    def btn_home_click(self, param):
        self.end_dialog()