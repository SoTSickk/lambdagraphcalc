# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lambda_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Lambda(object):
    def setupUi(self, Lambda):
        if not Lambda.objectName():
            Lambda.setObjectName(u"Lambda")
        Lambda.resize(1280, 720)
        Lambda.setStyleSheet(u"background: rgb(11, 11, 11)")
        self.centralwidget = QWidget(Lambda)
        self.centralwidget.setObjectName(u"centralwidget")
        self.typedin = QLabel(self.centralwidget)
        self.typedin.setObjectName(u"typedin")
        self.typedin.setGeometry(QRect(20, 130, 461, 101))
        self.typedin.setStyleSheet(u"color: white;\n"
"font-size: 48px;\n"
"background-color: rgb(0, 0, 0);\n"
"border-size: 5px;\n"
"border-radius: 20px;\n"
"border-color: rgb(18, 18, 18)")
        self.addx = QPushButton(self.centralwidget)
        self.addx.setObjectName(u"addx")
        self.addx.setGeometry(QRect(20, 250, 101, 61))
        self.addx.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.addy = QPushButton(self.centralwidget)
        self.addy.setObjectName(u"addy")
        self.addy.setGeometry(QRect(130, 250, 101, 61))
        self.addy.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.addpoint = QPushButton(self.centralwidget)
        self.addpoint.setObjectName(u"addpoint")
        self.addpoint.setGeometry(QRect(240, 250, 101, 61))
        self.addpoint.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.goback = QPushButton(self.centralwidget)
        self.goback.setObjectName(u"goback")
        self.goback.setGeometry(QRect(350, 250, 131, 61))
        self.goback.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add9 = QPushButton(self.centralwidget)
        self.add9.setObjectName(u"add9")
        self.add9.setGeometry(QRect(240, 320, 101, 61))
        self.add9.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add7 = QPushButton(self.centralwidget)
        self.add7.setObjectName(u"add7")
        self.add7.setGeometry(QRect(20, 320, 101, 61))
        self.add7.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add8 = QPushButton(self.centralwidget)
        self.add8.setObjectName(u"add8")
        self.add8.setGeometry(QRect(130, 320, 101, 61))
        self.add8.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(350, 320, 131, 61))
        self.plus.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add6 = QPushButton(self.centralwidget)
        self.add6.setObjectName(u"add6")
        self.add6.setGeometry(QRect(240, 390, 101, 61))
        self.add6.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add4 = QPushButton(self.centralwidget)
        self.add4.setObjectName(u"add4")
        self.add4.setGeometry(QRect(20, 390, 101, 61))
        self.add4.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add5 = QPushButton(self.centralwidget)
        self.add5.setObjectName(u"add5")
        self.add5.setGeometry(QRect(130, 390, 101, 61))
        self.add5.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(350, 390, 131, 61))
        self.minus.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add3 = QPushButton(self.centralwidget)
        self.add3.setObjectName(u"add3")
        self.add3.setGeometry(QRect(240, 460, 101, 61))
        self.add3.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add1 = QPushButton(self.centralwidget)
        self.add1.setObjectName(u"add1")
        self.add1.setGeometry(QRect(20, 460, 101, 61))
        self.add1.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add2 = QPushButton(self.centralwidget)
        self.add2.setObjectName(u"add2")
        self.add2.setGeometry(QRect(130, 460, 101, 61))
        self.add2.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.times = QPushButton(self.centralwidget)
        self.times.setObjectName(u"times")
        self.times.setGeometry(QRect(350, 460, 131, 61))
        self.times.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.equals = QPushButton(self.centralwidget)
        self.equals.setObjectName(u"equals")
        self.equals.setGeometry(QRect(130, 600, 211, 61))
        self.equals.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(20, 600, 101, 61))
        self.clear.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.divide = QPushButton(self.centralwidget)
        self.divide.setObjectName(u"divide")
        self.divide.setGeometry(QRect(350, 530, 131, 61))
        self.divide.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.power = QPushButton(self.centralwidget)
        self.power.setObjectName(u"power")
        self.power.setGeometry(QRect(350, 600, 131, 61))
        self.power.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.add0 = QPushButton(self.centralwidget)
        self.add0.setObjectName(u"add0")
        self.add0.setGeometry(QRect(20, 530, 211, 61))
        self.add0.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.decimal = QPushButton(self.centralwidget)
        self.decimal.setObjectName(u"decimal")
        self.decimal.setGeometry(QRect(240, 530, 101, 61))
        self.decimal.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(500, 20, 761, 411))
        self.render = QPushButton(self.centralwidget)
        self.render.setObjectName(u"render")
        self.render.setGeometry(QRect(1150, 450, 121, 61))
        self.render.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.stopplaying = QPushButton(self.centralwidget)
        self.stopplaying.setObjectName(u"stopplaying")
        self.stopplaying.setGeometry(QRect(1020, 450, 121, 61))
        self.stopplaying.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 16px")
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 20, 461, 101))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 32px")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 32px")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 32px")

        self.horizontalLayout.addWidget(self.pushButton_3)

        Lambda.setCentralWidget(self.centralwidget)

        self.retranslateUi(Lambda)

        QMetaObject.connectSlotsByName(Lambda)
    # setupUi

    def retranslateUi(self, Lambda):
        Lambda.setWindowTitle(QCoreApplication.translate("Lambda", u"Lambda", None))
        self.typedin.setText(QCoreApplication.translate("Lambda", u"TextLabel", None))
        self.addx.setText(QCoreApplication.translate("Lambda", u"Add X", None))
        self.addy.setText(QCoreApplication.translate("Lambda", u"Add Y", None))
        self.addpoint.setText(QCoreApplication.translate("Lambda", u"Add Point", None))
        self.goback.setText(QCoreApplication.translate("Lambda", u"<-------", None))
        self.add9.setText(QCoreApplication.translate("Lambda", u"9", None))
        self.add7.setText(QCoreApplication.translate("Lambda", u"7", None))
        self.add8.setText(QCoreApplication.translate("Lambda", u"8", None))
        self.plus.setText(QCoreApplication.translate("Lambda", u"+", None))
        self.add6.setText(QCoreApplication.translate("Lambda", u"6", None))
        self.add4.setText(QCoreApplication.translate("Lambda", u"4", None))
        self.add5.setText(QCoreApplication.translate("Lambda", u"5", None))
        self.minus.setText(QCoreApplication.translate("Lambda", u"-", None))
        self.add3.setText(QCoreApplication.translate("Lambda", u"3", None))
        self.add1.setText(QCoreApplication.translate("Lambda", u"1", None))
        self.add2.setText(QCoreApplication.translate("Lambda", u"2", None))
        self.times.setText(QCoreApplication.translate("Lambda", u"*", None))
        self.equals.setText(QCoreApplication.translate("Lambda", u"=", None))
        self.clear.setText(QCoreApplication.translate("Lambda", u"Clear", None))
        self.divide.setText(QCoreApplication.translate("Lambda", u"/", None))
        self.power.setText(QCoreApplication.translate("Lambda", u"^", None))
        self.add0.setText(QCoreApplication.translate("Lambda", u"0", None))
        self.decimal.setText(QCoreApplication.translate("Lambda", u".", None))
        self.render.setText(QCoreApplication.translate("Lambda", u"Render", None))
        self.stopplaying.setText(QCoreApplication.translate("Lambda", u"Stop Playing", None))
        self.pushButton.setText(QCoreApplication.translate("Lambda", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Lambda", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Lambda", u"PushButton", None))
    # retranslateUi

