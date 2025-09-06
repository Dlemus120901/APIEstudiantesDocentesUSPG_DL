from services.EstudianteService import EstudianteService

class EstudianteController:
    def __init__(self):
        self.service = EstudianteService()
    
    def manejar(self, method, id=None, data=None):
        if method == 'GET':
            if id is None:
                return self.service.listar()  # Obtener todos los estudiantes
            else:
                return self.service.obtener(id)  # Obtener un estudiante específico
        elif method == 'POST':
            return {"exito": self.service.crear(data)}
        elif method == 'PUT':
            if id is None:
                return {"error": "Se requiere ID para actualizar"}
            return {"exito": self.service.actualizar(id, data)}
        elif method == 'DELETE':
            if id is None:
                return {"error": "Se requiere ID para eliminar"}
            return {"exito": self.service.eliminar(id)}