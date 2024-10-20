# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'foodplace_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mostrar_minifoto_2 = QLabel(self.centralwidget)
        self.mostrar_minifoto_2.setObjectName(u"mostrar_minifoto_2")
        self.mostrar_minifoto_2.setGeometry(QRect(100, 420, 41, 41))
        self.mostrar_minifoto_4 = QLabel(self.centralwidget)
        self.mostrar_minifoto_4.setObjectName(u"mostrar_minifoto_4")
        self.mostrar_minifoto_4.setGeometry(QRect(240, 420, 41, 41))
        self.lista_comentarios = QListWidget(self.centralwidget)
        self.lista_comentarios.setObjectName(u"lista_comentarios")
        self.lista_comentarios.setGeometry(QRect(30, 480, 721, 71))
        self.mostrar_minifoto_5 = QLabel(self.centralwidget)
        self.mostrar_minifoto_5.setObjectName(u"mostrar_minifoto_5")
        self.mostrar_minifoto_5.setGeometry(QRect(310, 420, 41, 41))
        self.mostrar_minifoto_1 = QLabel(self.centralwidget)
        self.mostrar_minifoto_1.setObjectName(u"mostrar_minifoto_1")
        self.mostrar_minifoto_1.setGeometry(QRect(30, 420, 41, 41))
        self.mostrar_foto = QLabel(self.centralwidget)
        self.mostrar_foto.setObjectName(u"mostrar_foto")
        self.mostrar_foto.setGeometry(QRect(30, 70, 321, 321))
        self.mostrar_resultado = QLabel(self.centralwidget)
        self.mostrar_resultado.setObjectName(u"mostrar_resultado")
        self.mostrar_resultado.setGeometry(QRect(120, 10, 531, 41))
        self.mostrar_mapa = QLabel(self.centralwidget)
        self.mostrar_mapa.setObjectName(u"mostrar_mapa")
        self.mostrar_mapa.setGeometry(QRect(410, 70, 351, 401))
        self.mostrar_minifoto_3 = QLabel(self.centralwidget)
        self.mostrar_minifoto_3.setObjectName(u"mostrar_minifoto_3")
        self.mostrar_minifoto_3.setGeometry(QRect(170, 420, 41, 41))
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
        self.mostrar_minifoto_2.setText("")
        self.mostrar_minifoto_4.setText("")
        self.mostrar_minifoto_5.setText("")
        self.mostrar_minifoto_1.setText("")
        self.mostrar_foto.setText("")
        self.mostrar_resultado.setText("")
        self.mostrar_mapa.setText("")
        self.mostrar_minifoto_3.setText("")
    # retranslateUi

