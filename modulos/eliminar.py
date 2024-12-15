from cfg import prompt_is_valid
from cfg import is_int
from cfg import is_valid_str
from cfg import get_format_msg
from cfg import get_wrong_msg
import sqlite3
from colorama import init, Fore, Back
from modulos.registrar import get_volumes
from conexion import fetch_mangas
init(autoreset=True)

strWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))
intWrong = (Fore.RED + "Ingrese valores numericos".center(50))

titleFormat = ("\t" + Fore.RED + "Título: " + Fore.RESET)
optionFormat = ("\t" + Fore.CYAN + "Opción: " + Fore.RESET)
option2Format = ("\t" + Fore.CYAN + "SI/NO/SALIR: " + Fore.RESET)
volumeFormat = (Fore.CYAN + "Volumen a eliminar (0 para salir): " + Fore.RESET)

def delete_manga(conn,user_title):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Mangas WHERE Title = ?", (user_title,))
    cursor.execute("DELETE FROM Volumes WHERE Title = ?", (user_title,))
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = ?",(user_title,))
    conn.commit()
    prompt = get_format_msg(Fore.GREEN + f"\tManga {Fore.YELLOW}{user_title}{Fore.GREEN} eliminado con exito.{Fore.RESET}".center(50))
    print(prompt)

def eliminar_mangas(conn):
    print(f"\n{'='*50}")
    print(Back.BLUE + "ELIMINACIÓN DE MANGAS".center(50))
    print(f"=" * 50)
      
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
    print(("Ingrese el " + Fore.RED + "Titulo "+ Fore.RESET +  "del manga a eliminar").center(50))
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
    print("¿Qué desea eliminar?" + " (" + Fore.YELLOW + "Volumenes" + Fore.RESET + 
          "/" + Fore.RED + "Todo" + Fore.RESET + ")")
    print(f"{'.' * 50}")
    
    while True:
        user_option = prompt_is_valid(optionFormat,strWrong,is_valid_str)  
        user_option = user_option.upper()
        print(f"{'.' * 50}")
        if user_option == 'TODO':
            print(f"{Fore.RED}Eliminando el manga " + f"{Fore.GREEN}{user_title}{Fore.RED} y todos sus volúmenes de la base de datos.")
            
            print("\n" + "-" * 50)
            print("¿Los datos son correctos? " + "(" + Fore.GREEN + "SI" + Fore.RESET + "/" + Fore.RED + "NO" + Fore.RESET + "/" + "SALIR" + ")")
            print("." * 50)
            user_input = prompt_is_valid(option2Format, strWrong, is_valid_str)
            user_input = user_input.upper()
            user_input = user_input.strip()
            print("-" * 50)
            if user_input == 'SI':
                delete_manga(conn,user_title)
                print("\n" + Fore.CYAN + "=" * 50 )
                break
            elif user_input == 'NO':
                print(Fore.YELLOW + "\n" + "." * 50)
                print("Reiniciando el proceso...".center(50))
                print(Fore.YELLOW + "." * 50 + Fore.RESET)
            else:
                print(Fore.YELLOW + "\n" + "." * 50)
                print(Fore.YELLOW + "Volviendo al menu...".center(50) + Fore.RESET)
                print(Fore.YELLOW + "." * 50 + "\n")
                break
            
        elif user_option == 'VOLUMENES':
            print("\n" + Fore.CYAN + "=" * 50 + "\n")
            print("=" * 50)
            print(("Ingrese el número del volumen a eliminar de " + Fore.RED + f"{user_title}" + Fore.RESET).center(50))

            cursor.execute("SELECT Volume FROM Volumes WHERE Title = ?", (user_title,))
            volumes = [row[0] for row in cursor.fetchall()]

            if not volumes:
                print(Fore.RED + "No hay volúmenes disponibles para este manga.".center(50) + Fore.RESET)
                break

            print("=" * 50)
            print(Fore.GREEN + "Volúmenes disponibles:".center(50) + Fore.RESET)
            print("=" * 50)
            for volume in volumes:
                print(Fore.YELLOW + f"- Volumen: {Fore.RED}{volume}".center(50) + Fore.RESET)
            print("=" * 50)
            while True:
                try:
                    user_volume = int(prompt_is_valid(volumeFormat, strWrong, is_valid_str))
                    print("=" * 50)
                    if user_volume == 0:
                        print(Fore.YELLOW + "\n" + "." * 50)
                        print(Fore.YELLOW + "Volviendo al menu...".center(50) + Fore.RESET)
                        print(Fore.YELLOW + "." * 50 + "\n")
                        break
                    
                    if user_volume in volumes:
                        cursor.execute("DELETE FROM Volumes WHERE Title = ? AND Volume = ?", (user_title, user_volume))
                        conn.commit()
                        y = get_format_msg(Fore.GREEN + f"Volumen [{Fore.RED}{user_volume}{Fore.GREEN}] de [{Fore.YELLOW}{user_title}{Fore.GREEN}] eliminado correctamente.{Fore.RESET}".center(50) + Fore.RESET)
                        print(y)
                        
                        cursor.execute("SELECT Volume FROM Volumes WHERE Title = ?", (user_title,))
                        volumes = [row[0] for row in cursor.fetchall()]
                        
                        if len(volumes) == 0:
                            print("." * 50)
                            print(f"Como no hay mas volumenes ¿Desea eliminar el manga {Fore.RED}{user_title}? ({Fore.GREEN} Si {Fore.RESET} / {Fore.RED} No {Fore.RESET} )")
                            print(f"{'.' * 50}")
                            
                            user_input = prompt_is_valid(option2Format, strWrong, is_valid_str)
                            user_input = user_input.upper()
                            user_input = user_input.strip()
                            
                            if user_input == 'SI':
                                delete_manga(conn,user_title)
                                break
                            elif user_input == 'NO':
                                break
                            else:
                                x = get_wrong_msg(f"Entrada invalida. Por favor ingrese:{Fore.GREEN} Si {Fore.RESET} / {Fore.RED} No {Fore.RESET}")  
                    else:
                        x = get_wrong_msg(Fore.RED + "El volumen ingresado no existe. Intente de nuevo.".center(50) + Fore.RESET)
                        print(x)
                except ValueError:
                    x = get_wrong_msg(Fore.RED + "Por favor, ingrese un número válido.".center(50) + Fore.RESET)
                    print(x)
            print("\n" + Fore.CYAN + "=" * 50)
            break
        else:
            x = get_wrong_msg(Fore.RED + "Opcion incorrecta, porfavor ingrese: (" + Fore.GREEN + "Todo" 
            + Fore.RESET + "/" + Fore.YELLOW + "Volumenes" + Fore.RESET + ")")
            print(x)
            print("\n" + Fore.CYAN + "=" * 50 )
