# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_foodplace.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_RegisterFoodplaceWindow(object):
    def setupUi(self, RegisterFoodplaceWindow):
        if not RegisterFoodplaceWindow.objectName():
            RegisterFoodplaceWindow.setObjectName(u"RegisterFoodplaceWindow")
        RegisterFoodplaceWindow.resize(800, 600)
        self.centralwidget = QWidget(RegisterFoodplaceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.subir_comentarios = QListWidget(self.centralwidget)
        self.subir_comentarios.setObjectName(u"subir_comentarios")
        self.subir_comentarios.setGeometry(QRect(20, 430, 741, 81))
        self.subir_foto = QLabel(self.centralwidget)
        self.subir_foto.setObjectName(u"subir_foto")
        self.subir_foto.setGeometry(QRect(20, 10, 301, 401))
        self.subir_ubicacion = QLineEdit(self.centralwidget)
        self.subir_ubicacion.setObjectName(u"subir_ubicacion")
        self.subir_ubicacion.setGeometry(QRect(450, 120, 321, 24))
        self.crear_puesto = QPushButton(self.centralwidget)
        self.crear_puesto.setObjectName(u"crear_puesto")
        self.crear_puesto.setGeometry(QRect(660, 520, 101, 31))
        self.boton_cerrar = QPushButton(self.centralwidget)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setGeometry(QRect(660, 10, 121, 21))
        self.captura_nombre_puesto = QLineEdit(self.centralwidget)
        self.captura_nombre_puesto.setObjectName(u"captura_nombre_puesto")
        self.captura_nombre_puesto.setGeometry(QRect(450, 80, 321, 24))
        RegisterFoodplaceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RegisterFoodplaceWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        RegisterFoodplaceWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RegisterFoodplaceWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegisterFoodplaceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterFoodplaceWindow)

        QMetaObject.connectSlotsByName(RegisterFoodplaceWindow)
    # setupUi

    def retranslateUi(self, RegisterFoodplaceWindow):
        RegisterFoodplaceWindow.setWindowTitle(QCoreApplication.translate("RegisterFoodplaceWindow", u"MainWindow", None))
        self.subir_foto.setText("")
        self.subir_ubicacion.setPlaceholderText(QCoreApplication.translate("RegisterFoodplaceWindow", u"Ubicaci\u00f3n", None))
        self.crear_puesto.setText(QCoreApplication.translate("RegisterFoodplaceWindow", u"Crear Cuenta", None))
        self.boton_cerrar.setText(QCoreApplication.translate("RegisterFoodplaceWindow", u"Cerrar sesi\u00f3n", None))
        self.captura_nombre_puesto.setPlaceholderText(QCoreApplication.translate("RegisterFoodplaceWindow", u"Nombre del Puesto", None))
    # retranslateUi

