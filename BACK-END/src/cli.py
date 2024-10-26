from services.appointment_manager import AppointmentManager
from services.email_sender import EmailSender

email_sender = EmailSender("testingcorreo289@gmail.com", "lpse jcjg oxat udql"); #Recibe dos parametros, correo y contraseña de app
appointments = AppointmentManager(email_sender)

CREDENCIAL = 'admin'

def login():
    print('Por favor inicia sesion')
    username = input('Usuario: ')
    password = input('Contraseña: ')
    
    if username == CREDENCIAL and password == CREDENCIAL:
        print('Inicio de sesión exitoso')
        return True
    else:
        print('Usuario y/o contraseña incorrecto')
        return False


def main():
    if login():    
        while True:
            print('\n--- Sistema de citas ---')
            print('1. Programar cita')
            print('3. Salir')
        
            choice = int(input("Selecciona una opción: "))
            
            if choice == 1:
                client = input('Nombre del paciente: ')
                client_email = input('Correo electronico del paciente: ')
                doctor_id = input('ID del Doctor: ')
                date = input('Fecha de la cita: (YYYY-MM-DD HH:MM)')
                appointments.schedule_appointment(client, client_email, doctor_id, date)
            elif choice == 3:
                break
            else:
                print('Ingresa una opción válida')

        appointments.close()
    
if __name__ == "__main__":
    main()

