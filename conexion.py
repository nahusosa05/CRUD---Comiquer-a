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
        x = get_format_msg(Fore.GREEN + f"Autor [{autor}] insertado correctamente." + Fore.RESET)
        # Indica que la inserción fue exitosa
    
    except sqlite3.IntegrityError:  # Error por clave única o duplicados
        x = get_wrong_msg(Fore.RED + f"El autor '{autor}' ya existe en la base de datos." + Fore.RESET)
        flag = False
    
    except sqlite3.Error as e:  # Otros errores de SQLite
        x = get_wrong_msg(Fore.RED + f"Error al insertar el autor: {e}" + Fore.RESET)
        flag = False
        
    print(x)
    return flag
    
def insert_manga(conn, title, autor):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Mangas (Title, Autor) VALUES (?, ?)", (title, autor))
        conn.commit()
        y = get_format_msg(Fore.GREEN + f"Manga [{title}] insertado correctamente." + Fore.RESET)
        print(y)
        
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            x = get_wrong_msg(Fore.RED + f"El manga '{title}' ya está registrado." + Fore.RESET)
        else:
            x = get_wrong_msg(Fore.RED + f"Error al insertar el manga: {e}" + Fore.RESET)
        print(x)
        
    except sqlite3.Error as e:
        x = get_wrong_msg(Fore.RED + f"Error general: {e}" + Fore.RESET)
        print(x)
    
def last_id(conn):
    cursor = conn.cursor()
    id = cursor.lastrowid
    return id