from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox


# importado desde views 
from controllers.data import obtenerData
from controllers.modulo_principal.principal import Principal
from controllers.modulo_utils.credenciales_utils import evento_ocultar
from controllers.modulo_utils.utils import estilos_login, limpiar_login
from db.Modulo_base import BaseDatos
from view.ui_login import Ui_ventana_sesion



class Login(QtWidgets.QDialog):
    
    def __init__(self):

        super(Login, self).__init__()

        self.venLogin = Ui_ventana_sesion()
        self.venLogin.setupUi(self)
        self.base = BaseDatos()
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        estilos_login(self)
        
        self.venLogin.btn_aceptar.keyPressEvent = self.keyPressEvent

        self.venLogin.btn_close.clicked.connect(lambda: self.close())
        self.venLogin.tol_visible.hide()
        self.venLogin.tol_invsible.clicked.connect(lambda: evento_ocultar(
                    self.venLogin.tol_invsible,self.venLogin.tol_visible,self.venLogin.txtContrasena,1))
        self.venLogin.tol_visible.clicked.connect(lambda: evento_ocultar(
                    self.venLogin.tol_invsible,self.venLogin.tol_visible,self.venLogin.txtContrasena,2))
        
        self.venLogin.btn_aceptar.clicked.connect(lambda: self.logearse())

        
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        
    def logearse(self):
        
        username = self.venLogin.txtUsuario.text()
        contrasena = self.venLogin.txtContrasena.text()
        
        
        consulta = """
            SELECT usuario.*, rol.descripcion AS nombre_rol 
            FROM usuario 
            JOIN rol ON usuario.rol_id = rol.id 
            WHERE username = %s AND contrasena = %s
        """

        resultado = self.base.getDatos_condicion(consulta, [username, contrasena])
        
        if resultado:
            self.hide()
            QMessageBox.information(self, "Login existoso", "Bienvenido usuario: "+ resultado[0][1])
            self.main = Principal(resultado[0][1], resultado[0][0], self)
            self.main.show()
        else:
            QMessageBox.warning(self, "Inicio de sesión fallido", "Credenciales inválidas. Por favor, inténtelo de nuevo.")


