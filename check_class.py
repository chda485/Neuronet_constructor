from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from forms import check_window
import sys
sys.path.append("utils")
from utils import helper

class CheckWindow(QMainWindow):
    def __init__(self, parent=None, old_stdout=None):
        QMainWindow.__init__(self, parent)
        self.ui = check_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.label.setFocus()
        self.old_stdout = old_stdout

        self.ui.list_check.setChecked(True)
        self.ui.disk_button.setEnabled(False)

        self.model_path = "" #путь к тестируемой модели
        self.example_path = "" #путь к файлу, на котором будет тестироваться модель

        self.ui.list_check.clicked.connect(self.list_choice)
        self.ui.disk_check.clicked.connect(self.disk_choice)
        self.ui.disk_button.clicked.connect(lambda: self.choice_file(0))
        self.ui.example_button.clicked.connect(lambda: self.choice_file(1))
        self.ui.list_of_nets.addItems(helper.LIST_READY_NETS)
        
        self.ui.check_button.clicked.connect(self.proba)

    def list_choice(self):
        self.ui.list_of_nets.setEnabled(True)
        self.ui.disk_button.setEnabled(False)

    def disk_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.disk_button.setEnabled(True)

    def choice_file(self, code):
        if code == 0:
            #читаем путь к выбранному файлу модели
            path = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        filter="Keras model file (*.h5)")
            #если путь был выбран
            if len(path[0]) != 0:
                self.ui.console_train.append("The path to the model: \n" + path[0])
                self.model_path = path[0]
        elif code == 1:
            # читаем путь к выбранному файлу примера
            path = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         filter="Image files (*.png, *.jpg)")
            # если путь был выбран
            if len(path[0]) != 0:
                self.ui.lineEdit.setText(path[0])
                self.example_path = path[0]

    def write(self, text):
        text = str(text).replace('\n', '').replace('0', '')
        self.ui.console_train.append(text)
        
    def flush(self):
        sys.stdout = self.old_stdout
        
    def proba(self):
        print("proba")

