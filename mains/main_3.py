import pygame
#sys
from configuraciones import *
from modo import *

####################FUNCIONES DE MOVIMIENTO#############
def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos

    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1


def actualizar_pantalla(pantalla, que_hace, rectangulo_personaje, velocidad):
    #para usar variables declaradas fuera de la funcion
    global contador_pasos

    match que_hace:
        case "Derecha":
            animar_personaje(pantalla, rectangulo_personaje, personaje_camina)
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            animar_personaje(pantalla, rectangulo_personaje, personaje_camina_izquierda)
            mover_personaje()
        case "Quieto":
            animar_personaje(pantalla, rectangulo_personaje, personaje_quieto)
    
#############################################

pygame.init()

W, H = (720,480)
FPS = 18
RELOJ = pygame.time.Clock()

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Future")

#FONDO
fondo = pygame.image.load("background-future.jpg")
fondo_final = pygame.transform.scale(fondo, (W,H))
screen.blit(fondo_final, (0,0))

#PERSONAJE
#posicion donde empieza
x_inicial = H/2 - 400
y_inicial = 750
contador_pasos = 0
velocidad = 10

rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

posicion_actual_x = 0

lista_animaciones  = [personaje_quieto, personaje_camina, personaje_salta]

reescalar_imagenes(lista_animaciones, 75, 85)

que_hace = "Quieto"


flag = True

while flag:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()


    keys = pygame.key.get_pressed()

    if(keys[pygame.K_RIGHT]):
        que_hace = "Derecha"
    elif (keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    else:
        que_hace = "Quieto"

    screen.blit(fondo,(0,0))
    actualizar_pantalla(screen, que_hace, rectangulo_personaje, velocidad)
    
    if get_mode():
        pygame.draw.rect(screen, "Blue", rectangulo_personaje, 2)

    pygame.display.update()

pygame.quit()