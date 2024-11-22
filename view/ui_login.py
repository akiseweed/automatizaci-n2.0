# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginnfgsLZG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from view.image import source

class Ui_ventana_sesion(object):
    def setupUi(self, ventana_sesion):
        if not ventana_sesion.objectName():
            ventana_sesion.setObjectName(u"ventana_sesion")
        ventana_sesion.resize(362, 527)
        ventana_sesion.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(ventana_sesion)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(ventana_sesion)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{border:1px solid white;\n"
"background-color: #ffffff;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 33))
        self.frame.setMaximumSize(QSize(16777215, 33))
        self.frame.setStyleSheet(u"#frame{background:#ffffff;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_close = QToolButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(328, 2, 29, 29))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"#btn_close{\n"
"font-family: Roboto;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"background-color: #dfdfe3;\n"
"color: #6B7280;\n"
"border-radius:11px\n"
"}\n"
"\n"
"\n"
"\n"
"#btn_close:hover{background:#ce4d3a ;\n"
"border-radius:11px; }\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(12, 12))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{border:1px solid white;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QLabel{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #6B7280;\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"border: 2px solid #F3F4F6;\n"
"border-radius: 8px;\n"
"color:#9CA3AF;\n"
"padding:10px}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #477aaa;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"#stackedWidget{\n"
"border:1px solid white;\n"
"background-color: #ffffff;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px}")
        self.pag_inicio = QWidget()
        self.pag_inicio.setObjectName(u"pag_inicio")
        self.pag_inicio.setStyleSheet(u"#pag_inicio{background-color: #ffffff;\n"
"border:1px solid white;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px}\n"
"")
        self.txtUsuario = QLineEdit(self.pag_inicio)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(30, 190, 296, 40))
        self.txtUsuario.setStyleSheet(u"")
        self.txtUsuario.setMaxLength(100)
        self.label_Psicologa = QLabel(self.pag_inicio)
        self.label_Psicologa.setObjectName(u"label_Psicologa")
        self.label_Psicologa.setGeometry(QRect(30, 160, 121, 25))
        self.label_Psicologa.setStyleSheet(u"")
        self.frame_5 = QFrame(self.pag_inicio)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(28, 280, 296, 40))
        self.frame_5.setStyleSheet(u"#frame_5{background-color:#f3f4f6;\n"
"border-radius:8px}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(30, 30))
        self.frame_7.setStyleSheet(u"#frame_7{border:0px solid transparent}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.tol_invsible = QToolButton(self.frame_7)
        self.tol_invsible.setObjectName(u"tol_invsible")
        self.tol_invsible.setEnabled(True)
        self.tol_invsible.setGeometry(QRect(0, 5, 30, 30))
        self.tol_invsible.setMinimumSize(QSize(3, 0))
        self.tol_invsible.setCursor(QCursor(Qt.PointingHandCursor))
        self.tol_invsible.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/invisible.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tol_invsible.setIcon(icon1)
        self.tol_invsible.setIconSize(QSize(20, 20))
        self.tol_invsible.setCheckable(False)
        self.tol_invsible.setAutoRaise(True)
        self.tol_visible = QToolButton(self.frame_7)
        self.tol_visible.setObjectName(u"tol_visible")
        self.tol_visible.setEnabled(True)
        self.tol_visible.setGeometry(QRect(0, 4, 30, 30))
        self.tol_visible.setCursor(QCursor(Qt.PointingHandCursor))
        self.tol_visible.setMouseTracking(False)
        self.tol_visible.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/visible.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tol_visible.setIcon(icon2)
        self.tol_visible.setIconSize(QSize(20, 20))
        self.tol_visible.setAutoRaise(True)

        self.gridLayout_4.addWidget(self.frame_7, 0, 1, 1, 1)

        self.txtContrasena = QLineEdit(self.frame_5)
        self.txtContrasena.setObjectName(u"txtContrasena")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtContrasena.sizePolicy().hasHeightForWidth())
        self.txtContrasena.setSizePolicy(sizePolicy)
        self.txtContrasena.setStyleSheet(u"")
        self.txtContrasena.setMaxLength(50)
        self.txtContrasena.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.txtContrasena, 0, 0, 1, 1)

        self.label_contrasea = QLabel(self.pag_inicio)
        self.label_contrasea.setObjectName(u"label_contrasea")
        self.label_contrasea.setGeometry(QRect(30, 250, 111, 25))
        self.label_contrasea.setStyleSheet(u"")
        self.btn_aceptar = QToolButton(self.pag_inicio)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(30, 340, 296, 40))
        self.btn_aceptar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_aceptar.setFocusPolicy(Qt.NoFocus)
        self.btn_aceptar.setStyleSheet(u"QToolButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #477aaa;\n"
"border-radius: 4px;}\n"
"\n"
"QToolButton:hover{background: #365d81;\n"
"border-radius: 4px; }")
        self.btn_aceptar.setIconSize(QSize(20, 20))
        self.btn_aceptar.setAutoRaise(True)
        self.label = QLabel(self.pag_inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 211, 151))
        self.label.setPixmap(QPixmap(u":/icons/logooooo.png"))
        self.label.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_inicio)
        self.pag_recuperar = QWidget()
        self.pag_recuperar.setObjectName(u"pag_recuperar")
        self.pag_recuperar.setStyleSheet(u"#pag_recuperar{\n"
"border:1px solid white;\n"
"background-color: #ffffff;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;}\n"
"")
        self.btn_cancelarr = QToolButton(self.pag_recuperar)
        self.btn_cancelarr.setObjectName(u"btn_cancelarr")
        self.btn_cancelarr.setGeometry(QRect(32, 390, 296, 40))
        self.btn_cancelarr.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelarr.setFocusPolicy(Qt.NoFocus)
        self.btn_cancelarr.setStyleSheet(u"#btn_cancelarr{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:#374151;\n"
"padding:8px;\n"
"background: #F9FAFB;\n"
"border-radius: 8px;\n"
"border: 1px solid #E5E7EB;\n"
"}\n"
"\n"
"#btn_cancelarr:hover{background: #F3F4F6;\n"
"border: 1px solid #E5E7EB }\n"
"\n"
"")
        self.btn_cancelarr.setIconSize(QSize(20, 20))
        self.btn_enviar = QToolButton(self.pag_recuperar)
        self.btn_enviar.setObjectName(u"btn_enviar")
        self.btn_enviar.setGeometry(QRect(33, 340, 296, 40))
        self.btn_enviar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar.setFocusPolicy(Qt.NoFocus)
        self.btn_enviar.setStyleSheet(u"QToolButton{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"letter-spacing: 0.02em;\n"
"color:white;\n"
"padding:8px;\n"
"background: #477aaa;\n"
"border-radius: 4px;}\n"
"\n"
"QToolButton:hover{background: #365d81;\n"
"border-radius: 4px; }")
        self.btn_enviar.setIconSize(QSize(20, 20))
        self.label_contrasea_2 = QLabel(self.pag_recuperar)
        self.label_contrasea_2.setObjectName(u"label_contrasea_2")
        self.label_contrasea_2.setGeometry(QRect(34, 190, 171, 25))
        self.label_contrasea_2.setStyleSheet(u"")
        self.line_mensaje = QLabel(self.pag_recuperar)
        self.line_mensaje.setObjectName(u"line_mensaje")
        self.line_mensaje.setGeometry(QRect(33, 260, 241, 41))
        self.line_mensaje.setStyleSheet(u"background-color: transparent;\n"
"color:#0d73b1;\n"
"font-size:14px;")
        self.line_mensaje.setWordWrap(True)
        self.line_email2 = QLineEdit(self.pag_recuperar)
        self.line_email2.setObjectName(u"line_email2")
        self.line_email2.setGeometry(QRect(32, 220, 296, 40))
        self.line_email2.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: #F3F4F6;\n"
"border: 2px solid #F3F4F6;\n"
"border-radius: 8px;\n"
"color:#9CA3AF;\n"
"padding:10px}\n"
"\n"
"QLineEdit::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #3A4F50;\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.line_email2.setMaxLength(100)
        self.label_recuperar = QLabel(self.pag_recuperar)
        self.label_recuperar.setObjectName(u"label_recuperar")
        self.label_recuperar.setGeometry(QRect(60, 10, 291, 25))
        self.label_recuperar.setStyleSheet(u"#label_recuperar{font-size:22px;\n"
"font-family:Roboto\n"
"}")
        self.label_2 = QLabel(self.pag_recuperar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 40, 211, 151))
        self.label_2.setPixmap(QPixmap(u":/menu/logooooo.png"))
        self.label_2.setScaledContents(True)
        self.stackedWidget.addWidget(self.pag_recuperar)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(ventana_sesion)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ventana_sesion)
    # setupUi

    def retranslateUi(self, ventana_sesion):
        ventana_sesion.setWindowTitle(QCoreApplication.translate("ventana_sesion", u"Login", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("ventana_sesion", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText(QCoreApplication.translate("ventana_sesion", u"...", None))
        self.txtUsuario.setInputMask("")
        self.txtUsuario.setText("")
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("ventana_sesion", u"Ingrese correo", None))
        self.label_Psicologa.setText(QCoreApplication.translate("ventana_sesion", u"Username*", None))
        self.tol_invsible.setText("")
#if QT_CONFIG(shortcut)
        self.tol_invsible.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.tol_visible.setText("")
        self.txtContrasena.setInputMask("")
        self.txtContrasena.setText("")
        self.txtContrasena.setPlaceholderText(QCoreApplication.translate("ventana_sesion", u"Ingresar contrase\u00f1a", None))
        self.label_contrasea.setText(QCoreApplication.translate("ventana_sesion", u"Contrase\u00f1a*", None))
        self.btn_aceptar.setText(QCoreApplication.translate("ventana_sesion", u" Ingresar", None))
        self.label.setText("")
        self.btn_cancelarr.setText(QCoreApplication.translate("ventana_sesion", u"Cancelar", None))
        self.btn_enviar.setText(QCoreApplication.translate("ventana_sesion", u" Enviar", None))
        self.label_contrasea_2.setText(QCoreApplication.translate("ventana_sesion", u"Ingrese su correo*", None))
        self.line_mensaje.setText(QCoreApplication.translate("ventana_sesion", u"Despu\u00e9s del proceso revise su bandeja de entrada.", None))
        self.line_email2.setInputMask("")
        self.line_email2.setText("")
        self.line_email2.setPlaceholderText(QCoreApplication.translate("ventana_sesion", u"demo@gmail.com", None))
        self.label_recuperar.setText(QCoreApplication.translate("ventana_sesion", u"Recuperar Contrase\u00f1a", None))
        self.label_2.setText("")
    # retranslateUi

