from models.docente import Docente

class DocenteMapper:
    
    @staticmethod
    def to_entity(db_row):
        """Convierte una fila de la base de datos a una entidad Docente"""
        if not db_row:
            return None
            
        docente = Docente()
        docente.setId(db_row.get('id'))
        docente.setNombres(db_row.get('nombres'))
        docente.setApellidos(db_row.get('apellidos'))
        return docente
    
    @staticmethod
    def to_dict(docente):
        """Convierte una entidad Docente a un diccionario"""
        if not docente:
            return None
            
        return {
            'id': docente.getId(),
            'nombres': docente.getNombres(),
            'apellidos': docente.getApellidos()
        }
    
    @staticmethod
    def to_database(docente):
        """Convierte una entidad Docente a formato para base de datos"""
        if not docente:
            return None
            
        return {
            'nombres': docente.getNombres(),
            'apellidos': docente.getApellidos()
        }