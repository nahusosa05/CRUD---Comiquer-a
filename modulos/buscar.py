from colorama import init, Fore, Back
from cfg import get_format_msg, get_wrong_msg
from cfg import is_valid_str, is_int, prompt_is_valid
init(autoreset=True)

strWrong = (Fore.RED + "Entrada inválida. Asegúrate de ingresar solo letras. ".center(50))
intWrong = (Fore.RED + "Ingrese valores numericos".center(50))

numImputPrompt = f"{Fore.BLUE}Ingrese el número de algún Manga/Comic de la lista{Fore.RESET}: "
optionFormat = ("\t" + Fore.CYAN + "Opción: " + Fore.RESET)

def buscar_mangas(conn):
    print(f"\n{'=' * 50}")
    print(Back.BLUE + "BÚSQUEDA DE MANGAS".center(50))
    print(f"{'=' * 50}")
  
    cursor = conn.cursor()
    cursor.execute("SELECT Title, Autor FROM Mangas")  
    info_in_bd = cursor.fetchall()  
    titles = [info[0] for info in info_in_bd] 
    authors = [info[1] for info in info_in_bd] 

    # Mostrar la lista de mangas
    for i, (title, author) in enumerate(zip(titles, authors), start=1):
        print(f"\t{i}. {Fore.RED}{title}{Fore.RESET} | {Fore.GREEN}{author}{Fore.RESET}".center(50))
        
    print("=" * 50)
    # Ingreso de manga seleccionado
    num_input = prompt_is_valid(numImputPrompt, intWrong, is_int)
    num_input = int(num_input)

    print("=" * 50)
    print(f" Manga seleccionado: {Fore.RED}{titles[num_input - 1]}{Fore.RESET}".center(50))
    print(f"{'.' * 50}")
    print("¿Qué necesita de este manga? (" + Fore.YELLOW + "Titulo" + Fore.RESET + 
          "/" + Fore.RED + "Autor" + Fore.RESET + "/" + Fore.BLUE + "Volumenes" + Fore.RESET + ")")
    print(f"{'.' * 50}")

    # Preguntar qué detalle desea ver
    option = prompt_is_valid(optionFormat, strWrong, is_valid_str)
    option = option.upper()

    while True:

        if option == "TITULO":
            x = get_format_msg(f"{Fore.YELLOW}Título: {titles[num_input - 1]}{Fore.RESET}")
            print(x)
            break
        elif option == "AUTOR":
            x = get_format_msg(f"{Fore.RED}Autor: {authors[num_input - 1]}{Fore.RESET}")
            print(x)
            break
        elif option == "VOLUMENES":
            print("." * 50)
            print(f"{Fore.RED} Manga seleccionado: {Fore.YELLOW}{titles[num_input - 1]}{Fore.RESET}".center(50))
            print(f"{'.' * 50}")

            print(f"¿Desea ver todo los volumenes del autor o solamente de {titles[num_input - 1]}? (" + Fore.GREEN + "Todos" + Fore.RESET + 
            "/" + Fore.RED + f"{titles[num_input - 1]}" + Fore.RESET + ")")
            print(f"{'.' * 50}")
            
            option2Format = ("\t" + Fore.CYAN + f"{Fore.GREEN}Todos{Fore.RESET}/{Fore.RED}{titles[num_input - 1]}: " + Fore.RESET)
            user_input = prompt_is_valid(option2Format,strWrong,is_valid_str)
            user_input = user_input.upper()
            user_input = user_input.strip()
            istitle = titles[num_input - 1]
            istitle = istitle.upper()
            if user_input == str(istitle):
                # Obtener los volúmenes asociados con el manga seleccionado
                cursor.execute("SELECT Title, Volume, Quantity FROM Volumes WHERE Title = ?", (titles[num_input - 1],))
                volumes = cursor.fetchall()

                if volumes:
                    print(f"{'.' * 50}")
                    print(f"\n{Fore.BLUE}Volúmenes disponibles de{Fore.RED}{titles[num_input - 1]}:{Fore.RESET}")
                    print(f"{'.' * 50}")
                    for volume in volumes:
                        print(f"\t{Fore.YELLOW}{volume[0]} {Fore.RED}| Volumen {volume[1]}{Fore.RESET} | {Fore.GREEN}Cantidad: {volume[2]}{Fore.RESET}".center(50))
                    print(f"{'.' * 50}")
                    break
                else:
                    print(f"\n{Fore.YELLOW}No hay volúmenes registrados para este manga.{Fore.RESET}")
                    break
                    
            elif user_input == 'TODOS':
                author = authors[num_input - 1]
                cursor.execute("SELECT Title, Volume, Quantity FROM Volumes WHERE Title IN (SELECT Title FROM Mangas WHERE Autor = ?)", (author,))
                volumes = cursor.fetchall()

                if volumes:
                    print(f"{'.' * 50}")
                    print((f"Volúmenes de todos los mangas del autor {Fore.BLUE}{author}:{Fore.RESET}").center(50))
                    print(f"{'.' * 50}")
                    for volume in volumes:
                        print(f"\t{Fore.YELLOW}{volume[0]} {Fore.RED}| Volumen {volume[1]}{Fore.RESET} | {Fore.GREEN}Cantidad: {volume[2]}{Fore.RESET}".center(50))
                        
                    print(f"{'.' * 50}")
                    break
                else:
                    print(f"\n{Fore.YELLOW}No se encontraron volúmenes para este autor.{Fore.RESET}")
                    break    
            else:
                x = get_wrong_msg("{Fore.RED}Por favor ingrese:{Fore.GREEN}Todos{Fore.RESET}/{Fore.RED}{titles[num_input - 1]}")
                print(x)
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, elija entre 'Título', 'Autor' o 'Volúmenes'.{Fore.RESET}")
