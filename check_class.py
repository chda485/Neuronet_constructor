from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from forms import check_window
import numpy as np
import sys, os, cv2
import settings_class
sys.path.append("utils")
from utils import helper
from sklearn import metrics
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.applications import imagenet_utils

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
        self.ui.metrics_list.setEnabled(False)
        self.ui.metric_settings.setEnabled(False)

        self.model_path = "" #путь к тестируемой модели
        self.settings = None
        self.ready_net = None
        self.metric_str = None
        self.metric = None
        self.preds_label = None
        self.check_dataset = None
        self.model = None
        self.input_shape = None
        self.true_labels = None

        self.ui.list_check.clicked.connect(self.list_choice)
        self.ui.disk_check.clicked.connect(self.disk_choice)
        self.ui.metric_check.stateChanged.connect(self.metric_choice)
        self.ui.disk_button.clicked.connect(lambda: self.choice_file(0))
        self.ui.example_button.clicked.connect(lambda: self.choice_file(1))
        self.ui.list_of_nets.addItems(helper.LIST_READY_NETS)
        self.ui.metrics_list.addItems(helper.LIST_CHECK_METRIC)
        self.ui.net_settings.clicked.connect(lambda: self.show_settings(4))
        self.ui.metric_settings.clicked.connect(lambda: self.show_settings(5))
        self.ui.true_labels.clicked.connect(self.get_true_labels)
        
        self.ui.check_button.clicked.connect(self.proba)

    def list_choice(self):
        self.ui.list_of_nets.setEnabled(True)
        self.ui.disk_button.setEnabled(False)

    def disk_choice(self):
        self.ui.list_of_nets.setEnabled(False)
        self.ui.disk_button.setEnabled(True)
        
    def metric_choice(self):
        if self.ui.metric_check.isChecked():
            self.ui.metrics_list.setEnabled(True)
            self.ui.metric_settings.setEnabled(True)
        else:
            self.ui.metrics_list.setEnabled(False)
            self.ui.metric_settings.setEnabled(False)

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
            # читаем путь к выбранным проверочным данным
            self.check_dataset = QtWidgets.QFileDialog.getExistingDirectory(self)
            # если путь был выбран
            if len(self.check_dataset) != 0:
                self.ui.lineEdit.setText(self.check_dataset)

    def show_settings(self, win_type):
        if win_type == 4:
            self.settings = settings_class.Settings(current_text=self.ui.list_of_nets.currentText(),
                                                    win_type=win_type)
        else:
            self.settings = settings_class.Settings(current_text=self.ui.metrics_list.currentText(),
                                                    win_type=win_type)
        self.settings.setWindowModality(QtCore.Qt.ApplicationModal)
        self.settings.ui.buttons.accepted.connect(lambda: self.get_settings(win_type))
        self.settings.show()

    def get_settings(self, win_type):
        (status, obj) = self.settings.between_wins()
        self.settings.close()
        if status:
            if win_type == 4:
                self.ready_net = obj
            else:
                self.metric_str = obj
                QtWidgets.QMessageBox.information(self, "Testing", self.metric_str)
                
    def get_true_labels(self):
        info = "Файл должен содержать либо текстовые метки, либо числовые\n"
        info += "Если числовые, должен быть файл раскодировки числовых значений к текстовым"
        QtWidgets.QMessageBox.information(self, "Уведомление", info)
        #читаем путь к выбранному файлу меток
        path = QtWidgets.QFileDialog.getOpenFileName(self,
                                                    filter="CSV files (*.csv)")
        if len(path[0]) != 0:
            f = open(path[0], 'r')
            lines = f.read()
            f.close()
            lines = lines.split('\n')
            self.true_labels = lines

    def parse_metric_str(self):
        settings = self.metric_str.split(';')
        settings = [set_.split('|') for set_ in settings]
        sample_weight = np.asarray([set_[1] for set_ in settings if set_[0] == "sample_weight"])[0]
        sample_weight = helper.construct_tuple(sample_weight) if len(
            sample_weight) !=0  else None
            
        if self.ui.metrics_list.currentText == "F1" or (
           self.ui.metrics_list.currentText == "Precision") or (
           self.ui.metrics_list.currentText == "Recall") or (
           self.ui.metrics_list.currentText == "Jaccard"):
            labels = np.asarray([set_[1] for set_ in settings if set_[0] == "labels"])[0]
            labels = helper.construct_array(labels) if len(labels) != 0 else None
            pos_label = np.asarray([set_[1] for set_ in settings if set_[0] == "pos_label"])[0]
            pos_label = pos_label if len(pos_label) != 0 else 1
            if pos_label != 1:
                if pos_label.isdigit():
                    pos_label = int(pos_label)
            average = np.asarray([set_[1] for set_ in settings if set_[0] == "average"])[0]
            average = average if len(average) != 0 else 'binary'
            zero = np.asarray([set_[1] for set_ in settings if set_[0] == "zero_division"])[0]
            zero = zero if len(zero) != 0 else 'warn'
            if zero != 'warn':
                if zero.isdigit():
                    zero = int(zero)
            if self.ui.metrics_list.currentText == "F1":
                self.metric = metrics.f1_score(y_true=self.true_labels, y_pred=self.preds_label,
                                               label=labels, pos_label=pos_label,
                                               average=average, sample_weight=sample_weight,
                                               zero_division=zero)
            elif self.ui.metrics_list.currentText == "Precision":
                self.metric = metrics.precision_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                      label=labels, pos_label=pos_label,
                                                      average=average, sample_weight=sample_weight,
                                                      zero_division=zero)
            elif self.ui.metrics_list.currentText == "Recall":
                self.metric = metrics.recall_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                   label=labels, pos_label=pos_label,
                                                   average=average, sample_weight=sample_weight,
                                                   zero_division=zero)

            elif self.ui.metrics_list.currentText == "Jaccard":
                self.metric = metrics.jaccard_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                    label=labels, pos_label=pos_label,
                                                    average=average, sample_weight=sample_weight,
                                                    zero_division=zero)

        elif self.ui.metrics_list.currentText == "Accuracy":
            normalize = np.asarray([set_[1] for set_ in settings if set_[0] == "normalize"])[0]
            normalize = True if normalize=="True" else False
            self.metric = metrics.accuracy_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                 normalize=normalize, sample_weight=sample_weight)
            
        elif self.ui.metrics_list.currentText == "Balanced_accuracy":
            adjusted = np.asarray([set_[1] for set_ in settings if set_[0] == "adjusted"])[0]
            adjusted = True if adjusted=="True" else False
            self.metric = metrics.accuracy_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                 adjusted=adjusted, sample_weight=sample_weight)
            
        elif self.ui.metrics_list.currentText == "Top_K_accuracy":
            normalize = np.asarray([set_[1] for set_ in settings if set_[0] == "normalize"])[0]
            normalize = True if normalize=="True" else False
            k = np.asarray([set_[1] for set_ in settings if set_[0] == "k"])[0]
            k = int(k) if len(k) != 0 else 2
            labels = np.asarray([set_[1] for set_ in settings if set_[0] == "labels"])[0]
            labels = helper.construct_array(labels) if len(labels) != 0 else None
            self.metric = metrics.top_k_accuracy_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                       normalize=normalize, sample_weight=sample_weight,
                                                       k=k, label=labels)
            
        elif self.ui.metrics_list.currentText == "Average_precision":
            pos_label = np.asarray([set_[1] for set_ in settings if set_[0] == "pos_label"])[0]
            pos_label = pos_label if len(pos_label) != 0 else 1
            if pos_label != 1:
                if pos_label.isdigit():
                    pos_label = int(pos_label)
            average = np.asarray([set_[1] for set_ in settings if set_[0] == "average"])[0]
            average = average if len(average) != 0 else 'binary'
            self.metric = metrics.average_precision_score(y_true=self.true_labels, y_pred=self.preds_label,
                                                          pos_label=pos_label, average=average,
                                                          sample_weight=sample_weight)
            
        elif self.ui.metrics_list.currentText == "Neg_brief":
            pos_label = np.asarray([set_[1] for set_ in settings if set_[0] == "pos_label"])[0]
            pos_label = pos_label if len(pos_label) != 0 else 1
            if pos_label != 1:
                if pos_label.isdigit():
                    pos_label = int(pos_label)
            self.metric = metrics.brier_score_loss(y_true=self.true_labels, y_prob=self.preds_label,
                                                   pos_label=pos_label,
                                                   sample_weight=sample_weight)
            
        elif self.ui.metrics_list.currentText == "Neg_log":
            normalize = np.asarray([set_[1] for set_ in settings if set_[0] == "normalize"])[0]
            normalize = True if normalize=="True" else False
            eps = np.asarray([set_[1] for set_ in settings if set_[0] == "eps"])[0]
            eps = float(eps) if len(eps) != 0 else 1e-15
            labels = np.asarray([set_[1] for set_ in settings if set_[0] == "labels"])[0]
            labels = helper.construct_array(labels) if len(labels) != 0 else None
            self.metric = metrics.log_loss(y_true=self.true_labels, y_pred=self.preds_label,
                                           normalize=normalize, sample_weight=sample_weight,
                                           eps=eps, label=labels)
        
        elif self.ui.metrics_list.currentText == "ROC_AUC":
            average = np.asarray([set_[1] for set_ in settings if set_[0] == "average"])[0]
            average = average if len(average) != 0 else 'binary'
            max_fpr = np.asarray([set_[1] for set_ in settings if set_[0] == "max_fpr"])[0]
            max_fpr = float(max_fpr) if len(max_fpr) != 0 else None
            labels = np.asarray([set_[1] for set_ in settings if set_[0] == "labels"])[0]
            labels = helper.construct_array(labels) if len(labels) != 0 else None
            multi = np.asarray([set_[1] for set_ in settings if set_[0] == "multi_class"])[0]
            multi = multi if len(multi) != 0 else 'raise'
            self.metric = metrics.roc_auc_score(y_true=self.true_labels, y_score=self.preds_label,
                                                max_fpr=max_fpr, sample_weight=sample_weight,
                                                multi_class=multi, label=labels)
                                                  
            
    """алгоритм работы данной функции:
        сначал проверяется выбор модели и её настроек, потом выбор данных для проверки
        после данные собираются в массив с предварительным изменением 
        размера согласно выбранной сети
        после происходит проверка сети и вывод итоговой точности
        если выбраны расчёты метрики или rank, то они считаются
        и выводится результат"""       
    def test_model(self): 
        #если выбрана модель с диска и сама модель не выбрана
        if self.ui.disk_check.isChecked() and len(self.model_path) == 0: #OK
            er_win = QtWidgets.QErrorMessage(self)
            er_win.showMessage("Не выбрана модель для тестирования")
            return
        
        #если модель с диска выбрана
        elif self.ui.disk_check.isChecked(): #OK
            self.model = load_model(self.model_path)
        
        #если модель из списка
        elif self.ui.list_check.isChecked(): #OK
            #если были выбраны какие-то настройки
            if self.ready_net is not None:
                self.model = self.ready_net
            #если нет, просто берём сеть по умолчанию из keras
            else:
                self.model = helper.LIST_READY_NETS[self.ui.list_of_nets.currentText()]
        
        #форма входных данных модели
        self.input_shape = self.model.layers[0].input_shape #OK
        
        #если не выбраны данные для тестирования
        if self.check_dataset is None: #OK
            er_win = QtWidgets.QErrorMessage(self)
            er_win.showMessage("Не выбраны данные для проверки модели")
            return
        
        #проверяем, сколько экземпляров для тестирования
        one_file = True if len(os.listdir(self.check_dataset)) == 1 else False #OK
        
        #создаём список для всех файлов тестирования
        files = os.listdir(self.check_dataset) #OK
        samples = []
        for file in files:
            #загружаем файлы и преобразуем их в нужный формат
            path = os.path.join(self.check_dataset, file)
            img = load_img(path, target_size=self.input_shape)
            img = img_to_array(img)
            #если модель из списка, преобразуем файлы согласно правилам keras
            if self.ui.list_check.isChecked():
                if self.ui.list_of_nets.CurrentText() in ("Xception", "InceptionV3", "InceptionResNetV2"):
                    from keras.applications.inception_v3 import preprocess_input
                    img = preprocess_input(img)
                    img = cv2.resize(img, (229,229))
                else:
                    from keras.applications.imagenet_utils import preprocess_input
                    img = preprocess_input(img)
                    img = cv2.resize(img, (224, 224))
            samples.append(img)       
        samples = np.asarray(samples)
        
        #если выбрана модель с диска
        if self.ui.disk_check.isChecked(): #OK           
            #если данные меток текстовые, то кодируем их 
            if type(self.true_labels[0]) is str:
                #если использовался LabelBinarazer при обучении
                if self.model.layers[0].input_shape.shape[-1] != 1:
                    from sklearn.preprocessing import LabelBinarizer
                    lb = LabelBinarizer()
                else:
                    from sklearn.preprocessing import LabelEncoder
                    lb = LabelEncoder()
                self.true_labels = lb.fit_transform(self.true_labels)
                
            #вычисляем предсказания для возможного расчёта метрики
            self.preds_label = self.model.predict(samples)
            #если использовался LabelBinarazer при обучении
            if self.model.layers[0].input_shape.shape[-1] != 1:
                temp = []
                #преобразуем вектор в индекс предсказанного класса
                for pred in self.preds_label:
                    pred = np.argsort(pred)[::-1]
                    temp.append(pred)
                self.preds_label = np.asarray(temp)
            #считаем процент верных предсказаний
            truths = []
            for (T, P) in zip(self.true_labels, self.preds_label):
                truths.append(T == P)
            truths = np.asarray(truths)
            accuracy = np.cout_nonzero(truths) / len(truths)
            self.ui.console_train.append("Точность модели - {}%".fromat(np.around(accuracy*100, 2)))
              
        #если модель из списка    
        else: #NO OK!!!!!!!!!!!!!
            #если числове метки, декодироуем их в строковые согласно предоставленному файлу
            if type(self.true_labels[0]) is int:
                self.decode_labels()
            #делаем предсказания и преобразуем их в строки
            self.preds_label = self.model.predict(samples)
            self.preds_label = imagenet_utils.decode_predictions(self.preds_label)
         
        #если выбрана опция рассчёта метрики
        if self.ui.metric_check.isChecked():
            #парсим настройки метрики из строки и считаем её
            self.parse_metric_str()
            self.ui.console_train.append("{} - {}%".format(
                self.ui.metrics_list.currentText, np.around(self.metric * 100, 2)))
            
        #если выбрана опция рассчёта rank

        if self.ui.rank_check.isChecked():
            #если недостаточно файлов
            if one_file:
                er_win = QtWidgets.QErrorMessage(self)
                er_win.showMessage("Недостаточно файлов для расчёта rank")
                return
            
            (r1, r5) = helper.rank5_accuracy(self.preds_label, self.true_labels)
            self.console_train.append("R1 - {}, R5 - {}".format(
                np.around(r1*100, 2), np.around(r5*100, 2)))               
    
    def decode_labels(self):
        decod = {}
        info = "Выберите файл раскодировки числовых значений меток в CSV\n"
        info += "Файл должен содержать 1 столбец - числовая, 2 - строковая метка"
        QtWidgets.QMessageBox.information(self, "Файл раскодировки", info)
        path = QtWidgets.QFileDialog.getOpenFileName(self,
                                            filter="CSV files (*.csv)")
        if len(path[0]) != 0:
            f = open(path[0], 'r')
            lines = f.read()
            f.close()
            lines = lines.split('\n')
            for line in lines:
                if line.split(',')[0].isdigit():
                    mark = int(line.split(',')[0])
                    content = line.split(',')[1]
                else:
                    mark = int(line.split(',')[1])
                    content = line.split(',')[1]
                
                if mark not in decod:
                    decod[mark] = content
            
            temp = []
            for label in self.true_labels:
                new = decod[label].lower()
                temp.append(new)
            self.true_labels = np.asarray(temp)

    def write(self, text):
        text = str(text).replace('\n', '').replace('0', '')
        self.ui.console_train.append(text)
        
    def flush(self):
        sys.stdout = self.old_stdout
        
    def closeEvent(self, e):
        sys.stdout = self.old_stdout
        
    def proba(self):
        x = r"G:\proba.csv"
        print(self.read_csv_labels(x))

#("k:2", "average:macro")
#((k,2), (average, macro))
