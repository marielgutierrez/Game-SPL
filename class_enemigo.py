import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, tamaño, path_imagen, posicion_inicial, velocidad) -> None:
        super().__init__()
        #TAMAÑO IMAGEN
        self.imagen = pygame.image.load(path_imagen)
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        #RECTANGULOS
        self.listaDisparo = []
        self.rect = self.imagen.get_rect()
        self.rect.top = posicion_inicial[1]
        self.rect.left = posicion_inicial[0]
        # self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0

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