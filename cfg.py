# imports
from modulos.registrar import registrar_mangas
from modulos.actualizar import actualizar_mangas
from modulos.eliminar import eliminar_mangas
from modulos.eliminar import eliminar_mangas
from modulos.buscar import buscar_mangas
from modulos.listado import listado_mangas
import os

def limpiar_pantalla():
    "Limpia la consola según el sistema operativo"
    os.system('cls' if os.name == 'nt' else 'clear')