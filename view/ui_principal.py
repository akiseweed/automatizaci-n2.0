# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principalxfNiPL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from view.image import source

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(600, 700))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/login.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: #dadada ;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(29, 85))
        self.groupBox_3.setMaximumSize(QSize(16777215, 85))
        self.groupBox_3.setStyleSheet(u"#groupBox_3{\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"border: 1px solid #d6d7d8;\n"
"border-radius: 8px;\n"
"background-color:#f3f3f3 ;\n"
"color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cbo_tipo = QComboBox(self.groupBox_3)
        self.cbo_tipo.addItem("")
        self.cbo_tipo.addItem("")
        self.cbo_tipo.addItem("")
        self.cbo_tipo.setObjectName(u"cbo_tipo")
        self.cbo_tipo.setMinimumSize(QSize(200, 40))
        self.cbo_tipo.setStyleSheet(u"\n"
"QComboBox{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: white;\n"
"color:#9CA3AF;\n"
"border-radius:8px;\n"
"padding:10px;\n"
"combobox-popup: 0;\n"
"border: 2px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"	padding: 10px 10px 10px 20px;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color:#9CA3AF;\n"
"	font-size:14px;\n"
"	background-color: #F3F4F6;\n"
"	selection-background-color:#477aaa;\n"
"	selection-color:#ffffff;\n"
"	outline: 0px;\n"
" border-radius:4px;\n"
"   border: 1px solid #477aaa;\n"
"padding:10px\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/icons/contraerabajo.png);\n"
"     width: 11px;\n"
"     height: 11px;\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"background: #FFFFFF;\n"
"border: 2px solid #477aaa;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.cbo_tipo, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.line_busqueda = QLineEdit(self.groupBox_3)
        self.line_busqueda.setObjectName(u"line_busqueda")
        self.line_busqueda.setMinimumSize(QSize(0, 40))
        self.line_busqueda.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"letter-spacing: 0.02em;\n"
"background: white;\n"
"border: 3px solid white;\n"
"border-radius: 8px;\n"
"color:#9CA3AF;\n"
"padding:10px}\n"
"\n"
"\n"
"QLineEdit::hover{\n"
"background: #FFFFFF;\n"
"border: 2px solid #477aaa;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.line_busqueda, 0, 1, 1, 1)

        self.btn_export = QPushButton(self.groupBox_3)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setMinimumSize(QSize(143, 40))
        self.btn_export.setMaximumSize(QSize(158, 37))
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white; /* Color de texto blanco */\n"
"    padding: 8px 16px; /* Aumenta el espacio de relleno horizontal */\n"
"    background-color: #28a745; /* Fondo verde */\n"
"    border: 2px solid #28a745; /* Borde verde */\n"
"    border-radius: 10px;\n"
"    transition: color 0.3s, background-color 0.3s, transform 0.3s; /* Agrega transiciones suaves */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(40, 167, 69, 0.6); /* Fondo verde claro al pasar el rat\u00f3n */\n"
"    color: white; /* Cambia el color del texto a blanco */\n"
"    transform: scale(1.05); /* Escala el bot\u00f3n al 105% del tama\u00f1o original */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/exportar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export.setIcon(icon1)

        self.gridLayout_4.addWidget(self.btn_export, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"background-color: #f3f3f3;\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"border: 1px solid #d6d7d8;\n"
"border-radius: 8px;\n"
"color: #000000;\n"
"padding: 2px\n"
"}")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"#scrollArea{\n"
"	background-color: #f3f3f3;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 957, 756))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents{\n"
"	background-color: #f3f3f3;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbl_titulo01 = QLabel(self.scrollAreaWidgetContents)
        self.lbl_titulo01.setObjectName(u"lbl_titulo01")
        self.lbl_titulo01.setMinimumSize(QSize(0, 28))
        self.lbl_titulo01.setMaximumSize(QSize(16777215, 33))
        self.lbl_titulo01.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #000000;")

        self.gridLayout_5.addWidget(self.lbl_titulo01, 0, 0, 1, 4)

        self.lbl_titulo02 = QLabel(self.scrollAreaWidgetContents)
        self.lbl_titulo02.setObjectName(u"lbl_titulo02")
        self.lbl_titulo02.setMinimumSize(QSize(0, 35))
        self.lbl_titulo02.setMaximumSize(QSize(16777215, 35))
        self.lbl_titulo02.setStyleSheet(u"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"letter-spacing: 0.02em;\n"
"color: #000000;")

        self.gridLayout_5.addWidget(self.lbl_titulo02, 3, 0, 1, 4)

        self.tabla_credenciales = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tabla_credenciales.columnCount() < 7):
            self.tabla_credenciales.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_credenciales.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_credenciales.setObjectName(u"tabla_credenciales")
        self.tabla_credenciales.setMinimumSize(QSize(0, 286))
        self.tabla_credenciales.setMaximumSize(QSize(16777215, 16777215))
        self.tabla_credenciales.setAutoFillBackground(False)
        self.tabla_credenciales.setStyleSheet(u"QTableWidget {\n"
"outline: 0px;\n"
"border:5px solid #3f83be;\n"
"border-radius: 15px;\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"\n"
"/* cabezera*/\n"
"QHeaderView::section {\n"
"background-color:#3f83be;\n"
"border-style: none;\n"
"height:40px;\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget::disabled{\n"
"    background-color:#acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;}\n"
"\n"
"/*bordes internos*/\n"
"QTableWidget"
                        "::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #3f83be\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabla_credenciales.setFrameShape(QFrame.NoFrame)
        self.tabla_credenciales.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_credenciales.setAutoScroll(True)
        self.tabla_credenciales.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_credenciales.setAlternatingRowColors(False)
        self.tabla_credenciales.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_credenciales.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_credenciales.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tabla_credenciales.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_credenciales.setShowGrid(False)
        self.tabla_credenciales.setSortingEnabled(False)
        self.tabla_credenciales.setWordWrap(True)
        self.tabla_credenciales.setCornerButtonEnabled(False)
        self.tabla_credenciales.horizontalHeader().setVisible(True)
        self.tabla_credenciales.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_credenciales.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_credenciales.horizontalHeader().setDefaultSectionSize(137)
        self.tabla_credenciales.horizontalHeader().setHighlightSections(False)
        self.tabla_credenciales.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_credenciales.horizontalHeader().setStretchLastSection(False)
        self.tabla_credenciales.verticalHeader().setVisible(False)
        self.tabla_credenciales.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_credenciales.verticalHeader().setMinimumSectionSize(23)
        self.tabla_credenciales.verticalHeader().setDefaultSectionSize(47)
        self.tabla_credenciales.verticalHeader().setHighlightSections(True)
        self.tabla_credenciales.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_credenciales.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tabla_credenciales, 1, 0, 1, 4)

        self.tabla_automatizar = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tabla_automatizar.columnCount() < 7):
            self.tabla_automatizar.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_automatizar.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tabla_automatizar.setObjectName(u"tabla_automatizar")
        self.tabla_automatizar.setMinimumSize(QSize(0, 285))
        self.tabla_automatizar.setMaximumSize(QSize(16777215, 16777215))
        self.tabla_automatizar.setAutoFillBackground(False)
        self.tabla_automatizar.setStyleSheet(u"QTableWidget {\n"
"outline: 0px;\n"
"border:5px solid #3f83be;\n"
"border-radius: 15px;\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 19px;\n"
"letter-spacing: 0.02em;\n"
"color: #2c3d3e;\n"
"}\n"
"\n"
"\n"
"/* cabezera*/\n"
"QHeaderView::section {\n"
"background-color:#3f83be;\n"
"border-style: none;\n"
"height:40px;\n"
"font-family: \"Roboto\";\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 13px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal{\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"letter-spacing: 0.04em;\n"
"text-transform: uppercase;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget::disabled{\n"
"    background-color:#acacac;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;}\n"
"\n"
"/*bordes internos*/\n"
"QTableWidget"
                        "::item {\n"
"	border-bottom: 3px solid #f3f4f6;\n"
"\n"
"}\n"
"\n"
"QTableWidget:item:selected{\n"
"	background:white;/*color-seleccion*/\n"
"color: #3f83be\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabla_automatizar.setFrameShape(QFrame.NoFrame)
        self.tabla_automatizar.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_automatizar.setAutoScroll(True)
        self.tabla_automatizar.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_automatizar.setAlternatingRowColors(False)
        self.tabla_automatizar.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_automatizar.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_automatizar.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tabla_automatizar.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabla_automatizar.setShowGrid(False)
        self.tabla_automatizar.setSortingEnabled(False)
        self.tabla_automatizar.setWordWrap(True)
        self.tabla_automatizar.setCornerButtonEnabled(False)
        self.tabla_automatizar.horizontalHeader().setVisible(True)
        self.tabla_automatizar.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_automatizar.horizontalHeader().setMinimumSectionSize(38)
        self.tabla_automatizar.horizontalHeader().setDefaultSectionSize(137)
        self.tabla_automatizar.horizontalHeader().setHighlightSections(False)
        self.tabla_automatizar.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_automatizar.horizontalHeader().setStretchLastSection(False)
        self.tabla_automatizar.verticalHeader().setVisible(False)
        self.tabla_automatizar.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_automatizar.verticalHeader().setMinimumSectionSize(23)
        self.tabla_automatizar.verticalHeader().setDefaultSectionSize(47)
        self.tabla_automatizar.verticalHeader().setHighlightSections(True)
        self.tabla_automatizar.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_automatizar.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tabla_automatizar, 6, 0, 1, 4)

        self.btn_finalizar = QPushButton(self.scrollAreaWidgetContents)
        self.btn_finalizar.setObjectName(u"btn_finalizar")
        self.btn_finalizar.setMinimumSize(QSize(118, 37))
        self.btn_finalizar.setMaximumSize(QSize(180, 37))
        self.btn_finalizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizar.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #dc3545; /* Color de texto rojo */\n"
"    padding: 8px 16px; /* Aumenta el espacio de relleno horizontal */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: 2px solid #dc3545; /* Borde rojo */\n"
"    border-radius: 10px;\n"
"    transition: color 0.3s, background-color 0.3s, transform 0.3s; /* Agrega transiciones suaves */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(220, 53, 69, 0.6); /* Fondo rojo claro al pasar el rat\u00f3n */\n"
"    color: white; /* Cambia el color del texto a blanco */\n"
"    transform: scale(1.05); /* Escala el bot\u00f3n al 105% del tama\u00f1o original */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/borrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_finalizar.setIcon(icon2)
        self.btn_finalizar.setIconSize(QSize(16, 21))

        self.gridLayout_5.addWidget(self.btn_finalizar, 5, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 5, 1, 1, 1)

        self.btn_mover = QPushButton(self.scrollAreaWidgetContents)
        self.btn_mover.setObjectName(u"btn_mover")
        self.btn_mover.setMinimumSize(QSize(118, 37))
        self.btn_mover.setMaximumSize(QSize(180, 37))
        self.btn_mover.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mover.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: white; /* Color de texto rojo */\n"
"    padding: 8px 16px; /* Aumenta el espacio de relleno horizontal */\n"
"    background-color: #3f83be; /* Fondo predominante */\n"
"    border: 2px solid #3f83be; /* Borde del mismo color que el fondo */\n"
"    border-radius: 10px;\n"
"    transition: color 0.3s, background-color 0.3s, transform 0.3s; /* Agrega transiciones suaves */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(63, 131, 190, 0.6); /* Fondo azul claro al pasar el rat\u00f3n */\n"
"    color: white; /* Cambia el color del texto a blanco */\n"
"    transform: scale(1.05); /* Escala el bot\u00f3n al 105% del tama\u00f1o original */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/flecha3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mover.setIcon(icon3)
        self.btn_mover.setIconSize(QSize(16, 21))

        self.gridLayout_5.addWidget(self.btn_mover, 2, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 1, 1, 2)

        self.btn_iniciar = QPushButton(self.scrollAreaWidgetContents)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        self.btn_iniciar.setMinimumSize(QSize(118, 31))
        self.btn_iniciar.setMaximumSize(QSize(56, 37))
        self.btn_iniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_iniciar.setStyleSheet(u"QPushButton {\n"
"    font-family: Roboto;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.02em;\n"
"    color: #28a745; /* Color de texto rojo */\n"
"    padding: 8px 16px; /* Aumenta el espacio de relleno horizontal */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: 2px solid #28a745; /* Borde rojo */\n"
"    border-radius: 10px;\n"
"    transition: color 0.3s, background-color 0.3s; /* Agrega transiciones suaves */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(33, 136, 56, 0.6); /* Fondo rojo claro al pasar el rat\u00f3n */\n"
"    color: white; /* Cambia el color del texto a rojo */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iniciar.setIcon(icon4)
        self.btn_iniciar.setIconSize(QSize(20, 21))

        self.gridLayout_5.addWidget(self.btn_iniciar, 5, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(16, 72))
        self.frame_2.setMaximumSize(QSize(16777215, 55))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 24)
        self.horizontalSpacer = QSpacerItem(727, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.nombreusuario = QLabel(self.frame_2)
        self.nombreusuario.setObjectName(u"nombreusuario")
        self.nombreusuario.setStyleSheet(u"font: 13pt \"MS Reference Sans Serif\";")
        self.nombreusuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.nombreusuario)

        self.tipo = QLabel(self.frame_2)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setStyleSheet(u"font: 13pt \"MS Reference Sans Serif\";")

        self.horizontalLayout.addWidget(self.tipo)

        self.btn_cerrarsesion = QToolButton(self.frame_2)
        self.btn_cerrarsesion.setObjectName(u"btn_cerrarsesion")
        self.btn_cerrarsesion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrarsesion.setIcon(icon5)
        self.btn_cerrarsesion.setIconSize(QSize(23, 21))
        self.btn_cerrarsesion.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.btn_cerrarsesion)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n Credenciales", None))
        self.groupBox_3.setTitle("")
        self.cbo_tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Sunafil", None))
        self.cbo_tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Sunat", None))
        self.cbo_tipo.setItemText(2, QCoreApplication.translate("MainWindow", u"AFPnet", None))

        self.line_busqueda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por cualquier campo ....", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u" Exportar a Excel", None))
        self.lbl_titulo01.setText(QCoreApplication.translate("MainWindow", u"  Lista de credenciales AFPnet", None))
        self.lbl_titulo02.setText(QCoreApplication.translate("MainWindow", u"  Lista de credenciales seleccionadas AFPnet", None))
        ___qtablewidgetitem = self.tabla_credenciales.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_credenciales.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 EMPRESA", None));
        ___qtablewidgetitem2 = self.tabla_credenciales.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RAZON SOCIAL", None));
        ___qtablewidgetitem3 = self.tabla_credenciales.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"RUC", None));
        ___qtablewidgetitem4 = self.tabla_credenciales.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None));
        ___qtablewidgetitem5 = self.tabla_credenciales.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None));
        ___qtablewidgetitem6 = self.tabla_credenciales.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ACCION", None));
        ___qtablewidgetitem7 = self.tabla_automatizar.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem8 = self.tabla_automatizar.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 EMPRESA", None));
        ___qtablewidgetitem9 = self.tabla_automatizar.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"RAZON SOCIAL", None));
        ___qtablewidgetitem10 = self.tabla_automatizar.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"RUC", None));
        ___qtablewidgetitem11 = self.tabla_automatizar.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None));
        ___qtablewidgetitem12 = self.tabla_automatizar.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None));
        ___qtablewidgetitem13 = self.tabla_automatizar.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ACCION", None));
        self.btn_finalizar.setText(QCoreApplication.translate("MainWindow", u" Finalizar", None))
        self.btn_mover.setText(QCoreApplication.translate("MainWindow", u" Mover lote", None))
        self.btn_iniciar.setText(QCoreApplication.translate("MainWindow", u" Iniciar", None))
        self.nombreusuario.setText(QCoreApplication.translate("MainWindow", u"Jose Luis", None))
        self.tipo.setText(QCoreApplication.translate("MainWindow", u"| Empleado", None))
#if QT_CONFIG(tooltip)
        self.btn_cerrarsesion.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cerrarsesion.setText("")
    # retranslateUi

