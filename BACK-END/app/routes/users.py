from flask import Blueprint, jsonify, request
from app.services.user_service import get_all_users, get_user_by_id, create_new_user, update_user_by_id, delete_user_by_id
import datetime
import jwt
from app import mysql
from app.config import Config

users_bp = Blueprint('users', __name__)

# Ruta para el login
@users_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, email, password, role FROM users WHERE email = %s', (data['email'],))
    user = cursor.fetchone()
    cursor.close()

    if user is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Verificar si la contraseña ingresada coincide con la almacenada
    if user[2] != data['password']:  # Aquí solo comparamos texto plano
        return jsonify({'error': 'Contraseña incorrecta'}), 401

    # Si la contraseña es correcta, procedemos con la creación del JWT
    payload = {
        'user_id': user[0],
        'email': user[1],
        'role': user[3],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

    return jsonify({
        'message': 'Login exitoso',
        'token': token
    }), 200

# Ruta para obtener todos los usuarios
@users_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = get_all_users()
        users_list = [{
            'id': user[0],
            'email': user[1],
            'name': user[2],
            'role': user[3],
            'created_at': user[4].isoformat() if user[4] else None,
            'updated_at': user[5].isoformat() if user[5] else None
        } for user in users]
        return jsonify(users_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener un usuario por ID
@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = get_user_by_id(id)
        if user is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        return jsonify({
            'id': user[0],
            'email': user[1],
            'name': user[2],
            'role': user[3],
            'created_at': user[4].isoformat() if user[4] else None,
            'updated_at': user[5].isoformat() if user[5] else None
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear un nuevo usuario
@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Datos incompletos'}), 400

        email = data['email']
        password = data['password']
        # Puedes agregar más campos de usuario aquí si es necesario

        # Guardar el usuario en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (email, password, ...) VALUES (%s, %s, ...)', (email, password))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para actualizar un usuario por ID
@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No hay datos para actualizar'}), 400
        success = update_user_by_id(id, data)
        if not success:
            return jsonify({'error': 'Usuario no encontrado o sin cambios'}), 404
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para eliminar un usuario por ID
@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        success = delete_user_by_id(id)
        if not success:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
