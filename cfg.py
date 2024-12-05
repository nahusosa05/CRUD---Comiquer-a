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
    try:
        int(input)  # try convert to int
        return True
    except ValueError:
        print(f"\n" + "*" * 50)
        print("Debe ingresar un valor numérico válido. Por favor, inténtelo nuevamente.")
        print(f"*" * 50 + "\n")
        return False
    
def is_valid_str(input):
    min_length = 1
    
    if not isinstance(input, str):
        print("El valor ingresado no es una cadena.")
        return False
    
    # check allowed chars in str (only letters)
    if not input.isalpha():
        print(f"La cadena contiene caracteres no permitidos")
        return False
        
    if len(input) < min_length:
        print(f"La cadena debe tener al menos {min_length} caracter.")
        return False
    
    return True

def prompt_is_valid(prompt_message, validation_func):
    # Solicita una entrada al usuario hasta que sea válida.
    # prompt_message: Mensaje para mostrar al usuario.
    # validation_func: Función de validación que retorna True si el valor es válido.
    # return: La entrada válida.
    while True:
        user_input = input(prompt_message)
        if validation_func(user_input):
            return user_input
        else:
            print("Entrada no válida. Inténtelo de nuevo.")