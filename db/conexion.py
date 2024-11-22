from db.logger_base import logger
from pymysqlpool.pool import Pool
import pymysql

import sys


conn = 0

class Conexion:
    
    
    __MINISIZE = 1
    __MAXISIZE = 5
    __DATABASE = 'credencialesdb'
    __USERNAME = 'root' 
    __PASSWORD = '' 
    __DB_PORT = 3306
    __HOST = 'localhost'
    __pool = None
    
   
    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = Pool(host=cls.__HOST,
                                  port=cls.__DB_PORT,
                                  user=cls.__USERNAME,
                                  password=cls.__PASSWORD,
                                  db=cls.__DATABASE,
                                  min_size=cls.__MINISIZE,
                                  max_size=cls.__MAXISIZE,
                                  cursorclass=pymysql.cursors.Cursor
                                  )

                return cls.__pool
            except Exception as e:
                sys.exit()

        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_conn()
        return conexion


    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().release(conexion)


    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().destroy()

