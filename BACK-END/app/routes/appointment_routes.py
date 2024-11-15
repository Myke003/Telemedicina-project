from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
from app.services.notification_service import send_notification

appointment_bp = Blueprint('appointments', __name__)

@appointment_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    patient_id = data['patient_id']
    doctor_id = data['doctor_id']
    appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
    
    # Accede a mysql a través de current_app
    mysql = current_app.extensions['mysql']
    
    # Insertar la nueva cita en la base de datos
    cursor = mysql.connection.cursor()
    cursor.execute('''
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
        VALUES (%s, %s, %s, %s)
    ''', (patient_id, doctor_id, appointment_date, 'pending'))
    mysql.connection.commit()
    cursor.close()

    # Enviar notificaciones a paciente y doctor
    send_notification(patient_id, 'appointment_created', f'Your appointment with doctor {doctor_id} has been created for {appointment_date.strftime("%Y-%m-%d %H:%M:%S")}.')
    send_notification(doctor_id, 'appointment_created', f'You have a new appointment with patient {patient_id} scheduled for {appointment_date.strftime("%Y-%m-%d %H:%M:%S")}.')
    
    return jsonify({'message': 'Appointment created successfully!'}), 201

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, patient_id, doctor_id, appointment_date, status FROM appointments WHERE id = %s', (appointment_id,))
    appointment = cursor.fetchone()
    cursor.close()

    if appointment is None:
        return jsonify({'error': 'Appointment not found'}), 404

    return jsonify({
        'id': appointment[0],
        'patient_id': appointment[1],
        'doctor_id': appointment[2],
        'appointment_date': appointment[3].strftime('%Y-%m-%d %H:%M:%S'),
        'status': appointment[4]
    })

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()

    # Actualizar la cita
    if 'appointment_date' in data:
        appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
        cursor.execute('UPDATE appointments SET appointment_date = %s WHERE id = %s', (appointment_date, appointment_id))
    
    if 'status' in data:
        status = data['status']
        cursor.execute('UPDATE appointments SET status = %s WHERE id = %s', (status, appointment_id))
    
    mysql.connection.commit()
    cursor.close()

    # Obtener la cita actualizada
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT patient_id, doctor_id, appointment_date FROM appointments WHERE id = %s', (appointment_id,))
    appointment = cursor.fetchone()
    cursor.close()

    if appointment is None:
        return jsonify({'error': 'Appointment not found'}), 404

    # Enviar notificaciones
    send_notification(appointment[0], 'appointment_updated', f'Your appointment has been updated to {appointment[2].strftime("%Y-%m-%d %H:%M:%S")}.')
    send_notification(appointment[1], 'appointment_updated', f'You have an updated appointment scheduled for {appointment[2].strftime("%Y-%m-%d %H:%M:%S")}.')
    
    return jsonify({'message': 'Appointment updated successfully!'}), 200

@appointment_bp.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE appointments SET status = %s WHERE id = %s', ('cancelled', appointment_id))
    mysql.connection.commit()
    cursor.close()

    # Enviar notificaciones
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT patient_id, doctor_id FROM appointments WHERE id = %s', (appointment_id,))
    appointment = cursor.fetchone()
    cursor.close()

    if appointment is None:
        return jsonify({'error': 'Appointment not found'}), 404

    send_notification(appointment[0], 'appointment_cancelled', 'Your appointment has been cancelled.')
    send_notification(appointment[1], 'appointment_cancelled', 'Your appointment has been cancelled.')
    
    return jsonify({'message': 'Appointment cancelled successfully!'}), 200
