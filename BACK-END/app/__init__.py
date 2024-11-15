from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from .config import Config

mysql = MySQL()
def create_app():
    app = Flask(__name__)
    CORS(app,  resources={r"/*": {"origins": "http://localhost:5173"}})

    #CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route('/login', methods=['OPTIONS'])
    def options_login():
        response = app.make_response('')
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        return response

    # Cargar configuración
    app.config.from_object(Config)
    
    # Inicializar MySQL
    mysql.init_app(app)

    # Registrar rutas
    from .routes.users import users_bp
    from .routes.auth import auth_bp
    from .routes.appointment_routes import appointment_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(appointment_bp)

    return app
