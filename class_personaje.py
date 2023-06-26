from configuraciones import *

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
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
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0

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
        #por cada lado de la lista de lados
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, piso, plataformas):
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

        self.aplicar_gravedad(pantalla, piso, plataformas)

    def aplicar_gravedad(self, pantalla, piso, plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            #REPASAR EN EL VIDEO
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            #mientras que esa suma sea menor al limite velocidad caida
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top + 5
        else:
            self.esta_saltando = True
        
        for plataforma in plataformas:
            for rect in plataforma:
                if self.lados["bottom"].colliderect(rect["top"]):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.lados["main"].bottom = rect["main"].top + 5
                    break
            else:
                continue  # No se encontró colisión en esta plataforma, continuar con la siguiente
                break  # Se encontró colisión con una plataforma, salir del bucle exterior
        else:
            self.esta_saltando = True


#TODo SE EJECUTA EN UN BUCLE, ESTOS METODOS SE EJECUTARAN UNA Y OTRA VEZ MIENTRAS ESTE ANIMANDO AL PERSONAJE

#En cuanto a la gravedad:
#POTENCIA DEL SALTO
#POTENCIA DE LA CAIDA

#El rectangulo del personaje debe colisionar con el rectangulo del piso o de una plataforma
#para que a la hora de aplicar la gravedad caiga en el rectangulo de la superficie

#######EN COONFIGURACIONES