from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

# Simulando una base de datos de usuarios (puedes integrar con MySQL)
users_db = {
    "usuario@ejemplo.com": {
        "password": "hashed_password",  # Aquí deberías almacenar el hash de la contraseña real
        "role": "admin"  # Ejemplo de un rol
    }
}

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = users_db.get(email)

    if user and check_password_hash(user['password'], password):  # Verifica el hash de la contraseña
        # Si las credenciales son correctas, generamos un JWT
        token = jwt.encode({
            'sub': email,
            'role': user['role'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, 'mi_clave_secreta', algorithm='HS256')  # Usa tu propia clave secreta aquí

        return jsonify({'token': token})

    return jsonify({'message': 'Correo o contraseña incorrectos'}), 401
