# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Login(QDialog):
        def check(self):
                username = str(self.textEdit.toPlainText())
                password = str(self.textEdit_2.toPlainText())
                if username == "admin" and password == "123456":
                        self.variable = 1
                        super().check()
                else:
                        self.variable = 0
                        super().check()

        def setupUi(self, Login):
                Login.setObjectName("Login")
                Login.resize(350, 350)
                Login.setMinimumSize(QtCore.QSize(350, 350))
                Login.setMaximumSize(QtCore.QSize(350, 350))
                Login.setStyleSheet("background-color: rgb(35, 35, 35);")
                self.centralwidget = QtWidgets.QWidget(Login)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(100, 40, 151, 51))
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(30, 60, 301, 71))
                font = QtGui.QFont()
                font.setFamily("Georgia")
                font.setPointSize(12)
                font.setItalic(True)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setWordWrap(True)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(160, 20, 31, 31))
                self.label_3.setText("")
                self.label_3.setPixmap(QtGui.QPixmap("Images/cil-lock-locked.png"))
                self.label_3.setScaledContents(True)
                self.label_3.setObjectName("label_3")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(10, 150, 341, 51))
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(20, 10, 91, 31))
                font = QtGui.QFont()
                font.setFamily("Georgia")
                font.setPointSize(10)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.textEdit = QtWidgets.QTextEdit(self.frame)
                self.textEdit.setGeometry(QtCore.QRect(130, 10, 171, 31))
                self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 9pt;\n"
        "border:2px solid blue;\n"
        "border-color: rgb(35, 35, 35);\n"
        "border-bottom-color: rgb(85, 170, 255);\n"
        "")
                self.textEdit.setObjectName("textEdit")
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(10, 200, 341, 51))
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.label_5 = QtWidgets.QLabel(self.frame_2)
                self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 31))
                font = QtGui.QFont()
                font.setFamily("Georgia")
                font.setPointSize(10)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_5.setObjectName("label_5")
                self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
                self.textEdit_2.setGeometry(QtCore.QRect(130, 10, 171, 31))
                self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 9pt;\n"
        "border:2px solid blue;\n"
        "border-color: rgb(35, 35, 35);\n"
        "border-bottom-color: rgb(85, 170, 255);\n"
        "")
                self.textEdit_2.setObjectName("textEdit_2")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(120, 290, 111, 31))
                font = QtGui.QFont()
                font.setFamily("Georgia")
                font.setPointSize(12)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(85, 170, 255);\n"
        "border-radius:12px;")
                self.pushButton.setObjectName("pushButton")
                Login.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(Login)
                self.statusbar.setObjectName("statusbar")
                Login.setStatusBar(self.statusbar)

                self.retranslateUi(Login)
                QtCore.QMetaObject.connectSlotsByName(Login)
                self.pushButton.clicked.connect(lambda: self.check)

        def retranslateUi(self, Login):
                _translate = QtCore.QCoreApplication.translate
                Login.setWindowTitle(_translate("Login", "MainWindow"))
                self.label.setText(_translate("Login", "TextLabel"))
                self.label_2.setText(_translate("Login", "The content you are trying to view is hidden please login below to access it !!!"))
                self.label_4.setText(_translate("Login", "Username :"))
                self.label_5.setText(_translate("Login", "Password :"))
                self.pushButton.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

