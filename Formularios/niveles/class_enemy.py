import pygame
import random
from niveles.class_personaje import Personaje
from niveles.class_barra_de_vida import BarraDeVida
from niveles.class_proyectil import Proyectil

class Enemigos(Personaje):
    tipo = "enemigos varios"
    def __init__(self, tamaño: tuple, imagen, animaciones: dict, posicion_inicial, velocidad, img_proyectil) -> None: 
        super().__init__(tamaño, imagen, animaciones, posicion_inicial, velocidad, img_proyectil) 
        self.mover_arriba = False
        #self.es_caminante = es_caminante
        self.posicion_inicial = posicion_inicial
        self.lista_enemigos = []
        self.vivo = True
        self.direccion = random.choice([-1,1])

    def colisionar_proyectil(self, proyectil):
        return self.lados_rectangulo["main"].colliderect(proyectil.rectangulo)

    def morir(self):
        self.vivo = False
        muerte = pygame.mixer.Sound("Formularios/recursos/music/auch_robot.wav")
        muerte.set_volume(0.3)
        muerte.play(1)

    def muerte(self, pantalla):
        for lado in self.lados_rectangulo:
            self.lados_rectangulo[lado].y += self.velocidad + 10
            if not self.lados_rectangulo["main"].y > 1400:
                pantalla.blit(self.imagen, self.lados_rectangulo["main"])


class MiniBot(Enemigos):
    def __init__(self, tamaño: tuple, imagen, animaciones: dict, posicion_inicial, velocidad, es_caminante: bool, img_proyectil) -> None:
        super().__init__(tamaño, imagen, animaciones, posicion_inicial, velocidad, img_proyectil)
        self.es_caminante = es_caminante

    def mover_enemigo(self, pantalla, lista_lados_de_pisos, techo_lados_rect):
        if self.vivo:
            if self.es_caminante:
                for lado in self.lados_rectangulo:
                    self.lados_rectangulo[lado].x += self.velocidad * self.direccion
                for lados_rect in lista_lados_de_pisos:
                    if self.lados_rectangulo["right"].colliderect(lados_rect["top_right"]):
                        self.direccion = -1
                    elif self.lados_rectangulo["left"].colliderect(lados_rect["top_left"]):
                        self.direccion = 1
                if self.direccion == -1:
                    self.animar(pantalla, "camina_i")
                else:
                    self.animar(pantalla, "camina_d")
            else:
                for lado in self.lados_rectangulo:
                    self.lados_rectangulo[lado].y += self.velocidad * self.direccion
                for lados_plataforma in lista_lados_de_pisos:
                    if self.lados_rectangulo["bottom"].colliderect(techo_lados_rect):
                        self.direccion = 1
                    elif self.lados_rectangulo["bottom"].colliderect(lados_plataforma["top"]):
                        self.direccion = -1
                pantalla.blit(self.imagen, self.lados_rectangulo["main"])
        else:
            for lado in self.lados_rectangulo:
                self.lados_rectangulo[lado].y += 20

    def update_enemigo(self, pantalla, lista_lados_de_pisos, techo_lados_rect, paredes_lados_rect, jugador, distancia_minima, cantidad_daño):
        if self.vivo:
            self.mover_enemigo(pantalla, lista_lados_de_pisos, techo_lados_rect)
        else: 
            self.muerte(pantalla)


class FlyBot(Enemigos):
    def __init__(self, tamaño: tuple, imagen, animaciones: dict, posicion_inicial, velocidad, img_proyectil):
        super().__init__(tamaño, imagen, animaciones, posicion_inicial, velocidad, img_proyectil)

        self.direccion_x = random.choice([1,-1])
        self.direccion_y = random.choice([1,-1]) 

    def mover(self, pantalla, paredes_lados_rect):
        for lado in self.lados_rectangulo:
            self.lados_rectangulo[lado].x += self.velocidad * self.direccion_x
            self.lados_rectangulo[lado].y += self.velocidad * self.direccion_y
        for lados_rect in paredes_lados_rect:
            if self.lados_rectangulo["bottom"].colliderect(lados_rect["top"]):
                self.direccion_y = -1  # Cambiar dirección al chocar con una pared
            elif self.lados_rectangulo["top"].colliderect(lados_rect["bottom"]):
                self.direccion_y = 1  # Cambiar dirección al chocar con una pared
            elif self.lados_rectangulo["right"].colliderect(lados_rect["left"]):
                self.direccion_x = -1
            elif self.lados_rectangulo["left"].colliderect(lados_rect["right"]):
                self.direccion_x = 1
        if self.direccion_x == -1:
                self.animar(pantalla, "camina_i")#camina_izquierda
        else:
                self.animar(pantalla, "camina_d")


    def update_enemigo(self, pantalla, lista_lados_de_pisos, techo_lados_rect, paredes_lados_rect, jugador, distancia_minima, cantidad_daño):
        if self.vivo:
            self.mover(pantalla, paredes_lados_rect)
        #self.animar(pantalla, "camina_d")
        else:
            self.muerte(pantalla)

class BossFinal(Enemigos):
    def __init__(self, tamaño: tuple, imagen, animaciones: dict, posicion_inicial, velocidad, img_proyectil) -> None:
        super().__init__(tamaño, imagen, animaciones, posicion_inicial, velocidad, img_proyectil)
        self.barra_de_vida = BarraDeVida((850, 10), 100, 20)
        self.direccion = 1
        self.vida_actual = 100
        self.en_movimiento = False
        self.sonido = True
        #self.proyectiles = 3
        self.tiempo_entre_disparos = 5000
        self.puede_disparar = True

    def verificar_proximidad_jugador(self, jugador, distancia_minima):
        if abs(self.lados_rectangulo["main"].x - jugador.lados_rectangulo["main"].x) <= distancia_minima:
            self.activar_movimiento()
            self.efecto_sonido()
        else:
            self.desactivar_movimiento()

    def seguir_personaje(self, jugador, pantalla, paredes_lados_rect):
        if self.en_movimiento:
            desplazamiento_x = self.velocidad * self.direccion
            for lado in self.lados_rectangulo:
                if self.lados_rectangulo["main"].x < jugador.lados_rectangulo["main"].x:
                    colisiono = False
                    for rect_pared in paredes_lados_rect:
                        if self.lados_rectangulo["main"].colliderect(rect_pared["left"]):
                            colisiono = True
                    if not colisiono:
                        self.lados_rectangulo[lado].x += desplazamiento_x
                    self.animar(pantalla, "camina")
                elif self.lados_rectangulo["main"].x > jugador.lados_rectangulo["main"].x:
                    colisiono = False
                    for rect_pared in paredes_lados_rect:
                        if self.lados_rectangulo["main"].colliderect(rect_pared["right"]):
                            colisiono = True
                    if not colisiono:
                        self.lados_rectangulo[lado].x -= desplazamiento_x
                    self.animar(pantalla, "camina")
                else:
                    self.desactivar_movimiento()
        else:
            self.verificar_proximidad_jugador(jugador, 500)
                
    def recibir_daño(self, cantidad_daño):
        self.vida_actual -= cantidad_daño
        if self.vida_actual <= 0:
            self.morir()

    def disparar(self, pantalla):
        posicion_actual = (self.lados_rectangulo["main"].x, self.lados_rectangulo["main"].y + 40)
        
        #if self.proyectiles > 0:
        if self.puede_disparar:
            print("entro al if puede_disparar, enemigos")
            proyectil = Proyectil((30,20), self.img_proyectil, {"quieto":[self.img_proyectil]}, posicion_actual, False, self.direccion)
            self.lista_proyectiles.append(proyectil)
            self.tiempo_ultimo_disparo = pygame.time.get_ticks()
            self.puede_disparar = False
        tiempo_actual = pygame.time.get_ticks()
        if not self.puede_disparar and tiempo_actual - self.tiempo_ultimo_disparo >= self.tiempo_entre_disparos:
            self.puede_disparar = True
            #self.proyectiles -= 1
    
    def activar_movimiento(self):
        self.en_movimiento = True

    def desactivar_movimiento(self):
        self.en_movimiento = False

    def muerte(self, pantalla):
        self.animar(pantalla, "muerte")
        for lado in self.lados_rectangulo:
            self.lados_rectangulo[lado].y += self.velocidad
        
    def efecto_sonido(self):
        if self.sonido:
            efecto = pygame.mixer.Sound("Formularios/recursos/music/ruido.wav")
            efecto.play(1)
            self.sonido = False    
    
    def update_enemigo(self, pantalla, lista_lados_de_pisos, techo_lados_rect, paredes_lados_rect, jugador, distancia_minima): #self, pantalla, lista_lados_de_pisos, techo_lados_rect, paredes_lados_rect
        if self.vivo:
            self.verificar_proximidad_jugador(jugador, distancia_minima)
            self.seguir_personaje(jugador, pantalla, paredes_lados_rect)
            self.barra_de_vida.update_vida(pantalla, self.vida_actual)
            self.disparar(pantalla)
        else:
            self.muerte(pantalla)

