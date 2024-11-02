from database.database import Database
from services.email_sender import EmailSender
from services.review_manager import ReviewManager

class AppointmentManager:
    def __init__(self, email_sender: EmailSender):
        self._email_sender = email_sender
        self._db = Database()
        self._review_manager = ReviewManager(self._db)

    def schedule_appointment(self, client: str, client_email: str, doctor_id: int, date: str) -> int:
        appointment_id = self._db.insert_appointment(client, client_email, doctor_id, date)
        success = self._email_sender.send_notification(client_email, client, date)

        if success:
            print(f'Cita programada para {client}, ID: {appointment_id}, Fecha: {date}')
        else:
            print(f'Error al enviar la notificación. La cita para {client} no se programó.')

        return appointment_id

    def add_review(self, appointment_id: int, rating: int, comment: str) -> int:
        return self._review_manager.add_review(appointment_id, rating, comment)

    def close(self) -> None:
        self._db.close()
