from app import create_app
from flask import jsonify

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'mensaje': 'Bienvenido a la API de Telemed'
    })

if __name__ == '__main__':
    app.run(debug=True)
