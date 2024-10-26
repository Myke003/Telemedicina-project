import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, email_sender, password_sender):
        """
        Inicializa el gestor de envío de correos.

        :param email_sender: str - Correo electrónico del remitente.
        :param password_sender: str - Contraseña del remitente.
        """
        self._email_sender = email_sender
        self._password_sender = password_sender

    def send_notification(self, client_email, client, date):
        """
        Envía una notificación por correo electrónico sobre la cita programada.

        :param client_email: str - Correo electrónico del cliente.
        :param client: str - Nombre del cliente.
        :param date: str - Fecha de la cita.
        :return: bool - True si el correo fue enviado con éxito, False en caso contrario.
        """
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
