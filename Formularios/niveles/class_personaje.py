import pygame
from pygame.locals import *
from niveles.configuraciones import obtener_rectangulos, reescalar_imagenes


class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, puntaje) -> None:
        #TAMAÑO
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #SCORE
        self.puntaje = puntaje
        #ESTADO
        self.estado = "quieto"
        #SPRITE
        # self.rect = self.animaciones["camina_derecha"][0].get_rect()
        # self.rect.topleft = posicion_inicial
        # self.grupo_sprites = group

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            #algo interno de la clase el contador de pasos, no por afuera
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        #por cada lado de la lista de lados se aumenta la velocidad para que el rectangulo acompañe la imagen
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, plataformas, items):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * - 1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")

        self.colision_con_item(items)
        self.aplicar_gravedad(pantalla, plataformas)

    def aplicar_gravedad(self, pantalla, plataformas):

        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            #mientras que esa suma sea menor al limite velocidad caida
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for plataforma in plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados["main"].top + 5
                break
            else:
                self.esta_saltando = True

    def colision_con_item(self, lista_items):
        for item in lista_items:
            if self.lados["main"].colliderect(item.lados["main"]):
                self.puntaje += 10
                lista_items.remove(item)

        return lista_items    

    # def actualizar_personaje(self, nuevo_estado):
    #     if nuevo_estado == "izquierda":
    #         if self.estado != "izquierda":
    #             #self.modificar_superficie(PERSONAJE_MOVIENDOSE, TAMAÑO_PERSONAJE_X, TAMAÑO_PERSONAJE_Y)
    #             self.girar_superficies(True,False)
    #     elif nuevo_estado == "derecha":
    #         if self.estado != "derecha":
    #             self.estado = nuevo_estado
    # #             self.modificar_superficie(PERSONAJE_MOVIENDOSE, TAMAÑO_PERSONAJE_X, TAMAÑO_PERSONAJE_Y)
    #     elif nuevo_estado == "quieto":
    #         if self.estado != "quieto":
    #             self.contador_pasos = 0
    # #             self.modificar_superficie(PERSONAJE_QUIETO, TAMAÑO_PERSONAJE_X, TAMAÑO_PERSONAJE_Y)
    #             if self.estado == "izquierda":
    #                 self.girar_superficies(True, False)
    #             self.estado = "quieto"

    # def girar_superficies(self):
    #      = pygame.transform.flip(imagen_original, True, False)




        #ACA ESTA EL ERROR DE PQ NO SALTA######################################################################
        #Estoy intentando que el lado de abajo (bottom) del personaje colisione con el top del cada plataforma
        #cuando ejecuto este for el personaje no puede saltar, si lo comento este puede saltar pero no colisiona con los rectangulos de las plataformas
        # for plataforma in plataformas:
        #     for rect in plataforma:
        #         if self.lados["bottom"].colliderect(rect["top"]):
        #             self.desplazamiento_y = 0
        #             self.esta_saltando = False
        #             self.lados["main"].bottom = rect["main"].top + 5
        #             break
        #         else:
        #             self.esta_saltando = True














#TODo SE EJECUTA EN UN BUCLE, ESTOS METODOS SE EJECUTARAN UNA Y OTRA VEZ MIENTRAS ESTE ANIMANDO AL PERSONAJE

#En cuanto a la gravedad:
#POTENCIA DEL SALTO
#POTENCIA DE LA CAIDA

#El rectangulo del personaje debe colisionar con el rectangulo del piso o de una plataforma
#para que a la hora de aplicar la gravedad caiga en el rectangulo de la superficie

#######EN COONFIGURACIONES