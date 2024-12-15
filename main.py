# COMIQUERIA (MANGAS Y COMICS)
from colorama import init, Fore, Back
from modulos.registrar import registrar_mangas
from modulos.actualizar import actualizar_mangas
from modulos.eliminar import eliminar_mangas
from modulos.buscar import buscar_mangas
from modulos.listado import listado_mangas
import cfg 
import conexion
init(autoreset=True)

def main():
    db_name = 'inventario.db'
    conn = conexion.connect_to_db(db_name)
    
    if conn:
        while True:
            print(f"=" * 50)
            print(Back.CYAN + "Menú para gestión de Mangas".center(50)) 
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
                        cfg.clear()
                        registrar_mangas(conn)

                    # ACTUALIZAR
                    elif user_input == 2:
                        cfg.clear()
                        actualizar_mangas(conn)

                    # ELIMINAR 
                    elif user_input == 3:
                        cfg.clear()
                        eliminar_mangas(conn)

                    # BUSCAR 
                    elif user_input == 4:
                        cfg.clear()
                        buscar_mangas(conn)

                    # LISTADO
                    elif user_input == 5:
                        cfg.clear()
                        listado_mangas(conn)

                    # SALIR
                    elif user_input == 6:
                        conn.close()
                        break
                else:
                    print(f"\n" + "*" * 50)
                    print(Fore.RED + "Debe ingresar un valor numérico entre 1 y 6. Por favor, inténtelo nuevamente.".center(50))
                    print(f"*" * 50 + "\n")
    else:
        print(f"\n" + "*" * 50)
        print(Fore.RED + "Problema al conectar con la base de datos.".center(50))
        print(f"*" * 50 + "\n")
    

if __name__ == "__main__":
    main()
