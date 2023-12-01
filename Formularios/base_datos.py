import sqlite3

class BaseDeDatos:
    def __init__(self) -> None:
        self.path_db = "database.db"

    def insertar_datos(self, nombre, puntaje, nivel):
        with sqlite3.connect(self.path_db) as conexion:
            try:
                '''# CREATE TABLE
                sentencia ="""
                            create table Ranking
                            (
                                id integer primary key autoincrement,
                                nombre text,
                                puntaje integer
                            )
                            """'''
                conexion.execute("insert into Ranking(nombre, puntaje, nivel) values (?,?,?)", (nombre, puntaje, nivel))
                conexion.commit()
                print("INSERTADO CON ÉXITO")
            except:
                print("ERROR! NO se insertaron los datos correctamente")

    def traer_datos(self):
        with sqlite3.connect(self.path_db) as conexion:
            try:
                sentencia = "select nombre, puntaje, nivel from Ranking order by puntaje desc"# limit 3"
                cursor = conexion.execute(sentencia)
                resultados = []
                #print(cursor.fetchall())
                for tupla in cursor.fetchall():
                    jugador = tupla[0]
                    puntaje = tupla[1]
                    nivel = tupla[2]
                    diccionario = {"jugador": jugador, "puntaje": puntaje, "nivel": nivel}
                    resultados.append(diccionario)
                #print(resultados)
                print(resultados)
                print("LEIDO CON ÉXITO")
                return resultados
            except:
                print("ERROR! NO se leyeron los datos")
