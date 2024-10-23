import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Clase que se encarga de notificar el correo
class EmailSender:
    def __init__(self):
        # Email y contraseña de mi app de google (totalmente inseguro xd)
        self._email_sender = 'testingcorreo289@gmail.com' 
        self._password_sender = 'lpse jcjg oxat udql'

    def send_notification(self, client_email, client, date):
        body = f'Cordial saludo, señor(a) {client} tiene una cita programada para el día {date}'

        msg = MIMEMultipart()
        msg['From'] = self._email_sender  # Correo desde el que se envía el email
        msg['To'] = client_email  # Correo de quien va a recibirlo
        msg['Subject'] = 'Notificación de cita'  # Asunto del correo

        msg.attach(MIMEText(body, 'plain'))  # Contenido del correo

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Habilitar la seguridad
                server.login(self._email_sender, self._password_sender)  # Iniciar sesión
                server.send_message(msg)  # Enviar el mensaje
            return True

        except Exception as e:
            print(f'Ocurrió un error al enviar el correo: {e}')
            return False

# Clase que se encarga de apartar una cita
class AppointmentManager:
    def __init__(self, email_sender):
        self._email_sender = email_sender

    def schedule_appointment(self, client, client_email, date):  # Agregado client_email como parámetro
        self._email_sender.send_notification(client_email, client, date)  # Corrección aquí
        print(f'Cita programada para {client}, {date}')

# Instanciación de las clases
email_sender = EmailSender()
appointments = AppointmentManager(email_sender)

# Programación de la cita
appointments.schedule_appointment("Miguel", "miguellozano81@outlook.com", "30 de Octubre")
