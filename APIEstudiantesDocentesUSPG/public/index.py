# Punto de entrada al sistema
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manejar_rutas(path):
    # Aquí se incluiría la lógica de enrutamiento
    # similar a require_once __DIR__ . '/../routes/rutas.php';
    return jsonify({"error": "Endpoint no encontrado"}), 404

if __name__ == '__main__':
    app.run()