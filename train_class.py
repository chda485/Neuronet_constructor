from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from forms import train_window
import construct_class, settings_class
import sys, os
sys.path.append("utils")
from utils import helper 
from utils.net_builder import NetBuilder
import numpy as np
from keras.models import load_model   

class TrainWindow(QMainWindow):
    def __init__(self, old_stdout=None, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = train_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.old_std = None

        self.setWindowTitle("Обучение нейросети")
        self.ui.close_button.clicked.connect(self.close)
        #назначаем значения всем спискам
        self.ui.list_of_nets.addItems(helper.LISTS_NEURONETS.keys())
        self.ui.loss_list.addItems(helper.LIST_LOSSES.keys())
        self.ui.metrics_list.addItems(helper.LIST_METRICS.keys())
        self.ui.opts_list.addItems(helper.LIST_OPTS)
        self.ui.callbacks_list.addItems(helper.LIST_CALLBACKS)
        self.ui.label.setFocus()

        self.dataset_path = "" #путь к датасету
        self.path_model = "" #путь к файлу модели, которая открывается
        self.model_path = "" #путь к сохраняемому файлу модели
        self.diagramm_file = "" #путь к сохраняемому файлу диаграммы сети !!!!!!
        self.plots_file = None #путь к сохраняемому файлу графиков обучения
        self.path_weights = "" #путь к сохраняемому файлу весов модели
        self.inputShape = None 
        self.opt = None 
        self.loss = None
        self.metric = None
        self.callback = None
        self.neuronet = None

        self.settings = None #переменная для класса с настройками оптимизаторов, метрик и т.п.
        
        #переменные для сопровождение повторного обучения      
        self.again_train = False
        self.loss_set = False
        self.metric_set = False
        self.opt_set = False
        self.callback_set = False
        
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.list_check.setChecked(True)
        self.ui.disk_button.setEnabled(False)
        self.ui.construct_button.setEnabled(False)
        self.ui.callbacks_list.setEnabled(False)
        self.ui.display_plots.setEnabled(False)
        self.ui.file_plots.setEnabled(False)
        self.ui.auto_input.setChecked(True)
        self.ui.input_win.setEnabled(False)
        self.ui.callbacks_settings.setEnabled(False)
        self.ui.model_path.setEnabled(False)
        self.ui.weights_path.setEnabled(False)
        
        self.ui.list_check.clicked.connect(self.list_choice)
        self.ui.disk_check.clicked.connect(self.disk_choice)
        self.ui.construct_check.clicked.connect(self.construct_choice)
        self.ui.callbacks_check.stateChanged.connect(self.callbacks_choice)
        self.ui.plots_check.stateChanged.connect(self.plots_choice)
        self.ui.auto_input.clicked.connect(self.inputs_choice)
        self.ui.self_input.clicked.connect(self.inputs_self_choice)
        self.ui.train_button.clicked.connect(self.train)
        self.ui.disk_button.clicked.connect(self.choice_file)
        self.ui.construct_button.clicked.connect(self.show_construct)
        self.ui.model_check.stateChanged.connect(self.model_choice)
        self.ui.weights_check.stateChanged.connect(self.weights_choice)
        
        self.ui.path_diagram.clicked.connect(lambda:self.save_file(0, 0))
        self.ui.file_plots.clicked.connect(lambda:self.save_file(0, 1))
        self.ui.model_path.clicked.connect(lambda:self.save_file(1, 0))
        self.ui.weights_path.clicked.connect(lambda:self.save_file(1, 1))

        self.ui.path_button.clicked.connect(self.open_dataset)
        self.ui.input_win.clicked.connect(self.create_inputShape)
        self.ui.opts_settings.clicked.connect(lambda:self.show_settings(0))
        self.ui.callbacks_settings.clicked.connect(lambda:self.show_settings(3))
        self.ui.loss_details.clicked.connect(lambda:self.show_settings(1))
        self.ui.metrics_details.clicked.connect(lambda:self.show_settings(2))

    """functions that are responsible for switching the radiobutton boxes"""   
    def list_choice(self):
        self.ui.list_of_nets.setEnabled(True)
        self.ui.disk_button.setEnabled(False)
        self.ui.construct_button.setEnabled(False)

    def disk_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.disk_button.setEnabled(True)
        self.ui.construct_button.setEnabled(False)

    def construct_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.disk_button.setEnabled(False)
        self.ui.construct_button.setEnabled(True)

    def callbacks_choice(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.callbacks_list.setEnabled(True)
            self.ui.callbacks_settings.setEnabled(True)
        else:
            self.ui.callbacks_list.setEnabled(False)
            self.ui.callbacks_settings.setEnabled(False)

    def plots_choice(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.display_plots.setEnabled(True)
            self.ui.file_plots.setEnabled(True)
        else:
            self.ui.display_plots.setEnabled(False)
            self.ui.file_plots.setEnabled(False)

    def inputs_choice(self):
        self.ui.input_win.setEnabled(False)

    def inputs_self_choice(self):
        self.ui.input_win.setEnabled(True)
        
    def model_choice(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.model_path.setEnabled(True)
        else:
            self.ui.model_path.setEnabled(False)
            
    def weights_choice(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.weights_path.setEnabled(True)
        else:
            self.ui.weights_path.setEnabled(False)
    """---------------------------------------"""

    def show_construct(self):
        self.construct_window = construct_class.ConstructWindow()
        self.construct_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.construct_window.save_button.clicked.connect(self.get_neuronet)
        self.construct_window.show()
        
    def get_neuronet(self):
        (status, net) = self.construct_window.send_model()
        self.construct_window.close()
        if status:
            self.neuronet = net
    
    def choice_file(self):
        #читаем путь к файлу модели
        path = QtWidgets.QFileDialog.getOpenFileName(self,
                                                    filter="Keras model file (*.h5)")
        #если путь был выбран
        if len(path[0]) != 0:
            self.ui.console_train.append("The path to the model: \n" + path[0])
            self.path_model = path[0]

    def save_file(self, name, file):
        #если сохраняем картинку
        if name == 0:
            path = QtWidgets.QFileDialog.getSaveFileName(self,
                                                         filter="PNG files(*.png)")
            if len(path[0]) > 0:
                #если картинка диаграммы
                if file == 0:
                    self.diagramm_file = path[0]
                    if not self.diagramm_file.endswith('.png'):
                        self.diagramm_file += '.png'
                    self.ui.console_train.append("Diagramm path: \n" + self.diagramm_file)
                #если картинка графиков обучения
                else:
                    self.plots_file = path[0]
                    if not self.plots_file.endswith('.png'):
                        self.plots_file += '.png'
                    self.ui.console_train.append("Plots path: \n" + self.plots_file)
        #если сохраняем keras-файлы
        elif name == 1:
            path = QtWidgets.QFileDialog.getSaveFileName(self,
                                                         filter="Keras files(*.h5)")
            if len(path[0]) > 0:
                #если сохраняем обученную модель
                if file == 0:
                    self.model_path = path[0]
                    if not self.model_path.endswith('.h5'):
                        self.model_path += '.h5'
                    self.ui.console_train.append(
                        "Model path for saving: \n" + self.model_path)
                #если сохраняем веса модели
                else:
                    self.path_weights = path[0]
                    if not self.path_weights.endswith('.h5'):
                        self.path_weights += '.h5'
                    self.ui.console_train.append(
                        "Weights path: \n" + self.path_weights)

    def open_dataset(self):
        self.dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self)
        #если датасет выбран
        if len(self.dataset_path) != 0:
            #папки, на которые должен быть разбит датасет
            check_list = ("validation", "train", "test")
            dirs = os.listdir(self.dataset_path)
            for dir_ in dirs:
                #если структура датасета не соответсвует требуемой
                if dir_ not in check_list or len(dirs) < 3:
                    er_win = QtWidgets.QErrorMessage(self)
                    er_win.showMessage("""Неправильная структура датасета.
                                       Датасет должен быть разбит на 3 раздела:
                                       validation, train, test""")
                    return 
            self.ui.console_train.append("The path to dataset:\n" + self.dataset_path)

    def create_inputShape(self):
        (text, status) = QtWidgets.QInputDialog.getText(self, "Ввод формы данных",
                                                      "Введите форму данных в виде строки через запятую")
        #если форма была введена
        if status:
            #если форма верная
            if helper.check_input(text):
                #разбиваем на элементы
                shape = text.split(',')
                #преобразуем в массив чисел
                shape = np.asarray(shape).astype('int')
                #составляем форму
                self.inputShape = "".join([str(x) + ',' for x in shape])[:-1]
                self.ui.console_train.append("InputShape is: " + self.inputShape)
            else:
                er_win = QtWidgets.QErrorMessage(self)
                er_win.showMessage("Некорректный ввод формы")
                
    def show_settings(self, win_type):
        #если настройки оптимизаторов
        if win_type == 0:
            self.settings = settings_class.Settings(current_text=self.ui.opts_list.currentText(),
                                                    win_type=win_type)
        #если настройки функции потерь
        elif win_type == 1:
            self.settings = settings_class.Settings(current_text = self.ui.loss_list.currentText(),
                                                    win_type=win_type)
        #если настройки метрики
        elif win_type == 2:
            self.settings = settings_class.Settings(current_text = self.ui.metrics_list.currentText(),
                                                    win_type=win_type)
        #если настройки обратных вызовов
        else:
            self.settings = settings_class.Settings(current_text = self.ui.callbacks_list.currentText(),
                                                    win_type=win_type)
        self.settings.setWindowModality(QtCore.Qt.ApplicationModal)
        self.settings.ui.buttons.accepted.connect(lambda: self.get_settings(win_type))
        self.settings.show()
    
    def get_settings(self, win_type):
        (status, obj) = self.settings.between_wins()
        self.settings.close()
        #если были выбраны какие-то настройки
        if status:
            if win_type == 0:
                self.opt = obj
                self.opt_set = True
            elif win_type == 1:
                self.loss = obj
                self.loss_set = True
            elif win_type == 2:
                self.metric = obj
                self.metric_set = True
            else: 
                self.callback = obj
                self.callback_set = True

    def clear_settings(self):
        self.loss_set = False
        self.metric_set = False
        self.callback_set = False
        self.opt_set = False
        
    """алгоритм работы функции обучения:
           вначале проверяется, что указаны все необходимые для обучения параметры
           После проверяется наличие ввода формы входных данных, если нет, форма конструируется из самих данных.
           Далее провереятся установка оптимизатора и обратных вызовов.
           После этого загружается/строится модель и обучается"""
    def train(self):
        text = ""
        #проверяем, что всё необходимое введено
        check = helper.check_all_choised(self.dataset_path,
                                         self.ui.epochs.text())
        #если всё необходимое введено
        if check is None:
            #если выбрана модель из файла
            if self.ui.disk_check.isChecked():
                #если файл модели не выбран
                if len(self.path_model) == 0:
                    self.ui.console_train.append("Не выбран файл модели")
                    return
            elif self.ui.list_check.isChecked():
                text += "We choose " + self.ui.list_of_nets.currentText() + " model"                
            text += "\nParameters: \nLoss_function is " + self.ui.loss_list.currentText()
            text += "\nMetric is " + self.ui.metrics_list.currentText()
            text += "\nEpochs are " + self.ui.epochs.text()
            text += "\nOptimizers is " + self.ui.opts_list.currentText()
            self.ui.console_train.append(text)
        else:
            self.ui.console_train.append(check)
            return

        if self.inputShape is None:
            #если форма данных не установлена, берём по умолчанию
            if self.ui.list_check.isChecked():
                self.inputShape = (224,224,3)
        
        #если обучение запускаем в первый раз
        if self.again_train is False:
            if self.opt is None:
                self.opt = self.ui.opts_list.currentText()
    
            if self.loss is None:
                self.loss = self.ui.loss_list.currentText()
    
            if self.metric is None:
                if self.ui.metrics_list.currentText() in helper.LIST_ADJUST_ONLY_METRICS:
                    QtWidgets.QMessageBox.information(
                        self, "Предупреждение", 
                        "Данная метрика должна быть настроена вручную (второй параметр)")
                    return
                else:
                    self.metric = self.ui.metrics_list.currentText()
    
            if self.callback is None and self.ui.callbacks_check.checkState() == 2:
                self.callback = self.ui.callbacks_list.currentText()
                self.ui.console_train.append("\nCallbacks is :" + self.ui.callbacks_list.currentText())
        #если запускаем обучение повторно
        else:
            if self.opt_set is False:
                self.opt = self.ui.opts_list.currentText()
    
            if self.loss_set is False:
                self.loss = self.ui.loss_list.currentText()
    
            if self.metric_set is False:
                if self.ui.metrics_list.currentText() in helper.LIST_ADJUST_ONLY_METRICS:
                    QtWidgets.QMessageBox.information(
                        self, "Предупреждение", 
                        "Данная метрика должна быть настроена вручную (второй параметр)")
                    return
                else:
                    self.metric = self.ui.metrics_list.currentText()
    
            if self.callback_set is False and self.ui.callbacks_check.checkState() == 2:
                self.callback = self.ui.callbacks_list.currentText()
                self.ui.console_train.append("\nCallbacks is :" + self.ui.callbacks_list.currentText())
            
        builder = NetBuilder()
        if self.ui.disk_check.isChecked():
            model = load_model(self.path_model)
            #перестраиваем последний слой на нужное число выходных нейронов
            model = builder.rebuild_last_layer(model, self.dataset_path)
            self.inputShape = model.layers[0].input_shape[0][1:]
            from_disk = True
        else:
            model = builder.build_model(self.ui.list_of_nets.currentText(),
                                            self.inputShape,
                                            self.dataset_path)
            from_disk = False
            
        self.ui.console_train.append("InputShape is: {}".format(self.inputShape))
            
        #проверяем, выбрана ли опция "отобразить диаграмму сети"
        diagramm = self.ui.show_check.isChecked()
        #если выбрана либо установлен путь к файлу диаграммы
        if diagramm or len(self.diagramm_file) != 0:
            from keras.utils.vis_utils import plot_model
            #собираем путь к сохраняемому файлу
            if len(self.diagramm_file) != 0:
                path = self.diagramm_file
            #пишем название файла, если только отображаем диаграмму
            else:
                path = "{}.png".format(self.ui.list_of_nets.currentText())
            plot_model(model, to_file=path, show_shapes=True)
            #если надо отображать
            if diagramm:
                import cv2
                img = cv2.imread(path)
                cv2.imshow("Net diagramm", img)
            if not self.diagramm_file:
                os.remove(path)

        #делаем отмену вывода в консоль хода обучения, если на выбрали опцию подробного отчета
        if not self.ui.otchet_check.isChecked():
            w = open(os.devnull, "w")
            self.old_std = sys.stdout
            sys.stdout = w
        
        results, model, detail = builder.model_train(model, self.opt, self.loss, self.metric,
                                            self.ui.epochs.text(), self.dataset_path,
                                            detail_result=self.ui.result_check.isChecked(),
                                            from_disk=from_disk)
        
        self.again_train = True
        self.clear_settings()
        
        if not self.ui.otchet_check.isChecked():
            sys.stdout = self.old_std
            
        if detail != None:
            self.ui.console_train.append(detail)
        
        plots = self.ui.display_plots.isChecked()
        #если выбрана опция показа графиков обучения либо их сохранение в файл
        if plots or self.plots_file is not None:
            #если выбрано сохранение в файл
            if self.plots_file is not None:
                path = self.plots_file
            else:
                path = None
            helper.show_plot(self.ui.metrics_list.currentText(), results, int(self.ui.epochs.text()), path, plots)
        
        if self.ui.model_check.isChecked() and len(self.model_path) != 0:
            model.save(self.model_path)
            
        if self.ui.weights_check.isChecked() and len(self.path_weights) != 0:
            model.save_weights(self.path_weights)

        if os.path.exists("incl_fun.py"):
            os.remove("incl_fun.py")
               
    def write(self, text):
        cursor = self.ui.console_train.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.console_train.setTextCursor(cursor)
        self.ui.console_train.ensureCursorVisible()

    def flush(self):
        pass
