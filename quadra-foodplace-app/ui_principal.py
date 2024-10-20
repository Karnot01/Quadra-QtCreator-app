# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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

class Ui_PrincipalWindow(object):
    def setupUi(self, PrincipalWindow):
        if not PrincipalWindow.objectName():
            PrincipalWindow.setObjectName(u"PrincipalWindow")
        PrincipalWindow.resize(800, 600)
        self.centralwidget = QWidget(PrincipalWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mostrar_foto = QLabel(self.centralwidget)
        self.mostrar_foto.setObjectName(u"mostrar_foto")
        self.mostrar_foto.setEnabled(True)
        self.mostrar_foto.setGeometry(QRect(120, 90, 531, 331))
        self.mostrar_foto.setScaledContents(True)
        self.mostrar_foto.setOpenExternalLinks(False)
        self.boton_buscar = QPushButton(self.centralwidget)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(470, 50, 80, 24))
        self.agregar_puesto = QPushButton(self.centralwidget)
        self.agregar_puesto.setObjectName(u"agregar_puesto")
        self.agregar_puesto.setGeometry(QRect(290, 530, 191, 24))
        self.buscador = QLineEdit(self.centralwidget)
        self.buscador.setObjectName(u"buscador")
        self.buscador.setGeometry(QRect(0, 50, 461, 31))
        self.mostrar_correo = QLabel(self.centralwidget)
        self.mostrar_correo.setObjectName(u"mostrar_correo")
        self.mostrar_correo.setGeometry(QRect(0, 20, 661, 21))
        self.mostrar_correo.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.mostrar_resultado = QLabel(self.centralwidget)
        self.mostrar_resultado.setObjectName(u"mostrar_resultado")
        self.mostrar_resultado.setGeometry(QRect(120, 390, 531, 41))
        self.boton_siguiente = QPushButton(self.centralwidget)
        self.boton_siguiente.setObjectName(u"boton_siguiente")
        self.boton_siguiente.setGeometry(QRect(690, 230, 80, 24))
        self.boton_cerrar = QPushButton(self.centralwidget)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setGeometry(QRect(670, 10, 121, 21))
        self.lista_comentarios = QListWidget(self.centralwidget)
        self.lista_comentarios.setObjectName(u"lista_comentarios")
        self.lista_comentarios.setGeometry(QRect(30, 440, 721, 81))
        self.boton_anterior = QPushButton(self.centralwidget)
        self.boton_anterior.setObjectName(u"boton_anterior")
        self.boton_anterior.setGeometry(QRect(10, 230, 80, 24))
        self.boton_perfil_puesto = QPushButton(self.centralwidget)
        self.boton_perfil_puesto.setObjectName(u"boton_perfil_puesto")
        self.boton_perfil_puesto.setGeometry(QRect(30, 530, 101, 24))
        PrincipalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PrincipalWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        PrincipalWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PrincipalWindow)
        self.statusbar.setObjectName(u"statusbar")
        PrincipalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PrincipalWindow)

        QMetaObject.connectSlotsByName(PrincipalWindow)
    # setupUi

    def retranslateUi(self, PrincipalWindow):
        PrincipalWindow.setWindowTitle(QCoreApplication.translate("PrincipalWindow", u"MainWindow", None))
        self.mostrar_foto.setText("")
        self.boton_buscar.setText(QCoreApplication.translate("PrincipalWindow", u"Buscar", None))
        self.agregar_puesto.setText(QCoreApplication.translate("PrincipalWindow", u"Agregar nuevo puesto de comida", None))
        self.mostrar_correo.setText(QCoreApplication.translate("PrincipalWindow", u"Bienvenido: ", None))
        self.mostrar_resultado.setText("")
        self.boton_siguiente.setText(QCoreApplication.translate("PrincipalWindow", u"Siguiente", None))
        self.boton_cerrar.setText(QCoreApplication.translate("PrincipalWindow", u"Cerrar sesi\u00f3n", None))
        self.boton_anterior.setText(QCoreApplication.translate("PrincipalWindow", u"Anterior", None))
        self.boton_perfil_puesto.setText(QCoreApplication.translate("PrincipalWindow", u"Perfil del puesto", None))
    # retranslateUi

