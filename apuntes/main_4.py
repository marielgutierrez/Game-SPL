import pygame
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

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, piso: pygame.Rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje, personaje_animacion)

        rectangulo_personaje.y += desplazamiento_y
        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad
        if rectangulo_personaje.colliderect(piso):
            esta_saltando = False
            desplazamiento_y = 0
            rectangulo_personaje.bottom = piso.top
        

def actualizar_pantalla(pantalla, que_hace, rectangulo_personaje, velocidad, piso):
    #para usar variables declaradas fuera de la funcion
    global contador_pasos , esta_saltando
    global desplazamiento_y

    match que_hace:
        case "Derecha":
            if not esta_saltando:
                animar_personaje(pantalla, rectangulo_personaje, personaje_camina)
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
                animar_personaje(pantalla, rectangulo_personaje, personaje_camina_izquierda)
            mover_personaje(rectangulo_personaje, velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "Quieto":
            animar_personaje(pantalla, rectangulo_personaje, personaje_quieto)
    
    aplicar_gravedad(pantalla, personaje_salta, rectangulo_personaje, piso)
#############################################

pygame.init()

W, H =(720,480)
#720,480
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
x_inicial = H/2 - 30
y_inicial = 350
contador_pasos = 0
velocidad = 5

posicion_actual_x = 0

lista_animaciones  = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta]

reescalar_imagenes(lista_animaciones, 25, 40)

rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

#SALTO
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#SUPERFICIE

piso = pygame.Rect(0,0,W,20)
piso.top = rectangulo_personaje.bottom

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
    elif(keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    elif(keys[pygame.K_UP]):
        que_hace = "Salta"
    else:
        que_hace = "Quieto"

    screen.blit(fondo,(0,0))
    actualizar_pantalla(screen, que_hace, rectangulo_personaje, velocidad, piso)
    
    if get_mode():
        pygame.draw.rect(screen, "Blue", rectangulo_personaje, 2)
        #pygame.draw.rect(screen, "Green", piso, 2)

    pygame.display.update()

pygame.quit()