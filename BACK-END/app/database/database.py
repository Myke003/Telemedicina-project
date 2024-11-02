import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',  # Lugar de la base de datos
            user='telemed',  # Username
            password='telemed',  # password
            database='telemed_db'  # database_name
        )
        self.cursor = self.connection.cursor()

    def insert_appointment(self, client, client_email, doctor_id, date):
        query = "INSERT INTO appointments (client, client_email, doctor_id, date) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (client, client_email, doctor_id, date))
        self.connection.commit()  # Asegúrate de confirmar los cambios
        return self.cursor.lastrowid  # Retorna el ID de la cita insertada

    def close(self):
        self.cursor.close()
        self.connection.close()
