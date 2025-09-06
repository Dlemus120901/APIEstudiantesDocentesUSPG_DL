from connection.bd import ConexionBD
from mappers.EstudianteMapper import EstudianteMapper

class EstudianteRepository:
    def __init__(self):
        db = ConexionBD()
        self.conexion = db.getConexion()
        self.mapper = EstudianteMapper()
    
    def obtenerTodos(self):
        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes")
        db_rows = cursor.fetchall()
        cursor.close()
        
        # Convertir filas de BD a entidades usando el mapper
        return [self.mapper.to_entity(row) for row in db_rows]
    
    def obtenerPorId(self, id):
        cursor = self.conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
        db_row = cursor.fetchone()
        cursor.close()
        
        # Convertir fila de BD a entidad usando el mapper
        return self.mapper.to_entity(db_row)
    
    def crear(self, estudiante):
        cursor = self.conexion.cursor()
        
        # Convertir entidad a formato de BD usando el mapper
        data = self.mapper.to_database(estudiante)
        
        cursor.execute("INSERT INTO estudiantes (nombres, apellidos) VALUES (%s, %s)", 
                      (data['nombres'], data['apellidos']))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        
        if exito:
            estudiante.setId(cursor.lastrowid)
        
        cursor.close()
        return exito
    
    def actualizar(self, estudiante):
        cursor = self.conexion.cursor()
        
        # Convertir entidad a formato de BD usando el mapper
        data = self.mapper.to_database(estudiante)
        
        cursor.execute("UPDATE estudiantes SET nombres=%s, apellidos=%s WHERE id=%s", 
                      (data['nombres'], data['apellidos'], estudiante.getId()))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        cursor.close()
        return exito
    
    def eliminar(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
        self.conexion.commit()
        exito = cursor.rowcount > 0
        cursor.close()
        return exito