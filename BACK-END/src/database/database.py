import sqlite3
import os

class Database:
    def __init__(self, db_name='telemedicina.db'):
        # Construye la ruta absoluta de la base de datos
        db_path = os.path.join(os.path.dirname(__file__), db_name)
        self._conn = sqlite3.connect(db_path)
        self._create_tables()


    def _create_tables(self):
        cursor = self._conn.cursor()
        
        # Tabla para almacenar información de los doctores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialization TEXT NOT NULL
            )
        ''')
        
        # Tabla para almacenar citas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client TEXT NOT NULL,
                client_email TEXT NOT NULL,
                doctor_id INTEGER,
                date TEXT NOT NULL,
                status TEXT DEFAULT 'scheduled',
                FOREIGN KEY (doctor_id) REFERENCES doctors (id)
            )
        ''')
        
        # Tabla para almacenar reseñas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_id INTEGER,
                rating INTEGER NOT NULL,
                comment TEXT,
                FOREIGN KEY (appointment_id) REFERENCES appointments (id)
            )
        ''')
        
        # Tabla para gestionar disponibilidad de los doctores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS availability (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doctor_id INTEGER,
                date TEXT NOT NULL,
                time_slot TEXT NOT NULL,  -- Ejemplo: "09:00-10:00"
                is_available BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (doctor_id) REFERENCES doctors (id)
            )
        ''')
        
        self._conn.commit()

    def insert_doctor(self, name, specialization):
        cursor = self._conn.cursor()
        cursor.execute('''
            INSERT INTO doctors (name, specialization) 
            VALUES (?, ?)''', (name, specialization))
        self._conn.commit()
        return cursor.lastrowid  # Devuelve el ID del nuevo doctor

    def insert_appointment(self, client, client_email, doctor_id, date):
        cursor = self._conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (client, client_email, doctor_id, date) 
            VALUES (?, ?, ?, ?)''', (client, client_email, doctor_id, date))
        self._conn.commit()
        return cursor.lastrowid  # Devuelve el ID de la nueva cita

    def insert_review(self, appointment_id, rating, comment):
        cursor = self._conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (appointment_id, rating, comment) 
            VALUES (?, ?, ?)''', (appointment_id, rating, comment))
        self._conn.commit()
        return cursor.lastrowid  # Devuelve el ID de la nueva reseña

    def update_availability(self, doctor_id, date, time_slot, is_available):
        cursor = self._conn.cursor()
        cursor.execute('''
            INSERT INTO availability (doctor_id, date, time_slot, is_available) 
            VALUES (?, ?, ?, ?)
            ON CONFLICT(doctor_id, date, time_slot) 
            DO UPDATE SET is_available = excluded.is_available
        ''', (doctor_id, date, time_slot, is_available))
        self._conn.commit()

    def close(self):
        self._conn.close()
