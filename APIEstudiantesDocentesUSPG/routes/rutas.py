from flask import Flask, request, jsonify
from controllers.DocenteController import DocenteController
from controllers.EstudianteController import EstudianteController

app = Flask(__name__)

@app.route('/docentes', methods=['GET', 'POST'])
@app.route('/docentes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_docentes(id=None):
    controller = DocenteController()
    data = request.get_json() if request.method in ['POST', 'PUT'] else None
    return jsonify(controller.manejar(request.method, id, data))

@app.route('/estudiantes', methods=['GET', 'POST'])
@app.route('/estudiantes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_estudiantes(id=None):
    controller = EstudianteController()
    data = request.get_json() if request.method in ['POST', 'PUT'] else None
    return jsonify(controller.manejar(request.method, id, data))

@app.errorhandler(404)
def ruta_no_encontrada(error):
    return jsonify({"error": "Ruta no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)