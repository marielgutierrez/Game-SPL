import pygame
from pygame.locals import *
from niveles.configuraciones import obtener_rectangulos
from niveles.class_objeto_juego import Objeto_Juego

class Personaje(Objeto_Juego):
    def __init__(self, tamaño:tuple, imagen, animaciones, posicion_inicial:tuple, velocidad) -> None:
        super().__init__(tamaño, imagen, posicion_inicial)
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #ANIMACIONES
        self.fotograma_actual = 0
        self.que_hace = "quieto"
        self.direccion = 1
        self.contador_pasos = 0
        self.estado_normal = True
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        # #self.lados = obtener_rectangulos(self.rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.tengo_llave = False
        #SCORE
        self.puntaje = 0
        #ESTADO
        #self.estado = "quieto"
        #VIDAS
        self.vidas = 3
        #PARTIDA
        self.ganaste = False
        self.perdiste = False

        ## PROYECTILES
        # self.proyectiles = 0
        # self.lista_proyectiles = []
        # self.img_proyectil = img_proyectil
        # self.puede_disparar = True#False
        # self.tiempo_ultimo_disparo = 0
        # self.tiempo_entre_disparos = 1000

        # self.puede_colisionar = True

        # #tiempo
        # self.tiempo_colision = 0
        # self.tiempo_espera_colision = 1000

    def reescalar_animaciones(self):
        '''
        brief: se encarga de escalar las animaciones
        '''
        for clave, lista in self.animaciones.items():
            for i in range(len(lista)):
                lista[i] = self.reescalar_imagen(lista[i])

    # def reescalar_animaciones(self):
    #     for clave in self.animaciones:
    #         reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    ##esta bien
    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados_rectangulo["main"])
        self.contador_pasos += 1
    
    
    def mover(self, velocidad):
        '''
        brief: Desplaza al personaje en el eje horizontal según la velocidad
        '''
        for lado in self.lados_rectangulo:
            self.lados_rectangulo[lado].x += velocidad
        #super().mover(velocidad)
        # for lado in self.lados:
        #     self.lados[lado].x += velocidad

    def update(self, pantalla, plataformas_rect, traps):
        '''
        brief: Actualiza el estado del personaje según la acción actual se muestra
        la animación que corresponda y se realiza el desplazamiento
        '''
        match self.que_hace:
            case "derecha":
                colision = False
                if not self.esta_saltando:
                    if self.estado_normal:
                        self.animar(pantalla, "camina_derecha")
                    else:
                        self.animar(pantalla, "camina_d_muerte")
                self.direccion = 1

                for rect_plataforma in plataformas_rect:
                    if self.lados_rectangulo["right"].colliderect(rect_plataforma["left"]):
                        colision = True
                if not colision:
                    self.mover(self.velocidad)    
                #self.mover(self.velocidad)
            case "izquierda":
                colision = False
                if not self.esta_saltando:
                    if self.estado_normal:
                        self.animar(pantalla, "camina_izquierda")
                    else:
                        self.animar(pantalla, "camina_i_muerte")
                self.direccion = -1
                #self.mover(self.velocidad * - 1) ##por alguna razon hace vaya mas rapido

                for rect_plataforma in plataformas_rect:
                    if self.lados_rectangulo["left"].colliderect(rect_plataforma["right"]):
                        colision = True
                if not colision:
                    self.mover(self.velocidad * -1)
            case "salta":
                colision = False
                for rect_plataforma in plataformas_rect:
                    if self.lados_rectangulo["top"].colliderect(rect_plataforma["bottom"]):
                        colision = True
                if not colision:        
                    if not self.esta_saltando:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    if self.direccion == 1:
                        if self.estado_normal:
                            self.animar(pantalla, "quieto")
                        else:
                            self.animar(pantalla, "quieto_d_muerte")
                    else:
                        if self.estado_normal:
                            self.animar(pantalla, "quieto_i")
                        else:
                            self.animar(pantalla, "quieto_i_muerte")

        self.colision_trampa(traps)
        self.aplicar_gravedad(pantalla, plataformas_rect)
        #self.colision_plataformas(plataformas)


    def aplicar_gravedad(self, pantalla, plataformas_rect):
        '''
        brief: Aplica la gravedad al personaje permitiendo que caiga
        si no está en contacto con alguna plataforma
        '''
        # if self.esta_saltando:
        #     self.animar(pantalla, "salta")
        if self.esta_saltando:
            if self.direccion == 1:
                if self.estado_normal:
                    self.animar(pantalla, "salta")
                else:
                    self.animar(pantalla, "salta_d_muerte")
            else:
                if self.estado_normal:
                    self.animar(pantalla, "salta_i")
                else:
                    self.animar(pantalla, "salta_i_muerte")

            for lado in self.lados_rectangulo:
                self.lados_rectangulo[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for piso in plataformas_rect:
            if self.lados_rectangulo["bottom"].colliderect(piso["top"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados_rectangulo["main"].bottom = piso["main"].top
                break
            else:
                self.esta_saltando = True

        # for plataforma in plataformas:
        #     if self.lados["bottom"].colliderect(plataforma.lados["top"]):
        #         self.desplazamiento_y = 0
        #         self.esta_saltando = False
        #         self.lados["main"].bottom = plataforma.lados["main"].top + 5
        #         break

    def colision_con_item(self, lista_items):
        '''
        brief: Se encarga de la colision del personaje con cada item
        '''
        for item in lista_items:
            if self.lados_rectangulo["main"].colliderect(item.lados_rectangulo["main"]):
                self.puntaje += 100
                lista_items.remove(item)

        return lista_items
    
    def colision_trampa(self, traps):
        '''
        brief: Se encarga de la colision del personaje con cada trampa
        '''
        for trap in traps:
            if self.lados_rectangulo["bottom"].colliderect(trap.lados_rectangulo["top"]):
                self.vidas -= 1

    def efecto_sonido_auch(self):
        '''
        se encarga de reproducir un sonido de dolor
        '''
        auch = pygame.mixer.Sound("sonidos_personaje/sonido_auch.mp3")
        auch.set_volume(0.3)
        auch.play(1)


    # def colision_plataformas(self, plataformas):
    #     for plataforma in plataformas:
    #         if self.lados["main"].colliderect(plataforma.lados["main"]):
    #             pass

    #     else:
    #         self.esta_saltando = True














#TODo SE EJECUTA EN UN BUCLE, ESTOS METODOS SE EJECUTARAN UNA Y OTRA VEZ MIENTRAS ESTE ANIMANDO AL PERSONAJE

#En cuanto a la gravedad:
#POTENCIA DEL SALTO
#POTENCIA DE LA CAIDA

#El rectangulo del personaje debe colisionar con el rectangulo del piso o de una plataforma
#para que a la hora de aplicar la gravedad caiga en el rectangulo de la superficie

#######EN COONFIGURACIONES