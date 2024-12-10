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
    
def is_int(input):
    if input.isnumeric():
        return True
    
    return False 

def is_valid_str(input):
    min_length = 1
    
    if isinstance(input, str):
        return True
    
    # check allowed chars in str (only letters)
    if input.isalpha():
        return True
        
    if len(input) >= min_length:
        return True
    
    return False

def prompt_is_valid(prompt, els, validation):
    # Solicita una entrada al usuario hasta que sea válida.
    # prompt_message: Mensaje para mostrar al usuario.
    # validation_func: Función de validación que retorna True si el valor es válido.
    # return: La entrada válida.
    while True:
        user_input = input(prompt)
        if validation(user_input):
            return user_input
        else:
            print(els)
            
def get_wrong_msg(message):
    #Genera un mensaje de validación con un formato claro.#
    return (
        "\n" + "*" * 50 +
        f"\n{message}" +
        "\n" + "*" * 50
    )