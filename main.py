import sys
from PyQt5 import QtWidgets, uic
 
from main_window import Ui_MainWindow
from pages import Ui_Form

import datetime

defaultdata = [[1, "Jean Luc", "M", "18", "Goma", "Maux de tete", "17-09-2024"],
               [2, "Jeanne Marie", "F", "19", "Goma", "Maux de tete", "17-09-2024"],]

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.resize(1200, 900)

        self.pushButton.clicked.connect(self.to_page2)


    def to_page2(self):
        Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.ui.acceuil.mousePressEvent = self.to_page_3
        self.ui.Liste.mousePressEvent = self.to_page_4
        self.sexe = ""
        self.ui.radioButton.toggled.connect(self.change_state)
        self.ui.radioButton_2.toggled.connect(self.change_state)
        self.ui.pushButton.clicked.connect(self.add_data)
        self.id_tab = 0
        for data in defaultdata:
            print(data)
            self.id_tab += 1
            self.ui.tableau.setRowCount(self.id_tab)
            for i in range(len(data)):
                self.ui.tableau.setItem(self.id_tab-1, i, QtWidgets.QTableWidgetItem(data[i]))
        self.setCentralWidget(Form)

    def to_page_3(self, event):
        self.ui.Liste.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(12, 129, 255);")
        self.ui.acceuil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(12, 129, 255);")
        self.ui.stackedWidget.setCurrentIndex(0)

    def to_page_4(self, event):
        self.ui.acceuil.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(12, 129, 255);")
        self.ui.Liste.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(12, 129, 255);")
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def add_data(self):
        date_actuelle = datetime.datetime.now()
        print(date_actuelle.strftime("%d-%m-%Y"))
        data = [self.id_tab+1, self.ui.lineEdit.text(), self.sexe, self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text(), date_actuelle.strftime("%d-%m-%Y")]
        self.id_tab += 1
        self.ui.tableau.setRowCount(self.id_tab)
        for i in range(len(data)):
            self.ui.tableau.setItem(self.id_tab-1, i, QtWidgets.QTableWidgetItem(data[i]))
        self.to_page_4("")

    def change_state(self):
        if self.ui.radioButton.isChecked():
            self.sexe = "M"
        elif self.ui.radioButton_2.isChecked():
            self.sexe = "F"
        else:
            self.sexe = ""
        print(self.sexe)

 
 
app = QtWidgets.QApplication(sys.argv)
 
window = MainWindow()
window.show()
app.exec()