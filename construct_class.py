from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from forms import construct_window
import layers_class
import sys
import os
sys.path.append("utils")
from utils import helper 

class ConstructWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = construct_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.add_button.clicked.connect(self.show_layers)
        self.ui.change_button.clicked.connect(lambda: self.show_layers(collect=True))
        self.ui.delete_button.clicked.connect(lambda: self.delete_layers(self.ui.list_layers.selectedIndexes()))
        self.l_win = None
        self.currentItem = None
        
        self.model = QtGui.QStandardItemModel(parent=self)
        self.changed_layer = None
        
        self.ui.list_layers.setModel(self.model)
        
    def show_layers(self, collect=False):
        #если окно вызывается из кнопки "изменить слой"
        if collect:
            layer = self.collect_layer()
            self.l_win = layers_class.Layers(current_layer=layer)
        else:
            self.l_win = layers_class.Layers()
        self.l_win.setWindowModality(QtCore.Qt.ApplicationModal)
        self.l_win.ui.addButton.clicked.connect(self.get_layers)
        self.l_win.show()
        
    def get_layers(self):
        status, layer = self.l_win.send_layer()
        if layer == -1:
            return
        self.l_win.close()
        #если пользователь собрал какой-то слой
        if status:
            #создаем объект списка
            item = QtGui.QStandardItem(layer)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            item.setFont(font)
            #добавляем объект в модель списка
            self.model.appendRow(item)
            
    def collect_layer(self):
        #индексы всех выбранных элементов списка
        index = self.ui.list_layers.selectedIndexes()
        #если выбрано больше одного элемента списка
        if len(index) > 1:
            QtWidgets.QMessageBox.information(self, "Ошибка", 
                                            "Пожалуйста, выбирете только один слой для редактирования")
            return
        #если выбран один объект списка, выбираем его по индексу и возвращаем его текст
        self.currentItem = self.list_layers.itemFromIndex(index[0])
        return self.currentItem.text()
        
    def delete_layers(self, layers):
        #если ничего не выбрано для удаления
        if len(layers) == 0:
            QtWidgets.QMessageBox.information(self, "Ошибка", 
                                            "Не выбрано ни одного слоя")
            return
        #запрашиваем подтверждение удаления
        result = QtWidgets.QMessageBox.question(self, "Подтвержиение удаления",
                                                "Вы действительно хотите удалить {} слоёв".format(len(layers)))
        #если есть подтверждение (код кнопки 5)
        if result == 5:
            return
        for layer in layers:
            #построчно удаляем слои
            self.list_layers.removeRows(layer, 1)

