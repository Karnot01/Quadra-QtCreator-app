# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'foodplaceprofile.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_FoodPlaceProfileWindow(object):
    def setupUi(self, FoodPlaceProfileWindow):
        if not FoodPlaceProfileWindow.objectName():
            FoodPlaceProfileWindow.setObjectName(u"FoodPlaceProfileWindow")
        FoodPlaceProfileWindow.resize(800, 600)
        self.centralwidget = QWidget(FoodPlaceProfileWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        FoodPlaceProfileWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FoodPlaceProfileWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FoodPlaceProfileWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FoodPlaceProfileWindow)
        self.statusbar.setObjectName(u"statusbar")
        FoodPlaceProfileWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FoodPlaceProfileWindow)

        QMetaObject.connectSlotsByName(FoodPlaceProfileWindow)
    # setupUi

    def retranslateUi(self, FoodPlaceProfileWindow):
        FoodPlaceProfileWindow.setWindowTitle(QCoreApplication.translate("FoodPlaceProfileWindow", u"MainWindow", None))
    # retranslateUi

