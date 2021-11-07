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
#from keras import models, layers
import numpy as np

class ConstructWindow(QMainWindow):
    def __init__(self, stdout=None, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = construct_window.Ui_MainWindow()
        self.ui.setupUi(self)
        # установка вывода в консоль если делали перенаправление, для корректной работы отладочных print
        self.stdout = stdout
        sys.stdout = stdout

        self.ui.close_button.clicked.connect(self.close)
        self.ui.add_button.clicked.connect(self.show_layers)
        self.ui.change_button.clicked.connect(lambda: self.show_layers(collect=True))
        self.ui.delete_button.clicked.connect(lambda: self.delete_layers(self.ui.list_layers.selectedIndexes()))
        self.ui.file_check.stateChanged.connect(self.file_choice)
        self.ui.diagramm_path.clicked.connect(self.path_choice)
        self.l_win = None
        self.currentItem = None
        
        self.model = QtGui.QStandardItemModel(parent=self)
        self.changed_layer = None
        
        self.ui.list_layers.setModel(self.model)
        self.neuronet = None
        self.path_to_model = None
        self.ui.diagramm_path.setEnabled(False)

    def file_choice(self):
        if self.ui.file_check.isChecked():
            self.ui.diagramm_path.setEnabled(True)
        else:
            self.ui.diagramm_path.setEnabled(False)

    def path_choice(self):
        # читаем путь к файлу модели
        path = QtWidgets.QFileDialog.getSaveFileName(self,
                                                     filter="Keras model file (*.h5)")
        if len(path[0]) > 0:
            print(path[0])
            self.path_to_model = path[0]

    def show_layers(self, collect=False):
        #если окно вызывается из кнопки "изменить слой"
        if collect:
            ind, layer = self.collect_layer()
            #когда нажмали кнопку "изменить", а слой не выбрали
            if layer is not None:
                self.l_win = layers_class.Layers(current_layer=layer, index_change=ind)
            else:
                return
        else:
            self.l_win = layers_class.Layers()
        print("check")
        self.l_win.setWindowModality(QtCore.Qt.ApplicationModal)
        self.l_win.ui.addButton.clicked.connect(self.get_layers)
        self.l_win.show()
        
    def get_layers(self):
        status, layer, index = self.l_win.send_layer()
        if layer == -1:
            return
        self.l_win.close()
        #если пользователь собрал какой-то слой
        if status:
            #если до этого изменяли слой, то удаляем предыдущую версию
            if index is not None:
                self.model.removeRow(index)
            #создаем объект списка
            item = QtGui.QStandardItem(layer)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            item.setFont(font)
            #добавляем объект в модель списка
            if index is not None:
                self.model.insertRow(index, item)
            self.model.appendRow(item)
            
    def collect_layer(self):
        #индексы всех выбранных элементов списка
        index = self.ui.list_layers.selectedIndexes()
        #если выбрано больше одного элемента списка
        if len(index) > 1:
            QtWidgets.QMessageBox.information(self, "Ошибка", 
                                            "Пожалуйста, выбирете только один слой для редактирования")
            return None, None
        elif len(index) == 0:
            QtWidgets.QMessageBox.information(self, "Ошибка",
                                              "Не выбран слой для редактирования")
            return None, None
        #если выбран один объект списка, выбираем его по индексу и возвращаем его текст
        self.currentItem = self.model.itemFromIndex(index[0])
        #self.currentItem = self.ui.list_layers.itemFromIndex(index[0])
        return index[0].row(), self.currentItem.text()
        
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
            self.model.removeRow(layer.row())
            
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
                activity_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'activity_regularize'])
                activity_regularizer = activity_regularizer[0][1] if len(activity_regularizer[0] != 0) else None            
                kernel_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_constraint'])
                kernel_constraint = kernel_constraint[0][1] if len(kernel_constraint[0] != 0) else None             
                bias_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_constraint'])
                bias_constraint = bias_constraint[0][1] if len(bias_constraint[0] != 0) else None
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.Dense(input_shape = inputSh, units=units, activation=activation, use_bias=use_bias,
                                         kernel_initializer=kernel_initializer, bias_initializer=bias_initializer,
                                         kernel_regularizer=kernel_regularizer, bias_regularizer=bias_regularizer,
                                         activity_regularizer=activity_regularizer, kernel_constraint=kernel_constraint,
                                         bias_constraint=bias_constraint)
                else:
                    layer = layers.Dense(units, activation=activation, use_bias=use_bias,
                                         kernel_initializer=kernel_initializer, bias_initializer=bias_initializer,
                                         kernel_regularizer=kernel_regularizer, bias_regularizer=bias_regularizer,
                                         activity_regularizer=activity_regularizer, kernel_constraint=kernel_constraint,
                                         bias_constraint=bias_constraint)
            
            elif layer_name == "Activation":              
                activation = np.asarray([unit for unit in layer_settings if unit[0] == 'activation'])
                activation = activation[0][1] if len(activation[0]) != 0 else 'relu'
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.Activation(input_shape = inputSh, activation=activation)
                else:
                    layer = layers.Activation(activation=activation)
                    
            elif layer_name == "AveragePool2D":
                pool_size = np.asarray([unit for unit in layer_settings if unit[0] == 'pool_size'])
                pool_size = self.make_tuple(pool_size[0][1]) if len(pool_size) != 0 else (2,2)
                strides = np.asarray([unit for unit in layer_settings if unit[0] == 'strides'])
                strides = self.make_tuple(strides[0][1]) if len(strides) != 0 else None
                padding = np.asarray([unit for unit in layer_settings if unit[0] == 'padding'])
                padding = padding[0][1] if len(padding) != 0 else "valid"
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format) != 0 else None
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.AveragePooling2D(input_shape=inputSh, pool_size=pool_size,
                                                    strides=strides, padding=padding,
                                                    data_format=data_format)
                else:
                    layer = layers.AveragePooling2D(pool_size=pool_size,
                                                    strides=strides, padding=padding,
                                                    data_format=data_format)

            elif layer_name == "Conv2D":
                filters = np.asarray([unit for unit in layer_settings if unit[0] == 'filters'])
                filters = int(filters[0][1]) if len(filters[0] != 0) else 32               
                kernel_size = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_size'])
                kernel_size = self.make_tuple(kernel_size[0][1]) if len(kernel_size[0]) != 0 else (3,3) 
                strides = np.asarray([unit for unit in layer_settings if unit[0] == 'strides'])
                strides = self.make_tuple(strides[0][1]) if len(strides[0]) != 0 else (1,1)
                activation = np.asarray([unit for unit in layer_settings if unit[0] == 'activation'])
                activation = activation[0][1] if len(activation[0]) != 0 else 'relu'
                padding = np.asarray([unit for unit in layer_settings if unit[0] == 'padding'])
                padding = padding[0][1] if len(padding[0]) != 0 else "valid"
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                groups = np.asarray([unit for unit in layer_settings if unit[0] == 'groups'])
                groups = int(groups[0][1]) if len(groups[0] != 0) else 1              
                dilation_rate = np.asarray([unit for unit in layer_settings if unit[0] == 'dilation_rate'])
                dilation_rate = self.make_tuple(dilation_rate[0][1]) if len(dilation_rate[0]) != 0 else (1,1)                
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
                activity_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'activity_regularize'])
                activity_regularizer = activity_regularizer[0][1] if len(activity_regularizer[0] != 0) else None
                kernel_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_constraint'])
                kernel_constraint = kernel_constraint[0][1] if len(kernel_constraint[0] != 0) else None
                bias_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_constraint'])
                bias_constraint = bias_constraint[0][1] if len(bias_constraint[0] != 0) else None

                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.Conv2D(input_shape=inputSh, filters=filters, kernel_size=kernel_size, strides=strides,
                                          padding=padding, data_format=data_format, groups=groups, 
                                          dilation_rate=dilation_rate, activation=activation, use_bias=use_bias,
                                          kernel_initializer=kernel_initializer, bias_initializer=bias_initializer,
                                          kernel_regularizer=kernel_regularizer, bias_regularizer=bias_regularizer,
                                          activity_regularizer=activity_regularizer, kernel_constraint=kernel_constraint,
                                          bias_constraint=bias_constraint)
                else:
                    layer = layers.Conv2D(filters=filters, kernel_size=kernel_size, strides=strides,
                                          padding=padding, data_format=data_format, groups=groups, 
                                          dilation_rate=dilation_rate, activation=activation, use_bias=use_bias,
                                          kernel_initializer=kernel_initializer, bias_initializer=bias_initializer,
                                          kernel_regularizer=kernel_regularizer, bias_regularizer=bias_regularizer,
                                          activity_regularizer=activity_regularizer, kernel_constraint=kernel_constraint,
                                          bias_constraint=bias_constraint)
                    
            elif layer_name == "Conv2DTranspose":
                filters = np.asarray([unit for unit in layer_settings if unit[0] == 'filters'])
                filters = int(filters[0][1]) if len(filters[0] != 0) else 32               
                kernel_size = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_size'])
                kernel_size = self.make_tuple(kernel_size[0][1]) if len(kernel_size[0]) != 0 else (3,3)
                strides = np.asarray([unit for unit in layer_settings if unit[0] == 'strides'])
                strides = self.make_tuple(strides[0][1]) if len(strides[0]) != 0 else (1,1)
                activation = np.asarray([unit for unit in layer_settings if unit[0] == 'activation'])
                activation = activation[0][1] if len(activation[0]) != 0 else 'relu'
                padding = np.asarray([unit for unit in layer_settings if unit[0] == 'padding'])
                padding = padding[0][1] if len(padding[0]) != 0 else "valid"
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                output_padding = np.asarray([unit for unit in layer_settings if unit[0] == 'output_padding'])
                output_padding = self.make_tuple(output_padding[0][1]) if len(output_padding[0] != 0) else None              
                dilation_rate = np.asarray([unit for unit in layer_settings if unit[0] == 'dilation_rate'])
                dilation_rate = self.make_tuple(dilation_rate[0][1]) if len(dilation_rate[0]) != 0 else (1,1)                
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
                activity_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'activity_regularize'])
                activity_regularizer = activity_regularizer[0][1] if len(activity_regularizer[0] != 0) else None
                kernel_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_constraint'])
                kernel_constraint = kernel_constraint[0][1] if len(kernel_constraint[0] != 0) else None
                bias_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_constraint'])
                bias_constraint = bias_constraint[0][1] if len(bias_constraint[0] != 0) else None

                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.Conv2DTranspose(input_shape=inputSh, filters=filters, kernel_size=kernel_size,
                                          strides=strides, padding=padding, data_format=data_format, 
                                          output_padding=output_padding, dilation_rate=dilation_rate, activation=activation,
                                          use_bias=use_bias, kernel_initializer=kernel_initializer, 
                                          bias_initializer=bias_initializer, kernel_regularizer=kernel_regularizer,
                                          bias_regularizer=bias_regularizer, activity_regularizer=activity_regularizer,
                                          kernel_constraint=kernel_constraint, bias_constraint=bias_constraint)
                else:
                    layer = layers.Conv2DTranspose(filters=filters, kernel_size=kernel_size,
                                          strides=strides, padding=padding, data_format=data_format, 
                                          output_padding=output_padding, dilation_rate=dilation_rate, activation=activation,
                                          use_bias=use_bias, kernel_initializer=kernel_initializer, 
                                          bias_initializer=bias_initializer, kernel_regularizer=kernel_regularizer,
                                          bias_regularizer=bias_regularizer, activity_regularizer=activity_regularizer,
                                          kernel_constraint=kernel_constraint, bias_constraint=bias_constraint)
                    
            elif layer_name == "GlobalAveragePool2D":              
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.GlobalAveragePooling2D(input_shape = inputSh, data_format=data_format)
                else:
                    layer = layers.GlobalAveragePooling2D(data_format=data_format)
                    
            elif layer_name == "GlobalMaxPool2D":              
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.GlobalMaxPooling2D(input_shape = inputSh, data_format=data_format)
                else:
                    layer = layers.GlobalMaxPooling2D(data_format=data_format)
                    
            elif layer_name == "MaxPool2D":              
                pool_size = np.asarray([unit for unit in layer_settings if unit[0] == 'pool_size'])
                pool_size = self.make_tuple(pool_size[0][1]) if len(pool_size[0]) != 0 else (2,2)
                strides = np.asarray([unit for unit in layer_settings if unit[0] == 'strides'])
                strides = self.make_tuple(strides[0][1]) if len(strides[0]) != 0 else None
                padding = np.asarray([unit for unit in layer_settings if unit[0] == 'padding'])
                padding = padding[0][1] if len(padding[0]) != 0 else "valid"
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                
                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.MaxPooling2D(input_shape=inputSh, pool_size=pool_size,
                                                    strides=strides, padding=padding,
                                                    data_format=data_format)
                else:
                    layer = layers.MaxPooling2D(pool_size=pool_size,
                                                    strides=strides, padding=padding,
                                                    data_format=data_format)
                    
            elif layer_name == "SeparableConv2D":
                filters = np.asarray([unit for unit in layer_settings if unit[0] == 'filters'])
                filters = int(filters[0][1]) if len(filters[0] != 0) else 32               
                kernel_size = np.asarray([unit for unit in layer_settings if unit[0] == 'kernel_size'])
                kernel_size = self.make_tuple(kernel_size[0][1]) if len(kernel_size[0]) != 0 else (3,3)
                strides = np.asarray([unit for unit in layer_settings if unit[0] == 'strides'])
                strides = self.make_tuple(strides[0][1]) if len(strides[0]) != 0 else (1,1)
                activation = np.asarray([unit for unit in layer_settings if unit[0] == 'activation'])
                activation = activation[0][1] if len(activation[0]) != 0 else 'relu'
                padding = np.asarray([unit for unit in layer_settings if unit[0] == 'padding'])
                padding = padding[0][1] if len(padding[0]) != 0 else "valid"
                data_format = np.asarray([unit for unit in layer_settings if unit[0] == 'data_format']) 
                data_format = data_format[0][1] if len(data_format[0]) != 0 else None
                depth_multiplier = np.asarray([unit for unit in layer_settings if unit[0] == 'depth_multiplier'])
                depth_multiplier = int(depth_multiplier[0][1]) if len(depth_multiplier[0] != 0) else 1              
                dilation_rate = np.asarray([unit for unit in layer_settings if unit[0] == 'dilation_rate'])
                dilation_rate = self.make_tuple(dilation_rate[0][1]) if len(dilation_rate[0]) != 0 else (1,1)                
                use_bias = np.asarray([unit for unit in layer_settings if unit[0] == 'use_bias'])
                use_bias = use_bias[0][1] if len(use_bias[0] != 0) else True
                depthwise_initializer = np.asarray([unit for unit in layer_settings if unit[0] == 'depthwise_initializer'])                
                depthwise_initializer = depthwise_initializer[0][1] if len(
                    depthwise_initializer[0] != 0) else "glorot_uniform"
                pointwise_initializer = np.asarray([unit for unit in layer_settings if unit[0] == 'pointwise_initializer'])
                pointwise_initializer = pointwise_initializer[0][1] if len(pointwise_initializer[0] != 0) else "glorot_uniform"
                bias_initializer = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_initializer'])
                bias_initializer = bias_initializer[0][1] if len(bias_initializer[0] != 0) else "zeros"
                depthwise_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'depthwise_regularizer'])
                depthwise_regularizer = depthwise_regularizer[0][1] if len(depthwise_regularizer[0] != 0) else None
                pointwise_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'pointwise_regularizer'])
                pointwise_regularizer = pointwise_regularizer[0][1] if len(pointwise_regularizer[0] != 0) else None
                bias_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_regularizer'])
                bias_regularizer = bias_regularizer[0][1] if len(bias_regularizer[0] != 0) else None
                activity_regularizer = np.asarray([unit for unit in layer_settings if unit[0] == 'activity_regularize'])
                activity_regularizer = activity_regularizer[0][1] if len(activity_regularizer[0] != 0) else None
                depthwise_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'depthwise_constraint'])
                depthwise_constraint = depthwise_constraint[0][1] if len(depthwise_constraint[0] != 0) else None
                pointwise_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'pointwise_constraint'])
                pointwise_constraint = pointwise_constraint[0][1] if len(pointwise_constraint[0] != 0) else None
                bias_constraint = np.asarray([unit for unit in layer_settings if unit[0] == 'bias_constraint'])
                bias_constraint = bias_constraint[0][1] if len(bias_constraint[0] != 0) else None

                if len([sett for sett in layer_settings if sett[0] == 'input_shape'][0]) != 0:
                    inputSh = np.asarray([sett for sett in layer_settings if sett[0] == 'input_shape'])[0][1]
                    inputSh = tuple([int(i) for i in inputSh.split(',')])
                    layer = layers.SeparableConv2D(input_shape=inputSh, filters=filters, kernel_size=kernel_size, 
                                                   strides=strides, padding=padding, data_format=data_format, 
                                                   depth_multiplier=depth_multiplier, dilation_rate=dilation_rate,
                                                   activation=activation, use_bias=use_bias, depthwise_initializer=depthwise_initializer,
                                                   pointwise_initializer=pointwise_initializer, bias_initializer=bias_initializer,
                                                   depthwise_regularizer=depthwise_regularizer, pointwise_regularizer=pointwise_regularizer,
                                                   bias_regularizer=bias_regularizer, activity_regularizer=activity_regularizer,
                                                   depthwise_constraint=depthwise_constraint, pointwise_constraint=pointwise_constraint, 
                                                   bias_constraint=bias_constraint)
                else:
                    layer = layers.SeparableConv2D(filters=filters, kernel_size=kernel_size, 
                                                   strides=strides, padding=padding, data_format=data_format, 
                                                   depth_multiplier=depth_multiplier, dilation_rate=dilation_rate,
                                                   activation=activation, use_bias=use_bias, depthwise_initializer=depthwise_initializer,
                                                   pointwise_initializer=pointwise_initializer, bias_initializer=bias_initializer,
                                                   depthwise_regularizer=depthwise_regularizer, pointwise_regularizer=pointwise_regularizer,
                                                   bias_regularizer=bias_regularizer, activity_regularizer=activity_regularizer,
                                                   depthwise_constraint=depthwise_constraint, pointwise_constraint=pointwise_constraint, 
                                                   bias_constraint=bias_constraint)
                    
            model.add(layer)
            
        self.neuronet = model
        
    def send_model(self):
        if self.neuronet is not None:
            #если выбрана опция "сохранить сеть"
            if self.ui.file_check.isChecked():
                if self.path_to_model is None:
                    er_win = QtWidgets.QErrorMessage(self)
                    er_win.showMessage("Не выбран путь к сохраняемой модели")
                else:
                    self.neuronet.save(self.path_to_model)
            #если выбрана опция "показать диаграмму"
            if self.ui.diagram_check.isChecked():
                from keras.utils.vis_utils import plot_model
                from cv2 import imread, imshow
                plot_model('model.png', show_shapes=True,
                           show_dtype=True)
                img = imread('model.png')
                imshow("Neuronet diagramm", img)
                os.remove('model.png')
            return True, self.neuronet
        else:
            return False, None

    def make_tuple(self, str_tuple): #'(2,2)'
        if len(str_tuple == 1):
            return int(str_tuple)
        tup = str_tuple.split(',')
        return tuple([x for x in tup])
            
            
            

