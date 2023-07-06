import pygame, sys
from pygame.locals import *
from configuraciones import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_enemigo import Enemigo
from modo import *
'''
#Class = parte estatica, con atributos y variables, lo que me permite describir a un objeto
#Se define primero un constructor

# class Objeto_Juego():
#     def __init__(self, imagen, rectangulos:dict, posicion_inicial) -> None:
#         self.imagen = imagen
#         self.rectangulos = rectangulos

#Metodos: lo que puede hacer un objeto, parte dinamica de la clase 
'''

#######################################################################
def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, lados_piso, texto, lista_plataformas, lista_lados_plataformas,mini_bot):
    pantalla.blit(fondo, (0,0))
    pantalla.blit(texto, (10, 10))
    pantalla.blit(mini_bot.imagenA, mini_bot.rect.topleft)
    un_personaje.update(pantalla, lados_piso, lista_lados_plataformas)

    for plataforma in lista_plataformas:
        for rect in plataforma.rects:
            pantalla.blit(plataforma.image, (rect.x, rect.y))   
#######################################################################

#PANTALLA
W, H = (1000,600) #1280 #686
FPS = 15
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Futurist Hero")

#FONDO
fondo = pygame.image.load("backgrounds\\nuevo-fondo.jpeg")
fondo = pygame.transform.scale(fondo, (W,H))
PANTALLA.blit(fondo, (0,0))

pygame.init()

#MUSICA

# ruta_musica = "hero-80s-127027.mp3"
# musica_fondo = pygame.mixer.music.load(ruta_musica)
# pygame.mixer.music.play(-1)

#CRONOMETRO
tiempo_inicial = pygame.time.get_ticks()
tiempo_limite = 600000  
tipo_fuente = "Consolas"
tamaño = 20
fuente = pygame.font.SysFont(tipo_fuente, tamaño)

#PERSONAJE
posicion_inicial = (H/2 - 180, 444)
tamaño = (25,50)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 5)

#ENEMIGO
mini_bot = Enemigo((40,36),"mini-bot\\0.png", "mini-bot\\3.png",(450,350), 5)

#PISO
piso = pygame.Rect(0,0,W,20)
piso.top = mi_personaje.lados["main"].bottom

lados_piso = obtener_rectangulos(piso)

#PLATAFORMAS
plataformas_1 = Plataforma("recursos\\plataforma.png", 180, 50, [(330, 400), (200, 300), (100, 200)])
plataformas_2 = Plataforma("recursos\\0.png", 50, 50, [(690, 400), (500, 200), (600, 350)])
plataformas_3 = Plataforma("recursos\\suelo.png", 210, 210, (750, 150))

lados_plataformas_1 = [obtener_rectangulos(coordinate) for coordinate in plataformas_1.rects]
lados_plataformas_2 = [obtener_rectangulos(coordinate) for coordinate in plataformas_2.rects]
lados_plataformas_3 = [obtener_rectangulos(coordinate) for coordinate in plataformas_3.rects]

lista_plataformas = [plataformas_1, plataformas_2, plataformas_3]

# lista_lados_plataformas = []
# for plataforma in lista_plataformas:
#     lados_plataforma = [obtener_rectangulos(coordinate) for coordinate in plataforma.rects]
#     lista_lados_plataformas.append(lados_plataforma)
lista_lados_plataformas = [plataformas_1.rects, plataformas_2.rects, plataformas_3.rects]
#lista_lados_plataformas = [lados_plataformas_1, lados_plataformas_2, lados_plataformas_3]

while True:

    RELOJ.tick(FPS)
    #cronometro
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    if tiempo_transcurrido >= tiempo_limite:
        pygame.quit()
        sys.exit(0)


    texto = fuente.render(f"Time: {tiempo_transcurrido // 1000}", True, "White")
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()        
    keys = pygame.key.get_pressed()
    
    if(keys[pygame.K_RIGHT]) and posicion_inicial[0] > mi_personaje.velocidad:
        mi_personaje.que_hace = "derecha"
    elif(keys[pygame.K_LEFT]) and posicion_inicial[0] < W - mi_personaje.ancho - 5:
        mi_personaje.que_hace = "izquierda"
    elif(keys[pygame.K_UP]):
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"


    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lados_piso, texto, lista_plataformas, lista_lados_plataformas, mini_bot)

    if get_mode():
        pygame.draw.rect(PANTALLA, "Blue", piso, 2)
        for lado in mi_personaje.lados: 
            pygame.draw.rect(PANTALLA, "Red", mi_personaje.lados[lado] , 2)

        for lados_plataforma in lista_lados_plataformas:
            for lados in lados_plataforma:
                for lado in lados.values():
                    pygame.draw.rect(PANTALLA, "Green", lado, 2)

    pygame.display.update()