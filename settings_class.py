from PyQt5.QtWidgets import QMainWindow
from forms import settings
import sys
sys.path.append("utils")
from utils import helper
from utils.settings_logic import SettingsLogic
#from keras import optimizers

class Settings(QMainWindow):
    def __init__(self, current_text, win_type = 0, parent=None):
        QMainWindow.__init__(self,parent)
        self.ui = settings.Ui_Form()
        self.ui.setupUi(self)
        self.ui.buttons.rejected.connect(self.close)
        self.logic = SettingsLogic(win_type, parent=self)
        self.win_type = win_type
        
        """переменные для функций, используемых как параметры"""
        self.path = None
        self.truth_labels = None
        
        #0 - настройки оптимизатора, 1 - настройки функции потерь
        #2 - настройки метрики, 3 - настройки обратных вызовов
        if win_type == 0:
            self.ui.list.addItems(helper.LIST_OPTS)
            self.ui.list.activated.connect(self.choice_opts)
            self.ui.list_label.setText("Оптимизатор")
            self.setWindowTitle("Настройки оптимизатора")
            self.ui.list.setCurrentText(current_text)
            self.choice_opts(current_text)
        elif win_type == 1:
            self.ui.list.addItems(helper.LIST_LOSSES)
            self.ui.list.activated.connect(self.choice_losses)
            self.ui.list_label.setText("Функция потерь")
            self.setWindowTitle("Настройки функций потерь")
            self.ui.list.setCurrentText(current_text)
            self.choice_losses(current_text)
        elif win_type == 2:
            self.ui.list.addItems(helper.LIST_METRICS)
            self.ui.list.activated.connect(self.choice_metrics)
            self.ui.list_label.setText("Метрика оценки")
            self.setWindowTitle("Настройки метрик оценки")
            self.ui.list.setCurrentText(current_text)
            self.choice_metrics(current_text)
        elif win_type == 3:
            self.ui.list.addItems(helper.LIST_CALLBACKS)
            self.ui.list.activated.connect(self.choice_callbacks)
            self.ui.list_label.setText("Обратный вызов")
            self.setWindowTitle("Настройки обратных вызовов")
            self.ui.list.setCurrentText(current_text)
            self.choice_callbacks(current_text)
        elif win_type == 4:
            self.ui.list.addItems(helper.LIST_READY_NETS)
            self.ui.list.activated.connect(self.choice_nets)
            self.ui.list_label.setText("Готовая сеть")
            self.setWindowTitle("Настройки готовой сети")
            self.ui.list.setCurrentText(current_text)
            self.choice_nets(current_text)
        elif win_type == 5:
            self.ui.list.addItems(helper.LIST_CHECK_METRIC)
            self.ui.list.activated.connect(self.choice_check_metric)
            self.ui.list_label.setText("Метрика оценки")
            self.setWindowTitle("Настройки метрики оценки")
            self.ui.list.setCurrentText(current_text)
            self.choice_check_metric(current_text)            
        
    def choice_opts(self, opt=None):
        self.ui.par1_label.setText("Learning_rate")
        tooltip = "Параметр, характеризующий степень изменения весов при обучении"
        self.ui.par1_label.setToolTip(tooltip)
        if self.ui.list.currentText() == "SGD" or opt == "SGD":
            self.ui.par3_label.setText("Momentum")
            tooltip = "Отвечает за накапливание градиентного спуска\nв необходимом направлении и гашение колебаний обучения"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.bool_check1.setVisible(True)
            self.ui.par2_label.setText("Nesterov")
            self.ui.par2_label.setToolTip("Применять ли импульс Нестерова")
            self.logic.hide_elements(self.ui, 3, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "RMSprop" or opt == "RMSprop":
            self.ui.par2_label.setText("Centered")
            tooltip = "Если True, градиент нормализован оченочным различием градиента."
            tooltip += "\nЕсли False, то нецентрированным вторым моментом"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.bool_check1.setVisible(True)
            self.ui.par3_label.setText("Momentum")
            tooltip = "Отвечает за накапливание градиентного спуска\nв необходимом направлении и гашение колебаний обучения"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Rho")
            tooltip = "Понижающий фактор для истории градиента"
            self.ui.par4_label.setToolTip(tooltip)
            self.ui.par5_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par5_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 5, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
            
        elif self.ui.list.currentText() == "Adam" or opt == "Adam":
            self.ui.par2_label.setText("Amsgrad")
            tooltip = "Применять или нет AMSGrad вариант этого алгоритма оптимизации"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.bool_check1.setVisible(True)
            self.ui.par3_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Beta_1")
            tooltip = "Экспоненциональная ставка снижения для первого момента оценки"
            self.ui.par4_label.setToolTip(tooltip)
            self.ui.par5_label.setText("Beta_2")
            tooltip = "Экспоненциональная ставка снижения для второго момента оценки"
            self.ui.par5_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 5, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
            
        elif self.ui.list.currentText() == "Adadelta" or opt == "Adadelta":
            self.ui.par2_label.setText("Rho")
            tooltip = "Понижающий фактор для истории градиента"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par3_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "Nadam" or opt == "Nadam":
            self.ui.par2_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Beta_1")
            tooltip = "Экспоненциональная ставка снижения для первого момента оценки"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Beta_2")
            tooltip = "Экспоненциональная ставка снижения для второго момента оценки"
            self.ui.par4_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 4)
            self.resize(300, 260)
            self.ui.buttons.move(110, 220)
                    
        elif self.ui.list.currentText() == "Adagrad" or opt == "Adagrad":
            self.ui.par2_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Initial_accum_value")
            tooltip = "Начальное значение для аккумуляторов (препараметр значения momentum)"
            self.ui.par3_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "Adamax" or opt == "Adamax":
            self.ui.par2_label.setText("Epsilon")
            tooltip = "Маленькая константа для числовой стабильности"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Beta_1")
            tooltip = "Экспоненциональная ставка снижения для первого момента оценки"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Beta_2")
            tooltip = "Экспоненциональная ставка снижения для второго момента оценки"
            self.ui.par4_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 4)
            self.resize(300, 260)
            self.ui.buttons.move(110, 220)
            
        elif self.ui.list.currentText() == "Ftrl" or opt == "Ftrl":
            self.ui.par2_label.setText("Initial_accum_value")
            tooltip = "Начальное значение для аккумуляторов (препараметр значения momentum)"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("L1_regul_strength")
            tooltip = "Должно быть меньше или равно 0"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("L2_regul_strength")
            self.ui.par4_label.setToolTip(tooltip)
            self.ui.par4.setVisible(True)
            self.ui.par5_label.setText("L2_shrinkage")
            tooltip = "Отличается от L2 выше тем, что то стабилизационные штрафы,"
            tooltip += "\nа shrinkage штрафы магнитуды."
            tooltip += "\nКогда входные данные разреженные, усадка будет только на активных весах"
            self.ui.par5_label.setToolTip(tooltip)
            self.ui.par5.setVisible(True)
            self.ui.par6_label.setText("Beta")
            tooltip = "Представляет beta-значение из оригинальной работы"
            self.ui.par6_label.setToolTip(tooltip)
            self.ui.par6.setVisible(True)
            self.ui.par7_label.setText("Lr_power")
            tooltip = "Контролирует, как обучающая ставка снижается при обучении."
            tooltip += "\nДолжно быть меньше или равно 0"
            self.ui.par7_label.setToolTip(tooltip)
            self.ui.par7.setVisible(True)
            self.logic.hide_elements(self.ui, 7)
            self.resize(300, 380)
            self.ui.buttons.move(110, 340)

    def choice_losses(self, loss=None):
        self.ui.par1_label.setText("Reduction")
        tooltip = "Параметр, характеризующий использования опции понижения"
        self.ui.par1_label.setToolTip(tooltip)
        if (self.ui.list.currentText() == "BinaryCrossentropy" or loss == "BinaryCrossentropy") or (
            self.ui.list.currentText() == "CategoricalCrossentropy" or loss == "CategoricalCrossentropy"):
            self.ui.par2_label.setText("From logits")
            self.ui.par3_label.setText("Label smoothing")
            self.logic.hide_elements(self.ui, 3, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "SparseCategorical") or (loss == "SparseCategorical"):
            self.ui.par2_label.setText("From logits")
            self.logic.hide_elements(self.ui, 2, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "Huber") or (loss == "Huber"):
            self.ui.par2_label.setText("Delta")
            self.ui.par2_label.setToolTip("Значения точки, где функция меняется с квадратической на линейную")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "Poisson" or loss == "Poison") or (
            self.ui.list.currentText() == "MSE" or loss == "MSE") or (
            self.ui.list.currentText() == "MAE" or loss == "MAE") or (
            self.ui.list.currentText() == "MAEPercentage" or loss == "MAEPercentage") or (
            self.ui.list.currentText() == "MSEPLogarithmic" or loss == "MSEPLogarithmic") or (
            self.ui.list.currentText() == "Hinge" or loss == "Hinge") or (
            self.ui.list.currentText() == "SquaredHinge" or loss == "SquaredHinge") or (
            self.ui.list.currentText() == "CategoricalHinge" or loss == "CategoricalHinge") or (
            self.ui.list.currentText() == "LogCosh" or loss == "LogCosh") or (
            self.ui.list.currentText() == "KLDivergence" or loss == "KLDivergence"):
            self.logic.hide_elements(self.ui, 1)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "CosineSimilarity" or loss == "CosineSimilarity":
            self.ui.par2_label.setText("Axis")
            tooltip = "Ось, вдоль которой данная функция потерь вычисляется (ось признаков)"
            self.ui.par2_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
    def choice_metrics(self, metric=None):
        self.ui.par1_label.setText("Dtype")
        self.ui.par1_label.setToolTip("Тип данных для результатов метрики")
        if (self.ui.list.currentText() == "Accuracy" or metric == "Accuracy") or (
            self.ui.list.currentText() == "CategoricalAccuracy" or metric == "CategoricalAccuracy") or (
            self.ui.list.currentText() == "SparseCategorical" or metric == "SparseCategorical") or (
            self.ui.list.currentText() == "Hinge" or metric == "Hinge") or (
            self.ui.list.currentText() == "SquaredHinge" or metric == "SquaredHinge") or (
            self.ui.list.currentText() == "CategoricalHinge" or metric == "CategoricalHinge") or (
            self.ui.list.currentText() == "KLDivergence" or metric == "KLDivergence") or (
            self.ui.list.currentText() == "Poisson" or metric == "Poisson") or (
            self.ui.list.currentText() == "MSE" or metric == "MSE") or (
            self.ui.list.currentText() == "RootMSE" or metric == "RootMSE") or (
            self.ui.list.currentText() == "MAE" or metric == "MAE") or (
            self.ui.list.currentText() == "MAEPercentage" or metric == "MAEPercentage") or (
            self.ui.list.currentText() == "MSELogarithmic" or metric == "MSELogarithmic") or (
            self.ui.list.currentText() == "LogCoshError" or metric == "LogCoshError"):
            self.logic.hide_elements(self.ui, 1)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "TopKCategorical" or metric == "TopKCategorical") or (
            self.ui.list.currentText() == "SparseTopKCategorical" or metric == "SparseTopKCategorical"):
            self.ui.par2_label.setText("K")
            self.ui.par2_label.setToolTip("Число верхних элементов для расчёта метрики")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "BinaryAccuracy" or metric == "BinaryAccuracy"):
            self.ui.par2_label.setText("Threshold")
            self.ui.par2_label.setToolTip("Порог для решения, 1 ли предсказание или 0")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "AUC" or metric == "AUC":
            self.ui.par2_label.setText("Multi_label")
            tooltip = "Нужно ли считать с многими классами меток.\n"
            tooltip += "Тогда метрика считается отдельно для каждого класса и усредняется.\n"
            tooltip += "Инчае метки классов делаются плоскими перед расчётами метрик\n"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("From logits")
            self.ui.par3_label.setToolTip("Будут ли предсказания вероятностями или значениями сигмоиды")
            self.ui.par4_label.setText("Num thresholds")
            self.ui.par4_label.setToolTip("Число порогов, использующеяся когда дискретизируется кривая метрики")
            self.ui.par5_label.setText("Curve")
            self.ui.par5_label.setToolTip("Имя кривой для расчёта метрики")
            self.ui.par6_label.setText("Summation method")
            tooltip = "Описывает метод Riemann summation.\n"
            tooltip += "В зависимости от введённого значения, изменяются способ суммации"
            self.ui.par6_label.setToolTip(tooltip)
            self.ui.par7_label.setText("Thresholds")
            tooltip = "писок значений, использующихся как порог для дискретизации кривой\n"
            tooltip += "Если установлено, то параметр Num thresholds игнорируется"
            self.ui.par7_label.setToolTip(tooltip)
            self.ui.par8_label.setText("Labels weights") 
            tooltip = "Список, массив или тензор неотрицательных весов для рассчёта метрики для многоклассовых данных\n"
            tooltip = "Введите значения через запятую"
            self.ui.par8_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 8, bool_num=2)
            self.ui.par2.setVisible(False)
            self.ui.par3.setVisible(False)
            self.resize(300, 420)
            self.ui.buttons.move(110, 380)

        elif (self.ui.list.currentText() == "Precision" or metric == "Precision") or (
            self.ui.list.currentText() == "Recall" or metric == "Recall"):
            self.ui.par2_label.setText("Thresholds")
            self.ui.par2_label.setToolTip("Порог для решения, 1 ли предсказание или 0")
            self.ui.par3_label.setText("Top K")
            self.ui.par3_label.setToolTip("Количество верхних предсказаний для предположения о необходимости рассчёта метрики")
            self.ui.par4_label.setText("Class ID")
            self.ui.par4_label.setToolTip("Целочисленное ID для которого нужны бинарные метрики")
            self.logic.hide_elements(self.ui, 4)
            self.resize(300, 260)
            self.ui.buttons.move(110, 220)

        elif (self.ui.list.currentText() == "TruePositives" or metric == "TruePositives") or (
            self.ui.list.currentText() == "TrueNegatives" or metric == "TrueNegatives") or (
            self.ui.list.currentText() == "FalsePositives" or metric == "FalsePositives") or (
            self.ui.list.currentText() == "FalseNegatives" or metric == "FalseNegatives"):
            self.ui.par2_label.setText("Thresholds")
            self.ui.par2_label.setToolTip("Порог для решения, 1 ли предсказание или 0")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif (self.ui.list.currentText() == "PrecisionAtRecall" or metric == "PrecisionAtRecall"):
            self.ui.par2_label.setText("Recall")
            self.ui.par2_label.setToolTip("Скалярное значение от 0 до 1")
            self.ui.par3_label.setText("Num thresholds")
            self.ui.par3_label.setToolTip("Количество пороговых значений для рассчёта метрики")
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "SensitivityAtSpecificity" or metric == "SensitivityAtSpecificity"):
            self.ui.par2_label.setText("Specificity")
            self.ui.par2_label.setToolTip("Скалярное значение от 0 до 1")
            self.ui.par3_label.setText("Num thresholds")
            self.ui.par3_label.setToolTip("Количество пороговых значений для рассчёта метрики")
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "SpecificityAtSensitivity" or metric == "SpecificityAtSensitivity"):
            self.ui.par2_label.setText("Sensitivity")
            self.ui.par2_label.setToolTip("Скалярное значение от 0 до 1")
            self.ui.par3_label.setText("Num thresholds")
            self.ui.par3_label.setToolTip("Количество пороговых значений для рассчёта метрики")
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "MeanIoU" or metric == "MeanIou"):
            self.ui.par2_label.setText("Num classes")
            self.ui.par2_label.setToolTip("Возможное число классов для классификации")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "BinaryCrossentropy" or metric == "BinaryCrossentropy") or (
            self.ui.list.currentText() == "CategoricalCrossentropy" or metric == "CategoricalCrossentropy"):
            self.ui.par2_label.setText("From logits")
            self.ui.par2_label.setToolTip("Будет ли выходные данные логическим тензором")
            self.ui.par3_label.setText("Label smoothing")
            self.ui.par3_label.setToolTip("Значение, выражающее сглаживание предсказываемых меток")
            self.logic.hide_elements(self.ui, 3, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "SparseCategorical" or metric == "SparseCategorical"):
            self.ui.par2_label.setText("From logits")
            self.ui.par2_label.setToolTip("Будет ли выходные данные логическим тензором")
            self.ui.par3_label.setText("Axis")
            self.ui.par3_label.setToolTip("Ось, вдоль которой метрика высчитывается")
            self.logic.hide_elements(self.ui, 3, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif (self.ui.list.currentText() == "CosineSimilarity" or metric == "CosineSimilarity"):
            self.ui.par2_label.setText("Axis")
            self.ui.par2_label.setToolTip("Ось, вдоль которой метрика высчитывается")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)                                                                                                                     

    def choice_callbacks(self, callback=None):
        if self.ui.list.currentText() == "BackupAndRestore" or callback == "BackupAndRestore":
            self.ui.par1_label.setText("BackupDir")
            tooltip = "Путь к папке, где сохраняются файлы для восстановления модели\nпри неожиданном завершении обучения"
            self.ui.par1_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 1)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "CSVLogger" or callback == "CSVLogger":
            self.ui.par1_label.setText("Filename")
            self.ui.par1_label.setToolTip("Путь к CSV-файлу")
            self.ui.par2_label.setText("Append")
            tooltip = "Добавлять записи в файл или переписать его заново"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Separator")
            self.ui.par3_label.setToolTip("Разделитель для записей в файле")
            self.logic.hide_elements(self.ui, 3, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "EarlyStopping" or callback == "EarlyStopping":
            self.ui.par1_label.setText("Monitor")
            self.ui.par1_label.setToolTip("Количество записей для мониторинга")
            self.ui.par2_label.setText("Restore_best_weight")
            tooltip = "Хранить ли веса модели с лучшим значением обучения\n"
            tooltip += "Если False, то веса будут сохраняться вне зависимости от значения baseline\n"
            tooltip += "Тогда если нет улучшений в baseline-эпохах\n"
            tooltip += "обучение будет илти patience-эпох и сохраняться веса лучшей эпохи в данном наборе"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Min_delta")
            tooltip = "Минимальное значение качества обучения, принимаемое как улучшение"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Patience")
            tooltip = "Количество эпох без улучшения, после чего обучение остановится"
            self.ui.par4_label.setToolTip(tooltip)
            self.ui.par5_label.setText("Verbose")
            self.ui.par5_label.setToolTip("Режим повторений")
            self.ui.par6_label.setText("Mode")
            tooltip = "Один из {auto, min, max}. Если min, то обучение остановится когда потери перестануть падать\n"
            tooltip += "Если max, то обучение остановится когда точность перестнет расти\n"
            tooltip += "Если auto, направление изменений определяется само исходя из значения monitor"
            self.ui.par6_label.setToolTip(tooltip)
            self.ui.par7_label.setText("Baseline")
            self.ui.par7_label.setToolTip("Основное значение для отслеживаемого параметра качества обучения")
            self.logic.hide_elements(self.ui, 7, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 380)
            self.ui.buttons.move(110, 340)
        
        elif self.ui.list.currentText() == "LambdaCallback" or callback == "LambdaCallback":
            self.ui.par1_label.setText("OnEpochBegin")
            self.ui.par1_label.setToolTip("Анономная функция, вызываемая в начале эпохи\nНапишите её здесь")
            self.ui.par2_label.setText("OnEpochEnd")
            self.ui.par2_label.setToolTip("Анономная функция, вызываемая в конце эпохи\nНапишите её здесь")
            self.ui.par3_label.setText("OnBatchBegin")
            self.ui.par3_label.setToolTip("Анономная функция, вызываемая перед обработкой пакет\nНапишите её здесьа")
            self.ui.par4_label.setText("OnBatchEnd")
            self.ui.par4_label.setToolTip("Анономная функция, вызываемая в конце обработки пакета\nНапишите её здесь")
            self.ui.par5_label.setText("OnTrainBegin")
            self.ui.par5_label.setToolTip("Анономная функция, вызываемая в начале обучения\nНапишите её здесь")
            self.ui.par6_label.setText("OnTrainEnd")
            self.ui.par6_label.setToolTip("Анономная функция, вызываемая в конце обучения\nНапишите её здесь")
            self.logic.hide_elements(self.ui, 6)
            self.resize(300, 340)
            self.ui.buttons.move(110, 300)            
            
        elif self.ui.list.currentText() == "LearningRateSchedular" or callback == "LearningRateSchedular":
            self.ui.par1_label.setText("Schedule")
            self.ui.par1_label.setToolTip("Функция, меняющая скорость обучения")
            self.ui.par2_label.setText("Verbose")
            self.ui.par2_label.setToolTip("int. 0: quiet, 1: update messages.")
            self.logic.hide_elements(self.ui, 2, fun_number=True)
            self.ui.par1.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            self.ui.fun_button.clicked.connect(lambda: self.logic.choice_fun_file(
                obj=self))
            
        elif self.ui.list.currentText() == "ModelCheckpoint" or callback == "ModelCheckpoint":
            self.ui.par1_label.setText("Filepath")
            self.ui.par1_label.setToolTip("Путь к файлу сохраняемой модели")
            self.ui.par2_label.setText("Save_best_only")
            self.ui.par2_label.setToolTip("Сохранять или нет лучшую модель")
            self.ui.par3_label.setText("Save_weights_only")
            self.ui.par3_label.setToolTip("Сохранять полную модель или только веса")
            self.ui.par4_label.setText("Monitor")
            self.ui.par4_label.setToolTip("Название параметра, по которому отслеживается качество обучения")
            self.ui.par5_label.setText("Verbose")
            self.ui.par5_label.setToolTip("Режим повторений")
            self.ui.par6_label.setText("Mode")
            tooltip = "Один из {auto, min, max}. Если min, то файл результата перепишется когда потери перестануть падать\n"
            tooltip += "Если max, то файл результата перепишется когда точность перестнет расти\n"
            tooltip += "Если auto, направление изменений определяется само исходя из значения monitor"
            self.ui.par6_label.setToolTip(tooltip)
            self.ui.par7_label.setText("Save_freq")
            tooltip = "Если epoch, то модель сохраняется после каждой эпохи\n"
            tooltip += "Если число, то модель сохраняется после заданного количества эпох"
            self.ui.par7_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 7, bool_num=2)
            self.ui.par2.setVisible(False)
            self.ui.par3.setVisible(False)
            self.resize(300, 380)
            self.ui.buttons.move(110, 340)
            
        elif self.ui.list.currentText() == "ProgbarLogger" or callback == "ProgbarLogger":
            self.ui.par1_label.setText("Count_mode")
            self.ui.par1_label.setToolTip("Следует считать увиденные примеры или шаги\пакеты")
            self.ui.par2_label.setText("Stateful_metrics")
            tooltip = "Список метрик, что не должны быть усреднены\n"
            tooltip += "Введите список метрик через запятую"
            self.ui.par2_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "ReduceLROnPlateau" or callback == "ReduceLROnPlateau":
            self.ui.par1_label.setText("Monitor")
            self.ui.par1_label.setToolTip("Количество записей для мониторинга")
            self.ui.par2_label.setText("Factor")
            self.ui.par2_label.setToolTip("Фактор, на основе которого скорость обучения уменьшается")
            self.ui.par3_label.setText("Patience")
            tooltip = "Количество эпох без улучшения, после чего обучение остановится"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Verbose")
            self.ui.par4_label.setToolTip("Режим повторений")
            self.ui.par5_label.setText("Mode")
            tooltip = "Один из {auto, min, max}. Если min, то скорость обучения уменьшится когда потери перестануть падать\n"
            tooltip += "Если max, то скорость обучения уменьшится когда точность перестнет расти\n"
            tooltip += "Если auto, направление изменений определяется само исходя из значения monitor"
            self.ui.par5_label.setToolTip(tooltip)
            self.ui.par6_label.setText("Min_delta")
            self.ui.par6_label.setToolTip("Порог для отслеживания оптимума модели")
            self.ui.par7_label.setText("Cooldown")
            self.ui.par7_label.setToolTip("Количество эпох, после которых скорость обучения будет снижаться")
            self.ui.par8_label.setText("Min_lr")
            self.ui.par8_label.setToolTip("Минимальный допустимый порог скорости обучения")
            self.logic.hide_elements(self.ui, 8)
            self.resize(300, 420)
            self.ui.buttons.move(110, 380)
            
        elif self.ui.list.currentText() == "RemoteMonitor" or callback == "RemoteMonitor":
            self.ui.par1_label.setText("Root")
            self.ui.par1_label.setToolTip("Ссылка на удаленный сервер")
            self.ui.par2_label.setText("Send_as_JSON")
            self.ui.par2_label.setToolTip("Отправлять или нет запрос как application/json")
            self.ui.par3_label.setText("Path")
            tooltip = "Путь относительно сервера, куда будут отправляться файлы"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Field")
            self.ui.par4_label.setToolTip("JSON-поле, под которым данные будут хранится")
            self.ui.par5_label.setText("Headers")
            self.ui.par5_label.setToolTip("Опционально настраиваемые HTTP-заголовки\nВведите словарь Python текстом")
            self.logic.hide_elements(self.ui, 5, bool_num=1)
            self.ui.par2.setVisible(False)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
            
        elif self.ui.list.currentText() == "TensorBoard" or callback == "TensorBoard":
            self.ui.par1_label.setText("Log_dir")
            self.ui.par1_label.setToolTip("Путь к папке, куда будут сохраняться логи")
            self.ui.par2_label.setText("Write_graph")
            self.ui.par2_label.setToolTip("Визуализировать ли графики на TensorBoard")
            self.ui.par3_label.setText("Write_images")
            self.ui.par3_label.setToolTip("Визуализировать ли изображения весов в TensorBoard")
            self.ui.par4_label.setText("Write_steps\n_per_epoch")
            self.ui.par4_label.setToolTip("Записывать ли в логи значения на каждом шаге")
            self.ui.par5_label.setText("Histogram_freg")
            self.ui.par5_label.setToolTip("Частота, с которой вычисляются веса для гистограммы")
            self.ui.par6_label.setText("Update_freq")
            tooltip = "Если batch\epoch, то потери и метрики записываются после каждой эпохи\n"
            tooltip += "Если число, то после заданного числа обработанных пакетов"
            self.ui.par6_label.setToolTip(tooltip)
            self.ui.par7_label.setText("Profile_batch")
            self.ui.par7_label.setToolTip("Профиль пакетов для расчета характеристик")
            self.ui.par8_label.setText("Embeddings_freqs")
            self.ui.par8_label.setToolTip("Частота, с которой embeddings-слои будут визуализироваться")
            self.ui.par9_label.setText("Embeddings_metadata")
            tooltip = "Словарь, где указаны имена embeddings-слоев и путь к файлу для сохранения метаданных слоя\n"
            tooltip += "Введите словарь Python текстом"
            self.ui.par9_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 9, bool_num=3)
            self.ui.par2.setVisible(False)
            self.ui.par3.setVisible(False)
            self.ui.par4.setVisible(False)
            self.resize(300, 460)
            self.ui.buttons.move(110, 420)

        elif self.ui.list.currentText() == "TerminateOnNaN" or callback == "TerminateOnNaN":
            self.logic.hide_elements(self.ui, 1)
            self.ui.par1.setVisible(False)
            self.ui.par1_label.setVisible(False)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
    def choice_nets(self, net=None):
        self.ui.par1_label.setText("Weights")
        self.ui.par1_label.setToolTip("Выбор используемых весов модели")
        self.ui.par2_label.setText("Include_top")
        self.ui.par2_label.setToolTip("Включать или нет полносвязный классификатор")
        self.ui.par3_label.setText("Input_tensor")
        self.ui.par3_label.setToolTip("Входной тензор модели")
        self.ui.par4_label.setText("Input_shape")
        self.ui.par4_label.setToolTip("Форма входных данных")
        self.ui.par5_label.setText("Pooling")
        tooltip = "Способ извлечения признаков, когда include_top установлен в false"
        self.ui.par5_label.setToolTip(tooltip)
        self.ui.par6_label.setText("Classes")
        self.ui.par6_label.setToolTip("Число классов модели")
        self.ui.par7_label.setText("Activation")
        self.ui.par7_label.setToolTip("Функция активации последнего слоя классификатора")
        if self.ui.list.currentText() == "Xception" or net == "Xception" or (
           self.ui.list.currentText() == "InceptionResNetV2" or net == "InceptionResNetV2") or (
           self.ui.list.currentText() == "InceptionV3" or net == "InceptionV3") or (
           self.ui.list.currentText() == "ResNet50" or net == "ResNet50") or (
           self.ui.list.currentText() == "ResNet101" or net == "ResNet101") or (
           self.ui.list.currentText() == "ResNet152" or net == "ResNet152") or (
           self.ui.list.currentText() == "ResNet50V2" or net == "ResNet50V2") or (
           self.ui.list.currentText() == "VGG16" or net == "VGG16") or (
           self.ui.list.currentText() == "VGG19" or net == "VGG19"):
            self.logic.hide_elements(self.ui, 7, bool_num=1)
            self.resize(300, 380)
            self.ui.buttons.move(110, 340)
            
        elif self.ui.list.currentText() == "MobileNet" or net == "MobileNet":
            self.ui.par8_label.setText("Alpha")
            self.ui.par8_label.setToolTip("Параметр контроля ширины слоёв модели")
            self.ui.par9_label.setText("Depth_multiplier")
            self.ui.par9_label.setToolTip("Глубина свёртки по глубине")
            self.ui.par10_label.setText("Dropout")
            self.ui.par10_label.setToolTip("Степень применения размыкания")
            self.logic.hide_elements(self.ui, 10, bool_num=1)
            self.resize(300, 500)
            self.ui.buttons.move(110, 460)
            
        elif self.ui.list.currentText() == "MobileNetV2" or net == "MobileNetV2":
            self.ui.par8_label.setText("Alpha")
            self.ui.par8_label.setToolTip("Параметр контроля ширины слоёв модели")
            self.logic.hide_elements(self.ui, 8, bool_num=1)
            self.resize(300, 420)
            self.ui.buttons.move(110, 380)
            
        elif self.ui.list.currentText() == "DenseNet121" or net == "DenseNet121" or (
           self.ui.list.currentText() == "DenseNet169" or net == "DenseNet169") or (
           self.ui.list.currentText() == "DenseNet201" or net == "DenseNet201"):
            self.logic.hide_elements(self.ui, 5, bool_num=1)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
        self.ui.par2.setVisible(False)
            
    def choice_check_metric(self, check_metric=None): 
        self.ui.par1_label.setText("Sample weight")
        self.ui.par1_label.setToolTip("Веса примеров в форме массива")
        if self.ui.list.currentText() == "F1" or check_metric == "F1" or (
           self.ui.list.currentText() == "Precision" or check_metric == "Precision") or (
           self.ui.list.currentText() == "Recall" or check_metric == "Recall") or (
           self.ui.list.currentText() == "Jaccard" or check_metric == "Jaccard"):
            self.ui.par2_label.setText("Labels")
            self.ui.par2_label.setToolTip("Набор меток, если average != 'binary', или их порядок при average None")
            self.ui.par3_label.setText("Pos_label")
            self.ui.par4_label.setToolTip("Отчетный класс, если average 'binary', иначе параметр игнорируется")
            self.ui.par5_label.setText("Average")
            tooltip = "Если None, то оценки считаются для каждого класса\n"
            tooltip += "Иначе параметр определяет тип усреднения данных"
            self.ui.par4_label.setToolTip(tooltip)
            self.ui.par5_label.setText("Zero_division")
            tooltip = "Набор значений, возвращаемых когда все предсказания и метки негативные\n"
            tooltip += "(Есть деление на 0)"
            self.ui.par5_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 5)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
            
        elif self.ui.list.currentText() == "Accuracy" or check_metric == "Accuracy":
            self.ui.par2_label.setText("Normalize")
            tooltip = "Возвращать ли функцию от числа или число правильно классифицированных меток"
            self.ui.par2_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 2)
            self.ui.par2.setVisible(False)
            self.ui.bool_check1.setVisible(True)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "Balanced_accuracy" or check_metric == "Balanced_accuracy":
            self.ui.par2_label.setText("Adjusted")
            tooltip = "Настравивать или нет результат на рандомное представление как 0 и совершенное как 1"
            self.ui.par2_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 2)
            self.ui.par2.setVisible(False)
            self.ui.bool_check1.setVisible(True)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "Top_K_accuracy" or check_metric == "Top_K_accuracy":
            self.ui.par2_label.setText("Normalize")
            tooltip = "Возвращать ли функцию от числа или число правильно классифицированных меток"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("K")
            self.ui.par3_label.setToolTip("Число исходов для нахождения корректной метки")
            self.ui.par4_label.setText("Labels")
            self.ui.par4_label.setToolTip("Список меток что определяют классы предсказаний")
            self.logic.hide_elements(self.ui, 4)
            self.ui.par2.setVisible(False)
            self.ui.bool_check1.setVisible(True)
            self.resize(300, 260)
            self.ui.buttons.move(110, 220)
            
        elif self.ui.list.currentText() == "Average_precision" or check_metric == "Average_precision":
            self.ui.par2_label.setText("Pos_label")
            self.ui.par2_label.setToolTip("Метка положительного класса для бинарной классификации")
            self.ui.par3_label.setText("Average")
            tooltip = "Если None, то оценки считаются для каждого класса\n"
            tooltip += "Иначе параметр определяет тип усреднения данных"
            self.ui.par3_label.setToolTip(tooltip)
            self.logic.hide_elements(self.ui, 3)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)
            
        elif self.ui.list.currentText() == "Neg_brief" or check_metric == "Neg_brief":
            self.ui.par2_label.setText("Pos_label")
            self.ui.par2_label.setToolTip("Метка положительного класса для бинарной классификации")
            self.logic.hide_elements(self.ui, 2)
            self.resize(300, 230)
            self.ui.buttons.move(110, 180)

        elif self.ui.list.currentText() == "Neg_log" or check_metric == "Neg_log":
            self.ui.par2_label.setText("Normalize")
            self.ui.par2_label.setToolTip("Возвращать ли средние потери на экземпляр или сумму потерь")
            self.ui.par3_label.setText("Eps")
            tooltip = "Потери определеённые для р=0 и р=1, так что вероятности стремятся к максимуму"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Labels")
            self.ui.par4_label.setToolTip("Список меток что определяют классы предсказаний")
            self.logic.hide_elements(self.ui, 4)
            self.ui.par2.setVisible(False)
            self.ui.bool_check1.setVisible(True)
            self.resize(300, 260)
            self.ui.buttons.move(110, 220)

        elif self.ui.list.currentText() == "ROC_AUC" or check_metric == "ROC_AUC":
            self.ui.par2_label.setText("Average")
            tooltip = "Если None, то оценки считаются для каждого класса\n"
            tooltip += "Иначе параметр определяет тип усреднения данных"
            self.ui.par2_label.setToolTip(tooltip)
            self.ui.par3_label.setText("Max_fpr")
            tooltip = "Определяет величину возвращаемого стандартизированного частичного AUC в диапазоне от 0 до max_fpr"
            self.ui.par3_label.setToolTip(tooltip)
            self.ui.par4_label.setText("Multiclass")
            self.ui.par4_label.setToolTip("Тип метрики для многоклассовой классификации")
            self.ui.par5_label.setText("Labels")
            self.ui.par5_label.setToolTip("Список меток что определяют классы предсказаний")
            self.logic.hide_elements(self.ui, 5)
            self.resize(300, 300)
            self.ui.buttons.move(110, 260)
        
    def between_wins(self):
        #набор считанных значений параметров
        settings = (self.ui.par1.text(), self.ui.par2.text(),
                         self.ui.par3.text(), self.ui.par4.text(),
                         self.ui.par5.text(), self.ui.par6.text(),
                         self.ui.par7.text(), self.ui.par8.text(), self.ui.par9.text())

        #набор всех логических параметров
        bools = (self.ui.bool_check1.isChecked(), self.ui.bool_check2.isChecked(),
                 self.ui.bool_check3.isChecked())

        #набор всех путей к функциям параметрам
        buttons_par = (self.path, self.truth_labels)

        #проверяем, было ли что-то выбрано среди настроек
        check = helper.check_settings(settings, bools, buttons_par)
        if not check:
            return False, None

        #в зависимости от того, для чего вызваны настройки, создаем этот объект с введёнными настройками 
        if self.win_type == 0:
            opt = self.logic.pass_opts_settings(self.ui)
            return True, opt
        elif self.win_type == 1:
            loss = self.logic.pass_loss_settings(self.ui)
            return True, loss
        elif self.win_type == 2:
            metric = self.logic.pass_metric_settings(self.ui)
            return True, metric
        elif self.win_type == 3:
            callback = self.logic.pass_callbacks_settings(self.ui)
            return True, callback
        elif self.win_type == 4:
            net = self.logic.pass_net_settings(self.ui)
            return True, net
        else:
            check_metric = self.logic.pass_check_metric_settings(self.ui)
            return True, check_metric

        
            
