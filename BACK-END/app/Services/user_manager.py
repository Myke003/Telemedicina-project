from app.Database.database import Database
from datetime import datetime

class UserManager:
    def __init__(self):
        self._db = Database()  # Inicializar la conexión a la base de datos

    def user_exists(self, email: str) -> bool:
        query = "SELECT COUNT(*) FROM Usuarios WHERE email = %s"
        self._db.cursor.execute(query, (email,))
        result = self._db.cursor.fetchone()
        return result[0] > 0

    def register_user(self, nombre: str, apellido: str, email: str, contraseña: str, tipo_usuario: str) -> int:
        if self.user_exists(email):
            print("Error: Ya existe un usuario con ese correo.")
            return None

        query = """
        INSERT INTO Usuarios (nombre, apellido, email, contraseña, tipo_usuario)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self._db.cursor.execute(query, (nombre, apellido, email, contraseña, tipo_usuario))
            self._db.connection.commit()
            return self._db.cursor.lastrowid
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return None
        
    def get_all_users(self):
        users = self._db.fetch_all_users()  # Asumiendo que devuelve una lista de tuplas
        formatted_users = []
        
        for user in users:
            # Suponiendo que la tupla tiene (id, nombre, apellido, email, fecha_creacion)
            user_dict = {
                'id': user[0],
                'nombre': user[1],
                'apellido': user[2],
                'email': user[3],
                'fecha_creacion': user[4].strftime('%Y-%m-%d %H:%M:%S') if isinstance(user[4], datetime) else user[4],
            }
            formatted_users.append(user_dict)

        return formatted_users

    def close(self):
        self._db.close()  # Asegúrate de cerrar la conexión a la base de datos
