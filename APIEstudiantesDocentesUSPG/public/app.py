from flask import Flask, request, jsonify
import sys
import os

# Agrega la carpeta raíz al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Verifica el nombre EXACTO de tu archivo y clase
from controllers.DocenteController import DocenteController
from controllers.EstudianteController import EstudianteController

app = Flask(__name__)

docente_controller = DocenteController()
estudiante_controller = EstudianteController()

@app.route('/docentes', methods=['GET', 'POST'])
@app.route('/docentes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_docentes(id=None):
    method = request.method
    data = request.get_json() if method in ['POST', 'PUT'] else None
    return jsonify(docente_controller.manejar(method, id, data))

@app.route('/estudiantes', methods=['GET', 'POST'])
@app.route('/estudiantes/<int:id>', methods=['GET', 'PUT', 'DELETE'])   
def manejar_estudiantes(id=None):
    method = request.method
    data = request.get_json() if method in ['POST', 'PUT'] else None
    return jsonify(estudiante_controller.manejar(method, id, data))

if __name__ == '__main__':
    app.run(debug=True)