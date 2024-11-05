from app.Database.database import Database
from app.Services.email_sender import EmailSender

class AppointmentManager:
    def __init__(self, email_sender: EmailSender = None):
        self._email_sender = email_sender  # Ahora es opcional
        self._db = Database()

    def schedule_appointment(self, client_email: str, doctor_id: int, fecha_hora: str) -> int:
        # Obtener el ID del paciente a partir del correo electrónico
        id_paciente = self._db.get_patient_id_by_email(client_email)

        if id_paciente is None:
            print(f"No se encontró el paciente con el correo {client_email}.")
            return None

        # Verificar si el médico está disponible en la fecha y hora seleccionadas
        if not self._db.is_doctor_available(doctor_id, fecha_hora):
            print(f'El médico con ID {doctor_id} no está disponible en la fecha y hora seleccionadas.')
            return None

        # Si el médico está disponible, se programa la cita
        appointment_id = self._db.insert_appointment(id_paciente, doctor_id, fecha_hora)

        # Enviar notificación por correo si se ha proporcionado un email_sender
        if self._email_sender:
            success = self._email_sender.send_notification(client_email, "Nombre del Cliente", fecha_hora)

            if success:
                print(f'Cita programada, ID: {appointment_id}, Fecha: {fecha_hora}')
            else:
                print(f'Error al enviar la notificación. La cita no se programó.')
        else:
            print(f'Cita programada, ID: {appointment_id}, Fecha: {fecha_hora}. (Sin notificación de correo)')

        return appointment_id

    def get_all_appointments(self):
        """Recupera todas las citas de la base de datos."""
        appointments = self._db.get_all_appointments()  # Asegúrate de que tu clase Database tenga este método
        return appointments

    def close(self) -> None:
        self._db.close()
