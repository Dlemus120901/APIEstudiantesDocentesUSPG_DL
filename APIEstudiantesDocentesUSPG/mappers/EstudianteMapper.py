from models.estudiante import Estudiante

class EstudianteMapper:
    
    @staticmethod
    def to_entity(db_row):
        """Convierte una fila de la base de datos a una entidad Estudiante"""
        if not db_row:
            return None
            
        estudiante = Estudiante()
        estudiante.setId(db_row.get('id'))
        estudiante.setNombres(db_row.get('nombres'))
        estudiante.setApellidos(db_row.get('apellidos'))
        return estudiante
    
    @staticmethod
    def to_dict(estudiante):
        """Convierte una entidad Estudiante a un diccionario"""
        if not estudiante:
            return None
            
        return {
            'id': estudiante.getId(),
            'nombres': estudiante.getNombres(),
            'apellidos': estudiante.getApellidos()
        }
    
    @staticmethod
    def to_database(estudiante):
        """Convierte una entidad Estudiante a formato para base de datos"""
        if not estudiante:
            return None
            
        return {
            'nombres': estudiante.getNombres(),
            'apellidos': estudiante.getApellidos()
        }