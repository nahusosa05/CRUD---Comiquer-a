import sqlite3

# Conexión a la base de datos
def connect_to_db(nom):
    try:
        conn = sqlite3.connect(nom)
        return conn
    except sqlite3.Error:
        return None
 
def insert_autor(conn, autor):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Authors (AutorName) VALUES (?)", (autor))
        conn.commit()
        print(f"Autor [{autor}] insertado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar el autor: {e}")
        
def insert_manga(conn, title ,autor):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Mangas (Title,AutorName) VALUES (?,?)", (title,autor))
        conn.commit()
        print(f"Manga [{title}] insertado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar el autor: {e}")
        
