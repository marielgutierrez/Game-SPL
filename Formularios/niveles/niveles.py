import pygame, sys, json
from niveles.modo import *

class Nivel:
    def __init__(self, pantalla, w, h, personaje_principal, lista_plataformas, lista_plataformas_rect, imagen_fondo, time_inicial, time_limite, fuente, items, traps) -> None:
        self._slave = pantalla
        self.ancho = w
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.plataformas_rect = lista_plataformas_rect
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


        self.jugador.update(self._slave, self.plataformas_rect, self.traps)

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
            for lado in self.jugador.lados_rectangulo: 
                pygame.draw.rect(self._slave, "Red", self.jugador.lados_rectangulo[lado] , 2)

            for plataforma in self.plataformas:
                for lado in plataforma.lados_rectangulo:
                    pygame.draw.rect(self._slave, "Green", plataforma.lados_rectangulo[lado], 2)

            for item in self.items:
                for lado in item.lados_rectangulo:
                    pygame.draw.rect(self._slave, "Yellow", item.lados_rectangulo[lado], 2)
            
            for trap in self.traps:
                for lado in trap.lados_rectangulo:
                    pygame.draw.rect(self._slave, "Orange", trap.lados_rectangulo[lado], 2)

    def guardar_datos_nivel(self):
        '''
        funcion que guarda los datos del nivel en un JSON y desbloquea el siguiente
        '''
        try:
            with open('desbloqueo_niveles.json', 'r') as archivo:
                datos_niveles = json.load(archivo)
            
            for nivel in datos_niveles["niveles"]:
                if nivel["nivel"] == self.nivel_actual + 1:
                    nivel['desbloqueado'] = True
                    break
                nivel["puntaje"] = self.jugador.puntaje
            with open('desbloqueo_niveles.json', 'w') as archivo:
                json.dump(datos_niveles, archivo)
        except FileNotFoundError:
            print("No se encontró el archivo 'desbloqueo_niveles.json'")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON")
