import sqlite3
from cfg import prompt_is_valid
from cfg import is_int
from cfg import is_valid_str
from cfg import get_format_msg
from cfg import get_wrong_msg
from cfg import clear
from conexion import insert_volumes
from colorama import init, Fore, Back
from conexion import insert_autor,insert_manga
init(autoreset=True)

#validations prompts
titleFormat = ("\t" + Fore.CYAN + "Titulo: " + Fore.RESET)  
titleWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))

autorFormat = ("\t" + Fore.CYAN + "Autor: " + Fore.RESET)  
autorWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))

volumeFormat = ("\t" + Fore.CYAN + "Volumen: " + Fore.RESET)
volumeWrong = (Fore.RED + "Ingrese valores numericos".center(50))

quantityFormat = ("\t" + Fore.CYAN + "Cantidad: " + Fore.RESET)
quantityWrong = (Fore.RED + "Ingrese valores numericos".center(50))

def get_title():
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.BLUE + "Titulo "+ Fore.RESET +  "del manga").center(50))
    print("." * 50)
    title = prompt_is_valid(titleFormat, titleWrong, is_valid_str)
    title = title.title()
    return title

def get_autor():
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.BLUE + "Autor "+ Fore.RESET +  "del manga").center(50))
    print("." * 50)
    autor = prompt_is_valid(autorFormat, autorWrong, is_valid_str)
    autor = autor.title()
    return autor

def get_volumes():
    volumes_in_stock = {}  # Diccionario para almacenar volumen: cantidad
    volumes = -1
    
    # Introducción
    print("\n" + "-" * 50)
    print(("Ingrese los " + Fore.BLUE + "volúmenes "+ Fore.RESET +  "que hay en stock (0 para salir).").center(50))
    print("." * 50)
    
    # Bucle principal
    while volumes != 0:
        volumes = int(prompt_is_valid(volumeFormat, volumeWrong, is_int))
        print("." * 50 + "\n")
        
        if volumes in volumes_in_stock:
            print("\n" + "-" * 50)
            print(Fore.RED + f"Volumen [{volumes}] ya guardado. Por favor ingrese otro".center(50))
            print("-" * 50)
            continue
        
        if volumes != 0:
            # Pedir cantidad
            print(("Ingrese la " + Fore.BLUE + "cantidad "+ Fore.RESET +  "que hay en stock.").center(50))
            print("." * 50)
            
            quantity = int(prompt_is_valid(quantityFormat, quantityWrong, is_int))
            print("-" * 50)
            volumes_in_stock[volumes] = quantity  # Guardar volumen y cantidad en el diccionario
            
            # Confirmación
            print("\n" + "-" * 50)
            print(Fore.GREEN + f"Volumen [{volumes}] guardado con éxito.".center(50))
            print("-" * 50 + "\n")
        else:
            print("\n" + Fore.CYAN + "=" * 50)
    
    # Mostrar resumen de datos
    print("\n" + "-" * 50)
    print(Fore.BLUE + "Los datos ingresados son:".center(50) + Fore.RESET)
    print("-" * 50)
    
    for volume, quantity in volumes_in_stock.items():
        print((Fore.RED + f"Volumen: {volume}" + f" | Cantidad: {quantity}" + Fore.RESET).center(50))
    print("-" * 50)
    
    # Confirmar si los datos son correctos
    print("\n" + Fore.CYAN + "=" * 50)
    print("\n" + "-" * 50)
    print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
    print("." * 50)
    
    user_input = input("\t" + Fore.CYAN + "SI/NO/SALIR: " + Fore.RESET)
    user_input = user_input.upper()
    print("-" * 50)
    
    if user_input == 'SI':
        return volumes_in_stock  
    elif user_input == 'NO':
        print(Fore.YELLOW + "\n" + "." * 50)
        print(Fore.YELLOW + "Reiniciando el proceso...".center(50) + Fore.RESET)
        print(Fore.YELLOW + "." * 50)
        return get_volumes()  
    else:
        print("\n" + "-" * 50)
        print(Fore.RED + "Operación cancelada.".center(50) + Fore.RESET)
        print("-" * 50)
        return None


def registrar_mangas(conn):
    while True:  
        title = get_title()

        print("\n" + Fore.CYAN + "=" * 50)

        autor = get_autor()

        print("\n" + Fore.CYAN + "=" * 50)

        print("\n" + "-" * 50)
        print(f"Los datos ingresados son:".center(50))
        print((Fore.RED + "Manga: " + title).center(50))
        print((Fore.RED + "Autor: " + autor).center(50))
        print("-" * 50)

        print("\n" + Fore.CYAN + "=" * 50)

        print("\n" + "-" * 50)
        print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
        print("." * 50)
        user_input = input("\t" + Fore.CYAN + "SI/NO/SALIR: " + Fore.RESET)
        print("-" * 50)

        print("\n" + Fore.CYAN + "=" * 50)
        
        if is_valid_str(user_input):
            user_input = user_input.upper()
            if user_input == 'SI':
                insert_manga(conn, title, autor)
                insert_autor(conn, autor)
                
                volumes_in_stock = get_volumes()
                insert_volumes(conn,volumes_in_stock)
                break  
            elif user_input == 'NO':
                # Si el usuario ingresa 'NO', el proceso de registro se repite desde el principio
                print(Fore.YELLOW + "\n" + "." * 50)
                print(Fore.YELLOW + "Reiniciando el proceso..." + Fore.RESET)
                print(Fore.YELLOW + "." * 50)
            elif user_input == 'SALIR':
                print(Fore.BLUE + "\n" + "." * 50)
                print(Fore.BLUE + "Volviendo al menu...".center(50) + Fore.RESET)
                print(Fore.BLUE + "." * 50 + "\n")
                break
            else:
                prompt = get_wrong_msg(Fore.RED + "Entrada no válida. Por favor ingresa: " + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET)
                print(prompt)
        else:
            prompt = get_wrong_msg(Fore.RED + "Entrada no válida. Por favor ingresa: " + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET)
            print(prompt)

    print("\n" + Fore.CYAN + "=" * 50 + "\n")