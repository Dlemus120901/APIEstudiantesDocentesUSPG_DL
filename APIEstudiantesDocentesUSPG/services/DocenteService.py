from repositories.DocenteRepository import DocenteRepository
from mappers.DocenteMapper import DocenteMapper

class DocenteService:
    def __init__(self):
        self.repo = DocenteRepository()
        self.mapper = DocenteMapper()
    
    def listar(self):
        docentes = self.repo.obtenerTodos()
        # Convertir entidades a diccionarios usando el mapper
        return [self.mapper.to_dict(docente) for docente in docentes]
    
    def obtener(self, id):
        docente = self.repo.obtenerPorId(id)
        # Convertir entidad a diccionario usando el mapper
        return self.mapper.to_dict(docente)
    
    def crear(self, data):
        # Crear entidad desde los datos recibidos
        docente = self.mapper.to_entity(data)
        return self.repo.crear(docente)
    
    def actualizar(self, id, data):
        # Obtener el docente existente
        docente_existente = self.repo.obtenerPorId(id)
        if not docente_existente:
            return False
        
        # Actualizar los datos
        docente_existente.setNombres(data['nombres'])
        docente_existente.setApellidos(data['apellidos'])
        
        return self.repo.actualizar(docente_existente)
    
    def eliminar(self, id):
        return self.repo.eliminar(id)