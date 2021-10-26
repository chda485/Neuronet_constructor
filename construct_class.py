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
from keras import models, layers
import numpy as np

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
        self.neuronet = None
        
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
        self.currentItem = self.ui.list_layers.itemFromIndex(index[0])
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
            
    def construct_model(self):
        layers_count = self.ui.list_layers.rowCount()
        model = models.Sequentials()
        for i in layers_count:
            layer = self.ui.list_layers.item(i).text()
            layer_name = layer.split(':')[0]
            layer_settings = layer.replace(' ', '').split(';')
            layer_settings = [setting.split('=') for setting in layer_settings]
            
            if layer_name == "Dense":
                units = np.asarray([unit for unit in layer_settings if unit[0] == 'units'])
                units = int(units[0][1]) if len(units[0] != 0) else 32               
                activation = np.asarray([unit for unit in layer_settings if unit[0] == 'activation'])
                activation = activation[0][1] if len(activation[0]) != 0 else None
                use_bias = np.asarray([unit for unit in layer_settings if unit[0] == 'use_bias'])
                use_bias = use_bias[0][1] if len(use_bias[0] != 0) else True             
                kernel_initializer = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_initializer'])
                kernel_initializer = kernel_initializer[0][1] if len(
                                     kernel_initializer[0] != 0) else "glorot_uniform"          
                bias_initializer = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_initializer'])
                bias_initializer = bias_initializer[0][1] if len(bias_initializer[0] != 0) else "zeros"           
                kernel_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_regularizer'])
                kernel_regularizer = kernel_regularizer[0][1] if len(kernel_regularizer[0] != 0) else None               
                bias_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_regularizer'])
                bias_regularizer = bias_regularizer[0][1] if len(bias_regularizer[0] != 0) else None               
                activity_regularize = np.asarray([unit for unit in layer_settings if unit[0] == 'activity_regularize'])
                activity_regularize = activity_regularize[0][1] if len(activity_regularize[0] != 0) else None            
                kernel_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_constraint'])
                kernel_constraint = kernel_constraint[0][1] if len(kernel_constraint[0] != 0) else None             
                bias_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_constraint'])
                bias_constraint = bias_constraint[0][1] if len(bias_constraint[0] != 0) else None
                
                if len([sett for sett in layer_settings if set[0] == 'input_shape'][0]) != 0:
                    pass
                model.add(layers.Dense(units, activation=None, use_bias=True, kernel_initializer="glorot_uniform",
                                bias_initializer="zeros", kernel_regularizer=None, bias_regularizer=None,
                                activity_regularizer=None, kernel_constraint=None, bias_constraint=None))
            
        self.neuronet = model
        
    def send_model(self):
        if self.neuronet is not None:
            return True, self.neuronet
        else:
            return False, None
            
            
            

