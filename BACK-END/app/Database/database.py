import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",  # Lugar de la base de datos
            user="telemed",  # Username
            password="telemed",  # Password
            database="telemed_db",  # Nombre de la base de datos
        )
        self.cursor = self.connection.cursor()

    def insert_appointment(self, id_paciente, id_medico, fecha_hora):
        query = """
        INSERT INTO Citas (id_paciente, id_medico, fecha_hora, estado)
        VALUES (%s, %s, %s, 'pendiente')
        """
        try:
            self.cursor.execute(query, (id_paciente, id_medico, fecha_hora))
            self.connection.commit()  # Asegúrate de confirmar los cambios
            return self.cursor.lastrowid  # Retorna el ID de la cita insertada
        except Exception as e:
            print(f"Error al insertar la cita: {e}")
            return None  # O manejar el error como consideres

    def get_patient_id_by_email(self, email):
        query = "SELECT id FROM Usuarios WHERE email = %s"
        try:
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()
            return (
                result[0] if result else None
            )  # Retorna el id del paciente o None si no existe
        except Exception as e:
            print(f"Error al obtener el id del paciente: {e}")
            return None

    def user_exists(self, email: str) -> bool:
        """
        Verifica si un usuario con el correo proporcionado ya existe.
        """
        query = "SELECT COUNT(*) FROM Usuarios WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def create_user(
        self, nombre: str, apellido: str, email: str, contraseña: str, tipo_usuario: str
    ) -> int:
        """
        Crea un nuevo usuario en la base de datos.
        """
        # Verificar si el usuario ya existe
        if self.user_exists(email):
            print("Error: Ya existe un usuario con ese correo.")
            return None

        query = """
        INSERT INTO Usuarios (nombre, apellido, email, contraseña, tipo_usuario)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(
                query, (nombre, apellido, email, contraseña, tipo_usuario)
            )
            self.connection.commit()
            return self.cursor.lastrowid  # Retorna el ID del usuario creado
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return None

    def is_doctor_available(self, doctor_id, fecha_hora):
        query = """
        SELECT COUNT(*) FROM Citas 
        WHERE id_medico = %s AND fecha_hora = %s AND estado != 'cancelada'
        """
        self.cursor.execute(query, (doctor_id, fecha_hora))
        result = self.cursor.fetchone()
        return (
            result[0] == 0
        )  # Retorna True si está disponible, False si ya tiene una cita
        
    def get_all_appointments(self):
        # Implementa la lógica para recuperar todas las citas
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Citas")  # Asegúrate de que 'Citas' es el nombre correcto de tu tabla
        appointments = cursor.fetchall()
        cursor.close()
        return appointments
    
    def fetch_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Usuarios")  # Asegúrate de que este es el nombre de tu tabla
        return cursor.fetchall()


    def close(self):
        self.cursor.close()
        self.connection.close()
