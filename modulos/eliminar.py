from cfg import is_int
from cfg import is_valid_str
from cfg import prompt_is_valid

def eliminar_mangas(books_in_stock):
    if not len(books_in_stock) == 0:
        print(f"\n{'-'*50}")
        print("ELIMINACIÓN DE MANGAS".center(50))
        print(f"-" * 50)
        
        prompt_elseint_msg = ( "\n" + "*" * 50 +
                           "\nDebe ingresar un valor numérico de los mostrados en la lista." +
                           "\n" + "*" * 50)
        
        for books in books_in_stock:
            num = books_in_stock.index(books)
            print(f"{'\t.' + str(num+1):<16}{books[0]}")
        
        print(f"-" * 50 + "\n")
        promp_int = "Ingrese el número de algún Manga/Comic de la lista para eliminar: "
        num_input = prompt_is_valid(promp_int,prompt_elseint_msg,is_int)
        print(f"-" * 50)
        if num_input <= len(books_in_stock) and num_input > 0:
            promp = prompt_is_valid("\n¿Está seguro que quiere eliminar este manga? (SI/NO) : ",is_valid_str)
            print(f"-" * 50)
            if promp == 'SI':
                manga_removed = books_in_stock.pop(num_input - 1)
                print(f"\n{'-'*50}")
                print("REMOVIDO CON ÉXITO - Elementos removidos:".center(50))
                print(f"-" * 50)
                print(f"{' Manga:':<20}{manga_removed[0]}")
                print(f"{' Autor:':<20}{manga_removed[1]}")
                print(f"{' Tomos:':<20}{manga_removed[2]}")
                print(f"-" * 50 + "\n")
            elif promp == 'NO':
                print("Volviendo al menú...".center(50))
                print(f"-" * 50)
    else:
        print(f"\n{'*' * 50}")
        print("NO HAY MANGAS PARA ELIMINAR - REGÍSTRELOS PRIMERO".center(50))
        print(f"{'*' * 50}\n")

    return books_in_stock
