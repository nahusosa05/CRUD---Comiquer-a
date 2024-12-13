import sqlite3
from cfg import prompt_is_valid
from cfg import is_int
from cfg import is_valid_str
from cfg import get_wrong_msg
from conexion import insert_volumes
from colorama import init, Fore
from conexion import insert_autor,insert_manga
init(autoreset=True)

#validations prompts
intWrong = (Fore.RED + "Ingrese valores numericos".center(50))
strWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))

titleFormat = ("\t" + Fore.CYAN + "Titulo: " + Fore.RESET)  
autorFormat = ("\t" + Fore.CYAN + "Autor: " + Fore.RESET)  
volumeFormat = ("\t" + Fore.CYAN + "Volumen (0 para salir): " + Fore.RESET)
quantityFormat = ("\t" + Fore.CYAN + "Cantidad: " + Fore.RESET)
optionFormat = ("\t" + Fore.CYAN + "SI/NO/SALIR: " + Fore.RESET)

def get_title():
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.BLUE + "Titulo "+ Fore.RESET +  "del manga").center(50))
    print("." * 50)
    title = prompt_is_valid(titleFormat, strWrong, is_valid_str)
    title = title.title()
    return title

def get_autor():
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.BLUE + "Autor "+ Fore.RESET +  "del manga").center(50))
    print("." * 50)
    autor = prompt_is_valid(autorFormat, strWrong, is_valid_str)
    autor = autor.title()
    return autor

def get_volumes(conn):
    volumes_in_stock = {}  # Diccionario para almacenar volumen: cantidad
    volumes = -1
    
    cursor = conn.cursor()
    cursor.execute("SELECT Volume FROM Volumes")  
    info_in_bd = cursor.fetchall()  
    volumes_in_db = [info[0] for info in info_in_bd] 
    
    # Bucle principal
    while volumes != 0:
        volumes = int(prompt_is_valid(volumeFormat, intWrong, is_int))
        print("." * 50 + "\n")
        
        if volumes in volumes_in_stock:
            print("\n" + "-" * 50)
            print(Fore.RED + f"Volumen [{volumes}] ya guardado. Por favor ingrese otro".center(50))
            print("-" * 50)
            continue
        
        elif volumes in volumes_in_db:
            print("\n" + "-" * 50)
            print(Fore.RED + f"Volumen [{volumes}] ya guardado. Por favor ingrese otro".center(50))
            print("-" * 50)
            continue
        
        if volumes != 0:
            # Pedir cantidad
            print(("Ingrese la " + Fore.BLUE + "cantidad "+ Fore.RESET +  "que hay en stock.").center(50))
            print("." * 50)
            
            quantity = int(prompt_is_valid(quantityFormat, intWrong, is_int))
            if quantity != 0:
                print("-" * 50)
                volumes_in_stock[volumes] = quantity  # Guardar volumen y cantidad en el diccionario
            
                # Confirmación
                print("\n" + "-" * 50)
                print(Fore.GREEN + f"Volumen [{volumes}] guardado con éxito.".center(50))
                print("-" * 50 + "\n")
            else:
                prompt = get_wrong_msg(Fore.RED + "Cantidad no valida, ingrese valores mayores a 0".center(50) + Fore.RESET)
                print(prompt)
        else:
            print("\n" + Fore.CYAN + "=" * 50)
    
    print("\n" + "-" * 50)
    print(Fore.BLUE + "Los datos ingresados son:".center(50) + Fore.RESET)
    print("-" * 50)
    
    for volume, quantity in volumes_in_stock.items():
        print((Fore.RED + f"Volumen: {volume}" + f" | Cantidad: {quantity}" + Fore.RESET).center(50))
    print("-" * 50)
    
    print("\n" + Fore.CYAN + "=" * 50)
    print("\n" + "-" * 50)
    print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
    print("." * 50)
    
    user_input = prompt_is_valid(optionFormat, strWrong, is_valid_str)
    user_input = user_input.upper()
    print("-" * 50)
    
    if user_input == 'SI':
        return volumes_in_stock  
    
    elif user_input == 'NO':
        print(Fore.YELLOW + "\n" + "." * 50)
        print(Fore.YELLOW + "Reiniciando el proceso...".center(50) + Fore.RESET)
        print(Fore.YELLOW + "." * 50)
        return get_volumes()  
    elif user_input == 'SALIR':
        print("\n" + "-" * 50)
        print(Fore.RED + "Operación cancelada.".center(50) + Fore.RESET)
        print("-" * 50)
        return None
    else:
        x = get_wrong_msg(Fore.RED + "Seleccione una opcion correcta." + Fore.RESET)
        print(x)

def registrar_mangas(conn):
    while True:  
        print(f"\n{'-' * 50}")
        print(Fore.BLUE + "REGISTRAR MANGAS".center(50))
        print(f"{'-' * 50}" + "\n")
        
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
        user_input = prompt_is_valid(optionFormat, strWrong, is_valid_str)
        user_input = user_input.upper()
        print("-" * 50)

        print("\n" + Fore.CYAN + "=" * 50)
        
        if user_input == 'SI':
            manga_flag = insert_manga(conn, title, autor)
            autor_flag = insert_autor(conn, autor)
            
            if manga_flag and autor_flag:
                print("\n" + "-" * 50)
                print(("Ingrese los " + Fore.BLUE + "volúmenes "+ Fore.RESET +  "que hay en stock (0 para salir).").center(50))
                print("." * 50)
                volumes_in_stock = get_volumes(conn)
                if volumes_in_stock:
                    insert_volumes(conn,title,volumes_in_stock)
                else:
                    print("\n" + "-" * 50)
                    print(Fore.RED + "Error al insertar los volumenes.".center(50) + Fore.RESET)
                    print("-" * 50)
            else:
                print(Fore.YELLOW + "\n" + "." * 50)
                print(Fore.YELLOW + "Volviendo al menu..." + Fore.RESET)
                print(Fore.YELLOW + "." * 50)
            break  
        elif user_input == 'NO':
            print(Fore.YELLOW + "\n" + "." * 50)
            print(Fore.YELLOW + "Reiniciando el proceso..." + Fore.RESET)
            print(Fore.YELLOW + "." * 50)
        elif user_input == 'SALIR':
            print(Fore.YELLOW + "\n" + "." * 50)
            print(Fore.YELLOW + "Volviendo al menu...".center(50) + Fore.RESET)
            print(Fore.YELLOW + "." * 50 + "\n")
            break
        else:
            prompt = get_wrong_msg(Fore.RED + "Entrada no válida. Por favor ingresa: " + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET)
            print(prompt)

    print("\n" + Fore.CYAN + "=" * 50 )