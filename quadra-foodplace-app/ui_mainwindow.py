# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boton_registro = QPushButton(self.centralwidget)
        self.boton_registro.setObjectName(u"boton_registro")
        self.boton_registro.setGeometry(QRect(420, 370, 101, 31))
        self.input_email = QLineEdit(self.centralwidget)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setGeometry(QRect(280, 130, 261, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 241, 61))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(28)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 370, 111, 31))
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.texto_error = QLabel(self.centralwidget)
        self.texto_error.setObjectName(u"texto_error")
        self.texto_error.setGeometry(QRect(190, 460, 451, 51))
        self.texto_error.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Sitka Banner\";\n"
"	color: rgb(255,0,0)\n"
"\n"
"}")
        self.boton_inicio = QPushButton(self.centralwidget)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setGeometry(QRect(300, 270, 211, 51))
        self.boton_inicio.setStyleSheet(u"QPushButton {\n"
"    background-color:#9c120b; /* Color de fondo */\n"
"    border: 4px solid #000000; /* Borde del bot\u00f3n con el color RGB deseado */\n"
" 	color: #000000; /* Color del texto */\n"
"    padding: 10px 20px; /* Espaciado interno */\n"
"	text-align: center;\n"
"	text-decoration: none\n"
"    font-size: 16px; /* Tama\u00f1o de la fuente */\n"
"	margin: 4px 2px;\n"
"    cursor: pointer; /* Cambia el cursor a una mano al pasar sobre el bot\u00f3n */\n"
"	border-radius: 20px; /* Bordes un poco redondeados\n"
"    box-shadow: 0  4px 8px rgba(0, 0, 0, 0.2); /* Sombra de fondo */\n"
"    transition: background-color 0.3s; /* Transici\u00f3n suave al pasar el cursor */\n"
"}\n"
"\n"
"/* Oscurecer el bot\u00f3n al pasar el cursor */\n"
"QPushButton:hover {\n"
"    background-color: #1a1a1a; /* Color de fondo m\u00e1s oscuro */\n"
"}\n"
"")
        self.input_pass = QLineEdit(self.centralwidget)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setGeometry(QRect(280, 190, 261, 24))
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_registro.setText(QCoreApplication.translate("MainWindow", u"\u00a1Registrate!", None))
        self.input_email.setText("")
        self.input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu correo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicio de Sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfNo tienes cuenta? ", None))
        self.texto_error.setText("")
        self.boton_inicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.input_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu contrase\u00f1a", None))
    # retranslateUi

