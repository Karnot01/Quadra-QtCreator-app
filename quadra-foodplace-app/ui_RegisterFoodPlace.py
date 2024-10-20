# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterFoodPlace.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_RegisterFoodPlaceWindow(object):
    def setupUi(self, RegisterFoodPlaceWindow):
        if not RegisterFoodPlaceWindow.objectName():
            RegisterFoodPlaceWindow.setObjectName(u"RegisterFoodPlaceWindow")
        RegisterFoodPlaceWindow.resize(803, 602)
        self.centralwidget = QWidget(RegisterFoodPlaceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.subir_foto = QLabel(self.centralwidget)
        self.subir_foto.setObjectName(u"subir_foto")
        self.subir_foto.setGeometry(QRect(20, 10, 401, 401))
        self.subir_foto.setMaximumSize(QSize(401, 401))
        self.subir_foto.setScaledContents(False)
        self.ubicacion = QLineEdit(self.centralwidget)
        self.ubicacion.setObjectName(u"ubicacion")
        self.ubicacion.setGeometry(QRect(450, 120, 321, 24))
        self.crear_puesto = QPushButton(self.centralwidget)
        self.crear_puesto.setObjectName(u"crear_puesto")
        self.crear_puesto.setGeometry(QRect(660, 520, 101, 31))
        self.boton_cerrar = QPushButton(self.centralwidget)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setGeometry(QRect(660, 10, 121, 21))
        self.nombre_puesto = QLineEdit(self.centralwidget)
        self.nombre_puesto.setObjectName(u"nombre_puesto")
        self.nombre_puesto.setGeometry(QRect(450, 80, 321, 24))
        self.comentarios = QLineEdit(self.centralwidget)
        self.comentarios.setObjectName(u"comentarios")
        self.comentarios.setGeometry(QRect(20, 430, 741, 81))
        RegisterFoodPlaceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RegisterFoodPlaceWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 21))
        RegisterFoodPlaceWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RegisterFoodPlaceWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegisterFoodPlaceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterFoodPlaceWindow)

        QMetaObject.connectSlotsByName(RegisterFoodPlaceWindow)
    # setupUi

    def retranslateUi(self, RegisterFoodPlaceWindow):
        RegisterFoodPlaceWindow.setWindowTitle(QCoreApplication.translate("RegisterFoodPlaceWindow", u"MainWindow", None))
        self.subir_foto.setText("")
        self.ubicacion.setPlaceholderText(QCoreApplication.translate("RegisterFoodPlaceWindow", u"Ubicaci\u00f3n", None))
        self.crear_puesto.setText(QCoreApplication.translate("RegisterFoodPlaceWindow", u"Registrar Puesto", None))
        self.boton_cerrar.setText(QCoreApplication.translate("RegisterFoodPlaceWindow", u"Cerrar sesi\u00f3n", None))
        self.nombre_puesto.setPlaceholderText(QCoreApplication.translate("RegisterFoodPlaceWindow", u"Nombre del Puesto", None))
        self.comentarios.setPlaceholderText("")
    # retranslateUi

