import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

W,H = 1000, 600

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

personaje_quieto_muerte = [ 
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto_muerte/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_quieto_muerte/1.png")]

personaje_quieto_muerte_i = girar_imagenes(personaje_quieto_muerte, True, False)

personaje_salta_muerto = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta_muerto/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_salta_muerto/2.png"),
]

personaje_salta_muerto_i = girar_imagenes(personaje_salta_muerto, True, False)

personaje_camina_muerto = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/0.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina_muerto/1.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/2.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina_muerto/3.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina/4.png"),
    pygame.image.load("Formularios/niveles/main-character/punk/punk_camina_muerto/5.png"),
]
personaje_camina_muerto_i = girar_imagenes(personaje_camina_muerto, True, False)


personaje_dispara = [
    pygame.image.load("Formularios/niveles/main-character/punk/punk_armado/1.png")
]

personaje_dispara_i = girar_imagenes(personaje_dispara, True, False)


diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["quieto_i"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_i"] = personaje_salta_i
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["camina_d_muerte"] = personaje_camina_muerto
diccionario_animaciones["camina_i_muerte"] = personaje_camina_muerto_i
diccionario_animaciones["quieto_d_muerte"] = personaje_quieto_muerte
diccionario_animaciones["quieto_i_muerte"] = personaje_quieto_muerte_i
diccionario_animaciones["salta_d_muerte"] = personaje_salta_muerto
diccionario_animaciones["salta_i_muerte"] = personaje_salta_muerto_i
diccionario_animaciones["dispara"] = personaje_dispara
diccionario_animaciones["dispara_i"] = personaje_dispara_i

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

proyectil_surface = pygame.image.load("Formularios/recursos/items/bala.png")
proyectil_escalado = pygame.transform.scale(proyectil_surface, (25,14))
bala_item = [proyectil_escalado]


dolar_cargando = pygame.image.load("Formularios/recursos/items/money.png")
dolar_escalado = pygame.transform.scale(dolar_cargando, (24,20))
item_dolar = [dolar_escalado]

pinche_cargando = pygame.image.load("Formularios/recursos/items/pinche.png")
pinche_escalado = pygame.transform.scale(pinche_cargando, (90,28))
item_pinche = [pinche_escalado]

boss_final = [ pygame.image.load("Formularios/recursos/boss/nuevo_boss_izq.png")]
boss_final_dolor = [pygame.image.load("Formularios/recursos/boss/nuevo_boss_dolor.png")]
boss_final_muerte = [pygame.image.load("Formularios/recursos/boss/nuevo_boss_muerte.png")]

boss_final_der = girar_imagenes(boss_final, True, False)
boss_final_dolor_der = girar_imagenes(boss_final_dolor, True, False)
boss_final_muerte_der = girar_imagenes(boss_final_muerte, True, False)

flybot_d = [ pygame.image.load("Formularios/recursos/flybot/0.png"),
            pygame.image.load("Formularios/recursos/flybot/1.png"),
            pygame.image.load("Formularios/recursos/flybot/2.png"),
            pygame.image.load("Formularios/recursos/flybot/3.png"),
            pygame.image.load("Formularios/recursos/flybot/4.png")]
flybot_i = girar_imagenes(flybot_d, True, False)

robot_camina = [
                pygame.image.load("Formularios/recursos/robot/0.png"),
                pygame.image.load("Formularios/recursos/robot/1.png"),
                pygame.image.load("Formularios/recursos/robot/2.png"),
                pygame.image.load("Formularios/recursos/robot/3.png"),
                pygame.image.load("Formularios/recursos/robot/4.png"),
                pygame.image.load("Formularios/recursos/robot/5.png"),
                pygame.image.load("Formularios/recursos/robot/6.png"),
                pygame.image.load("Formularios/recursos/robot/7.png"),
                pygame.image.load("Formularios/recursos/robot/8.png")]

robot_camina_d = girar_imagenes(robot_camina, True, False)

minibot_techo = pygame.image.load("Formularios/recursos/mini_bot/0.png")

piso_s = pygame.Surface((W,100))
piso_s.fill("Black")
techo_s = pygame.Surface((W, 50))
techo_s.fill("Black")

pared = pygame.Surface((30, H))
pared.fill("Black")

vacio_surface = pygame.image.load("Formularios/recursos/vacio-png.png")
plataforma_surface = pygame.image.load("Formularios/recursos/plataforma.png")
miniplataforma_surface = pygame.image.load("Formularios/recursos/0.png")
