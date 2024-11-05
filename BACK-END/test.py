from app.Database.database import Database
from app.services.email_sender import EmailSender
from app.services.appointment_manager import AppointmentManager

# Función principal para ejecutar el ejemplo
def main():
    # Crea un objeto EmailSender con tus credenciales
    email_sender = EmailSender("testingcorreo289@gmail.com", "lpse jcjg oxat udql")  # Cambia por tus credenciales

    # Crea el gestor de citas
    manager = AppointmentManager(email_sender)

    # Ejemplo de programación de una cita
    client_email = "miguellozano81@outlook.com"  # Cambia esto por el email del cliente que esté en la base de datos
    doctor_id = 1  # ID del doctor asignado
    fecha_hora = "2024-11-10 15:00"  # Fecha y hora de la cita

    # Programa la cita
    appointment_id = manager.schedule_appointment(client_email, doctor_id, fecha_hora)
    if appointment_id is not None:
        print(f"Cita programada con éxito, ID: {appointment_id}")
    
    # Cierra la conexión con la base de datos
    manager.close()

# Ejecuta la función principal
if __name__ == "__main__":
    main()
