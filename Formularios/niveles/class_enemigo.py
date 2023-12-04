import pygame
from pygame.locals import *

class Enemy(object):
    def __init__(self, tamaño, path_imagenA, path_imagenB, posicion_inicial, velocidad, limite) -> None:
        #TAMAÑO IMAGEN
        self.imagenA = pygame.image.load(path_imagenA)
        self.imagenB = pygame.image.load(path_imagenB)

        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        
        self.imagenA = pygame.transform.scale(self.imagenA, (self.ancho, self.alto))
        self.imagenB = pygame.transform.scale(self.imagenB, (self.ancho, self.alto))

        #RECTANGULOS
        self.listaImagenes = [self.imagenA, self.imagenB]
        self.posImagen = 0
        self.imagenEnemigo = self.listaImagenes[self.posImagen]
        self.rect = self.imagenEnemigo.get_rect()

        self.listaDisparo = []
        self.y = posicion_inicial[1]
        self.x = posicion_inicial[0]
        # self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        ###
        self.va_izquierda = False
        self.va_derecha = False
        self.contador_pasos = 0
        self.camino = [self.x, limite]



        # self.tiempoCambio = 1

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            #algo interno de la clase el contador de pasos, no por afuera
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1


    def se_mueve_solo(self):
        if self.velocidad > 0:
            if self.x + self.velocidad < self.camino[1]:
                self.x += self.velocidad 
                self.va_derecha = True
                self.va_izquierda = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0
        else:
            if self.x - self.velocidad > self.camino[0]:
                self.x += self.velocidad 
                self.va_izquierda = True
                self.va_derecha = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0

    # def comportamiento(self, tiempo):
    #     #Definimos el comportamiento de la animacion en un determinado tiempo 
    #     if self.tiempoCambio == tiempo:
    #         self.posImagen += 1
    #         self.tiempoCambio += 1

    #         if self.posImagen > len(self.listaImagenes)-1:
    #             self.posImagen = 0

    # def reescalar_animaciones(self):
    #     for clave in self.animaciones:
    #         reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    # def animar(self, pantalla, que_animacion:str):
    #     animacion = self.animaciones[que_animacion]
    #     largo = len(animacion)

    #     if self.contador_pasos >= largo:
    #         #algo interno de la clase el contador de pasos, no por afuera
    #         self.contador_pasos = 0

    #     pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
    #     self.contador_pasos += 1

    # def mover(self, velocidad):
    #     #por cada lado de la lista de lados
    #     for lado in self.lados:
    #         self.lados[lado].x += velocidad

    # def update(self, pantalla):
    #     match self.que_hace:
    #         case "derecha":
    #             self.animar(pantalla, "camina_derecha")
    #             self.mover(self.velocidad)
    #         case "izquierda":
    #             self.animar(pantalla, "camina_izquierda")
    #             self.mover(self.velocidad * - 1)
    #         case "salta":
    #             self.esta_saltando = True
    #             self.desplazamiento_y = self.potencia_salto
    #         case "quieto":
    #             self.animar(pantalla, "quieto")

    #     self.aplicar_gravedad(pantalla)

#TODo SE EJECUTA EN UN BUCLE, ESTOS METODOS SE EJECUTARAN UNA Y OTRA VEZ MIENTRAS ESTE ANIMANDO AL PERSONAJE

#En cuanto a la gravedad:
#POTENCIA DEL SALTO
#POTENCIA DE LA CAIDA

#El rectangulo del personaje debe colisionar con el rectangulo del piso o de una plataforma
#para que a la hora de aplicar la gravedad caiga en el rectangulo de la superficie

#######EN COONFIGURACIONES