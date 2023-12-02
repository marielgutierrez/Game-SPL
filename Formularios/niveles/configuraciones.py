import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


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
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario


#set de imagenes del personaje
personaje_quieto = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto/2.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto/3.png")    
]

personaje_camina = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/2.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/3.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/4.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/5.png"),
]

personaje_salta = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/2.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/3.png"),]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)
personaje_salta_i = girar_imagenes(personaje_salta, True, False)


diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["quieto_i"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_i"] = personaje_salta_i
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

item_s = [pygame.image.load("Formularios/recursos/llaves/0.png"),
                    pygame.image.load("Formularios/recursos/llaves/1.png"),
                    pygame.image.load("Formularios/recursos/llaves/2.png"),
                    pygame.image.load("Formularios/recursos/llaves/3.png"),
                    pygame.image.load("Formularios/recursos/llaves/4.png"),
                    pygame.image.load("Formularios/recursos/llaves/5.png"),
                    pygame.image.load("Formularios/recursos/llaves/6.png"),
                    pygame.image.load("Formularios/recursos/llaves/7.png"),
                    pygame.image.load("Formularios/recursos/llaves/8.png"),
                    pygame.image.load("Formularios/recursos/llaves/9.png"),
                    pygame.image.load("Formularios/recursos/llaves/10.png")]

portal_s = pygame.image.load("Formularios/recursos/miportal.png")

dolar_cargando = pygame.image.load("Formularios/recursos/items/money.png")
dolar_escalado = pygame.transform.scale(dolar_cargando, (24,20))
item_dolar = [dolar_escalado]

pinche_cargando = pygame.image.load("Formularios/recursos/items/pinche.png")
pinche_escalado = pygame.transform.scale(pinche_cargando, (90,28))
item_pinche = [pinche_escalado]

piso_surface = pygame.image.load("Formularios/recursos/vacio-png.png")
plataforma_surface = pygame.image.load("Formularios/recursos/plataforma.png")
miniplataforma_surface = pygame.image.load("Formularios/recursos/0.png")
