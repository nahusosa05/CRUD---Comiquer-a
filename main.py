# COMIQUERIA (MANGAS Y COMICS)
from colorama import init, Fore, Back
from modulos.registrar import registrar_mangas
import cfg 
import conexion
init(autoreset=True)

def main():
    books_in_stock = []
    db_name = 'inventario.db'
    conn = conexion.connect_to_db(db_name)
    
    if conn:
        while True:
            print(f"=" * 50)
            print(Back.CYAN + Fore.GREEN + "       Menú para gestión de Mangas".center(50)) 
            print(Fore.RESET + f"=" * 50) 
            print(f"{Fore.BLUE + '\t 1.':<14}{Fore.RESET + 'Registrar mangas'}")         
            print(f"{Fore.BLUE + '\t 2.':<14}{Fore.RESET + 'Actualizar mangas'}")        
            print(f"{Fore.BLUE + '\t 3.':<14}{Fore.RESET + 'Eliminar mangas'}")          
            print(f"{Fore.BLUE + '\t 4.':<14}{Fore.RESET + 'Buscar mangas'}")             
            print(f"{Fore.BLUE + '\t 5.':<14}{Fore.RESET + 'Listado de mangas disponibles'}")     
            print(f"{Fore.BLUE + '\t 6.':<14}{Fore.RESET + 'Salir'}")
            print(f"=" * 50)
            user_input = input("\nElija su opción numerica del 1 al 6:    ")

            if cfg.is_int(user_input):
                user_input = int(user_input)
                if user_input >= 1 and user_input <= 6:
                    # AGREGAR
                    if user_input == 1:
                        registrar_mangas(conn)
                        #cfg.clear()

                    # ACTUALIZAR
                    elif user_input == 2:
                        #cfg.actualizar_mangas(books_in_stock)
                        cfg.clear()

                    # ELIMINAR 
                    elif user_input == 3:
                        #cfg.eliminar_mangas(books_in_stock)
                        cfg.clear()

                    # BUSCAR 
                    elif user_input == 4:
                        cfg.clear()
                        #cfg.buscar_mangas(books_in_stock)

                    # LISTADO
                    elif user_input == 5:
                        cfg.clear()
                        #cfg.listado_mangas(books_in_stock)

                    # SALIR
                    elif user_input == 6:
                        break
                else:
                    print(f"\n" + "*" * 50)
                    print("Debe ingresar un valor numérico entre 1 y 6. Por favor, inténtelo nuevamente.".center(50))
                    print(f"*" * 50 + "\n")
    else:
        print(f"\n" + "*" * 50)
        print("Problema al conectar con la base de datos.".center(50))
        print(f"*" * 50 + "\n")

if __name__ == "__main__":
    main()
