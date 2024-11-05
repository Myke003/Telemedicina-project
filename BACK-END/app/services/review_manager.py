from Database.database import Database

class ReviewManager:
    def __init__(self, db):
        """
        Inicializa el gestor de reseñas.

        :param db: Database - Instancia de la clase Database para interactuar con la base de datos.
        """
        self._db = db

    def add_review(self, appointment_id, rating, comment):
        """
        Agrega una reseña a una cita existente.

        :param appointment_id: int - ID de la cita relacionada.
        :param rating: int - Calificación dada en la reseña.
        :param comment: str - Comentario adicional en la reseña.
        :return: int - ID de la nueva reseña.
        """
        return self._db.insert_review(appointment_id, rating, comment)

    def get_reviews(self, appointment_id):
        """
        Obtiene las reseñas de una cita específica.

        :param appointment_id: int - ID de la cita.
        :return: list - Lista de tuplas con las calificaciones y comentarios.
        """
        cursor = self._db._conn.cursor()
        cursor.execute('SELECT rating, comment FROM reviews WHERE appointment_id = ?', (appointment_id,))
        return cursor.fetchall()  # Devuelve una lista de reseñas
