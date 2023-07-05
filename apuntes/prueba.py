import pygame, sys
from configuraciones import *
from class_personaje import *
from modo import *
####################FUNCIONES DE MOVIMIENTO#############

def obtener_rectangulos(principal: pygame.Rect):
    '''
    brief: Definir los rectangulos que voy a obtener a la izquierda, derecha, arriba y abajo
    esto tiene como fin definir los lados de un rectangulo (pasado por parametro)
    esto es necesario para que cuando colisionan dos rectangulos, por ej el personaje con la plataforma
    '''
    diccionario = {}
    #main - bottom - left - right
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2 , principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario

def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    for lado in rectangulo_personaje:
        rectangulo_personaje[lado].x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos

    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, pisos:list):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje["main"], personaje_animacion)

        for lado in rectangulo_personaje:
            rectangulo_personaje[lado].y += desplazamiento_y
        
        
        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad

    for plataforma in pisos:
        if rectangulo_personaje["bottom"].colliderect(plataforma["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            rectangulo_personaje["main"].bottom = plataforma["main"].top + 5
            break
        else:
            esta_saltando = True #esta cayendo
        

def actualizar_pantalla(pantalla, que_hace, lados_personaje, velocidad, lista_plataformas, lista_traps, texto):
    #usamos global para usar variables declaradas fuera de la funcion
    global esta_saltando, desplazamiento_y

    pantalla.blit(fondo,(0,0))
    pantalla.blit(plataforma,(rectangulo_plataforma.x, rectangulo_plataforma.y))
    pantalla.blit(otra_plataforma,(rectangulo_otra_plataforma.x, rectangulo_otra_plataforma.y))
    pantalla.blit(plataforma_final,(rectangulo_plataforma_final.x, rectangulo_plataforma_final.y))
    pantalla.blit(chains,(rectangulo_chains.x, rectangulo_chains.y))
    pantalla.blit(money,(rectangulo_money.x, rectangulo_money.y))
    pantalla.blit(texto, (10, 10))

    match que_hace:
        case "Derecha":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje["main"], personaje_camina)
            mover_personaje(lados_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje["main"], personaje_camina_izquierda)
            mover_personaje(lados_personaje, velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "Quieto":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje["main"], personaje_quieto)
    
    aplicar_gravedad(pantalla, personaje_salta, lados_personaje, lista_plataformas)
#############################################

pygame.init()

W, H = (1000,600)
FPS = 15
RELOJ = pygame.time.Clock()

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Futurist Hero")

#FONDO
fondo = pygame.image.load("backgrounds\\nuevo-fondo.jpeg")
fondo = pygame.transform.scale(fondo, (W,H))
screen.blit(fondo, (0,0))


#CRONOMETRO
tiempo_inicial = pygame.time.get_ticks()
tiempo_limite = 60000  
tipo_fuente = "Consolas"
tamaño = 20
fuente = pygame.font.SysFont(tipo_fuente, tamaño)

#PERSONAJE
#posicion donde empieza
x_inicial = H/2 - 180 #52
y_inicial = 444 #550
contador_pasos = 0
velocidad = 5

posicion_actual_x = 0

lista_animaciones  = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta]

reescalar_imagenes(lista_animaciones,25,50)

rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

#dict
lados_personaje = obtener_rectangulos(rectangulo_personaje) 

que_hace = "Quieto"
#SALTO
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#SUPERFICIE
#piso

piso = pygame.Rect(0,0,W,125)#20
piso.top = rectangulo_personaje.bottom

lados_piso = obtener_rectangulos(piso)

#Plataformas

plataforma = pygame.image.load("recursos\\plataforma.png")
plataforma = pygame.transform.scale(plataforma, (190, 60)) #250 #80
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma. x = 500 #500
rectangulo_plataforma. y = 450 #620

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

otra_plataforma = pygame.image.load("recursos\\0.png")
otra_plataforma = pygame.transform.scale(otra_plataforma, (50, 50))
rectangulo_otra_plataforma = otra_plataforma.get_rect()
rectangulo_otra_plataforma. x = 330 #500 200
rectangulo_otra_plataforma. y = 400 #620 300

lados_otra_plataforma = obtener_rectangulos(rectangulo_otra_plataforma)

plataforma_final = pygame.image.load("recursos\\suelo.png")
plataforma_final = pygame.transform.scale(plataforma_final, (250,250))
rectangulo_plataforma_final = plataforma_final.get_rect()
rectangulo_plataforma_final. x = 950 #500 200
rectangulo_plataforma_final. y = 150 #620 300

lados_plataforma_final = obtener_rectangulos(rectangulo_plataforma_final)


lista_plataformas = [lados_piso, lados_plataforma, lados_otra_plataforma, lados_plataforma_final]

#TRAPS

chains = pygame.image.load("recursos\\items\\chains.png")
chains = pygame.transform.scale(chains, (304, 38)) #250 #80
rectangulo_chains = chains.get_rect()
rectangulo_chains. x = 500 #500
rectangulo_chains. y = 540 #620

lados_chains = obtener_rectangulos(rectangulo_chains)

lista_traps = [lados_chains]

#CASH

money = pygame.image.load("recursos\\items\\money.png")
money = pygame.transform.scale(money, (24, 20)) #250 #80
rectangulo_money = money.get_rect()
rectangulo_money. x = 340 #500
rectangulo_money. y = 380 #620

lados_money = obtener_rectangulos(rectangulo_money)


flag = True
while flag:

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    if tiempo_transcurrido >= tiempo_limite:
        pygame.quit()
        sys.exit(0)

    texto = fuente.render(f"Time: {tiempo_transcurrido // 1000}", True, "Green")
    
    # screen.blit(texto, (10, 10))

    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()

    #si dentro de la lista de keys se encuentra la tecla RIGHT
    #si es verdadero se realiza la accion de que_hace    
    if(keys[pygame.K_RIGHT]) and rectangulo_personaje.x < W - velocidad - rectangulo_personaje.width:
        que_hace = "Derecha"
    elif(keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    elif(keys[pygame.K_UP]):
        que_hace = "Salta"
    else:
        que_hace = "Quieto"

    actualizar_pantalla(screen, que_hace, lados_personaje, velocidad, lista_plataformas, lista_traps, texto)
    
    if get_mode():
        for lado in lados_personaje: 
            pygame.draw.rect(screen, "Blue", lados_personaje[lado] , 2)

        for lado in lados_piso:
            pygame.draw.rect(screen, "Green", lados_piso[lado], 2)

        for lado in lados_plataforma:
            pygame.draw.rect(screen, "Green", lados_plataforma[lado], 2)

        for lado in lados_otra_plataforma:
            pygame.draw.rect(screen, "Green", lados_otra_plataforma[lado], 2)

        for lado in lados_plataforma_final:
            pygame.draw.rect(screen, "Green", lados_plataforma_final[lado], 2)

        for lado in lados_chains:
            pygame.draw.rect(screen, "Yellow", lados_chains[lado], 2)

        for lado in lados_money:
            pygame.draw.rect(screen, "Yellow", lados_money[lado], 2)

    pygame.display.update()

pygame.quit()


#SIN POO usamos diccionarios para guardar todos los rectangulos de una imagen ya sea
# una plataforma 