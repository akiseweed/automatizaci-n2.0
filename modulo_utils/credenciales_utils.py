from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon


from PySide2 import QtCore, QtWidgets , QtGui
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QFileDialog, QMessageBox


def evento_menu(parent, parentRaiz, tr=200, imagen=None):
    width = parentRaiz.frame_menu.width()

    if width == 91:
        newWidth = 220
    else:
        newWidth = 91

    parent.animation = QtCore.QPropertyAnimation(parentRaiz.frame_menu, b"minimumWidth")
    parent.animation.setDuration(tr)
    parent.animation.setStartValue(width)
    parent.animation.setEndValue(newWidth)
    parent.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    parent.animation.start()

    if imagen:
        imagen.setScaledContents(True) 
        if newWidth == 91:
            imagen.setMaximumWidth(newWidth)  
            imagen.setMaximumHeight(140)  
        else:
            imagen.setMaximumHeight(140) 
            imagen.setMaximumWidth(170) 

    
def evento_hora(self):

    hora = QtCore.QTime.currentTime().toString("hh:mm:ss AP")
    
    self.venPri.lbl_hora.setText(hora)
    fecha = QtCore.QDate.currentDate()
    
    fecha_formateada = fecha.toString("dddd d 'de' MMMM  yyyy")
    
    self.venPri.lbl_fecha.setText(fecha_formateada.capitalize())

    
    self.venPri.hora = QtCore.QTimer(self)
    self.venPri.hora.setInterval(1000)
    self.venPri.hora.timeout.connect(lambda:Hora(self))
    self.venPri.hora.start()
    
def Hora(self):
    hora = QtCore.QTime.currentTime().toString("hh:mm:ss")
    self.venPri.lbl_hora.setText(hora)

def evento_pagina_mantenimiento(parent, index, boton):
    # Estilo deseado para el botón cuando se hace clic
    estilo_clic = """
        QPushButton {
            color: #445d5e;
            font-weight: bold;
            font-size: 14px;
            border-bottom: 2px solid #445d5e;
        }
    """

    # Establecer el estilo al botón
    boton.setStyleSheet(estilo_clic)

    # Restablecer el estilo de los otros botones si es necesario
    for btn in [parent.venPri.btn_menu_institucion, parent.venPri.btn_menu_proyectos]:
        if btn != boton:
            btn.setStyleSheet("")  # Establecer un estilo vacío o inicial si es necesario

    # Cambiar la página actual
    parent.venPri.stackedWidget_6.setCurrentIndex(index)


def evento_pagina(parent,index,boton):

    stylox="{color: white;background:#477aaa;border-top-left-radius:25px;border-bottom-left-radius: 25px}"

    # Despinta
    for btn in [parent.venPri.btn_home, parent.venPri.btn_usuario, parent.venPri.btn_credenciales]:    
        btn.setStyleSheet(btn.styleSheet().replace("#"+btn.objectName()+ stylox,""))

    # Pinta
    boton.setStyleSheet("#"+boton.objectName()+"{color: white;background:#477aaa;border-top-left-radius:25px;border-bottom-left-radius: 25px}")
    parent.venPri.stackedWidget.setCurrentIndex(index)


def evento_ocultar(tol_inv,tol_vis,line,dato):
    """ 
    Esta funcion recibe por parametro los toolbutton de visible y invisible 
    para mostrar y ocultar el campo contraseña
    """
    if dato == 1:
        tol_inv.hide(),tol_vis.show()
        line.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        tol_vis.hide();tol_inv.show()
        line.setEchoMode(QtWidgets.QLineEdit.Password)

def eventorol(parent,parent2):
    """Funcion recibe por parametro clase """
    
    
    parent.listaseleccion=[]
    if(parent2.admi.isChecked()):
        parent.listaseleccion.append(3)
    if(parent2.user.isChecked()):
        parent.listaseleccion.append(4)
        

def estilo(parent):
    estiloDefecto =QtWidgets.QStyleFactory.create('windowsvista')
    parent.venedit.bnt_ojoInv.setStyle(estiloDefecto)
    parent.venedit.bnt_ojoVis.setStyle(estiloDefecto)


def evento_tabla(parent):
    # Mostrar encabezados
    parent.venPri.tabla_credenciales.horizontalHeader().setVisible(True)
    parent.venPri.tabla_automatizar.horizontalHeader().setVisible(True)

    # Establecer modo de ajuste de tamaño de sección
    parent.venPri.tabla_credenciales.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) 
    parent.venPri.tabla_automatizar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) 




def crearbotoneslista(stilo,icono,tooltip):
    
    btn_nuevo = QtWidgets.QToolButton()
    btn_nuevo.setMinimumSize(QtCore.QSize(35, 25))
    btn_nuevo.setIconSize(QtCore.QSize(20, 20))
    btn_nuevo.setStyleSheet(stilo)
    btn_nuevo.setIcon(QtGui.QIcon(icono))
    btn_nuevo.setToolTip(tooltip)
    btn_nuevo.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    return btn_nuevo

def llenar_tabla_credenciales(parent, tabla, dato):
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(7)
   
        for fila in range(len(dato)):

            botonseleccionar = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #91cbcf; border-radius:8px}
                            QToolButton:hover{background-color:#82b5b9}""",
                icono = u':/icons/check.png',
                tooltip = 'Seleccionar')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botonseleccionar)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_seleccionar(botonseleccionar, fila, tabla, parent)

            tabla.setCellWidget(fila ,6,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)


    else:
        tabla.setRowCount(0) 
          

    

def btn_seleccionar(boton,fila,tabla,parent):

    boton.clicked.connect(lambda: tabla.selectRow(fila))              
    boton.clicked.connect(lambda: btn_seleccionar_accion(fila,parent)) 
    
def btn_seleccionar_accion(fila, parent):
    tabla_origen = parent.venPri.tabla_credenciales
    tabla_destino = parent.venPri.tabla_automatizar
    
    id_credencial = tabla_origen.item(fila, 0).text()

    id_credenciales_destino = [tabla_destino.item(i, 0).text() for i in range(tabla_destino.rowCount()) if tabla_destino.item(i, 0) is not None]

    if id_credencial not in id_credenciales_destino:
        tabla_destino.insertRow(tabla_destino.rowCount())

        for columna in range(tabla_origen.columnCount()):
            item = tabla_origen.item(fila, columna)
            if item is not None:
                tabla_destino.setItem(tabla_destino.rowCount() - 1, columna, item.clone())

        # Obtener los datos de la tabla de automatización para actualizarla
        datos_tabla_automatizacion = []
        for fila in range(tabla_destino.rowCount()):
            fila_datos = []
            for columna in range(tabla_destino.columnCount()):
                item = tabla_destino.item(fila, columna)
                if item is not None:
                    fila_datos.append(item.text())
                else:
                    fila_datos.append("")
            datos_tabla_automatizacion.append(fila_datos)

        # Llamar a llenar_tabla_automatizacion con los nuevos datos
        llenar_tabla_automatizacion(parent, tabla_destino, datos_tabla_automatizacion)
    else:
        QMessageBox.warning(parent, "Duplicado", "La credencial seleccionada ya existe en la tabla de automatización.")




def llenar_tabla_automatizacion(parent, tabla, dato):
    
    if dato:
        tabla.setRowCount(0)
        tabla.setRowCount(len(dato))
        tabla.setColumnCount(7)
   
        for fila in range(len(dato)):
            
            botoneliminar = crearbotoneslista(
                stilo = u"""QToolButton{background-color: #FBE9E9; border-radius:8px}
                            QToolButton:hover{background-color:#ebdada}""",
                icono = u':/icons/borrar.png',
                tooltip = 'eliminar de selección')

            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(1,1,1,1)
            layout.setSpacing(3)
            layout.addWidget(botoneliminar)

            widget = QtWidgets.QWidget()
            widget.setLayout(layout)

            btn_eliminar(botoneliminar, fila, tabla, parent)

            tabla.setCellWidget(fila ,6,widget)

            for columna in range(len(dato[fila])):
                item = QtWidgets.QTableWidgetItem(str(dato[fila][columna]))
                item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                tabla.setItem(fila, columna, item)
    else:
        tabla.setRowCount(0) 
        


def btn_eliminar(boton,fila,tabla,parent):
    
    boton.clicked.connect(lambda: tabla.selectRow(fila))              
    boton.clicked.connect(lambda: btn_eliminar_accion(fila,parent)) 
    
    
def btn_eliminar_accion(fila, parent):

    if parent.venPri.tabla_automatizar.item(fila, 0) is not None:
        id_credencial = parent.venPri.tabla_automatizar.item(fila, 0).text()
        tabla_destino = parent.venPri.tabla_automatizar
        for i in range(tabla_destino.rowCount()):
            if tabla_destino.item(i, 0) is not None and tabla_destino.item(i, 0).text() == id_credencial:
                tabla_destino.removeRow(i)
                break
