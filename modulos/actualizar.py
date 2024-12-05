def actualizar_mangas(books_in_stock):
    if books_in_stock:
        print(f"\n{'-' * 50}")
        print("MODIFICACIÓN DE MANGAS".center(50))
        print(f"{'-' * 50}")

        for num, book in enumerate(books_in_stock, start=1):
            print(f"{'\t.' + str(num):<16}{book[0]}")
            print(f"{'-' * 50}\n")

            num_input = input("Ingrese el número de algún Manga/Comic de la lista para modificar: ")
            print(f"{'-' * 50}")

            if num_input.isdigit():
                num_input = int(num_input)
                if 0 < num_input <= len(books_in_stock):
                    option = input("¿Qué desea modificar? (Titulo, Autor, Tomos): ").capitalize()
                    print(f"{'-' * 50}")
                    book = books_in_stock[num_input - 1]
                    if option == "Titulo":
                        book[0] = input("Ingrese el nuevo nombre del Manga/Comic: ")
                        print(f"{'-' * 50}")
                        print("-MODIFICACIÓN EXITOSA-".center(50))
                        print(f"{'-' * 50}")
                    elif option == "Autor":
                        book[1] = input("Ingrese el nuevo nombre del Autor: ")
                        print(f"{'-' * 50}")
                        print("-MODIFICACIÓN EXITOSA-".center(50))
                        print(f"{'-' * 50}")
                    elif option == "Tomos":
                        while True:
                            action = input("¿Desea AGREGAR o ELIMINAR tomos en stock? (0 para salir): ").upper()
                            print(f"{'-' * 50}")
                            if action in ["AGREGAR", "ELIMINAR",0]:
                                print("Ingrese los números de tomos separados por comas (0 para salir): ")
                                volumes = input().replace(" ", "").split(",")
                                print(f"{'-' * 50}")
                                for volume in volumes:
                                    if action == "AGREGAR" and int(volume) > 0:
                                        if volume not in book[2]:
                                            book[2].append(volume)
                                            print(f"Tomo {volume} agregado con éxito.")
                                        else:
                                            print(f"Tomo {volume} ya estaba en stock. No se ha agregado.")
                                    elif action == "ELIMINAR" and int(volume) > 0:
                                        if volume in book[2]:
                                            book[2].remove(volume)
                                            print(f"Tomo {volume} eliminado con éxito.")
                                        else:
                                            print(f"Tomo {volume} no encontrado en stock. No se ha eliminado.")
                                    elif action == 0:
                                        break
                                if "0" in volumes:
                                    print(f"{'-' * 50}")
                                    print("-MODIFICACIÓN EXITOSA-".center(50))
                                    print(f"{'-' * 50}\n")
                                    break
                                print(f"{'-' * 50}\n")
                            else:
                                print(f"\n{'*' * 50}")
                                print("Ingrese una opción válida (AGREGAR/ELIMINAR).".center(50))
                                print(f"{'*' * 50}\n")
                    else:
                        print(f"\n{'*' * 50}")
                        print("Ingrese una opción válida (Titulo, Autor, Tomos).".center(50))
                        print(f"{'*' * 50}\n")
                else:
                    print(f"\n{'*' * 50}")
                    print("Debe ingresar un número de la lista.".center(50))
                    print(f"{'*' * 50}\n")
            else:
                print(f"\n{'*' * 50}")
                print("Ingrese un valor numérico válido.".center(50))
                print(f"{'*' * 50}\n")
    else:
        print(f"\n{'*' * 50}")
        print("NO HAY MANGAS PARA MODIFICAR - REGÍSTRELOS PRIMERO".center(50))
        print(f"{'*' * 50}\n")

    return books_in_stock
