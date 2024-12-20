from db.conexion import Conexion
from db.logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #inicio de with
    def __enter__(self):
        #logger.debug('Inicio de with método __enter__')
    
        self.__conn = Conexion.obtenerConexion()
        self.__conn.ping(True)
        self.__cursor = self.__conn.cursor()

        return self.__cursor


    #fin del bloque with
    def __exit__(self, exception_type, exception_value, exception_traceback):
        #logger.debug('Se ejecuta método __exit__()')
        
        #if exception_value is not None:
        if exception_value:
            self.__conn.rollback()  
            logger.debug(f'Ocurrió una excepción: {exception_value}')  
        else:
            self.__conn.commit() 
            #logger.debug('Commit de la transacción')

        #Cerramos el cursor
        self.__cursor.close()    
        #Regresar la conexión al pool
        Conexion.liberarConexion(self.__conn) # regresa
        

                    
 
             
    
    