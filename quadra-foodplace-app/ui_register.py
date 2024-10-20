# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(800, 600)
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.captura_mail = QLineEdit(self.centralwidget)
        self.captura_mail.setObjectName(u"captura_mail")
        self.captura_mail.setGeometry(QRect(270, 210, 221, 24))
        self.crear_cuenta = QPushButton(self.centralwidget)
        self.crear_cuenta.setObjectName(u"crear_cuenta")
        self.crear_cuenta.setGeometry(QRect(330, 500, 101, 31))
        self.alerta_error = QLabel(self.centralwidget)
        self.alerta_error.setObjectName(u"alerta_error")
        self.alerta_error.setGeometry(QRect(300, 460, 171, 31))
        self.alerta_error.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 0, 0)\n"
"}")
        self.captura_pass_confirm = QLineEdit(self.centralwidget)
        self.captura_pass_confirm.setObjectName(u"captura_pass_confirm")
        self.captura_pass_confirm.setGeometry(QRect(270, 390, 221, 24))
        self.captura_pass_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.captura_username = QLineEdit(self.centralwidget)
        self.captura_username.setObjectName(u"captura_username")
        self.captura_username.setGeometry(QRect(270, 140, 221, 24))
        self.captura_pass = QLineEdit(self.centralwidget)
        self.captura_pass.setObjectName(u"captura_pass")
        self.captura_pass.setGeometry(QRect(270, 300, 221, 24))
        self.captura_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_registrate = QLabel(self.centralwidget)
        self.label_registrate.setObjectName(u"label_registrate")
        self.label_registrate.setGeometry(QRect(300, 30, 161, 71))
        self.label_registrate.setStyleSheet(u"font: 14pt \"Sitka\";\n"
"font: 700 24pt \"Segoe UI\";\n"
"")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RegisterWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RegisterWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.captura_mail.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Correo electr\u00f3nico", None))
        self.crear_cuenta.setText(QCoreApplication.translate("RegisterWindow", u"Crear Cuenta", None))
        self.alerta_error.setText("")
        self.captura_pass_confirm.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Confirmar contrase\u00f1a", None))
        self.captura_username.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Nombre de usuario", None))
        self.captura_pass.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Contrase\u00f1a", None))
        self.label_registrate.setText(QCoreApplication.translate("RegisterWindow", u"Registrate", None))
    # retranslateUi

