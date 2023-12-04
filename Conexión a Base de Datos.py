# Kattherine Guadalupe Marina Cazares 951 25/Agosto/2023

from mysql.connector import connect, Error
import mysql.connector

# Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database. Debe crear sus
# métodos set y get (property, setters). Debe tener los siguientes métodos:
# conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
# desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

class MySQL:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    def connect(self):
        if not self._connection:
            self._connection = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            database = self._database)

            return self._connection

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None

mysql_connection = MySQL("localhost", "root", "12345678", "olimpiadas")
connection = mysql_connection.connect()
if connection:
    print("Conexion exitosa")
    mysql_connection.disconnect()
    print("Conexion cerrada")
else:
    print("Conexión erronea")

# Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la
# clase padre. Debe agregar los siguientes métodos:
# insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla
# y debe retornar True si se inserta el dato o False en caso contrario.
# editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
# eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna
# True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de
# la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”

class PaisMySQL(MySQL):
    def __int__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "INSERT INTO olimpiadas.pais (id, nombre) VALUES(%s, %s)"
            cursor.execute(sql, (id, nombre))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al insertar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def editar(self, nuevo_pais, id):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."
        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.pais WHERE nombre=%s;"
            cursor.execute(sql, (nuevo_pais, ))
            if cursor.fetchall():
                return "Nombre de pais ya existente."
            else:
                sql = "UPDATE olimpiadas.pais SET nombre=%s WHERE id=%s"
                cursor.execute(sql, (nuevo_pais, id))
                connection.commit()
                return "Update realizado."
        except mysql.connector.Error as error:
            print(f"Error al editar datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def eliminar(self, id):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexcion.")
        cursor = connection.cursor()

        try:
            sql = "DELETE FROM olimpiadas.pais WHERE id = %s"
            cursor.execute(sql, (id, ))
            if cursor.rowcount == 0:
                print("No se encontró un país con el ID especificado.")
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"Error al eliminar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def consultar(self, filter):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexion.")
        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.pais WHERE "+filter
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Error al consultar los datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

# Desarrollar una clase llamada OlimpiadaMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes
# de la clase padre. Debe agregar los siguientes métodos:
# insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la
# tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(year): Método para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
# eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria,
# retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de
# la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

class OlimpiadaMySQL(MySQL):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        print(f"Conectado a la base de datos {database} en {host} como {user}")

    def insertar(self, id, year_olimpiada):
        connection = self.conectar()
        if connection is not None:
            try:
                cursor = connection.cursor()
                query = "select * from Olimpiada where year_olimpiada = %s"
                cursor.execute(query, (year_olimpiada,))
                if cursor.fetchone() is not None:
                    print("El año de la Olimpiada ya existe en la tabla Olimpiada")
                else:
                    insert_query = "insert into Olimpiada (id, year_olimpiada) values (%s, %s)"
                    cursor.execute(insert_query, (id, year_olimpiada))
                    connection.commit()
                    print("Inserción exitosa en la tabla Olimpiada")
            except Error as err:
                print(f"Error al insertar en la tabla Olimpiada {err}")
            finally:
                cursor.close()
                self.desconectar(connection)
        else:
            print("No se pudo establecer la conexión")

    def editar(self, id, new_year_olimpiada):
        connection = self.conectar()
        if connection is not None:
            try:
                cursor = connection.cursor()
                query_existencia = "select id from Olimpiada where year_olimpiada = %s and id != %s"
                cursor.execute(query_existencia, (new_year_olimpiada, id))
                if cursor.fetchone() is not None:
                    print("El nuevo año de la Olimpiada ya existe en la tabla")
                else:
                    update_query = "update Olimpiada set year_olimpiada = %s where id = %s"
                    cursor.execute(update_query, (new_year_olimpiada, id))
                    connection.commit()
                    print("Actualización exitosa en la tabla Olimpiada")
            except Error as err:
                print(f"Error al editar en la tabla Olimpiada {err}")
            finally:
                cursor.close()
                self.desconectar(connection)
        else:
            print("No se pudo establecer la conexión")

    def eliminar(self, id):
        connection = self.conectar()
        if connection is not None:
            try:
                cursor = connection.cursor()
                query = "Delete from Olimpiada where id = %s"
                cursor.execute(query, (id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminación exitosa en la tabla Olimpiada")
                else:
                    print("No se encontró el elemento con el ID proporcionado")
            except Error as err:
                print(f"Error al eliminar en la tabla Olimpiada {err}")
            finally:
                cursor.close()
                self.desconectar(connection)
        else:
            print("No se pudo establecer la conexión")

    def consultar(self, filtro):
        connection = self.conectar()
        resultados = []
        if connection is not None:
            try:
                cursor = connection.cursor()
                query = f"select * from Olimpiada where {filtro}"
                cursor.execute(query)
                resultados = cursor.fetchall()
                print(f"Resultados de la consulta en la tabla Olimpiada {resultados}")
            except Error as err:
                print(f"Error al consultar en la tabla Olimpiada {err}")
            finally:
                cursor.close()
                self.desconectar(connection)
        return resultados

if __name__ == "__main__":
    olimpiada_db = OlimpiadaMySQL(host="localhost", user="root", password="12345678", database="olimpiadas")
    olimpiada_db.insertar(id=1, year_olimpiada=2023)
    olimpiada_db.editar(id=1, new_year_olimpiada=2024)
    olimpiada_db.eliminar(id=1)
    resultados = olimpiada_db.consultar("year_olimpiada > 1990")
    print(resultados)

# Desarrollar una clase llamada ResultadosMySQL que herede de MySQLConnect. Debe agregar los atributos correspondientes
# de la clase padre. Debe agregar los siguientes métodos:
# insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, debe
# recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores
# enteros positivos.
# eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. Debe tener como
# parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de
# la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”

class ResultadosMySQL(MySQL):
    def __int__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "INSERT INTO olimpiadas.resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al insertar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            if all(isinstance(valor, int) and valor % 1 == 0 for valor in (oro, plata, bronce)):
                if oro >= 0 and plata >= 0 and bronce >= 0:
                    sql = "UPDATE olimpiadas.resultados SET oro=%s, plata=%s, bronce=%s WHERE idOlimpiada=%s and idPais=%s and idGenero=%s"
                    cursor.execute(sql, (oro, plata, bronce, idOlimpiada, idPais, idGenero))
                    connection.commit()
                    return "Update realizado."
            else:
                return "Tus valores deben ser números enteros y positivos."

        except mysql.connector.Error as error:
            print(f"Error al editar datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def eliminar(self, idOlimpiada, idPais, idGenero):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexcion.")

        cursor = connection.cursor()

        try:
            sql = "DELETE FROM olimpiadas.resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
            cursor.execute(sql, (idOlimpiada, idPais, idGenero))
            if cursor.rowcount == 0:
                print("No se encontró el resultado especificado.")
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"Error al eliminar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def consultar(self, filter):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexion.")

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.resultados WHERE "+filter
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Error al consultar los datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

resultados_sql = ResultadosMySQL("localhost", "root", "12345678", "olimpiadas")