import pygame, sys
from modo import *
#from main_copy import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo, time_inicial, time_limite, fuente) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.time_inicial = time_inicial
        self.time_limite = time_limite
        self.fuente = fuente


    def update(self, lista_eventos):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.time_inicial
        texto = self.fuente.render(f"Time: {tiempo_transcurrido // 1000}", True, "White")

        if tiempo_transcurrido >= self.time_limite:
            pygame.quit()
            sys.exit(0)

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()      
        self.leer_inputs()
        self.actualizar_pantalla(texto)
        self.dibujar_rectangulos()

    def actualizar_pantalla(self, texto):
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(texto, (10, 10))
        #self._slave.blit(mini_bot.imagenA, mini_bot.rect.topleft)

        for plataforma in self.plataformas:
            plataforma.draw(self._slave) #hacer arreglos con .draw definirlo en la clase Plataforma

        self.jugador.update(self._slave, self.plataformas)


    def leer_inputs(self):
    
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_RIGHT]):
            #and self.jugador.rectangulo.x > self.jugador.velocidad
            self.jugador.que_hace = "derecha"
        elif(keys[pygame.K_LEFT]):
            #and self.jugador.rectangulo.x < self._slave.width - self.jugador.ancho - 5
            #verificar la logica para que el personaje no se salga de la pantalla
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
