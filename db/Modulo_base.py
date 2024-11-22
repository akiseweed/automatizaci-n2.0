

from db.logger_base import logger
from db.cursor_del_pool import CursorDelPool


class BaseDatos:
    
    
    @classmethod
    def getDatos(cls,consulta):
        with CursorDelPool() as cursor:    
            cursor.execute(consulta)
            registros = cursor.fetchall()
            #logger.debug(f'Metodo getDatos:  return {registros}') 
            return registros
        
    @classmethod
    def getDatos_condicion(cls,consulta,dato):
        with CursorDelPool() as cursor:    
            cursor.execute(consulta, dato)
            registros = cursor.fetchall()
            #logger.debug(f'Metodo getDatos_condicion:  return {registros}') 
            return registros

    @classmethod
    def getDatosProcess(cls,consulta):
        with CursorDelPool() as cursor:
            cursor.callproc(consulta)
            results = [cursor.fetchall()]
            
            while cursor.nextset():
                results.append(cursor.fetchall())
            
            results = results[0:-1]
            #logger.debug(f'Metodo getDatosProcess:  return {results}')
            return results  

    @classmethod
    def getDatosProcess_condicion(cls,consulta,dato):
        with CursorDelPool() as cursor:    
            cursor.callproc(consulta, dato)
            results = [cursor.fetchall()]
            
            while cursor.nextset():
                results.append(cursor.fetchall())
            
            results = results[0:-1]
            #logger.debug(f'Metodo getDatosProcess_condicion:  return {results}')
            return results

    @classmethod
    def setDatos(cls, consulta,dato):
        with CursorDelPool() as cursor:
            #logger.debug(f'Metodo setDatos: consulta {consulta}')
            #logger.debug(f'Metodo setDatos: dato {dato}')
            cursor.execute(consulta, dato)
            
    @classmethod
    def setDatosProcess(cls, nomprocess, dato):
        with CursorDelPool() as cursor:
            #logger.debug(f'Metodo setDatosProcess: noombre proceso {nomprocess}')
            #logger.debug(f'Metodo setDatosProcess: dato {dato}')
            cursor.callproc(nomprocess, dato)

    @classmethod
    def setDatosListFor(cls, consulta,dato):
        with CursorDelPool() as cursor:
            #logger.debug(f'Metodo setDatosListFor: consulta {consulta}')
            #logger.debug(f'Metodo setDatosListFor: dato {dato}')
            cursor.executemany(consulta,dato)
                    
    @classmethod
    def updateDatos(cls, consulta,datos):
        with CursorDelPool() as cursor:
            #logger.debug(f'Metodo updateDatos: consulta {consulta}')
            #logger.debug(f'Metodo updateDatos: dato {datos}')
            cursor.execute(consulta, datos)
                
    @classmethod
    def deleteDatos(cls, consulta,dato):
        with CursorDelPool() as cursor:
            #logger.debug(f'Metodo deleteDatos: consulta {consulta}')
            #logger.debug(f'Metodo deleteDatos: dato {dato}')
            cursor.execute(consulta, dato)
            
 