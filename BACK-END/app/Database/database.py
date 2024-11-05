import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',  # Lugar de la base de datos
            user='telemed',    # Username
            password='telemed',  # Password
            database='telemed_db'  # Nombre de la base de datos
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
        query = "SELECT id FROM Usuarios WHERE email = %s"  # Cambiado a 'email'
        try:
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()
            return result[0] if result else None  # Retorna el id del paciente o None si no existe
        except Exception as e:
            print(f"Error al obtener el id del paciente: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()
