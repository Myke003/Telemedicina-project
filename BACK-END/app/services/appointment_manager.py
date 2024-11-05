from app.Database.database import Database
from app.services.email_sender import EmailSender

class AppointmentManager:
    def __init__(self, email_sender: EmailSender):
        self._email_sender = email_sender
        self._db = Database()

    def schedule_appointment(self, client_email: str, doctor_id: int, fecha_hora: str) -> int:
        # Obtener el ID del paciente a partir del correo electrónico
        id_paciente = self._db.get_patient_id_by_email(client_email)

        if id_paciente is None:
            print(f"No se encontró el paciente con el correo {client_email}.")
            return None

        appointment_id = self._db.insert_appointment(id_paciente, doctor_id, fecha_hora)
        success = self._email_sender.send_notification(client_email, "Nombre del Cliente", fecha_hora)

        if success:
            print(f'Cita programada, ID: {appointment_id}, Fecha: {fecha_hora}')
        else:
            print(f'Error al enviar la notificación. La cita no se programó.')

        return appointment_id

    def close(self) -> None:
        self._db.close()
