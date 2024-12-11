# imports
from colorama import init, Fore, Back
import os
init(autoreset=True)

def clear():
    "Limpia la consola según el sistema operativo"
    os.system('cls' if os.name == 'nt' else 'clear')
    
def is_int(input):
    if input.isnumeric() and int(input)>= 0:
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
            print("\n" + "*" * 50)
            print(els)
            print("\n" + "*" * 50)
            
#formatos de mensajes     
def get_wrong_msg(message):
    return (
        "\n" + "*" * 50 +
        f"\n" + message +
        "\n" + "*" * 50
    )

def get_format_msg(message):
    return (
        "\n" + "-" * 50 +
        f"\n" + message +
        "\n" + "-" * 50
    )