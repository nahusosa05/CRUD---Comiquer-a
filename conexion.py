import sqlite3
from cfg import get_format_msg, get_wrong_msg
from colorama import init, Fore, Back
init(autoreset=True)

# Conexión a la base de datos
def connect_to_db(nom):
    try:
        conn = sqlite3.connect(nom)
        return conn
    except sqlite3.Error:
        return None
 
def insert_autor(conn, autor):
    flag = True
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Authors (AutorName) VALUES (?)", (autor,))
        conn.commit()
        x = get_format_msg(Fore.GREEN + f"Autor [{autor}] insertado correctamente.".center(50) + Fore.RESET)
        # Indica que la inserción fue exitosa
    
    except sqlite3.IntegrityError:  # Error por clave única o duplicados
        x = get_wrong_msg(Fore.RED + f"El autor '{autor}' ya existe en la base de datos.".center(50) + Fore.RESET)
        flag = False
        
    except sqlite3.Error as e:  # Otros errores de SQLite
        x = get_wrong_msg(Fore.RED + f"Error al insertar el autor: {e}".center(50) + Fore.RESET)    
        flag = False
        
    print(x)
    return flag

    
def insert_manga(conn, title, autor):
    flag = True
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Mangas (Title, Autor) VALUES (?, ?)", (title, autor))
        conn.commit()
        x = get_format_msg(Fore.GREEN + f"Manga [{title}] insertado correctamente." + Fore.RESET)
        
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            x = get_wrong_msg(Fore.RED + f"El manga '{title}' ya está registrado.".center(50) + Fore.RESET)
            flag = False
        else:
            x = get_wrong_msg(Fore.RED + f"Error al insertar el manga: {e}".center(50) + Fore.RESET)
            flag = False
    except sqlite3.Error as e:
        x = get_wrong_msg(Fore.RED + f"Error general: {e}".center(50) + Fore.RESET)
        flag = False
        
    print(x)
    return flag
    
def insert_volumes(conn,title,volumes_in_stock):
    flag = True
    try:
        cursor = conn.cursor()
        for volume,quantity in volumes_in_stock.items():
            cursor.execute(
                "INSERT INTO Volumes (Title, Volume, Quantity) VALUES (?, ?, ?)",
                (title, int(volume), int(quantity))
            )
        conn.commit()
        x = get_format_msg(Fore.GREEN + f"Volúmenes de [{title}] insertados correctamente." + Fore.RESET)

    except sqlite3.Error:
        x = get_wrong_msg(Fore.RED + f"Error al insertar el volumen.".center(50) + Fore.RESET)
        flag = False
        
    print(x)
    return flag

def fetch_mangas(conn):  
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Title FROM Mangas")  # Asegúrate de que 'Mangas' sea la tabla correcta
        titles = cursor.fetchall()  # Obtiene todas las filas de la consulta
        titles = [title[0] for title in titles] 
        
        # Si no hay mangas, se puede devolver una lista vacía o un mensaje adecuado
        if not titles:
            x = get_wrong_msg(Fore.RED + f"No se encontraron mangas en la base de datos.".center(50) + Fore.RESET)
            print(x)
            return None
    
    except sqlite3.Error as e:
        x = get_wrong_msg(Fore.RED + f"Ocurrió un error inesperado: {e}".center(50) + Fore.RESET)
        print(x)
        return None  

    return titles

def fetch_authors(conn):  
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT AutorName FROM Authors")  # Asegúrate de que 'Mangas' sea la tabla correcta
        authors = cursor.fetchall()  # Obtiene todas las filas de la consulta
        authors = [author[0] for author in authors] 
        
        # Si no hay mangas, se puede devolver una lista vacía o un mensaje adecuado
        if not authors:
            x = get_wrong_msg(Fore.RED + f"No se encontraron autores en la base de datos.".center(50) + Fore.RESET)
            print(x)
            return None
    
    except sqlite3.Error as e:
        x = get_wrong_msg(Fore.RED + f"Ocurrió un error inesperado: {e}".center(50) + Fore.RESET)
        print(x)
        return None  

    return authors
