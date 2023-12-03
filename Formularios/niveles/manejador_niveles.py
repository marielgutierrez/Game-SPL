import pygame
import json
from pygame.locals import *
from niveles.nivel_uno import NivelUno
from niveles.nivel_dos import NivelDos


class Manejador_niveles:
    '''Instanciar los niveles al momento de usar la interfaz grafica'''
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno":  NivelUno, "nivel_dos": NivelDos}
        self.datos_niveles = self.leer_archivo()

    def get_nivel(self, nombre_nivel):
        if nombre_nivel == "nivel_uno":
            return self.niveles[nombre_nivel](self._slave)
        elif self.nivel_desbloqueado(nombre_nivel):
            return self.niveles[nombre_nivel](self._slave)
        if not self.nivel_desbloqueado(nombre_nivel):
            print("esta bloqueado")
            return False

        #return self.niveles[nombre_nivel](self._slave)
    
    def leer_archivo(self):
        try:
            with open('Formularios/desbloqueo_niveles.json', 'r') as archivo:
                datos_niveles = json.load(archivo)
            return datos_niveles
        except FileNotFoundError:
            print("ERROR! no se abrio el archivo json en desbloquear niveles")

    def nivel_desbloqueado(self, nombre_nivel):
        match nombre_nivel:
            case "nivel_uno":
                numero_nivel = 1
            case "nivel_dos":
                numero_nivel = 2
            case "nivel_tres":
                numero_nivel = 3
        for nivel in self.datos_niveles['niveles']:
            if nivel['nivel'] == numero_nivel and nivel['desbloqueado']:
                return True
        return False