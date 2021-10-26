from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from forms import layers_window
import sys, os
sys.path.append("utils")
from utils import helper 

class Layers(QMainWindow):
    def __init__(self, current_layer=None, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = layers_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.inputShape = None
        self.ui.label3.setTooltip("Введите входную форму через запятую")
        self.ui.list.addItems(helper.LIST_LAYERS)
        self.ui.checkIsInput.stateChanged.connect(self.choice_input)
        if current_layer:
           self.insert_layer_setting(current_layer)


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
            self.resize(525,320)
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
            self.resize(525,320)
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
            self.resize(525, 320)
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
            self.resize(525,440)
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
            self.resize(525,560)
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
            self.resize(525,560)
            self.ui.addButton.move(320, 510)
            self.ui.closeButton.move(440, 510)

        if bool_number==0:
            self.ui.boolcheck1.setVisible(False)
        else:
            self.ui.boolcheck1.setVisible(True)
            
    def set_layers_settings(self, current=None):
        if self.ui.list.currentText() == "Activation" or current == "Activation":
            self.ui.par1_label.setText("Activation")
            self.ui.par1_label.setTooltip("Функция активации к предыдущему слою")
            self.hide_elements(number=1)
        
        elif self.ui.list.currentText() == "AveragePool2D" or current == "AveragePool2D" or (
            self.ui.list.currentText() == "MaxPool2D" or current == "MaxPool2D"):
            self.ui.par1_label.setText("Pool size")
            tooltip = "Фактор, сообразно которому идёт уменьшение пространственных измерений"
            self.ui.par1_label.setTooltip(tooltip)
            self.ui.par2_label.setText("Strides")
            self.ui.par2_label.setTooltip("Значение шага уменьшения")
            self.ui.par3_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par3_label.setTooltip(tooltip)
            self.ui.par4_label.setText("Data format")
            self.ui.par4_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.hide_elements(number=4)

        elif self.ui.list.currentText() == "Conv2D" or current == "Conv2D":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setTooltip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setTooltip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setTooltip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setTooltip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Groups")
            self.ui.par8_label.setTooltip("Число групп, в которых вход разделяется вдоль оси каналов")
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setTooltip("Функция активации для слоя")
            self.ui.par10_label.setText("Kernel initializer")
            self.ui.par10_label.setTooltip("Инициализатор для весов матрицы ядра")
            self.ui.par11_label.setText("Bias initializer")
            self.ui.par11_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par12_label.setText("Kernel regulizer")
            self.ui.par12_label.setTooltip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par13_label.setText("Bias regulizer")
            self.ui.par13_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par14_label.setText("Activity regulizer")
            self.ui.par14_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par15_label.setText("Kernel constraint")
            self.ui.par15_label.setTooltip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par16_label.setText("Bias constraint")
            self.ui.par16_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=16, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "Conv2DTranspose" or current == "Conv2DTranspose":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setTooltip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setTooltip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setTooltip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setTooltip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Out padding")
            self.ui.par8_label.setTooltip("Отступы вдоль высоты и ширины выхода")
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setTooltip("Функция активации для слоя")
            self.ui.par10_label.setText("Kernel initializer")
            self.ui.par10_label.setTooltip("Инициализатор для весов матрицы ядра")
            self.ui.par11_label.setText("Bias initializer")
            self.ui.par11_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par12_label.setText("Kernel regulizer")
            self.ui.par12_label.setTooltip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par13_label.setText("Bias regulizer")
            self.ui.par13_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par14_label.setText("Activity regulizer")
            self.ui.par14_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par15_label.setText("Kernel constraint")
            self.ui.par15_label.setTooltip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par16_label.setText("Bias constraint")
            self.ui.par16_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=16, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "Dense" or current == "Dense":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Units")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Activation")
            self.ui.par3_label.setTooltip("Функция активации для слоя")
            self.ui.par4_label.setText("Kernel initializer")
            self.ui.par4_label.setTooltip("Инициализатор для весов матрицы ядра")
            self.ui.par5_label.setText("Bias initializer")
            self.ui.par5_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par6_label.setText("Kernel regulizer")
            self.ui.par6_label.setTooltip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par7_label.setText("Bias regulizer")
            self.ui.par7_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par8_label.setText("Activity regulizer")
            self.ui.par8_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par9_label.setText("Kernel constraint")
            self.ui.par9_label.setTooltip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par10_label.setText("Bias constraint")
            self.ui.par10_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=10, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "GlobalAveragePool2D" or current == "GlobalAveragePool2D" or (
            self.ui.list.currentText() == "GlobalMaxPool2D" or current == "GlobalMaxPool2D"):
            self.ui.par1_label.setText("Data format")
            self.ui.par1_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.hide_elements(number=1)

        elif self.ui.list.currentText() == "SeparableConv2D" or current == "SeparableConv2D":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setTooltip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setTooltip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setTooltip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setTooltip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Depth multi")
            tooltip = "Количество выходных каналов сёрток по глубине для каждого входного канала"
            self.ui.par8_label.setTooltip(tooltip)
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setTooltip("Функция активации для слоя")
            self.ui.par10_label.setText("Depth initializer")
            self.ui.par10_label.setTooltip("Инициализатор для ядра свёрток по глубине")
            self.ui.par11_label.setText("Point initializer")
            self.ui.par11_label.setTooltip("Инициализатор для ядра свёрток по точкам")
            self.ui.par12_label.setText("Bias initializer")
            self.ui.par12_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par13_label.setText("Depth regulizer")
            self.ui.par13_label.setTooltip("Функция регуляризации для матрицы глубинного ядра")
            self.ui.par14_label.setText("Point regulizer")
            self.ui.par14_label.setTooltip("Функция регуляризации для матрицы ядра точек")
            self.ui.par15_label.setText("Bias regulizer")
            self.ui.par15_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par16_label.setText("Activity regulizer")
            self.ui.par16_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par17_label.setText("Depth constraint")
            self.ui.par17_label.setTooltip("Протяжённая функция, применяемая к глубинному ядру матрицы")
            self.ui.par18_label.setText("Point constraint")
            self.ui.par18_label.setTooltip("Протяжённая функция, применяемая к ядру точек матрицы")
            self.ui.par19_label.setText("Bias constraint")
            self.ui.par19_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
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
        bools = (self.ui.boolcheck1.isChecked())
        status = helper.check_settings(settings, bools)
        if not status:
            return status, None
        if self.ui.checkIsInput.isChecked():
            status = helper.check_input(self.ui.inputShape.text())
            if status:
                self.inputShape = self.ui.inputShape.text()
            else:
                er_win = QtWidgets.QErrirMessage(self)
                er_win.shoMessage("Не введена входная форма данных")
                return _, -1
            
        if self.ui.list.currentText() == "Activation":
            results += "Activation: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "activation=" + self.ui.par1.text() if len(self.ui.par1.text()) !=0 else "relu"
            return True, results

        elif self.ui.list.currentText() == "AveragePool2D":
            results += "AveragePooling2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "pool_size=" + self.ui.par1.text() if len(self.ui.par1.text()) !=0 else "(2,2)" + "; "
            results += "strides=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "None" + "; "
            results += "padding=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "valid" + "; "
            results += "data_format=" + self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "None"
            return True, results

        elif self.ui.list.currentText() == "Conv2D":
            results += "Conv2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "filters=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "32" + "; "
            results += "kernel_size=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "(1,1)" + "; "
            results += "strides=" + self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "(1,1)" + "; "
            results += "padding=" + self.ui.par5.text() if len(self.ui.par5.text()) !=0 else "valid" + "; "
            results += "data_format=" + self.ui.par6.text() if len(self.ui.par6.text()) !=0 else "None" + "; "
            results += "dilation_rate=" + self.ui.par7.text() if len(self.ui.par7.text()) !=0 else "(1,1)" + "; "
            results += "groups=" + self.ui.par8.text() if len(self.ui.par8.text()) !=0 else "1" + ";"
            results += "activation=" + self.ui.par9.text() if len(self.ui.par9.text()) !=0 else "None" + "; "
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + ";"
            results += "kernel_initializer="
            results += self.ui.par10.text() if len(self.ui.par10.text()) !=0 else "glorot_uniform" + "; "
            results += "bias_initializer="
            results += self.ui.par11.text() if len(self.ui.par11.text()) !=0 else "zeros" + "; "
            results += "kernel_regularizer="
            results += self.ui.par12.text() if len(self.ui.par12.text()) !=0 else "None" + "; "
            results += "bias_regularizer="
            results += self.ui.par13.text() if len(self.ui.par13.text()) !=0 else "None" + "; "
            results += "activity_regularizer="
            results += self.ui.par14.text() if len(self.ui.par14.text()) !=0 else "None" + "; "
            results += "kernel_constraint="
            results += self.ui.par15.text() if len(self.ui.par15.text()) !=0 else "None" + "; "
            results += "bias_constraint="
            results += self.ui.par16.text() if len(self.ui.par16.text()) !=0 else "None"
            return True, results

        elif self.ui.list.currentText() == "Conv2DTranspose":
            results += "Conv2DTranspose: " 
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "filters=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "32" + "; "
            results += "kernel_size=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "(1,1)" + "; "
            results += "strides=" + self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "(1,1)" + "; "
            results += "padding=" + self.ui.par5.text() if len(self.ui.par5.text()) !=0 else "valid" + "; "
            results += "data_format=" + self.ui.par6.text() if len(self.ui.par6.text()) !=0 else "None" + "; "
            results += "dilation_rate=" + self.ui.par7.text() if len(self.ui.par7.text()) !=0 else "(1,1)" + "; "
            results += "output_padding=" + self.ui.par8.text() if len(self.ui.par8.text()) !=0 else "None" + "; "
            results += "activation=" + self.ui.par9.text() if len(self.ui.par9.text()) !=0 else "None" + "; "
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + ";"
            results += "kernel_initializer="
            results += self.ui.par10.text() if len(self.ui.par10.text()) !=0 else "glorot_uniform" + "; "
            results += "bias_initializer="
            results += self.ui.par11.text() if len(self.ui.par11.text()) !=0 else "zeros" + "; "
            results += "kernel_regularizer="
            results += self.ui.par12.text() if len(self.ui.par12.text()) !=0 else "None" + "; "
            results += "bias_regularizer="
            results += self.ui.par13.text() if len(self.ui.par13.text()) !=0 else "None" + "; "
            results += "activity_regularizer="
            results += self.ui.par14.text() if len(self.ui.par14.text()) !=0 else "None" + "; "
            results += "kernel_constraint="
            results += self.ui.par15.text() if len(self.ui.par15.text()) !=0 else "None" + "; "
            results += "bias_constraint="
            results += self.ui.par16.text() if len(self.ui.par16.text()) !=0 else "None"
            return True, results

        elif self.ui.list.currentText() == "Dense":
            results += "Dense: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "units=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "32" + "; "
            results += "activation=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "None" + "; "
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + ";"
            results += "kernel_initializer="
            results += self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "glorot_uniform" + "; "
            results += "bias_initializer="
            results += self.ui.par5.text() if len(self.ui.par5.text()) !=0 else "zeros" + "; "
            results += "kernel_regularizer="
            results += self.ui.par6.text() if len(self.ui.par6.text()) !=0 else "None" + "; "
            results += "bias_regularizer="
            results += self.ui.par7.text() if len(self.ui.par7.text()) !=0 else "None" + "; "
            results += "activity_regularizer="
            results += self.ui.par8.text() if len(self.ui.par8.text()) !=0 else "None" + "; "
            results += "kernel_constraint="
            results += self.ui.par9.text() if len(self.ui.par9.text()) !=0 else "None" + "; "
            results += "bias_constraint="
            results += self.ui.par10.text() if len(self.ui.par10.text()) !=0 else "None"
            return True, results

        elif self.ui.list.currentText() == "GlobalAveragePool2D":
            results += "GlobalAveragePooling2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "data_format=" + self.ui.par2.text() if len(self.ui.par1.text()) !=0 else "None" + "; "
            return True, results

        elif self.ui.list.currentText() == "GlobalMaxPool2D":
            results += "GlobalMaxPooling2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "data_format=" + self.ui.par2.text() if len(self.ui.par1.text()) !=0 else "None" + "; "
            return True, results

        elif self.ui.list.currentText() == "MaxPool2D":
            results += "MaxPooling2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "pool_size=" + self.ui.par1.text() if len(self.ui.par1.text()) !=0 else "(2,2)" + "; "
            results += "strides=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "None" + "; "
            results += "padding=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "valid" + "; "
            results += "data_format=" + self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "None"
            return True, results

        elif self.ui.list.currentText() == "SeparableConv2D":
            results += "SeparableConv2D: "
            if len(self.inputShape) != 0:
                results += "input_shape=" + self.inputShape + "; "
            results += "filters=" + self.ui.par2.text() if len(self.ui.par2.text()) !=0 else "32" + "; "
            results += "kernel_size=" + self.ui.par3.text() if len(self.ui.par3.text()) !=0 else "(1,1)" + "; "
            results += "strides=" + self.ui.par4.text() if len(self.ui.par4.text()) !=0 else "(1,1)" + "; "
            results += "padding=" + self.ui.par5.text() if len(self.ui.par5.text()) !=0 else "valid" + "; "
            results += "data_format=" + self.ui.par6.text() if len(self.ui.par6.text()) !=0 else "None" + "; "
            results += "dilation_rate=" + self.ui.par7.text() if len(self.ui.par7.text()) !=0 else "(1,1)" + "; "
            results += "depth_multiplier=" + self.ui.par8.text() if len(self.ui.par8.text()) !=0 else "1" + "; "
            results += "activation=" + self.ui.par9.text() if len(self.ui.par9.text()) !=0 else "None" + "; "
            results += "use_bias=" + str(self.ui.boolcheck1.isChecked()) + ";"
            results += "depthwise_initializer="
            results += self.ui.par10.text() if len(self.ui.par10.text()) !=0 else "glorot_uniform" + "; "
            results += "pointwise_initializer="
            results += self.ui.par11.text() if len(self.ui.par11.text()) !=0 else "glorot_uniform" + "; "
            results += "bias_initializer="
            results += self.ui.par12.text() if len(self.ui.par12.text()) !=0 else "zeros" + "; "
            results += "depthwise_regularizer="
            results += self.ui.par13.text() if len(self.ui.par13.text()) !=0 else "None" + "; "
            results += "pointwise_regularizer="
            results += self.ui.par14.text() if len(self.ui.par14.text()) !=0 else "None" + "; "
            results += "bias_regularizer="
            results += self.ui.par15.text() if len(self.ui.par15.text()) !=0 else "None" + "; "
            results += "activity_regularizer="
            results += self.ui.par16.text() if len(self.ui.par16.text()) !=0 else "None" + "; "
            results += "depthwise_constraint="
            results += self.ui.par17.text() if len(self.ui.par17.text()) !=0 else "None" + "; "
            results += "pointwise_constraint="
            results += self.ui.par18.text() if len(self.ui.par18.text()) !=0 else "None" + "; "
            results += "bias_constraint="
            results += self.ui.par19.text() if len(self.ui.par19.text()) !=0 else "None"
            return True, results
            
    def insert_layer_settings(self, layer):
        #берём имя слоя, оно слева от :
        layer_name = layer.split(':')[0][:-1]
        #устанавливаем нужные поля настроек для переданного слоя
        self.set_layers_settings(current=layers_name)
        #получаем все переданные настройки в список элементов имя=значение
        settings = layer.split(':')[1].split(';')
        #разделяем каждый элемент по '='
        settings = [item.split('=') for item in settings]
        #проверяем, была ли среди настроек указана форма входных данных
        inputShape = [value for value in settings if value[0] == "input_shape"][0][1]
        if len(inputShape) != 0:
            self.inputShape.setText(inputShape)
        
        if self.ui.list.currentText() == "Activation" or current == "Activation":
            self.ui.par1.setText(
                [value for value in settings if value[0] == "activation"][0][1])    
        
        elif self.ui.list.currentText() == "AveragePool2D" or current == "AveragePool2D" or (
            self.ui.list.currentText() == "MaxPool2D" or current == "MaxPool2D"):
            self.ui.par1.setText(
                [value for value in settings if value[0] == "pool_size"][0][1])
            self.ui.par2.setText(
                [value for value in settings if value[0] == "strides"][0][1])
            self.ui.par3.setText(
                [value for value in settings if value[0] == "padding"][0][1])
            self.ui.par4.setText(
                [value for value in settings if value[0] == "data_format"][0][1])

        elif self.ui.list.currentText() == "Conv2D" or current == "Conv2D":
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
                [value for value in settings if value[0] == "activation"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)
            
        elif self.ui.list.currentText() == "Conv2DTranspose" or current == "Conv2DTranspose":
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
                [value for value in settings if value[0] == "activation"][0][1]) != 0 else self.ui.boolcheck1.setChecked(0)

        elif self.ui.list.currentText() == "Dense" or current == "Dense":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Units")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Activation")
            self.ui.par3_label.setTooltip("Функция активации для слоя")
            self.ui.par4_label.setText("Kernel initializer")
            self.ui.par4_label.setTooltip("Инициализатор для весов матрицы ядра")
            self.ui.par5_label.setText("Bias initializer")
            self.ui.par5_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par6_label.setText("Kernel regulizer")
            self.ui.par6_label.setTooltip("Функция регуляризации для весовой матрицы ядра")
            self.ui.par7_label.setText("Bias regulizer")
            self.ui.par7_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par8_label.setText("Activity regulizer")
            self.ui.par8_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par9_label.setText("Kernel constraint")
            self.ui.par9_label.setTooltip("Протяжённая функция, применяемая к ядру матрицы")
            self.ui.par10_label.setText("Bias constraint")
            self.ui.par10_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=10, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "GlobalAveragePool2D" or current == "GlobalAveragePool2D" or (
            self.ui.list.currentText() == "GlobalMaxPool2D" or current == "GlobalMaxPool2D"):
            self.ui.par2_label.setText("Data format")
            self.ui.par2_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par1_label.setText("Keepdims")
            self.ui.par1_label.setTooltip("Хранить или нет пространственные измерения")
            self.hide_elements(number=2, bool_number=1)
            self.ui.par1.setVisible(False)

        elif self.ui.list.currentText() == "SeparableConv2D" or current == "SeparableConv2D":
            self.ui.par1_label.setText("Use bias")
            self.ui.par1_label.setTooltip("Использовать или нет биас-вектор")
            self.ui.par2_label.setText("Filters")
            tooltip = "Размерность выходного пространства слоя"
            self.ui.par2_label.setTooltip(tooltip)
            self.ui.par3_label.setText("Kernel size")
            self.ui.par3_label.setTooltip("Размеры окна свёртки")
            self.ui.par4_label.setText("Strides")
            self.ui.par4_label.setTooltip("Шаги свёртки изображения")
            self.ui.par5_label.setText("Padding")
            tooltip = "Может быть valid, тогда нет отступов\n"
            tooltip += "Или same, тогда равномерные отступы так, чтобы выход был такой же, как вход"
            self.ui.par5_label.setTooltip(tooltip)
            self.ui.par6_label.setText("Data format")
            self.ui.par6_label.setTooltip("Строка, описывающая порядок измерений во входных данных")
            self.ui.par7_label.setText("Dilation rate")
            self.ui.par7_label.setTooltip("Значение, описывающее уровень дилатации для свёртки")
            self.ui.par8_label.setText("Depth multi")
            tooltip = "Количество выходных каналов сёрток по глубине для каждого входного канала"
            self.ui.par8_label.setTooltip(tooltip)
            self.ui.par9_label.setText("Activation")
            self.ui.par9_label.setTooltip("Функция активации для слоя")
            self.ui.par10_label.setText("Depth initializer")
            self.ui.par10_label.setTooltip("Инициализатор для ядра свёрток по глубине")
            self.ui.par11_label.setText("Point initializer")
            self.ui.par11_label.setTooltip("Инициализатор для ядра свёрток по точкам")
            self.ui.par12_label.setText("Bias initializer")
            self.ui.par12_label.setTooltip("Инициализатор биас-вектора")
            self.ui.par13_label.setText("Depth regulizer")
            self.ui.par13_label.setTooltip("Функция регуляризации для матрицы глубинного ядра")
            self.ui.par14_label.setText("Point regulizer")
            self.ui.par14_label.setTooltip("Функция регуляризации для матрицы ядра точек")
            self.ui.par15_label.setText("Bias regulizer")
            self.ui.par15_label.setTooltip("Функция регуляризации, применяемая к вектору биаса")
            self.ui.par16_label.setText("Activity regulizer")
            self.ui.par16_label.setTooltip("Функция регуляризации для выхода слоя")
            self.ui.par17_label.setText("Depth constraint")
            self.ui.par17_label.setTooltip("Протяжённая функция, применяемая к глубинному ядру матрицы")
            self.ui.par18_label.setText("Point constraint")
            self.ui.par18_label.setTooltip("Протяжённая функция, применяемая к ядру точек матрицы")
            self.ui.par19_label.setText("Bias constraint")
            self.ui.par19_label.setTooltip("Протяжённая функция, применяемая к биас-вектору")
            self.hide_elements(number=19)
            self.ui.par1.setVisible(False)  

