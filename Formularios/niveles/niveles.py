import pygame, sys, json
from niveles.modo import *
from form_ganador import FormGanador
from form_perdedor import FormPerdedor

class Nivel:
    def __init__(self, pantalla, w, h, personaje_principal, lista_plataformas, lista_plataformas_rect, imagen_fondo, fuente, items, traps, llave, 
                lista_armas, portal, nivel_actual:int, aparece:bool, lista_enemigos, boss, lista_paredes_rect, lista_cajas) -> None:
        self._slave = pantalla
        self.ancho = w
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.plataformas_rect = lista_plataformas_rect
        self.lista_paredes_rect = lista_paredes_rect
        self.img_fondo = imagen_fondo
        self.fuente = fuente
        self.items = items
        self.lista_armas = lista_armas
        self.traps = traps
        self.llave = llave
        self.portal = portal
        self.lista_cajas = lista_cajas
        self.enemigos = lista_enemigos
        self.boss_final = boss
        self.aparece = aparece
        self.nivel_actual = nivel_actual
        self.nivel_puntaje = 0
        ### vidas
        img_corazon = pygame.image.load("Formularios/recursos/corazon.png")
        self.img_corazon = pygame.transform.scale(img_corazon, (20,20))
        self.rect_corazon = self.img_corazon.get_rect()
        self.rect_corazon.x = 470
        self.rect_corazon.y = 10
        ### proyectiles
        self.lista_proyectiles_eliminar = []
        self.lista_enemigos_eliminar = []
        self.lista_proyectilesboss_eliminar = []
        ### tiempo
        self.pausado = False
        self.tiempo_limite = 60000
        self.tiempo_pausado = 0
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tiempo_transcurrido = 0
        ##formularios
        self.game_over = False

    def update(self, lista_eventos):
        '''
        Se encarga de actualizar el juego
        '''
        # if tiempo_transcurrido >= self.time_limite:
        #     pygame.quit()
        #     sys.exit(0)
        #score = self.fuente.render("Score: {0}".format(self.jugador.puntaje), True, "White")
        vidas = self.fuente.render("VIDAS:", True, "White")

        if self.tiempo_transcurrido >= self.tiempo_limite:
            self.jugador.perdiste = True
            print("tiempo acabado 1")
        # if self.tiempo_restante < 0:
        #     self.jugador.perdiste = True  # Marcar el jugador como perdedor
        #     print("tiempo acabado")
        if not self.pausado:
            self.tiempo_pausado = pygame.time.get_ticks() - self.tiempo_inicio
            if not self.jugador.ganaste and not self.jugador.perdiste:
                for evento in lista_eventos:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_TAB:
                            cambiar_modo()      
                self.leer_inputs()
                self.actualizar_pantalla(vidas)
                self.dibujar_rectangulos()
                self.dibujar_vidas_score()
            else:
                self.mostrar_mensaje(lista_eventos)
                print("el jugador perdio o ganó, muestra msj")
        else:
            self.tiempo_pausado = pygame.time.get_ticks()
    

    def actualizar_pantalla(self, vidas):
        '''
        Se encarga de blitear y actualizar los objetos del juego
        '''
        self._slave.blit(self.img_fondo, (0,0))
        self._slave.blit(vidas, (400, 10))
        #self._slave.blit(mini_bot.imagenA, mini_bot.rect.topleft)
        self.portal.draw(self._slave)
        #self.llave.draw(self._slave)
        self.jugador.update(self._slave, self.plataformas_rect, self.traps, self.llave, 
                            self.portal, self.enemigos, self.boss_final, self.traps, self.aparece)
        #FALTA CAJAS
        for plataforma in self.plataformas:
            plataforma.draw(self._slave)
        
        for item in self.jugador.colision_con_item(self.items):
            item.draw(self._slave)

        for trap in self.traps:
            trap.draw(self._slave)

        for arma in self.lista_armas:
            arma.acumular_armas(self._slave, self.jugador)
            if self.nivel_actual == 1:
                arma.mostrar_mensaje(self._slave)

        for enemigo in self.enemigos: 
            enemigo.update_enemigo(self._slave, self.plataformas_rect, self.plataformas_rect[1]["bottom"], self.lista_paredes_rect, self.jugador, 500, 100)#self, pantalla, lista_lados_de_pisos, techo_lados_rect, paredes_lados_rect, jugador, distancia_minima, cantidad_daño

        for proyectil in self.jugador.lista_proyectiles:
            proyectil.update(self._slave)
            for enemigo in self.enemigos:
                if proyectil.colisionar_enemigo(enemigo):
                    self.lista_proyectiles_eliminar.append(proyectil)
                    enemigo.morir()
                    self.jugador.puntaje += 100
                    break
                elif proyectil.rectangulo.x >= 1400 or proyectil.rectangulo.x < 0: ##OJO ACA 1400
                    self.lista_proyectiles_eliminar.append(proyectil)
                    break
        for proyectil in self.lista_proyectiles_eliminar:
            self.jugador.lista_proyectiles.remove(proyectil)
        self.lista_proyectiles_eliminar.clear()

        for proyectil in self.boss_final.lista_proyectiles:
            proyectil.mover_proyectil_boss(self._slave)
            if proyectil.colisionar_enemigo(self.jugador):
                self.lista_proyectilesboss_eliminar.append(proyectil)
                break
            elif proyectil.rectangulo.y >= 900 or proyectil.rectangulo.y < 0:
                    self.lista_proyectilesboss_eliminar.append(proyectil)
                    break
        for proyectil in self.lista_proyectiles_eliminar:
            pass
        self.lista_proyectilesboss_eliminar.clear()

        for caja in self.lista_cajas:
            caja.update_caja(self._slave, self.jugador, self.plataformas)
            if caja.colisionar_boss(self.boss_final):
                auch_boss = pygame.mixer.Sound("Formularios/recursos/music/auch_robot.wav")
                auch_boss.set_volume(0.3)
                auch_boss.play(1)
                self.lista_cajas.remove(caja)
                self.boss_final.recibir_daño(35)
                self.jugador.puntaje += 500
        if self.aparece:
            self.boss_final.update_enemigo(self._slave, self.plataformas_rect, 
                                        self.plataformas_rect[1]["bottom"], self.lista_paredes_rect, self.jugador, 200)
        #self._slave.blit(score, (200, 10))

    def leer_inputs(self):
        '''
        Se encarga de leer las teclas apretadas
        '''
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_RIGHT]): #and self.jugador.rectangulo.x < self.ancho - self.jugador.velocidad - self.jugador.rectangulo.width:
            for plataforma_rect in self.plataformas_rect:
                if not self.jugador.lados_rectangulo["right"].colliderect(plataforma_rect["left"]):
                    self.jugador.que_hace = "derecha"
        elif(keys[pygame.K_LEFT]): #and self.jugador.rectangulo.x > 0:
            self.jugador.que_hace = "izquierda"
        elif(keys[pygame.K_UP]):
            self.jugador.que_hace = "salta"
        elif(keys[pygame.K_SPACE]):
            # match self.jugador.que_hace:
            #     case "derecha":
            #         self.jugador.direccion_dispara = "derecha"
            #     case "izquierda":
            #         self.jugador.direccion_dispara = "izquierda"
            self.jugador.disparar(self._slave)
        else:
            self.jugador.que_hace = "quieto"

    def dibujar_vidas_score(self):
        '''
        Se encarga de blitear el tiempo, las vidas y puntaje del jugador en pantalla
        '''
        texto_puntaje = self.fuente.render("SCORE: {0}".format(self.jugador.puntaje), True, "White")
        self._slave.blit(texto_puntaje, (200,10))

        texto_proyectiles = self.fuente.render("PROYECTILES: {0}X".format(self.jugador.proyectiles), True, "White")
        self._slave.blit(texto_proyectiles, (580,10))

        rectangulo = self.rect_corazon.copy()
        for vida in range(self.jugador.vidas):
            self._slave.blit(self.img_corazon, (rectangulo.x, rectangulo.y))
            rectangulo.x += self.img_corazon.get_width() + 10

        if not self.pausado:
            tiempo_actual = pygame.time.get_ticks() 
            self.tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
            self.tiempo_restante = self.tiempo_limite - self.tiempo_transcurrido 
        if self.tiempo_restante < 0:
            self.game_over = True
            #self.pausado = True
            self.jugador.perdiste = True
        texto_cronometro = self.fuente.render(f"TIEMPO 00:{self.tiempo_restante // 1000}", True, "White")
        self._slave.blit(texto_cronometro, (10, 10))

    def mostrar_mensaje(self, lista_eventos):
        '''
        Se encarga de mostrar un formulario si ganaste o perdiste
        '''
        if self.jugador.ganaste:
            print("EL JUGADOR GANO")
            form = FormGanador(self._slave, 250,100,1000, 600, "Black", "Black", 1, True)
            form.update(lista_eventos) ##1400 900
        elif self.jugador.perdiste or (self.tiempo_restante < 0):
            print("EL JUGADOR PERDIO")
            form = FormPerdedor(self._slave, 250,100,1000, 600, "Black", "Black", 1, True)
            form.update(lista_eventos)

    def mostrar_pausado(self):
        '''
        Se encarga de blitear en pantalla cuando se pausa el juego
        '''
        fuente = pygame.font.SysFont("Consolas", 100)
        resultado = fuente.render("PAUSA", True, "White")
        self._slave.blit(resultado, (200, 350))


    def verificar_victoria_game_over(self)-> bool :
        '''
        Se encarga de verificar si ganaste o perdiste. Si ganaste, guarda los datos en un JSON.
        Devuelve un bool
        '''
        if self.jugador.ganaste:
            self.pausado = True
            puntos_extra = self.tiempo_restante//10
            self.jugador.puntaje += puntos_extra
            self.nivel_puntaje = self.jugador.puntaje
            self.guardar_datos_nivel()
            print("Se guardaron datos partida ganada")
            return True
        elif self.jugador.perdiste or self.game_over or (self.tiempo_restante < 0):
            self.pausado = True
            print("perdio")
            return False

    def dibujar_rectangulos(self):
        
        if get_mode():
            for pared in self.lista_paredes_rect:
                for lado in pared:
                    pygame.draw.rect(self._slave, "Yellow", pared[lado], 5)
            for lado in self.jugador.lados_rectangulo:
                pygame.draw.rect(self._slave, "Green", self.jugador.lados_rectangulo[lado], 2)
            for plataforma in self.plataformas:
                for lado in plataforma.lados_rectangulo:
                    pygame.draw.rect(self._slave, "Red", plataforma.lados_rectangulo[lado], 2)
            #pygame.draw.rect(self._slave, "Blue", piso, 2)
            # for lado in self.jugador.lados_rectangulo: 
            #     pygame.draw.rect(self._slave, "Red", self.jugador.lados_rectangulo[lado] , 2)

            # for plataforma in self.plataformas:
            #     for lado in plataforma.lados_rectangulo:
            #         pygame.draw.rect(self._slave, "Green", plataforma.lados_rectangulo[lado], 2)

            # for item in self.items:
            #     for lado in item.lados_rectangulo:
            #         pygame.draw.rect(self._slave, "Yellow", item.lados_rectangulo[lado], 2)
            
            # for trap in self.traps:
            #     for lado in trap.lados_rectangulo:
            #         pygame.draw.rect(self._slave, "Orange", trap.lados_rectangulo[lado], 2)

    def guardar_datos_nivel(self):
        '''
        Se encarga de guardar los datos del nivel en un JSON y desbloquea el siguiente
        '''
        try:
            with open('Formularios/desbloqueo_niveles.json', 'r') as archivo:
                datos_niveles = json.load(archivo)
            
            for nivel in datos_niveles["niveles"]:
                if nivel["nivel"] == self.nivel_actual + 1:
                    nivel['desbloqueado'] = True
                    break
                nivel["puntaje"] = self.jugador.puntaje
            with open('Formularios/desbloqueo_niveles.json', 'w') as archivo:
                json.dump(datos_niveles, archivo)
        except FileNotFoundError:
            print("No se encontró el archivo 'desbloqueo_niveles.json'")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON")
