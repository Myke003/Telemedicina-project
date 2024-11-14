# app/__init__.py

from flask import Flask, make_response, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from .config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)
    
    # Inicializar MySQL
    mysql.init_app(app)
    
    # Habilitar CORS
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

    # Manejador para solicitudes OPTIONS (para evitar bloqueo CORS)
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = make_response()
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type"
            return response
    
    # Registrar rutas
    from .routes.users import users_bp
    app.register_blueprint(users_bp)
    
    return app
