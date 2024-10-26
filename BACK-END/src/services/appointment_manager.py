from database.database import Database
from services.email_sender import EmailSender
from services.review_manager import ReviewManager

class AppointmentManager:
    def __init__(self, email_sender):
        """
        Inicializa el gestor de citas.

        :param email_sender: EmailSender - Instancia de la clase EmailSender para enviar correos.
        """
        self._email_sender = email_sender
        self._db = Database()  # Inicializa la base de datos
        self._review_manager = ReviewManager(self._db)  # Inicializa el gestor de reseñas

    def schedule_appointment(self, client, client_email, doctor_id, date):
        """
        Programa una cita y envía una notificación al cliente.

        :param client: str - Nombre del cliente.
        :param client_email: str - Correo electrónico del cliente.
        :param doctor_id: int - ID del doctor asignado.
        :param date: str - Fecha y hora de la cita.
        """
        # Inserta la cita en la base de datos
        appointment_id = self._db.insert_appointment(client, client_email, doctor_id, date)
        
        # Envía la notificación por correo
        success = self._email_sender.send_notification(client_email, client, date)
        
        if success:
            print(f'Cita programada para {client}, ID: {appointment_id}, Fecha: {date}')
        else:
            print(f'Error al enviar la notificación. La cita para {client} no se programó.')

    def add_review(self, appointment_id, rating, comment):
        """
        Agrega una reseña a una cita existente.

        :param appointment_id: int - ID de la cita.
        :param rating: int - Calificación de la reseña.
        :param comment: str - Comentario adicional en la reseña.
        :return: int - ID de la reseña añadida.
        """
        return self._review_manager.add_review(appointment_id, rating, comment)

    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        self._db.close()  # Cierra la conexión a la base de datos
