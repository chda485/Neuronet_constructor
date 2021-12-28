from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets
from forms import layers_window
import sys, os
sys.path.append("utils")
from utils import helper 

class Layers(QMainWindow):
    def __init__(self, current_layer=None, parent=None, index_change=None):
        QMainWindow.__init__(self, parent)
        self.ui = layers_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.inputShape = None
        self.index = index_change
        self.ui.label_3.setToolTip("Введите входную форму через запятую")
        self.ui.list.addItems(helper.LIST_LAYERS)
        self.ui.list.activated.connect(self.set_layers_settings)
        self.ui.checkIsInput.stateChanged.connect(self.choice_input)
        self.ui.closeButton.clicked.connect(self.close)
        if current_layer:
           self.insert_layer_settings(current_layer)
           self.ui.addButton.setText("Изменить")
        else:
            self.set_layers_settings(current="Activation")
            self.ui.addButton.setText("Добавить")


    def choice_input(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.inputShape.setEnabled(True)
        else:
            self.ui.inputShape.setEnabled(False)

    def hide_elements(self, number, bool_number=0):
        if number == 1:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(False)
            self.ui.par3_label.setVisible(False)
            self.ui.par4_label.setVisible(False)
            self.ui.par5_label.setVisible(False)
            self.ui.par6_label.setVisible(False)
            self.ui.par7_label.setVisible(False)
            self.ui.par8_label.setVisible(False)
            self.ui.par9_label.setVisible(False)
            self.ui.par10_label.setVisible(False)
            self.ui.par11_label.setVisible(False)
            self.ui.par12_label.setVisible(False)
            self.ui.par13_label.setVisible(False)
            self.ui.par14_label.setVisible(False)
            self.ui.par15_label.setVisible(False)
            self.ui.par16_label.setVisible(False)
            self.ui.par17_label.setVisible(False)
            self.ui.par18_label.setVisible(False)
            self.ui.par19_label.setVisible(False)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(False)
            self.ui.par3.setVisible(False)
            self.ui.par4.setVisible(False)
            self.ui.par5.setVisible(False)
            self.ui.par6.setVisible(False)
            self.ui.par7.setVisible(False)
            self.ui.par8.setVisible(False)
            self.ui.par9.setVisible(False)
            self.ui.par10.setVisible(False)
            self.ui.par11.setVisible(False)
            self.ui.par12.setVisible(False)
            self.ui.par13.setVisible(False)
            self.ui.par14.setVisible(False)
            self.ui.par15.setVisible(False)
            self.ui.par16.setVisible(False)
            self.ui.par17.setVisible(False)
            self.ui.par18.setVisible(False)
            self.ui.par19.setVisible(False)
            self.resize(565,320)
            self.ui.addButton.move(320, 280)
            self.ui.closeButton.move(440, 280)

        elif number == 2:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(True)
            self.ui.par3_label.setVisible(False)
            self.ui.par4_label.setVisible(False)
            self.ui.par5_label.setVisible(False)
            self.ui.par6_label.setVisible(False)
            self.ui.par7_label.setVisible(False)
            self.ui.par8_label.setVisible(False)
            self.ui.par9_label.setVisible(False)
            self.ui.par10_label.setVisible(False)
            self.ui.par11_label.setVisible(False)
            self.ui.par12_label.setVisible(False)
            self.ui.par13_label.setVisible(False)
            self.ui.par14_label.setVisible(False)
            self.ui.par15_label.setVisible(False)
            self.ui.par16_label.setVisible(False)
            self.ui.par17_label.setVisible(False)
            self.ui.par18_label.setVisible(False)
            self.ui.par19_label.setVisible(False)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(True)
            self.ui.par3.setVisible(False)
            self.ui.par4.setVisible(False)
            self.ui.par5.setVisible(False)
            self.ui.par6.setVisible(False)
            self.ui.par7.setVisible(False)
            self.ui.par8.setVisible(False)
            self.ui.par9.setVisible(False)
            self.ui.par10.setVisible(False)
            self.ui.par11.setVisible(False)
            self.ui.par12.setVisible(False)
            self.ui.par13.setVisible(False)
            self.ui.par14.setVisible(False)
            self.ui.par15.setVisible(False)
            self.ui.par16.setVisible(False)
            self.ui.par17.setVisible(False)
            self.ui.par18.setVisible(False)
            self.ui.par19.setVisible(False)
            self.resize(565,320)
            self.ui.addButton.move(320, 280)
            self.ui.closeButton.move(440, 280)
            
        elif number == 4:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(True)
            self.ui.par3_label.setVisible(True)
            self.ui.par4_label.setVisible(True)
            self.ui.par5_label.setVisible(False)
            self.ui.par6_label.setVisible(False)
            self.ui.par7_label.setVisible(False)
            self.ui.par8_label.setVisible(False)
            self.ui.par9_label.setVisible(False)
            self.ui.par10_label.setVisible(False)
            self.ui.par11_label.setVisible(False)
            self.ui.par12_label.setVisible(False)
            self.ui.par13_label.setVisible(False)
            self.ui.par14_label.setVisible(False)
            self.ui.par15_label.setVisible(False)
            self.ui.par16_label.setVisible(False)
            self.ui.par17_label.setVisible(False)
            self.ui.par18_label.setVisible(False)
            self.ui.par19_label.setVisible(False)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(True)
            self.ui.par3.setVisible(True)
            self.ui.par4.setVisible(True)
            self.ui.par5.setVisible(False)
            self.ui.par6.setVisible(False)
            self.ui.par7.setVisible(False)
            self.ui.par8.setVisible(False)
            self.ui.par9.setVisible(False)
            self.ui.par10.setVisible(False)
            self.ui.par11.setVisible(False)
            self.ui.par12.setVisible(False)
            self.ui.par13.setVisible(False)
            self.ui.par14.setVisible(False)
            self.ui.par15.setVisible(False)
            self.ui.par16.setVisible(False)
            self.ui.par17.setVisible(False)
            self.ui.par18.setVisible(False)
            self.ui.par19.setVisible(False)
            self.resize(565, 320)
            self.ui.addButton.move(320, 280)
            self.ui.closeButton.move(440, 280)

        elif number == 10:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(True)
            self.ui.par3_label.setVisible(True)
            self.ui.par4_label.setVisible(True)
            self.ui.par5_label.setVisible(True)
            self.ui.par6_label.setVisible(True)
            self.ui.par7_label.setVisible(True)
            self.ui.par8_label.setVisible(True)
            self.ui.par9_label.setVisible(True)
            self.ui.par10_label.setVisible(True)
            self.ui.par11_label.setVisible(False)
            self.ui.par12_label.setVisible(False)
            self.ui.par13_label.setVisible(False)
            self.ui.par14_label.setVisible(False)
            self.ui.par15_label.setVisible(False)
            self.ui.par16_label.setVisible(False)
            self.ui.par17_label.setVisible(False)
            self.ui.par18_label.setVisible(False)
            self.ui.par19_label.setVisible(False)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(True)
            self.ui.par3.setVisible(True)
            self.ui.par4.setVisible(True)
            self.ui.par5.setVisible(True)
            self.ui.par6.setVisible(True)
            self.ui.par7.setVisible(True)
            self.ui.par8.setVisible(True)
            self.ui.par9.setVisible(True)
            self.ui.par10.setVisible(True)
            self.ui.par11.setVisible(False)
            self.ui.par12.setVisible(False)
            self.ui.par13.setVisible(False)
            self.ui.par14.setVisible(False)
            self.ui.par15.setVisible(False)
            self.ui.par16.setVisible(False)
            self.ui.par17.setVisible(False)
            self.ui.par18.setVisible(False)
            self.ui.par19.setVisible(False)
            self.resize(565,440)
            self.ui.addButton.move(320, 400)
            self.ui.closeButton.move(440, 400)

        elif number == 16:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(True)
            self.ui.par3_label.setVisible(True)
            self.ui.par4_label.setVisible(True)
            self.ui.par5_label.setVisible(True)
            self.ui.par6_label.setVisible(True)
            self.ui.par7_label.setVisible(True)
            self.ui.par8_label.setVisible(True)
            self.ui.par9_label.setVisible(True)
            self.ui.par10_label.setVisible(True)
            self.ui.par11_label.setVisible(True)
            self.ui.par12_label.setVisible(True)
            self.ui.par13_label.setVisible(True)
            self.ui.par14_label.setVisible(True)
            self.ui.par15_label.setVisible(True)
            self.ui.par16_label.setVisible(True)
            self.ui.par17_label.setVisible(False)
            self.ui.par18_label.setVisible(False)
            self.ui.par19_label.setVisible(False)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(True)
            self.ui.par3.setVisible(True)
            self.ui.par4.setVisible(True)
            self.ui.par5.setVisible(True)
            self.ui.par6.setVisible(True)
            self.ui.par7.setVisible(True)
            self.ui.par8.setVisible(True)
            self.ui.par9.setVisible(True)
            self.ui.par10.setVisible(True)
            self.ui.par11.setVisible(True)
            self.ui.par12.setVisible(True)
            self.ui.par13.setVisible(True)
            self.ui.par14.setVisible(True)
            self.ui.par15.setVisible(True)
            self.ui.par16.setVisible(True)
            self.ui.par17.setVisible(False)
            self.ui.par18.setVisible(False)
            self.ui.par19.setVisible(False)
            self.resize(565,560)
            self.ui.addButton.move(320, 510)
            self.ui.closeButton.move(440, 510)

        elif number == 19:
            self.ui.par1_label.setVisible(True)
            self.ui.par2_label.setVisible(True)
            self.ui.par3_label.setVisible(True)
            self.ui.par4_label.setVisible(True)
            self.ui.par5_label.setVisible(True)
            self.ui.par6_label.setVisible(True)
            self.ui.par7_label.setVisible(True)
            self.ui.par8_label.setVisible(True)
            self.ui.par9_label.setVisible(True)
            self.ui.par10_label.setVisible(True)
            self.ui.par11_label.setVisible(True)
            self.ui.par12_label.setVisible(True)
            self.ui.par13_label.setVisible(True)
            self.ui.par14_label.setVisible(True)
            self.ui.par15_label.setVisible(True)
            self.ui.par16_label.setVisible(True)
            self.ui.par17_label.setVisible(True)
            self.ui.par18_label.setVisible(True)
            self.ui.par19_label.setVisible(True)
            self.ui.par1.setVisible(True)
            self.ui.par2.setVisible(True)
            self.ui.par3.setVisible(True)
            self.ui.par4.setVisible(True)
            self.ui.par5.setVisible(True)
            self.ui.par6.setVisible(True)
            self.ui.par7.setVisible(True)
            self.ui.par8.setVisible(True)
            self.ui.par9.setVisible(True)
            self.ui.par10.setVisible(True)
            self.ui.par11.setVisible(True)
            self.ui.par12.setVisible(True)
            self.ui.par13.setVisible(True)
            self.ui.par14.setVisible(True)
            self.ui.par15.setVisible(True)
            self.ui.par16.setVisible(True)
            self.ui.par17.setVisible(True)
            self.ui.par18.setVisible(True)
            self.ui.par19.setVisible(True)
            self.resize(565,560)
            self.ui.addButton.move(320, 510)
            self.ui.closeButton.move(440, 510)

        if bool_number==0: 
            self.ui.boolcheck1.setVisible(False)
        else:
            self.ui.boolcheck1.setVisible(True)
            
    def set_layers_settings(self, current=None):
        if self.ui.list.currentText() == "Activation" or current == "Activation":
            self.ui.par1_label.setText("Activation")
            self.ui.par1_label.setToolTip("Функция активации к предыдущему слою")
            self.hide_elements(number=1)
        
        elif self.ui.list.currentText() == "AveragePool2D" or current == "AveragePool2D" or (
            self.ui.list.currentText() == "MaxPooling2D" or current == "MaxPooling2D"):
            self.ui.par1_label.setText("Pool size")
            tooltip = "Фактор, сообразно которому идёт уменьшение пространственных измерений"
            self.ui.par1_label.setToolTip(tooltip)
            self.ui.par2_label.setText("Strides")
            self.ui.par2_label.setToolTip("Значение шага уменьшения")
            self.ui.par3_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Data format")
            self.ui.par4_label.setToolTip("Строка, описывающая порядок измерений во входных данных")
            self.hide_elements(number=4)

        elif self.ui.list.currentText() == "Conv2D" or current == "Conv2D":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setToolTip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setToolTip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setToolTip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setToolTip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setToolTip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setToolTip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Groups")
            self.ui.par8_label.setToolTip("Число групп, в которых вход разделяется вдоль оси каналов")
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setToolTip("Функция активации для слоя")
            self.ui.par10_label.setText("Kernel initializer")
            self.ui.par10_label.setToolTip("Инициализатор для весов матрицы ядра")
            self.ui.par11_label.setText("Bias initializer")
            self.ui.par11_label.setToolTip("Инициализатор биас-вектора")
            self.ui.par12_label.setText("Kernel regulizer")
            self.ui.par12_label.setToolTip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par13_label.setText("Bias regulizer")
            self.ui.par13_label.setToolTip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par14_label.setText("Activity regulizer")
            self.ui.par14_label.setToolTip("Функция регуляризации для выхода слоя")
            self.ui.par15_label.setText("Kernel constraint")
            self.ui.par15_label.setToolTip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par16_label.setText("Bias constraint")
            self.ui.par16_label.setToolTip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=16, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "Conv2DTranspose" or current == "Conv2DTranspose":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setToolTip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setToolTip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setToolTip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setToolTip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setToolTip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setToolTip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Out padding")
            self.ui.par8_label.setToolTip("Отступы вдоль высоты и ширины выхода")
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setToolTip("Функция активации для слоя")
            self.ui.par10_label.setText("Kernel initializer")
            self.ui.par10_label.setToolTip("Инициализатор для весов матрицы ядра")
            self.ui.par11_label.setText("Bias initializer")
            self.ui.par11_label.setToolTip("Инициализатор биас-вектора")
            self.ui.par12_label.setText("Kernel regulizer")
            self.ui.par12_label.setToolTip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par13_label.setText("Bias regulizer")
            self.ui.par13_label.setToolTip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par14_label.setText("Activity regulizer")
            self.ui.par14_label.setToolTip("Функция регуляризации для выхода слоя")
            self.ui.par15_label.setText("Kernel constraint")
            self.ui.par15_label.setToolTip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par16_label.setText("Bias constraint")
            self.ui.par16_label.setToolTip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=16, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "Dense" or current == "Dense":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setToolTip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Units")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Activation")
            self.ui.par3_label.setToolTip("Функция активации для слоя")
            self.ui.par4_label.setText("Kernel initializer")
            self.ui.par4_label.setToolTip("Инициализатор для весов матрицы ядра")
            self.ui.par5_label.setText("Bias initializer")
            self.ui.par5_label.setToolTip("Инициализатор биас-вектора")
            self.ui.par6_label.setText("Kernel regulizer")
            self.ui.par6_label.setToolTip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par7_label.setText("Bias regulizer")
            self.ui.par7_label.setToolTip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par8_label.setText("Activity regulizer")
            self.ui.par8_label.setToolTip("Функция регуляризации для выхода слоя")
            self.ui.par9_label.setText("Kernel constraint")
            self.ui.par9_label.setToolTip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par10_label.setText("Bias constraint")
            self.ui.par10_label.setToolTip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=10, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "GlobalAveragePool2D" or current == "GlobalAveragePool2D" or (
            self.ui.list.currentText() == "GlobalMaxPool2D" or current == "GlobalMaxPool2D"):
            self.ui.par1_label.setText("Data format")
            self.ui.par1_label.setToolTip("Строка, описывающая порядок измерений во входных данных")
            self.hide_elements(number=1)

        elif self.ui.list.currentText() == "SeparableConv2D" or current == "SeparableConv2D":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setToolTip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setToolTip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setToolTip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setToolTip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setToolTip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setToolTip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Depth multi")
            tooltip = "Количество выходных каналов сёрток по глубине для каждого входного канала"
            self.ui.par8_label.setToolTip(tooltip)
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setToolTip("Функция активации для слоя")
            self.ui.par10_label.setText("Depth initializer")
            self.ui.par10_label.setToolTip("Инициализатор для ядра свёрток по глубине")
            self.ui.par11_label.setText("Point initializer")
            self.ui.par11_label.setToolTip("Инициализатор для ядра свёрток по точкам")
            self.ui.par12_label.setText("Bias initializer")
            self.ui.par12_label.setToolTip("Инициализатор биас-вектора")
            self.ui.par13_label.setText("Depth regulizer")
            self.ui.par13_label.setToolTip("Функция регуляризации для матрицы глубинного ядра")
            self.ui.par14_label.setText("Point regulizer")
            self.ui.par14_label.setToolTip("Функция регуляризации для матрицы ядра точек")
            self.ui.par15_label.setText("Bias regulizer")
            self.ui.par15_label.setToolTip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par16_label.setText("Activity regulizer")
            self.ui.par16_label.setToolTip("Функция регуляризации для выхода слоя")
            self.ui.par17_label.setText("Depth constraint")
            self.ui.par17_label.setToolTip("Протяжённая функция, применяемая к глубинному ядру матрицы")
            self.ui.par18_label.setText("Point constraint")
            self.ui.par18_label.setToolTip("Протяжённая функция, применяемая к ядру точек матрицы")
            self.ui.par19_label.setText("Bias constraint")
            self.ui.par19_label.setToolTip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=19)
            self.ui.par1.setVisible(False)   
                
    def send_layer(self):
        results = ""
        settings = (self.ui.par1.text(), self.ui.par2.text(), self.ui.par3.text(),
                    self.ui.par4.text(), self.ui.par5.text(), self.ui.par6.text(),
                    self.ui.par7.text(), self.ui.par8.text(), self.ui.par9.text(),
                    self.ui.par10.text(), self.ui.par11.text(), self.ui.par12.text(),
                    self.ui.par13.text(), self.ui.par14.text(), self.ui.par15.text(),
                    self.ui.par16.text(), self.ui.par17.text(), self.ui.par18.text(),
                    self.ui.par19.text())
        bools = (self.ui.boolcheck1.isChecked(),)
        status = helper.check_settings(settings, bools)
        if not status and not (self.ui.list.currentText() == "GlobalAveragePool2D" or
                self.ui.list.currentText() == "GlobalMaxPool2D"):
            print(self.ui.list.currentText())
            return status, None, self.index
        if self.ui.checkIsInput.isChecked():
            status = helper.check_input(self.ui.inputShape.text())
            if status:
                self.inputShape = self.ui.inputShape.text()
            else:
                er_win = QtWidgets.QErrorMessage(self)
                er_win.showMessage("Не введена входная форма данных")
                return None, -1, self.index
            
        if self.ui.list.currentText() == "Activation":
            results += "Activation: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "activation=" + self.ui.par1.text() if len(self.ui.par1.text()) !=0 else ""
            return True, results, self.index

        elif self.ui.list.currentText() == "AveragePool2D":
            results += "AveragePooling2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "pool_size=" + self.ui.par1.text() + "; " if len(self.ui.par1.text()) !=0 else ""
            results += "strides=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "padding=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "data_format=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            return True, results[:-2], self.index

        elif self.ui.list.currentText() == "Conv2D":
            results += "Conv2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "filters=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "kernel_size=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "strides=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            results += "padding=" + self.ui.par5.text() + "; " if len(self.ui.par5.text()) !=0 else ""
            results += "data_format=" + self.ui.par6.text() + "; " if len(self.ui.par6.text()) !=0 else ""
            results += "dilation_rate=" + self.ui.par7.text() + "; " if len(self.ui.par7.text()) !=0 else ""
            results += "groups=" + self.ui.par8.text() + "; " if len(self.ui.par8.text()) !=0 else ""
            results += "activation=" + self.ui.par9.text() + "; " if len(self.ui.par9.text()) !=0 else ""
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + "; "
            results += "kernel_initializer=" + self.ui.par10.text() + "; " if len(
                self.ui.par10.text()) !=0 else ""
            results += "bias_initializer=" + self.ui.par11.text() + "; " if len(self.ui.par11.text()) !=0 else ""
            results += "kernel_regularizer=" + self.ui.par12.text() + "; " if len(self.ui.par12.text()) !=0 else ""
            results += "bias_regularizer=" + self.ui.par13.text() + "; " if len(self.ui.par13.text()) !=0 else ""
            results += "activity_regularizer=" + self.ui.par14.text() + "; " if len(self.ui.par14.text()) !=0 else ""
            results += "kernel_constraint=" + self.ui.par15.text() + "; " if len(self.ui.par15.text()) !=0 else ""
            results += "bias_constraint=" + self.ui.par16.text() + "; " if len(self.ui.par16.text()) !=0 else ""
            return True, results[:-2], self.index

        elif self.ui.list.currentText() == "Conv2DTranspose":
            results += "Conv2DTranspose: " 
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "filters=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "kernel_size=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "strides=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            results += "padding=" + self.ui.par5.text() + "; " if len(self.ui.par5.text()) !=0 else ""
            results += "data_format=" + self.ui.par6.text() + "; " if len(self.ui.par6.text()) !=0 else ""
            results += "dilation_rate=" + self.ui.par7.text() + "; " if len(self.ui.par7.text()) !=0 else ""
            results += "output_padding=" + self.ui.par8.text() + "; " if len(self.ui.par8.text()) !=0 else ""
            results += "activation=" + self.ui.par9.text() + "; " if len(self.ui.par9.text()) !=0 else ""
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + "; "
            results += "kernel_initializer=" + self.ui.par10.text() + "; " if len(self.ui.par10.text()) !=0 else ""
            results += "bias_initializer=" + self.ui.par11.text() + "; " if len(self.ui.par11.text()) !=0 else ""
            results += "kernel_regularizer=" + self.ui.par12.text() + "; " if len(self.ui.par12.text()) !=0 else ""
            results += "bias_regularizer=" + self.ui.par13.text() + "; " if len(self.ui.par13.text()) !=0 else ""
            results += "activity_regularizer=" + self.ui.par14.text() + "; " if len(self.ui.par14.text()) !=0 else ""
            results += "kernel_constraint=" + self.ui.par15.text() + "; " if len(self.ui.par15.text()) !=0 else ""
            results += "bias_constraint=" + self.ui.par16.text() + "; " if len(self.ui.par16.text()) !=0 else ""
            return True, results[:-2], self.index

        elif self.ui.list.currentText() == "Dense":
            results += "Dense: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "units=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "activation=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + "; "
            results += "kernel_initializer=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            results += "bias_initializer=" + self.ui.par5.text() + "; " if len(self.ui.par5.text()) !=0 else ""
            results += "kernel_regularizer=" + self.ui.par6.text() + "; " if len(self.ui.par6.text()) !=0 else ""
            results += "bias_regularizer=" + self.ui.par7.text() + "; " if len(self.ui.par7.text()) !=0 else ""
            results += "activity_regularizer=" + self.ui.par8.text() + "; " if len(self.ui.par8.text()) !=0 else ""
            results += "kernel_constraint=" + self.ui.par9.text() + "; " if len(self.ui.par9.text()) !=0 else ""
            results += "bias_constraint=" + self.ui.par10.text() + "; " if len(self.ui.par10.text()) !=0 else ""
            return True, results[:-2], self.index

        elif self.ui.list.currentText() == "GlobalAveragePool2D":
            results += "GlobalAveragePooling2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "data_format=" + self.ui.par2.text() if len(self.ui.par1.text()) !=0 else ""
            if results.endswith(": "):
                results = results[:-2]
            return True, results, self.index

        elif self.ui.list.currentText() == "GlobalMaxPool2D":
            results += "GlobalMaxPooling2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "data_format=" + self.ui.par2.text() if len(self.ui.par1.text()) !=0 else ""
            if results.endswith(": "):
                results = results[:-2]
            return True, results, self.index

        elif self.ui.list.currentText() == "MaxPooling2D":
            results += "MaxPooling2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "pool_size=" + self.ui.par1.text() + "; " if len(self.ui.par1.text()) !=0 else ""
            results += "strides=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "padding=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "data_format=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            return True, results[:-2], self.index

        elif self.ui.list.currentText() == "SeparableConv2D":
            results += "SeparableConv2D: "
            if len(self.ui.inputShape.text()) != 0:
                results += "input_shape=" + self.ui.inputShape.text() + "; "
            results += "filters=" + self.ui.par2.text() + "; " if len(self.ui.par2.text()) !=0 else ""
            results += "kernel_size=" + self.ui.par3.text() + "; " if len(self.ui.par3.text()) !=0 else ""
            results += "strides=" + self.ui.par4.text() + "; " if len(self.ui.par4.text()) !=0 else ""
            results += "padding=" + self.ui.par5.text() + "; " if len(self.ui.par5.text()) !=0 else ""
            results += "data_format=" + self.ui.par6.text() + "; " if len(self.ui.par6.text()) !=0 else ""
            results += "dilation_rate=" + self.ui.par7.text() + "; " if len(self.ui.par7.text()) !=0 else ""
            results += "depth_multiplier=" + self.ui.par8.text() + "; " if len(self.ui.par8.text()) !=0 else ""
            results += "activation=" + self.ui.par9.text() + "; " if len(self.ui.par9.text()) !=0 else ""
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + "; "
            results += "depthwise_initializer=" + self.ui.par10.text() + "; " if len(self.ui.par10.text()) !=0 else ""
            results += "pointwise_initializer=" + self.ui.par11.text() + "; " if len(self.ui.par11.text()) !=0 else ""
            results += "bias_initializer=" + self.ui.par12.text() + "; " if len(self.ui.par12.text()) !=0 else ""
            results += "depthwise_regularizer=" + self.ui.par13.text() + "; " if len(self.ui.par13.text()) !=0 else ""
            results += "pointwise_regularizer=" + self.ui.par14.text() + "; " if len(self.ui.par14.text()) !=0 else ""
            results += "bias_regularizer=" + self.ui.par15.text() + "; " if len(self.ui.par15.text()) !=0 else ""
            results += "activity_regularizer=" + self.ui.par16.text() + "; " if len(self.ui.par16.text()) !=0 else ""
            results += "depthwise_constraint=" + self.ui.par17.text() + "; " if len(self.ui.par17.text()) !=0 else ""
            results += "pointwise_constraint=" + self.ui.par18.text() + "; " if len(self.ui.par18.text()) !=0 else ""
            results += "bias_constraint=" + self.ui.par19.text() + "; " if len(self.ui.par19.text()) !=0 else ""
            return True, results[:-2], self.index
            
    def insert_layer_settings(self, layer):
        #берём имя слоя, оно слева от :
        layer_name = layer.split(':')[0]
        self.ui.list.setCurrentText(layer_name)
        #устанавливаем нужные поля настроек для переданного слоя
        self.set_layers_settings(current=layer_name)
        #получаем все переданные настройки в список элементов имя=значение
        settings = layer.split(': ')[1].split('; ')
        #разделяем каждый элемент по '='
        settings = [item.split('=') for item in settings]
        #проверяем, была ли среди настроек указана форма входных данных
        inputShape = [value for value in settings if value[0] == "input_shape"]
        if len(inputShape) != 0:
            self.inputShape.setText(inputShape[0][1])
        
        if layer_name == "Activation":
            self.ui.par1.setText(
                [value for value in settings if value[0] == "activation"][0][1])
        
        elif layer_name == "AveragePool2D" or layer_name == "MaxPool2D":
            self.ui.par1.setText(
                [value for value in settings if value[0] == "pool_size"][0][1])
            self.ui.par2.setText(
                [value for value in settings if value[0] == "strides"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "padding"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "data_format"][0][1])

        elif layer_name == "Conv2D":
            self.ui.par2.setText(
                [value for value in settings if value[0] == "filters"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "kernel_size"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "strides"][0][1])
            self.ui.par5.setText(
                [value for value in settings if value[0] == "padding"][0][1])
            self.ui.par6.setText(
                [value for value in settings if value[0] == "data_format"][0][1])
            self.ui.par7.setText(
                [value for value in settings if value[0] == "dilation_rate"][0][1])
            self.ui.par8.setText(
                [value for value in settings if value[0] == "groups"][0][1])
            self.ui.par9.setText(
                [value for value in settings if value[0] == "activation"][0][1])
            self.ui.par10.setText(
                [value for value in settings if value[0] == "kernel_initializer"][0][1])
            self.ui.par11.setText(
                [value for value in settings if value[0] == "bias_initializer"][0][1])
            self.ui.par12.setText(
                [value for value in settings if value[0] == "kernel_regularizer"][0][1])
            self.ui.par13.setText(
                [value for value in settings if value[0] == "bias_regularizer"][0][1])
            self.ui.par14.setText(
                [value for value in settings if value[0] == "activity_regularizer"][0][1])
            self.ui.par15.setText(
                [value for value in settings if value[0] == "kernel_constraint"][0][1])
            self.ui.par16.setText(
                [value for value in settings if value[0] == "bias_constraint"][0][1])
            self.ui.boolcheck1.setCheckState(2) if len(
                [value for value in settings if value[0] == "use_bias"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)
            
        elif layer_name == "Conv2DTranspose":
            self.ui.par2.setText(
                [value for value in settings if value[0] == "filters"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "kernel_size"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "strides"][0][1])
            self.ui.par5.setText(
                [value for value in settings if value[0] == "padding"][0][1])
            self.ui.par6.setText(
                [value for value in settings if value[0] == "data_format"][0][1])
            self.ui.par7.setText(
                [value for value in settings if value[0] == "dilation_rate"][0][1])
            self.ui.par8.setText(
                [value for value in settings if value[0] == "groups"][0][1])
            self.ui.par9.setText(
                [value for value in settings if value[0] == "activation"][0][1])
            self.ui.par10.setText(
                [value for value in settings if value[0] == "kernel_initializer"][0][1])
            self.ui.par11.setText(
                [value for value in settings if value[0] == "bias_initializer"][0][1])
            self.ui.par12.setText(
                [value for value in settings if value[0] == "kernel_regularizer"][0][1])
            self.ui.par13.setText(
                [value for value in settings if value[0] == "bias_regularizer"][0][1])
            self.ui.par14.setText(
                [value for value in settings if value[0] == "activity_regularizer"][0][1])
            self.ui.par15.setText(
                [value for value in settings if value[0] == "kernel_constraint"][0][1])
            self.ui.par16.setText(
                [value for value in settings if value[0] == "bias_constraint"][0][1])
            self.ui.boolcheck1.setCheckState(2) if len(
                [value for value in settings if value[0] == "use_bias"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)

        elif layer_name == "Dense":
            self.ui.par2.setText(
                [value for value in settings if value[0] == "units"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "activation"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "kernel_initializer"][0][1])
            self.ui.par5.setText(
                [value for value in settings if value[0] == "bias_initializer"][0][1])
            self.ui.par6.setText(
                [value for value in settings if value[0] == "kernel_regularizer"][0][1])
            self.ui.par7.setText(
                [value for value in settings if value[0] == "bias_regularizer"][0][1])
            self.ui.par8.setText(
                [value for value in settings if value[0] == "activity_regularizer"][0][1])
            self.ui.par9.setText(
                [value for value in settings if value[0] == "kernel_constraint"][0][1])
            self.ui.par10.setText(
                [value for value in settings if value[0] == "bias_constraint"][0][1])
            self.ui.boolcheck1.setCheckState(2) if len(
                [value for value in settings if value[0] == "use_bias"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)

        elif layer_name == "GlobalAveragePool2D" or layer_name == "GlobalMaxPool2D":
            self.ui.par1.setText(
                [value for value in settings if value[0] == "data_format"][0][1])

        elif layer_name == "SeparableConv2D":
            self.ui.par2.setText(
                [value for value in settings if value[0] == "filters"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "kernel_size"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "strides"][0][1])
            self.ui.par5.setText(
                [value for value in settings if value[0] == "padding"][0][1])
            self.ui.par6.setText(
                [value for value in settings if value[0] == "data_format"][0][1])
            self.ui.par7.setText(
                [value for value in settings if value[0] == "dilation_rate"][0][1])
            self.ui.par8.setText(
                [value for value in settings if value[0] == "depth_multiplier"][0][1])
            self.ui.par9.setText(
                [value for value in settings if value[0] == "activation"][0][1])
            self.ui.par10.setText(
                [value for value in settings if value[0] == "depthwise_initializer"][0][1])
            self.ui.par11.setText(
                [value for value in settings if value[0] == "pointwise_initializer"][0][1])
            self.ui.par12.setText(
                [value for value in settings if value[0] == "bias_initializer"][0][1])
            self.ui.par13.setText(
                [value for value in settings if value[0] == "depthwise_regularizerr"][0][1])
            self.ui.par14.setText(
                [value for value in settings if value[0] == "pointwise_regularizerr"][0][1])
            self.ui.par15.setText(
                [value for value in settings if value[0] == "bias_regularizer"][0][1])
            self.ui.par16.setText(
                [value for value in settings if value[0] == "activity_regularizer"][0][1])
            self.ui.par17.setText(
                [value for value in settings if value[0] == "depthwise_constraint"][0][1])
            self.ui.par18.setText(
                [value for value in settings if value[0] == "pointwise_constraint"][0][1])
            self.ui.par19.setText(
                [value for value in settings if value[0] == "bias_constraint"][0][1])
            self.ui.boolcheck1.setCheckState(2) if len(
                [value for value in settings if value[0] == "use_bias"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)

