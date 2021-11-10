import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np  
from datetime import datetime
import time
from ui import Ui_MainWindow 
from ui_functions import UIFunctions
from main_splash import SplashScreen
from login import Ui_Login
import webbrowser
from bs4 import BeautifulSoup
import requests

class MainWindow(QMainWindow):
    

    def mysql_connect(self):
        global mydb
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cs_project"
        )

        global mycursor 
        mycursor = mydb.cursor()

    def __init__(self):
        QMainWindow.__init__(self)
        self.splash = SplashScreen()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.mysql_connect()
        self.get_id()
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btn_page_1.clicked.connect(self.btn_page_1_functions)
        self.ui.btn_page_2.clicked.connect(self.btn_page_2_functions)
        self.ui.btn_page_3.clicked.connect(self.btn_page_3_functions)
        self.ui.btn_page_4.clicked.connect(self.btn_page_4_functions)
        self.ui.cases_button.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_11))
        self.ui.death_radio_button.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_12))
        self.ui.gender_radio_button.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_8))
        self.ui.recovery_radio_button.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page))
        self.ui.state_radio_button.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7))
        self.ui.Other_state_button.clicked.connect(self.other_state_button_function)
        self.ui.Select_state_button.clicked.connect(self.select_state_button_function)
        self.ui.update_page_button.clicked.connect(self.update_page_button_function)
        self.ui.add_page_button.clicked.connect(self.add_page_button_function)
        self.ui.search_button.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_16))
        self.ui.list_update_results.clicked.connect(self.list_update_results_functions)
        self.ui.discharge_add_checkbox.toggled.connect(self.discharge_add_function)
        self.ui.discharge_check.toggled.connect(self.discharge_update_function)
        self.ui.listWidget_case.clicked.connect(self.listWidget_case_function)
        self.ui.death_list.clicked.connect(self.death_list_function)
        self.ui.list_recovery.clicked.connect(self.list_recovery_function)
        self.ui.pushButton.clicked.connect(self.login_button_function)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_functions)
        self.ui.calendarWidget_2.selectionChanged.connect(self.calendarWidget_2_function)
        self.ui.calendarWidget.selectionChanged.connect(self.calendarWidget_function)
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        # Print Graphs

        self.ui.Analyse_button.clicked.connect(self.Analyse_button_function)
        self.ui._Other_state_analyse_button.clicked.connect(self._Other_state_analyse_button_function)
        self.ui.Analyse_button__death_3.clicked.connect(self.Analyse_button__death_3_function)
        self.ui._analyse_case_button.clicked.connect(self._analyse_case_button_function)
        self.ui.Analyse_button__death.clicked.connect(self.Analyse_button__death_function)
        self.ui.analyse_for_recovery.clicked.connect(self.analyse_for_recovery_function)
        self.ui.add_button.clicked.connect(self.add_button_function)
        self.ui.search_button.clicked.connect(self.search_button_function)
        self.ui.update_button.clicked.connect(self.update_button_function)
        self.ui.More_news_button.clicked.connect(self.more_news_button_function)
        self.ui.Live_cases_button.clicked.connect(self.live_cases_button_function)
        self.ui.Go_online_button.clicked.connect(self.go_online_button_function)
        self.ui.Analyse_button_4.clicked.connect(self.analyse_button_4_function)
        self.show()
        self.splash.splash()

    def analyse_button_4_function(self):
        webbrowser.open("https://covid19.who.int/region/searo/country/in")

    def go_online_button_function(self):
        webbrowser.open("https://www.google.com/search?sxsrf=ALeKk02ZGKL5B3pEYwO7lcS2wxhgLfIC4g%3A1612290174539&ei=fpgZYNzJIM2a4-EP9bK2kA4&q=covid+indian+states+graph&oq=covid+indian+states&gs_lcp=CgZwc3ktYWIQAxgBMgIIADICCAAyAggAMgYIABAWEB4yBQgAEIYDOgQIIxAnOgQIABBDOgcIABCxAxBDOg0IABCxAxCDARAUEIcCOgcIIxDqAhAnOgcIIxDJAxAnOgUIABCSAzoKCAAQsQMQFBCHAjoICAAQsQMQkQI6BQgAEJECOgUIABCxAzoICAAQsQMQgwE6BwgAEBQQhwI6CggAELEDEIMBEAo6BwgAELEDEAo6BAgAEAo6CAghEBYQHRAeUPLdCFizyglg_9YJaAhwAXgAgAGiAogBjSKSAQYwLjE0LjmYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab")

    def live_cases_button_function(self):
        webbrowser.open("https://www.google.com/search?sxsrf=ALeKk03UlGlgBC2zw1ZJryzBcmmvFX1F-w%3A1612290164525&ei=dJgZYKvkH9LF4-EP9cyx6AQ&q=covid+cases&oq=covid+cases&gs_lcp=CgZwc3ktYWIQAzIICAAQsQMQkQIyDQgAELEDEMkDEBQQhwIyBQgAEJIDMgUIABCSAzIFCAAQkQIyCggAELEDEBQQhwIyCAgAELEDEIMBMgUIABCxAzICCAAyBQgAELEDOgQIABBHOgQIIxAnOg0IABCxAxCDARAUEIcCOgcIABAUEIcCUMoUWMQ7YOlBaABwAngAgAGvAYgBqQaSAQMwLjaYAQCgAQGqAQdnd3Mtd2l6yAEEwAEB&sclient=psy-ab&ved=0ahUKEwir7p_06MvuAhXS4jgGHXVmDE0Q4dUDCA0&uact=5")

    def more_news_button_function(self):
        webbrowser.open("https://www.google.com/search?q=covid+news&sxsrf=ALeKk03qsD7fNDOR50LBHxIQnYXvKN0ABA:1612289798412&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjmhtbF58vuAhXmxjgGHZJyA-8Q_AUoAXoECAcQAw&biw=1536&bih=796")

    def pushButton_2_functions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        self.ui.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")


    def update_button_function(self):
        id =  self.ui.Id_upadate_label.toPlainText()
        name = self.ui.name_update_text.toPlainText()
        if self.ui.gemder_update.currentText() == "Male":
            gender = "M"
        else:
            gender = "F"
        state = self.ui.state_update.currentText()
        blood_group = self.ui.bloodgroup_update.currentText()
        admit = self.ui.admit_update.toPlainText()
        if self.ui.discharge_check.isChecked():
            discharge = self.ui.discharge_update.toPlainText()
        if self.ui.active_radio.isChecked():
            status = "active"
        elif self.ui.dead_radio.isChecked():
            status = "died"
        elif self.ui.recovered_radio.isChecked():
            status = "recovered"  
        mycursor = mydb.        cursor()
        try:
            str1 = "update covid_patients set date_of_discharge = " + "'" + discharge + "'" + " where ID = " + "'" + id + "'" + ";"

            str2 = "update covid_patients set status = " + "'" + status + "'" + " where ID = " + "'" + id + "'" + ";"

            mycursor.execute(str1)
            mycursor.execute(str2)
            mydb.commit()
            self.show_popup_add()
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_16)
            self.ui.name_update_text.setText("")
            self.ui.discharge_update.setText("")
        except :
            self.show_popup_fail()
        

    def list_update_results_functions(self):
        index = self.ui.list_update_results.currentRow()
        choice = myresult1[index]
        self.ui.Id_upadate_label.setText(str(choice[0]))
        self.ui.name_update_text.setText(choice[1])
        if choice[3] == "M":
            self.ui.gemder_update.setCurrentText("Male")
        else:
            self.ui.gemder_update.setCurrentText("Female")
        if choice[7] == "other states":
            self.ui.state_update.setCurrentText("Other States")
        else:
            self.ui.state_update.setCurrentText(str(choice[7]))
        self.ui.bloodgroup_update.setCurrentText(str(choice[6]))
        self.ui.admit_update.setText(choice[2].strftime('%Y-%m-%d'))
        try :
            self.ui.discharge_update.setText(choice[4].strftime('%Y-%m-%d'))
        except :
            self.ui.discharge_update.setText("")
        if choice[5] == 'active' :
            self.ui.active_radio.setChecked(True)
        elif choice[5] == 'recovered' :
            self.ui.recovered_radio.setChecked(True)
        elif choice[5] == 'died' :
            self.ui.dead_radio.setChecked(True)
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_17)

    def search_button_function(self):
        if self.ui.id_radio.isChecked():
            str1 = "select * from covid_patients where ID = " + str(self.ui.Id_upadate_label.toPlainText()) + ";"
        elif self.ui.name_update_raadio.isChecked():
            str1 = "select * from covid_patients where name = " + "'" + str(self.ui.name_update_text.toPlainText()) + "'" + ";"
        mycursor.execute(str1)
        global myresult1
        myresult1 = mycursor.fetchall()
        for i in range(len(myresult1)):
            self.ui.list_update_results.item(i).setText(str(myresult1[i]))
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_16)

    def get_id(self):
        mycursor = mydb.cursor()
        mycursor.execute("select max(ID) from covid_patients;")
        myresult = mycursor.fetchall()
        global current_id
        current_id = str(myresult[0][0] + 1)
        self.ui.patient_id_add_label.setText(current_id)

    def show_popup(self,str1):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(str1)
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def add_button_function(self):
        name = self.ui.name_testedit_add.toPlainText()
        if self.ui.gender_combobox_add.currentText() == "Male":
            gender = "M"
        else:
            gender = "F"
        state = self.ui.state_combobox_add.currentText()
        blood_group = self.ui.blood_gorup_combobox.currentText()
        admit = self.ui.admit_on_add.toPlainText()
        if self.ui.discharge_add_checkbox.isChecked():
            discharge = self.ui.discharge_add.toPlainText()
        if self.ui.active_add_radio.isChecked():
            status = "active"
        elif self.ui.dead_add_radio.isChecked():
            status = "died"
        elif self.ui.recovered_add_radio.isChecked():
            status = "recovered"  
        mycursor = mydb.cursor()
        try :
            str1 = "insert into covid_patients values(" + "'" + current_id + "'"  + "," + "'" + name + "'" + "," + "'" + admit + "'" + "," + "'" + gender + "'" + "," + "'" + discharge + "'" + "," + "'" + status + "'" + "," + "'" + blood_group + "'" + "," + "'" + state + "'" + ");"
            mycursor.execute(str1)
            pop = "Added to database !!!!"
            self.show_popup(pop)
            self.ui.name_testedit_add.setText("")
            self.ui.admit_on_add.setText("")
            self.ui.discharge_add.setText("")
            mydb.commit()
        except :
            str1 = "Something went wrong please check !!!!"
            self.show_popup(str1)

    def takeSecond(self,a):
        return a[1]

    def analyse_for_recovery_function(self):
        mycursor = mydb.cursor()
        mycursor.execute("select count(*),month(date_of_admn) from covid_patients where status = 'recovered' group by month(date_of_admn);")
        myresult = mycursor.fetchall()
        myresult.sort(key=self.takeSecond)
        x=[]
        y=[]
        for i in myresult:
            x.append(i[1])
            y.append(i[0])
        plt.plot(x, y)
        plt.show()

    def Analyse_button__death_function(self):
        mycursor = mydb.cursor()
        mycursor.execute("select count(*),month(date_of_admn) from covid_patients where status = 'died' group by month(date_of_admn);")
        myresult = mycursor.fetchall()
        myresult.sort(key=self.takeSecond)
        x=[]
        y=[]
        for i in myresult:
            x.append(i[1])
            y.append(i[0])
        plt.plot(x, y)
        plt.show()

    def _analyse_case_button_function(self):
        mycursor = mydb.cursor()
        mycursor.execute("select count(*),month(date_of_admn) from covid_patients group by month(date_of_admn);")
        myresult = mycursor.fetchall()
        myresult.sort(key=self.takeSecond)
        x=[]
        y=[]
        
        if self.ui.list_case_label.text() == "All (Jan 2020 - Jan 2021)":
            for i in myresult:
                x.append(i[1])
                y.append(i[0])
            plt.plot(x, y)
            plt.show()

        elif self.ui.list_case_label.text() == "January 2020 - April 2020":
            for i in myresult:
                if i[1] >= 1 and i[1] <= 4:
                    x.append(i[1])
                    y.append(i[0])
            plt.plot(x, y)
            plt.show()

        elif self.ui.list_case_label.text() == "May 2020 - September 2020":
            for i in myresult:
                if i[1] >= 5 and i[1] <= 9:
                    x.append(i[1])
                    y.append(i[0])
            plt.plot(x, y)
            plt.show()

        elif self.ui.list_case_label.text() == "October 2020 - January 2021":
            for i in myresult:
                if i[1] >= 10 and i[1] <= 12:
                    x.append(i[1])
                    y.append(i[0])  
            plt.plot(x, y)
            plt.show()    

    def Analyse_button__death_3_function(self):
        mycursor = mydb.cursor()

        mycursor.execute("select count(*) from covid_patients group by gender;")

        myresult = mycursor.fetchall()
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        langs = ["Males","Females"]
        students = np.array([int(myresult[0][0]),int(myresult[1][0])])
        ax.pie(students, labels = langs,autopct='%1.2f%%')
        plt.show()

    def _Other_state_analyse_button_function(self):
        mycursor = mydb.cursor()

        mycursor.execute("select count(*),state from covid_patients group by state;")

        myresult = mycursor.fetchall()
        x=[]
        y=[]
        for i in myresult:
            x.append(i[1])
            y.append(i[0])
        barlist = plt.bar(x,y)
        barlist[5].set_color('r')
        plt.show()

    def Analyse_button_function(self):
        color=["blue","blue","blue","blue","blue","blue","blue","blue"]
        if self.ui.punjab.isChecked():
            state = "Punjab"
            color[7] = "red"
        elif self.ui.delhi.isChecked():
            state = "Delhi"
            color[4] = "red"
        elif self.ui.Uttar_Pradesh.isChecked():
            state = "Uttar_Pradesh"
            color[3] = "red"
        elif self.ui.madhyapradesh.isChecked():
            state = "Madhya_Pradesh"
            color[2] = "red"
        elif self.ui.maharashtra.isChecked():
            state = "Maharashtra"
            color[0] = "red"
        elif self.ui.rajasthan.isChecked():
            state = "Rajasthan"
            color[6] = "red"
        elif self.ui.tamil_nadu.isChecked():
            state = "Tamilnadu"
            color[1] = "red"

        mycursor = mydb.cursor()

        mycursor.execute("select count(*),state from covid_patients group by state;")

        myresult = mycursor.fetchall()
        x=[]
        y=[]
        for i in myresult:
            x.append(i[1])
            y.append(i[0])
        barlist = plt.bar(x,y)
        if state == "Tamilnadu":
            barlist[1].set_color('r')
        elif state == "Rajasthan":
            barlist[6].set_color('r')
        elif state == "Maharashtra":
            barlist[0].set_color('r')
        elif state == "Madhya_Pradesh":
            barlist[2].set_color('r')
        elif state == "Uttar_Pradesh":
            barlist[3].set_color('r')
        elif state == "Delhi":
            barlist[4].set_color('r')
        elif state == "Punjab":
            barlist[7].set_color('r')
        plt.show()

    def calendarWidget_2_function(self):
        date = self.ui.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)
        date_to_string = date
        text_admit_update = self.ui.admit_update.toPlainText()
        text_discharge_update = self.ui.discharge_update.toPlainText()
        if text_admit_update == "":
            self.ui.admit_update.setPlainText(date_to_string)
        elif text_discharge_update == "":
            self.ui.discharge_update.setPlainText(date_to_string)

    def calendarWidget_function(self):
        date = self.ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        date_to_string = date
        text_admit_add = self.ui.admit_on_add.toPlainText()
        text_discharge_add = self.ui.discharge_add.toPlainText()
        if text_admit_add == "":
            self.ui.admit_on_add.setPlainText(date_to_string)
        elif text_discharge_add == "":
            self.ui.discharge_add.setPlainText(date_to_string)

    def listWidget_case_function(self):
        item = self.ui.listWidget_case.currentItem()
        self.ui.list_case_label.setText(item.text())

    def death_list_function(self):
        item = self.ui.death_list.currentItem()
        self.ui.selected_label.setText(item.text())

    def list_recovery_function(self):
        item = self.ui.list_recovery.currentItem()
        self.ui._recovery_label.setText(item.text())

    def update_page_button_function(self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_15)
        self.ui.add_page_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.update_page_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")

    def add_page_button_function(self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_14)
        self.ui.update_page_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.add_page_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")

    def other_state_button_function(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_10)
        self.ui.Select_state_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.Other_state_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")

    def select_state_button_function(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_9)
        self.ui.Other_state_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.Select_state_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")

    def discharge_add_function(self):
        if self.ui.discharge_add_checkbox.isChecked():
            self.ui.discharge_add.setEnabled(True)
        else :
            self.ui.discharge_add.setEnabled(False)
            self.ui.discharge_add.setText("")

    def discharge_update_function(self):
        if self.ui.discharge_check.isChecked():
            self.ui.discharge_update.setEnabled(True)
        else :
            self.ui.discharge_update.setEnabled(False)
            self.ui.discharge_update.toPlainText("")

    def btn_page_1_functions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        self.ui.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        UIFunctions.toggleMenu(self, 250, True)

    def btn_page_2_functions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.analysis_page)
        self.ui.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        UIFunctions.toggleMenu(self, 250, True)

    def btn_page_3_functions(self):
        self.ui.textEdit_2.setText("")
        self.ui.textEdit.setText("")
        self.ui.stackedWidget.setCurrentWidget(self.ui.data_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_5)
        UIFunctions.toggleMenu(self, 250, True)

    def login_button_function(self):
        username = self.ui.textEdit.toPlainText()
        password = self.ui.textEdit_2.toPlainText()
        mycursor = mydb.cursor()
        mycursor.execute("select * from users;")
        myresult = mycursor.fetchall()
        x = []
        y = []
        for i in myresult:
            x.append(i[0])
            y.append(i[1])
        if username in x and password in y:
            self.login_valid_functions()
        else:
            self.show_popup("Wrong username or password !!!")

    def login_valid_functions(self):
        print("hello")
        self.ui.stackedWidget.setCurrentWidget(self.ui.data_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
        self.ui.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")


    def btn_page_4_functions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.credits_page)
        self.ui.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n")
        self.ui.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.ui.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        UIFunctions.toggleMenu(self, 250, True)

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainWindow()
    sys.exit(app.exec_())
