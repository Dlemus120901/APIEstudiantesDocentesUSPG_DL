from services.DocenteService import DocenteService

class DocenteController:
    def __init__(self):
        self.service = DocenteService()
    
    def manejar(self, method, id=None, data=None):
        if method == 'GET':
            if id is None:
                return self.service.listar()  # Obtener todos los docentes
            else:
                return self.service.obtener(id)  # Obtener un docente específico
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