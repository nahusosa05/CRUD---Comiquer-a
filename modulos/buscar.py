def buscar_mangas(books_in_stock):
    if not len(books_in_stock) == 0:
        print(f"\n{'-' * 50}")
        print("BÚSQUEDA DE MANGAS".center(50))
        print(f"{'-' * 50}")
        
        for books in books_in_stock:
            num = books_in_stock.index(books)
            print(f"{'\t.' + str(num + 1):<16}{books[0]}")
        
        print(f"{'-' * 50}\n")

        num_input = input("Ingrese el número de algún Manga/Comic de la lista: ")
        if num_input.isdigit():
            num_input = int(num_input)
            if num_input <= len(books_in_stock) and num_input > 0:
                bookpromp = books_in_stock[num_input-1]
                print(f"{'-' * 50}")
                print(f"{' Manga seleccionado:  ':<20}{bookpromp[0]}".center(50))
                print(f"{'-' * 50}")
                option = input("¿Que necesita de este manga? Titulo/Autor/Tomos/ID : ").capitalize()
                option = option.lower()
                if option == "titulo":
                    print(f"\n{'-' * 50}")
                    print(f"{' Titulo:':<20}{bookpromp[0]}".center(50))    
                    print(f"{'-' * 50}\n")
                elif option == "autor":
                    print(f"\n{'-' * 50}")
                    print(f"{' Autor:':<20}{bookpromp[1]}".center(50))    
                    print(f"{'-' * 50}\n")   
                elif option == "tomos":
                    print(f"\n{'-' * 50}")
                    print(f"{' Tomos en stock:':<20}{bookpromp[2]}".center(50))   
                    print(f"{'-' * 50}\n")
                elif option == "id": 
                    print(f"\n{'-' * 50}")
                    print(f"{' ID:':<20}{books_in_stock.index(books)}".center(50))   
                    print(f"{'-' * 50}\n")
            else:
                print(f"\n{'*' * 50}")
                print("Manga/Comic no encontrado, por favor intente de nuevo".center(50))
                print(f"{'*' * 50}\n")
        else:
            print(f"\n{'*' * 50}")
            print("Debe ingresar un valor numérico de los mostrados en la lista.".center(50))
            print(f"{'*' * 50}\n")
    else:
        print(f"\n{'*' * 50}")
        print("NO HAY MANGAS EN STOCK - REGÍSTRELOS PRIMERO".center(50))
        print(f"{'*' * 50}\n")
    
    return books_in_stock
