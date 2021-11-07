from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from forms import check_window
import sys

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
        self.ui.construct_button.setEnabled(False)
        self.ui.list_of_weights.setEnabled(False)
        
        self.ui.list_check.clicked.connect(self.list_choice)
        self.ui.disk_check.clicked.connect(self.disk_choice)
        self.ui.construct_check.clicked.connect(self.construct_choice)
        self.ui.weights_check.stateChanged.connect(self.weights_choice)
        
        self.ui.construct_button.clicked.connect(self.proba)

    def list_choice(self):
        self.ui.list_of_nets.setEnabled(True)
        self.ui.list_of_weights.setEnabled(True)
        self.ui.weights_check.setEnabled(True)
        self.ui.disk_button.setEnabled(False)
        self.ui.construct_button.setEnabled(False)

    def disk_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.list_of_weights.setEnabled(False)
        self.ui.weights_check.setEnabled(False)
        self.ui.disk_button.setEnabled(True)
        self.ui.construct_button.setEnabled(False)

    def construct_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.list_of_weights.setEnabled(False)
        self.ui.weights_check.setEnabled(False)
        self.ui.disk_button.setEnabled(False)
        self.ui.construct_button.setEnabled(True)

    def weights_choice(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.list_of_weights.setEnabled(True)
        else: self.ui.list_of_weights.setEnabled(False)     

    def write(self, text):
        self.ui.console_train.append(str(text))
        
    def flush(self):
        sys.stdout = self.old_stdout
        
    def proba(self):
        print("proba")

        
