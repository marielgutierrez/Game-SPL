import sqlite3

nombre_jugador = "Ejemplo"
puntaje_jugador = 100

with sqlite3.connect("mi_base_de_datos.db") as conexion:
    try:
        setencia = """
                    create table Score
                    (
                        Nombre text,
                        Puntaje integer
                    )
                    """
        #conexion.execute(setencia)
        conexion.execute("insert into Score (Nombre, Puntaje) values (?, ?)", (nombre_jugador, puntaje_jugador))
        print("Tabla creado con exito")
    except:
        print("Error!!")