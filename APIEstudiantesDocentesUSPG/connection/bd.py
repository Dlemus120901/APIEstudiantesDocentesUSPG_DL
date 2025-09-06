import mysql.connector
from mysql.connector import Error, pooling

class ConexionBD:
    def __init__(self):
        self.host = "b47020davemzha0z8srb-mysql.services.clever-cloud.com"
        self.usuario = "usxu9ggxf0ckw1sr"
        self.clave = "umxF8MErMb0Ci375f79b"
        self.bd = "b47020davemzha0z8srb"  
        self.pool = None
        
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name="db_pool",
                pool_size=1,
                pool_reset_session=True,
                host=self.host,
                user=self.usuario,
                password=self.clave,
                database=self.bd
            )
                
        except Error as e:
            raise Exception(f"Error de conexión a la base de datos: {e}")
    
    def getConexion(self):  
        return self.pool.get_connection()