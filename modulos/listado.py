from colorama import init, Fore, Back

def listado_mangas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Title,Autor FROM Mangas")  
    info_in_bd = cursor.fetchall()  
    titles = [info[0] for info in info_in_bd] 
    authors = [info[1] for info in info_in_bd] 
    
    print(f"\n{'=' * 50}")
    print(("\t" + Back.RED + "Lista de volumenes en " + Fore.YELLOW + "stock").center(50))
    print(f"{'=' * 50}")
    print((Fore.RED + "\t Título" + Fore.RESET + " | " + Fore.GREEN + "Autor").center(50))
    for i,(title,author) in enumerate(zip(titles,authors),start=1):
        cursor = conn.cursor()
        cursor.execute("SELECT Volume, Quantity FROM Volumes WHERE Title = ?", (title,))
        volumes_info = cursor.fetchall()  
        volumes = [volume[0] for volume in volumes_info] 
        quantitys = [quantity[1] for quantity in volumes_info] 
        print(f"{'=' * 50}")
        print((f"\t{str(i)}. {Fore.RED}{title}{Fore.RESET} | {Fore.GREEN}{author}{Fore.RESET}").center(50))
        print(f"{'.' * 50}")
        for volume,quantity in zip(volumes,quantitys):
            if quantity<5:
                print((f"\t{" Volumen:"} {Fore.RED}{volume}{Fore.RESET} | Cantidad: {Fore.GREEN}{quantity}{Fore.RESET}  {Back.YELLOW}POCO STOCK").center(50))
            else:
                print((f"\t{" Volumen:"} {Fore.RED}{volume}{Fore.RESET} | Cantidad: {Fore.GREEN}{quantity}{Fore.RESET}").center(50))
    print(f"{'-' * 50}")    