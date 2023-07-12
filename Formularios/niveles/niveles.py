import pygame, sys
from niveles.modo import *

class Nivel:
    def __init__(self, pantalla, w, h, personaje_principal, lista_plataformas, imagen_fondo, time_inicial, time_limite, fuente, items, traps) -> None:
        self._slave = pantalla
        self.ancho = w
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.time_inicial = time_inicial
        self.time_limite = time_limite
        self.fuente = fuente
        self.items = items
        self.traps = traps


    def update(self, lista_eventos):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.time_inicial
        cronometro = self.fuente.render(f"Time: {tiempo_transcurrido // 1000}", True, "White")

        if tiempo_transcurrido >= self.time_limite:
            pygame.quit()
            sys.exit(0)
        
        score = self.fuente.render("Score: {0}".format(self.jugador.puntaje), True, "White")
        vidas = self.fuente.render("Vidas: {0}".format(self.jugador.vidas), True, "White")

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()      
        self.leer_inputs()
        self.actualizar_pantalla(cronometro, score, vidas)
        self.dibujar_rectangulos()

    def actualizar_pantalla(self, cronometro, score, vidas):
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(cronometro, (10, 10))
        self._slave.blit(vidas, (400, 10))
        
        #self._slave.blit(mini_bot.imagenA, mini_bot.rect.topleft)
        
        for plataforma in self.plataformas:
            plataforma.draw(self._slave)
        
        for item in self.jugador.colision_con_item(self.items):
            item.draw(self._slave)

        for trap in self.traps:
            trap.draw(self._slave)


        self.jugador.update(self._slave, self.plataformas, self.traps)

        self._slave.blit(score, (200, 10))

    def leer_inputs(self):
        #estado = "quieto"
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_RIGHT]) and self.jugador.rectangulo.x < self.ancho - self.jugador.velocidad - self.jugador.rectangulo.width:
            self.jugador.que_hace = "derecha"
        elif(keys[pygame.K_LEFT]) and self.jugador.rectangulo.x > 0:
            self.jugador.que_hace = "izquierda"
        elif(keys[pygame.K_UP]):
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"

    def dibujar_rectangulos(self):
        
        if get_mode():
            #pygame.draw.rect(self._slave, "Blue", piso, 2)
            for lado in self.jugador.lados: 
                pygame.draw.rect(self._slave, "Red", self.jugador.lados[lado] , 2)

            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 2)

            for item in self.items:
                for lado in item.lados:
                    pygame.draw.rect(self._slave, "Yellow", item.lados[lado], 2)
            
            for trap in self.traps:
                for lado in trap.lados:
                    pygame.draw.rect(self._slave, "Orange", trap.lados[lado], 2)

