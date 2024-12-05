# COMIQUERIA (MANGAS Y COMICS)
# from colorama import init
import cfg
import conexion

def main():
    books_in_stock = []
    db_name = 'comiqueria.db'
    conn = conexion.connect_to_db(db_name)
    
    if conn:
        while True:
            print(f"=" * 50)
            print("Menú para gestión de libros".center(50))
            print(f"=" * 50)
            print(f"{'\t 1.':<14}{'Registrar mangas'}")           # new mangas to up
            print(f"{'\t 2.':<14}{'Actualizar mangas'}")         # update mangas in stock (volumes)
            print(f"{'\t 3.':<14}{'Eliminar mangas'}")           # delete mangas without stock
            print(f"{'\t 4.':<14}{'Buscar mangas'}")             # shows the specific stock of a product
            print(f"{'\t 5.':<14}{'Listado de mangas disponibles'}")  # shows all mangas in stock   
            print(f"{'\t 6.':<14}{'Salir'}")
            print(f"=" * 50)
            user_input = input("\nElija su opción numerica del 1 al 6:    ")

            if cfg.is_int(user_input):
                user_input = int(user_input)
                if user_input >= 1 and user_input <= 6:
                    # AGREGAR
                    if user_input == 1:
                        cfg.registrar_mangas(conn)
                        cfg.limpiar_pantalla()

                    # ACTUALIZAR
                    elif user_input == 2:
                        cfg.actualizar_mangas(books_in_stock)
                        cfg.limpiar_pantalla()

                    # ELIMINAR 
                    elif user_input == 3:
                        cfg.eliminar_mangas(books_in_stock)
                        cfg.limpiar_pantalla()

                    # BUSCAR 
                    elif user_input == 4:
                        cfg.limpiar_pantalla()
                        cfg.buscar_mangas(books_in_stock)

                    # LISTADO
                    elif user_input == 5:
                        cfg.limpiar_pantalla()
                        cfg.listado_mangas(books_in_stock)

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
