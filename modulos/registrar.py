def registrar_mangas(books_in_stock):
    print(f"\n"+"-"*50)
    name = input("Ingrese nombre del Manga/Comic: ")
    print(f"-"*50)
    autor = input("Ingrese nombre del Autor: ")
    print(f"-"*50)
    volumes_in_stock = []
    volumes = -1

    while volumes != '0':
        volumes = input("Ingrese los tomos que hay en stock (0 para salir): ")
        if volumes.isdigit() and int(volumes)>= 0: 
            if volumes == '0':
                volumes_in_stock.sort()
                book = [name, autor, volumes_in_stock]
                books_in_stock.append(book)
                print(f"-"*50)
                print("-REGISTRO CON EXITO-".center(50))
                print(f"-"*50+"\n")
                break
            elif volumes == -1:
                break
            elif volumes in volumes_in_stock:
                print(f"Tomo {volumes} YA REGISTRADO. Ingrese un valor nuevo")
                print(f"." * 50)
            else:
                volumes_in_stock.append(volumes)
                print(f"Tomo {volumes} registrado con éxito.")
                print(f"."*50)
        else:
            print(f"\n" + "*" * 50)
            print("Ingrese el numero del tomo.".center(50))
            print(f"*" * 50 + "\n")
    return books_in_stock        
