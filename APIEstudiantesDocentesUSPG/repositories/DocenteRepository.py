from connection.bd import ConexionBD
from mappers.DocenteMapper import DocenteMapper

class DocenteRepository:
    def __init__(self):
        db = ConexionBD()
        self.conexion = db.getConexion()
        self.mapper = DocenteMapper()
    
    def obtenerTodos(self):
        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM docentes")
        db_rows = cursor.fetchall()
        cursor.close()
        
        # Convertir filas de BD a entidades usando el mapper
        return [self.mapper.to_entity(row) for row in db_rows]
    
    def obtenerPorId(self, id):
        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM docentes WHERE id = %s", (id,))
        db_row = cursor.fetchone()
        cursor.close()
        
        # Convertir fila de BD a entidad usando el mapper
        return self.mapper.to_entity(db_row)
    
    def crear(self, docente):
        cursor = self.conexion.cursor()
        
        # Convertir entidad a formato de BD usando el mapper
        data = self.mapper.to_database(docente)
        
        cursor.execute("INSERT INTO docentes (nombres, apellidos) VALUES (%s, %s)", 
                      (data['nombres'], data['apellidos']))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        
        if exito:
            docente.setId(cursor.lastrowid)
        
        cursor.close()
        return exito
    
    def actualizar(self, docente):
        cursor = self.conexion.cursor()
        
        # Convertir entidad a formato de BD usando el mapper
        data = self.mapper.to_database(docente)
        
        cursor.execute("UPDATE docentes SET nombres=%s, apellidos=%s WHERE id=%s", 
                      (data['nombres'], data['apellidos'], docente.getId()))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        cursor.close()
        return exito
    
    def eliminar(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM docentes WHERE id=%s", (id,))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        cursor.close()
        return exito