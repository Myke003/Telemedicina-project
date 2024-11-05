from flask_restful import Resource, reqparse
from app.Services.user_manager import UserManager
from app.Services.appointment_manager import AppointmentManager
from app.Services.email_sender import EmailSender

# Parser para recibir datos en formato JSON
user_parser = reqparse.RequestParser()
user_parser.add_argument('nombre', required=True, help='Nombre del usuario')
user_parser.add_argument('apellido', required=True, help='Apellido del usuario')
user_parser.add_argument('email', required=True, help='Email del usuario')
user_parser.add_argument('contraseña', required=True, help='Contraseña del usuario')
user_parser.add_argument('tipo_usuario', required=True, help='Tipo de usuario')

appointment_parser = reqparse.RequestParser()
appointment_parser.add_argument('email', required=True, help='Email del paciente')
appointment_parser.add_argument('doctor_id', required=True, help='ID del doctor')
appointment_parser.add_argument('fecha_hora', required=True, help='Fecha y hora de la cita')

class UserResource(Resource):
    def post(self):
        args = user_parser.parse_args()
        user_manager = UserManager()
        
        user_id = user_manager.register_user(
            args['nombre'], args['apellido'], args['email'], args['contraseña'], args['tipo_usuario']
        )
        
        if user_id is not None:
            return {'message': 'Usuario creado con éxito', 'user_id': user_id}, 201
        else:
            return {'message': 'Error al crear el usuario'}, 400

    def get(self):
        user_manager = UserManager()
        users = user_manager.get_all_users()  # Asegúrate de implementar este método en UserManager
        return {'usuarios': users}, 200

class AppointmentResource(Resource):
    def post(self):
        args = appointment_parser.parse_args()
        email_sender = EmailSender("your_email@gmail.com", "your_password")  # Reemplaza con tus credenciales
        manager = AppointmentManager(email_sender)

        appointment_id = manager.schedule_appointment(args['email'], args['doctor_id'], args['fecha_hora'])
        
        if appointment_id is not None:
            return {'message': 'Cita programada con éxito', 'appointment_id': appointment_id}, 201
        else:
            return {'message': 'Error al programar la cita'}, 400

    def get(self):
        # Crear el AppointmentManager sin necesidad de email_sender
        manager = AppointmentManager()  # Asegúrate de que el constructor pueda funcionar sin email_sender

        appointments = manager.get_all_appointments()  # Asegúrate de implementar este método en AppointmentManager
        return {'citas': appointments}, 200
