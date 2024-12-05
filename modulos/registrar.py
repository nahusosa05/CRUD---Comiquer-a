import sqlite3
from cfg import prompt_is_valid
from cfg import is_int
from cfg import is_valid_str
from conexion import insert_autor
from conexion import insert_manga

def registrar_mangas(conn):
    print(f"\n"+"-"*50)
    name = prompt_is_valid("Ingrese el titulo del Manga:",is_valid_str)
    print(f"-"*50)
    autor = prompt_is_valid("Ingrese nombre del Autor: ",is_valid_str)
    print(f"-"*50)
    volumes_in_stock = []
    volumes = -1
    
    try:
        insert_autor(conn,autor)
    except sqlite3.Error:
        print(f"\n" + "*" * 50)
        print("El autor ya existe o ocurrió un error.")
        print(f"*" * 50 + "\n")


    while volumes != '0':
        volumes = prompt_is_valid("Ingrese los tomos que hay en stock (0 para salir): ", is_int)
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
