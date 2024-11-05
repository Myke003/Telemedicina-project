from app.Database.database import Database
from app.Services.email_sender import EmailSender
from app.Services.appointment_manager import AppointmentManager
from app.Services.user_manager import UserManager


# Función principal para crear un usuario
def crear_usuario():
    # Crea una instancia de UserManager
    user_manager = UserManager()
    
    nombre = 'paciente_prueba'
    apellido = 'apellido_prueba'
    email = 'miguellozano627@gmail.com'  # Asegúrate de que este correo no exista en la base de datos
    contraseña = 'contraseña123'
    tipo_usuario = 'paciente'
    
    # Comprobar si el usuario ya existe
    if user_manager.user_exists(email):
        print(f"El usuario con el correo {email} ya existe. No se creará un nuevo usuario.")
        user_manager.close()  # Cierra la conexión al finalizar
        return

    user_id = user_manager.register_user(nombre, apellido, email, contraseña, tipo_usuario)
    
    if user_id is not None:
        print(f"Usuario creado con éxito, ID: {user_id}")
    else:
        print("No se pudo crear el usuario.")

    user_manager.close()  # Cierra la conexión al finalizar


# Función principal para crear una cita
def crear_cita():
    # Crea un objeto EmailSender con tus credenciales
    email_sender = EmailSender(
        "testingcorreo289@gmail.com", "lpse jcjg oxat udql"
    )  # Cambia por tus credenciales

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


# Ejecuta la creación de usuario
crear_usuario()

# Ejecuta la creación de cita
#crear_cita()
