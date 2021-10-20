from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from forms import main
import check_class, construct_class, train_class, sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_button.clicked.connect(self.close)
        self.ui.train_button.clicked.connect(self.show_train)
        self.ui.construct_button.clicked.connect(self.show_construct)
        self.ui.check_button.clicked.connect(self.show_check)
        self.ui.exit_button.setIcon(QtGui.QIcon('cutton_exit.jpg'))
        self.ui.exit_button.setIconSize(QtCore.QSize(70,70))

    def show_train(self):
        self.train_window = train_class.TrainWindow()
        self.train_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.train_window.show()

    def show_construct(self):
        self.construct_window = construct_class.ConstructWindow()
        self.construct_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.construct_window.show()

    def show_check(self):
        self.check_window = check_class.CheckWindow()
        
        sys.stdout = self.check_window
        
        self.check_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.check_window.show()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

        
