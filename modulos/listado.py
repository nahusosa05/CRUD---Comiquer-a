def listado_mangas(books_in_stock):
    if not len(books_in_stock) == 0:
        print(f"\n{'-' * 50}")
        print("LISTADO DE MANGAS".center(50))
        print(f"{'-' * 50}")
        
        for books in books_in_stock:
            name = books[0]
            autor = books[1]
            volumes_in_stock = books[2]
            print(f"{' Manga:':<20}{name}")
            print(f"{' Autor:':<20}{autor}")
            print(f"{' Tomos en stock:':<20}{volumes_in_stock}")
            print(f"{'-' * 50}\n")
    else:
        print(f"\n{'*' * 50}")
        print("LISTA VACÍA - REGÍSTRELOS PRIMERO".center(50))
        print(f"{'*' * 50}\n")

    return books_in_stock
