
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui import Ui_MainWindow 

class UIFunctions(QMainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
                self.ui.btn_page_1.setEnabled(True)
                self.ui.btn_page_2.setEnabled(True)
                self.ui.btn_page_3.setEnabled(True)
                self.ui.btn_page_4.setEnabled(True)
                self.ui.btn_page_1.setText('  Home')
                self.ui.btn_page_2.setText('  Analyse')
                self.ui.btn_page_3.setText('  Database')
                self.ui.btn_page_4.setText('  Credits')
                self.ui.btn_page_4.setGeometry(QtCore.QRect(0, 479, 250, 61))
            else:
                widthExtended = standard
                self.ui.btn_page_1.setEnabled(False)
                self.ui.btn_page_2.setEnabled(False)
                self.ui.btn_page_3.setEnabled(False)
                self.ui.btn_page_4.setEnabled(False)
                self.ui.btn_page_1.setText('')
                self.ui.btn_page_2.setText('')
                self.ui.btn_page_3.setText('')
                self.ui.btn_page_4.setText('')
                self.ui.btn_page_4.setGeometry(QtCore.QRect(0, 479, 68, 61))

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
