from repositories.EstudianteRepository import EstudianteRepository
from mappers.EstudianteMapper import EstudianteMapper

class EstudianteService:
    def __init__(self):
        self.repo = EstudianteRepository()
        self.mapper = EstudianteMapper()
    
    def listar(self):
        estudiantes = self.repo.obtenerTodos()
        # Convertir entidades a diccionarios usando el mapper
        return [self.mapper.to_dict(estudiante) for estudiante in estudiantes]
    
    def obtener(self, id):
        estudiante = self.repo.obtenerPorId(id)
        # Convertir entidad a diccionario usando el mapper
        return self.mapper.to_dict(estudiante)
    
    def crear(self, data):
        # Crear entidad desde los datos recibidos
        estudiante = self.mapper.to_entity(data)
        return self.repo.crear(estudiante)
    
    def actualizar(self, id, data):
        # Obtener el estudiante existente
        estudiante_existente = self.repo.obtenerPorId(id)
        if not estudiante_existente:
            return False
        
        # Actualizar los datos
        estudiante_existente.setNombres(data['nombres'])
        estudiante_existente.setApellidos(data['apellidos'])
        
        return self.repo.actualizar(estudiante_existente)
    
    def eliminar(self, id):
        return self.repo.eliminar(id)