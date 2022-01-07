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
        self.stdout = sys.stdout

    def show_train(self):
        self.train_window = train_class.TrainWindow(old_stdout=self.stdout)
        sys.stdout = self.train_window
        #self.train_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.train_window.show()

    def show_construct(self):
        self.construct_window = construct_class.ConstructWindow(stdout=self.stdout)
        #self.construct_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.construct_window.show()

    def show_check(self):
        self.check_window = check_class.CheckWindow(old_stdout=self.stdout)
        sys.stdout = self.check_window
        #self.check_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.check_window.show()

'''
def prepare_dataset():
    import os, shutil
    PATH = r"/home/dmitry/Документы/17FlowerOxfordDataset"
    cats = os.listdir(PATH)
    train = os.path.join(PATH, 'train')
    os.mkdir(train)
    test = os.path.join(PATH, 'test')
    os.mkdir(test)
    val = os.path.join(PATH, 'validation')
    os.mkdir(val)
    for cat in cats:
        folder = os.path.join(PATH, cat)
        os.mkdir(os.path.join(train, cat))
        os.mkdir(os.path.join(test, cat))
        os.mkdir(os.path.join(val, cat))
        num_files = len(os.listdir(folder))
        for i, file in enumerate(os.listdir(folder)):
            if i <= int(num_files * 0.7):
                shutil.move(os.path.join(folder, file), os.path.join(train, cat, file))
            elif i > int(num_files * 0.7) and i <= int(num_files * 0.9):
                shutil.move(os.path.join(folder, file), os.path.join(val, cat, file))
            else:
                shutil.move(os.path.join(folder, file), os.path.join(test, cat, file))
'''   
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

