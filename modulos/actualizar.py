from cfg import prompt_is_valid
from cfg import is_int
from cfg import is_valid_str
from cfg import get_format_msg
from cfg import get_wrong_msg
import sqlite3
from colorama import init, Fore, Back
from modulos.registrar import get_volumes
from conexion import insert_volumes 
from conexion import fetch_mangas
init(autoreset=True)

strWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))
intWrong = (Fore.RED + "Ingrese valores numericos".center(50))

titleFormat = ("\t" + Fore.RED + "Título: " + Fore.RESET)
authorFormat = ("\t" + Fore.CYAN + "Nuevo autor: " + Fore.RESET)
optionFormat = ("\t" + Fore.CYAN + "Opción: " + Fore.RESET)
option2Format = ("\t" + Fore.CYAN + "SI/NO/SALIR: " + Fore.RESET)
oldVolumeFormat = ("\t" + Fore.CYAN + "Volumen actual: " + Fore.RESET)
newVolumeFormat = ("\t" + Fore.CYAN + "Volumen nuevo: " + Fore.RESET)
volumeFormat = ("\t" + Fore.CYAN + "Volumen a modificar: " + Fore.RESET)
quantityFormat = ("\t" + Fore.CYAN + "Cantidad: " + Fore.RESET)

def title_change(conn,user_title):
    print("\n" + "-" * 50)
    print(("Ingrese el nuevo " + Fore.GREEN + "Título" + Fore.RESET + ":").center(50))
    print("." * 50)
    new_title = prompt_is_valid(titleFormat, strWrong, is_valid_str)
    new_title = new_title.title() 
    print("-" * 50)
    
    print("\n" + "-" * 50)      
    print(f"Actualizando título '{user_title}' a '{new_title}'".center(50))
    print("-" * 50)   
    
    print("\n" + "-" * 50)
    print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
    print("." * 50)
    while True:
        user_input = prompt_is_valid(option2Format, strWrong, is_valid_str)
        user_input = user_input.upper()
    
        if user_input == 'SI':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM Mangas WHERE Title = ?", (new_title,))
                if cursor.fetchone():
                    prompt = get_wrong_msg(Fore.RED + "Error: El nuevo título ya existe en la base de datos. Por favor, elija otro." + Fore.RESET)
                    print(prompt)
                    return actualizar_mangas(conn)
                else:
                    cursor.execute("UPDATE Mangas SET Title = ? WHERE Title = ?", (new_title, user_title))
                    conn.commit()
                    prompt = get_format_msg(Fore.GREEN + "Título actualizado correctamente.".center(50) + Fore.RESET)
                    print(prompt)
            except sqlite3.Error as e:
                print(Fore.RED + f"Error al actualizar el título: {e}" + Fore.RESET)
                
        elif user_input == 'NO':
            print(Fore.YELLOW + "\n" + "." * 50)
            print(Fore.YELLOW + "Reiniciando el proceso..." + Fore.RESET)
            print(Fore.YELLOW + "." * 50)
        elif user_input == 'SALIR':
            print(Fore.YELLOW + "\n" + "." * 50)
            print(Fore.YELLOW + "Volviendo al menu...".center(50) + Fore.RESET)
            print(Fore.YELLOW + "." * 50 + "\n")
            break
            
           
def author_change(conn, user_title):
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.BLUE + "nuevo autor" + Fore.RESET + " del manga a modificar").center(50))
    print("." * 50)

    # Validar el nuevo autor
    new_author = prompt_is_valid(authorFormat, strWrong, is_valid_str)
    new_author = new_author.title()
    print("-" * 50)

    cursor = conn.cursor()

    cursor.execute("SELECT Autor FROM Mangas WHERE Title = ?", (user_title,))
    result = cursor.fetchone()

    old_author = result[0]  

    print("\n" + "-" * 50)
    print(("  Actualización de " + Fore.BLUE + "autor " + Fore.RESET + "de " + Fore.YELLOW +  f"{user_title}").center(50))
    print("."*50)
    print((Fore.RED + "Autor viejo: " + old_author).center(50))
    print((Fore.RED + "Autor nuevo: " + new_author).center(50))
    print("-" * 50)

    print("\n" + "-" * 50)
    print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
    print("." * 50)

    while True:
        user_input = prompt_is_valid(option2Format, strWrong, is_valid_str)
        user_input = user_input.upper()

        if user_input == "SI":
            try:
                cursor.execute("UPDATE Mangas SET Autor = ? WHERE Title = ?", (new_author, user_title))
                cursor.execute("UPDATE Authors SET AutorName = ? WHERE AutorName = ?", (new_author, old_author))
                conn.commit()
                
                msg = get_format_msg(Fore.GREEN + f"Autor actualizado correctamente a '{new_author}' para el manga '{user_title}'.".center(50) + Fore.RESET)
                print(msg)
                break
            
            except sqlite3.Error as e:
                print(Fore.RED + f"Error al actualizar el autor: {e}" + Fore.RESET)
                break

        elif user_input == "NO":
            print(Fore.YELLOW + "\n" + "." * 50)
            print("Reiniciando el proceso...".center(50))
            print(Fore.YELLOW + "." * 50 + Fore.RESET)
            return author_change(conn, user_title)

        elif user_input == "SALIR":
            print(Fore.YELLOW + "\n" + "." * 50)
            print("Volviendo al menú...".center(50))
            print(Fore.YELLOW + "." * 50 + "\n" + Fore.RESET)
            break

        else:
            prompt = get_wrong_msg(Fore.RED + "Entrada no válida. Por favor ingresa: " + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET)
            print(prompt)     

def volumes_change(conn, user_title):
    print(f"\n{'-' * 50}")
    print(("\t" + Back.RED + "Lista de volumenes en stock de " + Fore.YELLOW + f"{user_title}").center(50))
    print(f"{'.' * 50}")
    print((Fore.RED + "\t Volumen" + Fore.RESET + " | " + Fore.GREEN + "Cantidad").center(50))
    print(f"{'.' * 50}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT Volume,Quantity FROM Volumes WHERE Title = ?", (user_title,))  
    volumes_info = cursor.fetchall()  
    volumes = [volume[0] for volume in volumes_info] 
    quantitys = [quantity[1] for quantity in volumes_info] 
    
    for volume,quantity in zip(volumes,quantitys):
        print((f"\t{" Volumen:"} {Fore.RED}{volume}{Fore.RESET} | Cantidad: {Fore.GREEN}{quantity}{Fore.RESET}").center(50))

    print("-" * 50)
    
    print("\n" + "-" * 50)
    print(("\t¿Que desea hacer? (" + Fore.BLUE + "Agregar" + Fore.RESET + "/" + Fore.RED + "Modificar" + Fore.RESET + ")").center(50))
    print("-" * 50)
    
    while True:
        user_option = prompt_is_valid(optionFormat,strWrong,is_valid_str)  
        user_option = user_option.upper()
        if user_option == 'AGREGAR':
            print("\n" + "-" * 50)
            print(("Ingrese los " + Fore.BLUE + "volúmenes "+ Fore.RESET +  "que hay en stock (0 para salir).").center(50))
            print("." * 50)
            volumes_in_stock = get_volumes(conn)
            if volumes_in_stock:
                insert_volumes(conn,user_title,volumes_in_stock)
                prompt = get_format_msg(Fore.GREEN + "Modificacion hecha con exito.".center(50) + Fore.RESET)
                print(prompt)
            else:
                prompt = get_wrong_msg(Fore.RED + "Error al insertar los volumenes 1.".center(50) + Fore.RESET)
                print(prompt)
            break   
        elif user_option == 'MODIFICAR':
            print("\n" + "-" * 50)
            print(("\t¿Que desea modificar? (" + Fore.BLUE + "Volumen" + Fore.RESET + "/" + Fore.RED + "Cantidad" + Fore.RESET + ")").center(50))
            print("-" * 50)
            
            while True:
                user_option = prompt_is_valid(optionFormat,strWrong,is_valid_str)  
                user_option = user_option.upper()
                if user_option == 'VOLUMEN':
                    # Modificar un volumen existente
                    print("\n" + "-" * 50)
                    print("Ingrese el " + Fore.BLUE +  "volumen " + Fore.RESET + "que desea modificar: " + Fore.RESET)
                    print("." * 50)
                    old_volume = int(prompt_is_valid(oldVolumeFormat, intWrong, is_int))
                    print("." * 50)
                    print("Ingrese el " + Fore.BLUE + "nuevo número " + Fore.RESET + "de volumen: " + Fore.RESET)
                    print("." * 50)
                    new_volume = int(prompt_is_valid(newVolumeFormat, intWrong, is_int))
                    print("." * 50)
                    
                    if new_volume > 0:
                        cursor = conn.cursor()
                        cursor.execute("SELECT Volume FROM Volumes WHERE Title = ?", (user_title,)) 
                        info_in_bd = cursor.fetchall()  
                        volumes_in_db = [info[0] for info in info_in_bd]
                        if new_volume in volumes_in_db:
                            print("\n" + "-" * 50)
                            print(Fore.RED + f"Volumen [{volumes}] ya guardado. Por favor ingrese otro".center(50))
                            print("-" * 50)
                            continue
                        else:
                            try:
                                cursor.execute("UPDATE Volumes SET Volume = ? WHERE Title = ? AND Volume = ?", 
                                        (new_volume, user_title, old_volume))
                                conn.commit()
                                prompt = get_format_msg(Fore.GREEN + "El volumen fue actualizado correctamente.".center(50) + Fore.RESET)
                                print(prompt)
                            except sqlite3.Error as e:
                                prompt = get_wrong_msg(Fore.RED + f"Error al modificar el volumen: {e}".center(50) + Fore.RESET)
                                print(prompt)
                    else:
                        x = get_wrong_msg(Fore.RED + "Volumen 0 ingresado. Por favor reintente el ingreso".center(50) + Fore.RESET)
                        print(x)
                        
                        print("\n" + "-" * 50)
                        print(("\t¿Que desea hacer? (" + Fore.BLUE + "Reintentar" + Fore.RESET + "/" + Fore.RED + "Salir" + Fore.RESET + ")").center(50))
                        print("-" * 50)
    
                        while True:
                            user_option = prompt_is_valid(optionFormat,strWrong,is_valid_str)  
                            user_option = user_option.upper()
                            if user_option == 'REINTENTAR':
                                print(Fore.YELLOW + "\n" + "." * 50)
                                print("Reiniciando el proceso...".center(50))
                                print(Fore.YELLOW + "." * 50 + Fore.RESET)
                                
                                volumes_change(conn,user_title)
                                break
                            elif user_option == 'SALIR':
                                print(Fore.YELLOW + "\n" + "." * 50)
                                print(Fore.YELLOW + "Volviendo al menu...".center(50) + Fore.RESET)
                                print(Fore.YELLOW + "." * 50 + "\n")
                                break
                            else:
                                x = get_wrong_msg(Fore.RED + "Opcion incorrecta, porfavor ingrese:" + Fore.RESET + " (" + Fore.GREEN + "Reintentar" 
                                    + Fore.RESET + "/" + Fore.YELLOW + "Salir" + Fore.RESET + ")")
                                print(prompt)
                    break
                elif user_option == 'CANTIDAD':
                    # Modificar la cantidad de un volumen existente
                    print("\n" + "-" * 50)
                    print("Ingrese el " + Fore.BLUE + "volumen " + Fore.RESET + "para modificar la cantidad: " + Fore.RESET)
                    print("." * 50)
                    volume_to_modify = prompt_is_valid(volumeFormat, intWrong, is_int)
                    print("." * 50)
                    print("Ingrese la " + Fore.BLUE + "nueva cantidad" + Fore.RESET + ": ")
                    print("." * 50)
                    new_quantity = prompt_is_valid(quantityFormat, intWrong, is_int)
                    print("." * 50)
                    
                    try:
                        cursor.execute("UPDATE Volumes SET Quantity = ? WHERE Title = ? AND Volume = ?", 
                                      (new_quantity, user_title, volume_to_modify))
                        conn.commit()
                        prompt = get_format_msg(Fore.GREEN + "La cantidad fue actualizada correctamente." + Fore.RESET)
                        print(prompt)
                    except sqlite3.Error as e:
                        prompt = get_wrong_msg(Fore.RED + f"Error al modificar la cantidad: {e}" + Fore.RESET)
                        print(prompt)
                    break        
                else:
                    x = get_wrong_msg(Fore.RED + "Opcion incorrecta, porfavor ingrese:" + Fore.RESET + " (" + Fore.GREEN + "Volumen" 
                    + Fore.RESET + "/" + Fore.YELLOW + "Cantidad" + Fore.RESET + ")")
                    print(x)
            break
        else:
            x = get_wrong_msg(Fore.RED + "Opcion incorrecta, porfavor ingrese:" + Fore.RESET + " (" + Fore.GREEN + "Agregar" 
            + Fore.RESET + "/" + Fore.YELLOW + "Modificar" + Fore.RESET + ")")
            print(x)
    
def actualizar_mangas(conn):
    print(f"\n{'-' * 50}")
    print(Back.BLUE + "MODIFICACIÓN DE MANGAS".center(50))
    print(f"{'-' * 50}")

    titles = fetch_mangas(conn)  # Lista de títulos

    print(f"\n{'.' * 50}")
    print(Back.RED + "Lista de mangas en stock".center(50))
    print(f"{'.' * 50}")
    print((Fore.RED + "\t Título" + Fore.RESET + " | " + Fore.GREEN + "Autor").center(50))
    print(f"{'.' * 50}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT Title,Autor FROM Mangas")  
    info_in_bd = cursor.fetchall()  
    titles = [info[0] for info in info_in_bd] 
    authors = [info[1] for info in info_in_bd] 
    
    for i,(title,author) in enumerate(zip(titles,authors),start=1):
        print((f"\t{str(i)}. {Fore.RED}{title}{Fore.RESET} | {Fore.GREEN}{author}{Fore.RESET}").center(50))

    print("-" * 50)
    
    print("\n" + Fore.CYAN + "=" * 50 )
    
    print("\n" + "-" * 50)
    print(("Ingrese el " + Fore.RED + "Titulo "+ Fore.RESET +  "del manga a modificar").center(50))
    print("." * 50)
    
    while True:
        user_title = prompt_is_valid(titleFormat,strWrong,is_valid_str)   
        user_title = user_title.title()  
        if user_title in titles:  
            break
        else:
            x = get_wrong_msg(Fore.RED + "El título ingresado no se encuentra en la lista." + Fore.RESET)
            print(x)
    
    print("." * 50)
    print("¿Qué desea modificar?" + " (" + Fore.GREEN + "Titulo" + Fore.RESET + 
          "/" + Fore.RED + "Autor" + Fore.RESET + 
          "/" + Fore.YELLOW + "Volumenes" + Fore.RESET + ")")
    print(f"{'.' * 50}")
    
    while True:
        user_option = prompt_is_valid(optionFormat,strWrong,is_valid_str)  
        user_option = user_option.upper()
        if user_option == 'TITULO':
            title_change(conn,user_title)
            print("\n" + Fore.CYAN + "=" * 50 )
            break   
        elif user_option == 'AUTOR':
            author_change(conn,user_title)
            print("\n" + Fore.CYAN + "=" * 50 )
            break
        elif user_option == 'VOLUMENES':
            volumes_change(conn,user_title)
            print("\n" + Fore.CYAN + "=" * 50 )
            break
        else:
            x = get_wrong_msg(Fore.RED + "Opcion incorrecta, porfavor ingrese: (" + Fore.GREEN + "Titulo" 
            + Fore.RESET + "/" + Fore.RED + "Autor" + Fore.RESET + "/" 
            + Fore.YELLOW + "Volumenes" + Fore.RESET + ")")
            print(x)
            print("\n" + Fore.CYAN + "=" * 50 )
    
