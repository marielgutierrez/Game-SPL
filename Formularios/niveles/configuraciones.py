import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def reescalar_imagenes(lista_animaciones, tamaño):
        for i in range(len(lista_animaciones)):
            imagen = lista_animaciones[i]
            lista_animaciones[i] = pygame.transform.scale(imagen, tamaño)

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
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_quieto\\0.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_quieto\\1.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_quieto\\2.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_quieto\\3.png")    
]

personaje_camina = [
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\0.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\1.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\2.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\3.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\4.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_camina\\5.png"),
]

personaje_salta = [
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_salta\\0.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_salta\\1.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_salta\\2.png"),
    pygame.image.load("Formularios\\niveles\\main-character\\punk\\punk_salta\\3.png"),]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)



