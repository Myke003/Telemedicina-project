from flask import Flask
from flask_restful import Api
from app.routes import UserResource, AppointmentResource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Bienvenido a la API de TeleMed </h1>'

api.add_resource(UserResource, '/api/usuarios')  # Asegúrate de que comienza con /
api.add_resource(AppointmentResource, '/api/citas')  # Asegúrate de que comienza con /

if __name__ == '__main__':
    app.run(debug=True)
