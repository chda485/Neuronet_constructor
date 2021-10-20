from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
#from keras import optimizers, metrics, losses, callbacks
import helper, os


class SettingsLogic():
    def __init__(self, win_type, parent):
        self.win_type = win_type
        self.fun_path = None
        self.parent = parent

    def hide_elements(self, ui, number=9, bool_num=0, fun_number=False):
        if number == 1:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(False)
            ui.par3_label.setVisible(False)
            ui.par4_label.setVisible(False)
            ui.par5_label.setVisible(False)
            ui.par6_label.setVisible(False)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(False)
            ui.par3.setVisible(False)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 2:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(False)
            ui.par4_label.setVisible(False)
            ui.par5_label.setVisible(False)
            ui.par6_label.setVisible(False)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(False)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 3:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(False)
            ui.par5_label.setVisible(False)
            ui.par6_label.setVisible(False)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 4:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(False)
            ui.par6_label.setVisible(False)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 5:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(False)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 6:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(True)
            ui.par7_label.setVisible(False)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 7:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(True)
            ui.par7_label.setVisible(True)
            ui.par8_label.setVisible(False)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
        elif number == 8:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(True)
            ui.par7_label.setVisible(True)
            ui.par8_label.setVisible(True)
            ui.par9_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(True)
            ui.par9.setVisible(False)
        else:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(True)
            ui.par7_label.setVisible(True)
            ui.par8_label.setVisible(True)
            ui.par9_label.setVisible(True)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(True)
            ui.par9.setVisible(True)
            
        if bool_num == 0:
            ui.bool_check1.setVisible(False)
            ui.bool_check2.setVisible(False)
            ui.bool_check3.setVisible(False)
        elif bool_num == 1:
            ui.bool_check1.setVisible(True)
            ui.bool_check2.setVisible(False)
            ui.bool_check3.setVisible(False)
        elif bool_num == 2:
            ui.bool_check1.setVisible(True)
            ui.bool_check2.setVisible(True)
            ui.bool_check3.setVisible(False)
        else:
            ui.bool_check1.setVisible(True)
            ui.bool_check2.setVisible(True)
            ui.bool_check3.setVisible(True)
            
        if fun_number:
            ui.fun_button.setVisible(True)
        else:
        	ui.fun_button.setVisible(False)

    def pass_opts_settings(self, ui):
        if ui.list.currentText() == "SGD":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.01
            momentum = ui.par3.text() if len(ui.par3.text()) != 0 else 0.0
            opt = optimizers.SGD(learning_rate=float(lr), momentum=float(momentum), 
                                 nesterov=ui.bool_check1.isChecked())
            return True, opt
        
        elif ui.list.currentText() == "RMSprop":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.01
            epsilon = ui.par5.text() if len(ui.par5.text()) != 0 else 1e-7
            momentum = ui.par3.text() if len(ui.par3.text()) != 0 else 0.0
            rho = ui.par4.text() if len(ui.par4.text()) != 0 else 0.9
            opt = optimizers.RMSprop(learning_rate=float(lr), epsilon=float(epsilon),
                                     momentum=float(momentum),
                                     centered=ui.bool_check1.isChecked())
            return True, opt
        
        elif ui.list.currentText() == "Adam":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            beta1 = ui.par4.text() if len(ui.par4.text()) != 0 else 0.9
            beta2 = ui.par5.text() if len(ui.par5.text()) != 0 else 0.999
            epsilon = ui.par3.text() if len(ui.par3.text()) != 0 else 1e-7
            opt = optimizers.Adam(learning_rate=float(lr), beta_1=float(beta1),
                                  beta_2=float(beta2), epsilon=float(epsilon),
                                  amsgrad=ui.bool_check1.isChecked())
            return True, opt
        
        elif ui.list.currentText() == "Adadelta":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            epsilon = ui.par3.text() if len(ui.par3.text()) != 0 else 1e-7
            rho = ui.par2.text() if len(ui.par2.text()) != 0 else 0.95
            opt = optimizers.Adadelta(learning_rate=float(lr), rho=float(rho),
                                      epsilon=float(epsilon))
            return True, opt
        
        elif ui.list.currentText() == "Nadam":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            beta1 = ui.par3.text() if len(ui.par3.text()) != 0 else 0.9
            beta2 = ui.par4.text() if len(ui.par4.text()) != 0 else 0.999
            epsilon = ui.par2.text() if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Nadam(learning_rate=float(lr), beta_1=float(beta1),
                                   beta_2=float(beta2), epsilon=float(epsilon))
            return True, opt
        
        elif ui.list.currentText() == "Adagrad":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            in_acc_val = ui.par3.text() if len(ui.par3.text()) != 0 else 0.1
            epsilon = ui.par2.text() if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Adagrad(learning_rate=float(lr),
                                     initial_accumulator_value=float(in_acc_val),
                                     epsilon=float(epsilon))
            return True, opt
        
        elif ui.list.currentText() == "Adamax":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            beta1 = ui.par3.text() if len(ui.par3.text()) != 0 else 0.9
            beta2 = ui.par4.text() if len(ui.par4.text()) != 0 else 0.999
            epsilon = ui.par2.text() if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Adamax(learning_rate=float(lr), beta_1=float(beta1),
                                   beta_2=float(beta2), epsilon=float(epsilon))
            return True, opt
        
        elif ui.list.currentText() == "Ftrl":
            lr = ui.par1.text() if len(ui.par1.text()) != 0 else 0.001
            lr_power = ui.lr_power.text() if len(ui.lr_power.text()) != 0 else -0.5
            in_acc_val = ui.par2.text() if len(ui.par2.text()) != 0 else 0.1
            l1_reg_str = ui.par3.text() if len(ui.par3.text()) != 0 else 0.0
            l2_reg_str = ui.par4.text() if len(ui.par4.text()) != 0 else 0.0
            l2_shrin = ui.par5.text() if len(ui.par5.text()) != 0 else 0.0
            beta = ui.par6.text() if len(ui.par6.text()) != 0 else 0.0
            opt = optimizers.Ftrl(learning_rate=float(lr), lr_power=float(lr_power),
                                  initial_accumulator_value=float(in_acc_val),
                                  l1_regularization_strength=float(l1_reg_str),
                                  l2_regularization_strength=float(l2_reg_str),
                                  l2_shrinkage_regularization_strength=float(l2_shrin),
                                  beta=float(beta))
            return True, opt

    def pass_loss_settings(self, ui):
        if ui.list.currentText() == "BinaryCrossentropy":
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            label_smoothing = ui.par3.text() if len(ui.par3.text()) != 0 else 0
            axis = ui.par4.text() if len(ui.par4.text()) != 0 else -1
            loss = losses.BinaryCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                            labels_smothing=int(label_smoothing),
                                           axis=int(axis), reduction=reduction)
            return True, loss

        elif ui.list.currentText() == "CategoricalCrossentropy":
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            label_smoothing = ui.par3.text() if len(ui.par3.text()) != 0 else 0
            axis = ui.par4.text() if len(ui.par4.text()) != 0 else -1
            loss = losses.CategoricalCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                            labels_smothing=int(label_smoothing),
                                           axis=int(axis), reduction=reduction)
            return True, loss

        elif ui.list.currentText() == "SparseCategorical":
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            loss = losses.SparseCategoricalCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                                        reduction=reduction)
            return True, loss

        elif (ui.list.currentText() == "Poisson") or (ui.list.currentText() == "MSE") or (
            ui.list.currentText() == "MAE") or (ui.list.currentText() == "MAEPercentage") or (
            ui.list.currentText() == "MSEPLogarithmic") or (ui.list.currentText() == "Hinge") or (
            ui.list.currentText() == "SquaredHinge") or (ui.list.currentText() == "CategoricalHinge") or (
            ui.list.currentText() == "LogCosh"):
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            if ui.list.currentText() == "Poisson":
                loss = losses.Poisson(reduction=reduction)
            elif ui.list.currentText() == "MSE":
                loss = losses.MeanSquaredError(reduction=reduction)
            elif ui.list.currentText() == "MAE":
                loss = losses.MeanAbsoluteError(reduction=reduction)
            elif ui.list.currentText() == "MAEPercentage":
                loss = losses.MeanAbsolutePercentageError(reduction=reduction)
            elif ui.list.currentText() == "MSEPLogarithmic":
                loss = losses.MeanSquaredLogarithmicError(reduction=reduction)
            elif ui.list.currentText() == "Hinge":
                loss = losses.Hinge(reduction=reduction)
            elif ui.list.currentText() == "SquaredHinge":
                loss = losses.SquaredHinge(reduction=reduction)
            elif ui.list.currentText() == "CategoricalHinge":
                loss = losses.CategoricalHinge(reduction=reduction)
            elif ui.list.currentText() == "LogCosh":
                loss = losses.LogCosh(reduction=reduction)
            return True, loss

        elif ui.list.currentText() == "CosineSimilarity":
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            axis = ui.par2.text() if len(ui.par2.text()) != 0 else -1
            loss = losses.CosineSimilarity(axis=int(axis), reduction=reduction)
            return True, loss

        elif ui.list.currentText() == "Huber":
            reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
            delta = ui.par2.text() if len(ui.par2.text()) != 0 else 1.0
            loss = losses.CosineSimilarity(delta=float(delta), reduction=reduction)
            return True, loss

    def pass_metric_settings(self, ui):
        if (ui.list.currentText() == "Accuracy") or (ui.list.currentText() == "CategoricalAccuracy") or (
            ui.list.currentText() == "SparseCategorical") or (
            ui.list.currentText() == "Hinge") or (ui.list.currentText() == "SquaredHinge") or (
            ui.list.currentText() == "CategoricalHinge") or (
            ui.list.currentText() == "KLDivergence") or (ui.list.currentText() == "Poisson") or (
            ui.list.currentText() == "MSE") or (ui.list.currentText() == "RootMSE") or (
            ui.list.currentText() == "MAE") or (ui.list.currentText() == "MAEPercentage") or (
            ui.list.currentText() == "MSELogarithmic") or (ui.list.currentText() == "LogCoshError"):
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            if ui.list.currentText() == "Accuracy":
                metric = metrics.Accuracy(dtype=dtype)
            elif ui.list.currentText() == "CategoricalAccuracy":
                metric = metrics.CategoricalAccuracy(dtype=dtype)
            elif ui.list.currentText() == "SparseCategorical":
                metric = metrics.SparseCategoricalAccuracy(dtype=dtype)
            elif ui.list.currentText() == "Hinge":
                metric = metrics.Hinge(dtype=dtype)
            elif ui.list.currentText() == "SquaredHinge":
                metric = metrics.SquaredHinge(dtype=dtype)
            elif ui.list.currentText() == "CategoricalHinge":
                metric = metrics.CategoricalHinge(dtype=dtype)
            elif ui.list.currentText() == "KLDivergence":
                metric = metrics.KLDivergence(dtype=dtype)
            elif ui.list.currentText() == "Poisson":
                metric = metrics.Poisson(dtype=dtype)
            elif ui.list.currentText() == "MSE":
                metric = metrics.MeanSquaredError(dtype=dtype)
            elif ui.list.currentText() == "RootMSE":
                metric = metrics.RootMeanSquaredError(dtype=dtype)
            elif ui.list.currentText() == "MAE":
                metric = metrics.MeanAbsoluteError(dtype=dtype)
            elif ui.list.currentText() == "MAEPercentage":
                metric = metrics.MeanAbsolutePercentageError(dtype=dtype)
            elif ui.list.currentText() == "MSELogarithmic":
                metric = metrics.MeanSquaredLogarithmicError(dtype=dtype)
            elif ui.list.currentText() == "LogCoshError":
                metric = metrics.LogCoshError(dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "TopKCategorical":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            k = ui.par2.text() if len(ui.par2.text()) != 0 else 5
            metric = metrics.TopKCategoricalAccuracy(k=int(k), dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "SparseTopKCategorical":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            k = ui.par2.text() if len(ui.par2.text()) != 0 else 5
            metric = metrics.SparseTopKCategoricalAccuracy(k=int(k), dtype=dtype)
            return True, metric
        
        elif ui.list.currentText() == "BinaryAccuracy":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            threshold = ui.par2.text() if len(ui.par2.text()) != 0 else 0.5
            metric = metrics.BinaryAccuracy(threshold=float(threshold), dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "AUC":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            num_thresholds = ui.par4.text() if len(ui.par4.text()) != 0 else 200
            curve = ui.par5.text() if len(ui.par5.text()) != 0 else "ROC"
            summation = ui.par6.text() if len(ui.par6.text()) != 0 else "interpolation"
            thresholds = ui.par7.text() if len(ui.par7.text()) != 0 else None
            num_labels = ui.par8.text() if len(ui.par8.text()) != 0 else None
            label_weights = ui.par9.text() if len(ui.par9.text()) != 0 else None
            if not label_weights:
                label_weights = make_array(label_weights)
            metric = metrics.AUC(num_thresholds=int(num_thresholds), curve=curve,
                                 summation_method=summation, dtype=dtype,
                                 thresholds=float(thresholds), multi_label=ui.bool_check1.isCheck(),
                                 num_labels=int(num_labels), label_weights=label_weights,
                                 from_logits=ui.bool_check2.isCheck())
            return True, metric

        elif ui.list.currentText() == "Precision":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            thresholds = ui.par2.text() if len(ui.par2.text()) != 0 else None
            topK = ui.par3.text() if len(ui.par3.text()) != 0 else None
            classID = ui.par4.text() if len(ui.par4.text()) != 0 else None
            metric = metrics.Precision(threshold=float(threshold), top_k=int(topK),
                                       class_id=int(classID), dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "Recall":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            thresholds = ui.par2.text() if len(ui.par2.text()) != 0 else None
            topK = ui.par3.text() if len(ui.par3.text()) != 0 else None
            classID = ui.par4.text() if len(ui.par4.text()) != 0 else None
            metric = metrics.Recall(threshold=float(threshold), top_k=int(topK),
                                       class_id=int(classID), dtype=dtype)
            return True, metric

        elif (ui.list.currentText() == "TruePositives") or (ui.list.currentText() == "TrueNegatives") or (
            ui.list.currentText() == "FalsePositives") or (ui.list.currentText() == "FalseNegatives"):
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            thresholds = ui.par2.text() if len(ui.par2.text()) != 0 else None
            if ui.list.currentText() == "TruePositives":
                metric = metrics.TruePositives(dtype=dtype, thresholds=float(thresholds))
            elif ui.list.currentText() == "TrueNegatives":
                metric = metrics.TrueNegatives(dtype=dtype, thresholds=float(thresholds))
            elif ui.list.currentText() == "FalsePositives":
                metric = metrics.FalsePositives(dtype=dtype, thresholds=float(thresholds))
            elif ui.list.currentText() == "FalseNegatives":
                metric = metrics.FalseNegatives(dtype=dtype, thresholds=float(thresholds))
            return True, metric

        elif (ui.list.currentText() == "PrecisionAtRecall") or (
              ui.lost.currentText() == "SensitivityAtSpecificity") or (
              ui.lost.currentText() == "SpecificityAtSensitivity"):
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            if ui.list.currentText() == "PrecisionAtRecall":
                recall = ui.par2.text() if len(ui.par2.text()) != 0 else None
            elif ui.lost.currentText() == "SensitivityAtSpecificity":
                specificity = ui.par2.text() if len(ui.par2.text()) != 0 else None
            elif ui.lost.currentText() == "SpecificityAtSensitivity":
                sensitivity = ui.par2.text() if len(ui.par2.text()) != 0 else None
            num_thresholds = ui.par3.text() if len(ui.par3.text()) != 0 else 200
            classID = ui.par4.text() if len(ui.par4.text()) != 0 else None
            if ui.list.currentText() == "PrecisionAtRecall":
                metric = metrics.PrecisionAtRecall(num_thresholds=int(num_thresholds), recall=int(recall),
                                                   class_id=int(classID), dtype=dtype)
            elif ui.lost.currentText() == "SensitivityAtSpecificity":
                metric = metrics.SensitivityAtSpecificity(num_thresholds=int(num_thresholds),
                                                   specificity=int(specificity),
                                                   class_id=int(classID), dtype=dtype)
            elif ui.lost.currentText() == "SpecificityAtSensitivity":
                metric = metrics.SpecificityAtSensitivity(num_thresholds=int(num_thresholds),
                                                          sensitivity=int(sensitivity),
                                                          class_id=int(classID), dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "MeanIoU":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            classes = ui.par2.text() if len(ui.par2.text()) != 0 else None
            metric = metrics.MeanIoU(num_classes=int(classes), dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "BinaryCrossentropy":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            label_smoothing = ui.par3.text() if len(ui.par3.text()) != 0 else 0
            metric = metrics.BinaryCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                            labels_smothing=int(label_smoothing),
                                            dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "CategoricalCrossentropy":
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            label_smoothing = ui.par3.text() if len(ui.par3.text()) != 0 else 0
            metric = metrics.CategoricalCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                            labels_smothing=int(label_smoothing),
                                            dtype=dtype)
            return True, metric

        elif ui.list.currentText() == "SparseCategorical" or (
             ui.list.currentText() == "CosineSimilarity"):
            dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
            axis = ui.par3.text() if len(ui.par3.text()) != 0 else -1
            if ui.list.currentText() == "SparseCategorical":
                metric = metrics.SparseCategoricalCrossentropy(from_logits=ui.bool_check1.isCheck(),
                                                            axis=int(axis), dtype=dtype)
            else:
                metric = metrics.CosineSimilarity(from_logits=ui.bool_check1.isCheck(),
                                               axis=int(axis), dtype=dtype)
            return True, metric

    def pass_callbacks_settings(self, ui):
        if ui.list.currentText() == "BackupAndRestore":
            dir_ = ui.par1.text() if len(ui.par1.text()) != 0 else None
            callback = callbacks.BackupAndRestore(backup_dir=dir_)
            return True, callback

        elif ui.list.currentText() == "CSVLogger":
            file = ui.par1.text() if len(ui.par1.text()) != 0 else None
            sep = ui.par3.text() if len(ui.par3.text()) != 0 else ","
            callback = callbacks.CSVLogger(filename=file, separator=sep,
                                           append=ui.bool_check1.isCheck())
            return True, callback

        elif ui.list.currentText() == "EarlyStopping":
            monitor = ui.par1.text() if len(ui.par1.text()) != 0 else "val_loss"
            delta = ui.par3.text() if len(ui.par3.text()) != 0 else 0
            patience = ui.par4.text() if len(ui.par4.text()) != 0 else 0
            verbose = ui.par5.text() if len(ui.par5.text()) != 0 else 0
            mode = ui.par6.text() if len(ui.par6.text()) != 0 else "auto"
            baseline = ui.par7.text() if len(ui.par7.text()) != 0 else None
            callback = callbacks.EarlyStopping(monitor=monitor, restore_best_weights=ui.bool_check1.isCheck(),
                                               min_delta=int(delta), patience=int(patience),
                                               verbose=int(verbose), mode=mode,
                                               baseline=float(baseline))
            return True, callback

        elif ui.list.currentText() == "LambdaCallback":
            on_epoch_begin = ui.par1.text() if len(ui.par1.text()) != 0 else "None"
            on_epoch_end = ui.par2.text() if len(ui.par2.text()) != 0 else "None"
            on_batch_begin = ui.par3.text() if len(ui.par3.text()) != 0 else "None"
            on_batch_end = ui.par4.text() if len(ui.par4.text()) != 0 else "None"
            on_train_begin = ui.par5.text() if len(ui.par5.text()) != 0 else "None"
            on_train_end = ui.par6.text() if len(ui.par6.text()) != 0 else "None"

            f = open("lambda.py", 'w+')
            content = f.read()
            new_content = content.replace("(parameter1)", on_epoch_begin)
            new_content = content.replace("(parameter2)", on_epoch_end)
            new_content = content.replace("(parameter3)", on_batch_begin)
            new_content = content.replace("(parameter4)", on_batch_end)
            new_content = content.replace("(parameter5)", on_train_begin)
            new_content = content.replace("(parameter6)", on_train_end)
            f.write(new_content)
            f.close()
            
            import lambda_           
            callback = lambda_.create_lambda()
            return True, callback

        elif ui.list.currentText() == "LearningRateSchedular":
            if self.fun_path:
                fun = helper.include_function(self.fun_path, os.getcwd())
            else:
                fun = None
            verbose = ui.par2.text() if len(ui.par2.text()) != 0 else 0
            callback = callbacks.LearningRateScheduler(schedule=fun, verbose=int(verbose))
            return True, callback

        elif ui.list.currentText() == "ModelCheckpoint":
            file = ui.par1.text() if len(ui.par1.text()) != 0 else None
            monitor = ui.par4.text() if len(ui.par4.text()) != 0 else "val_loss"
            verbose = ui.par5.text() if len(ui.par5.text()) != 0 else 0
            mode = ui.par6.text() if len(ui.par6.text()) != 0 else "auto"
            save_freq = ui.par7.text() if len(ui.par7.text()) != 0 else "epoch"
            callback = callbacks.ModelCheckpoint(filepath=file, save_best_only=ui.bool_check1.isCheck(),
                                                 save_weights_only=ui.bool_check2.isCheck(),
                                                 verbose=int(verbose), mode=mode,
                                                 monitor=monitor, save_freq=save_freq)
            return True, callback

        elif ui.list.currentText() == "ProgbarLogger":
            mode = ui.par1.text() if len(ui.par1.text()) != 0 else "samples"
            stateful = ui.par2.text() if len(ui.par2.text()) != 0 else None
            if stateful:
                stateful = make_array(stateful)
            callback = callbacks.ProgbarLogger(count_mode=mode, stateful_metrics=stateful)
            return True, callback

        elif ui.list.currentText() == "ReduceLROnPlateau":
            monitor = ui.par1.text() if len(ui.par1.text()) != 0 else "val_loss"
            factor = ui.par2.text() if len(ui.par2.text()) != 0 else 0.1
            patience = ui.par3.text() if len(ui.par3.text()) != 0 else 10
            verbose = ui.par4.text() if len(ui.par4.text()) != 0 else 0
            mode = ui.par5.text() if len(ui.par5.text()) != 0 else "auto"
            delta = ui.par6.text() if len(ui.par6.text()) != 0 else 0.0001
            cooldown = ui.par7.text() if len(ui.par7.text()) != 0 else 0
            min_lr = ui.par8.text() if len(ui.par8.text()) != 0 else 0
            callback = callbacks.ReduceLROnPlateau(factor=int(factor), patience=int(patience),
                                                 verbose=int(verbose), mode=mode,
                                                 monitor=monitor, min_delta=float(delta),
                                                 cooldown=int(cooldown), min_lr=int(min_lr))
            return True, callback

        elif ui.list.currentText() == "RemoteMonitor":
            root = ui.par1.text() if len(ui.par1.text()) != 0 else "http://localhost:9000"
            path = ui.par3.text() if len(ui.par3.text()) != 0 else "/publish/epoch/end/"
            field = ui.par4.text() if len(ui.par4.text()) != 0 else "data"
            headers = ui.par5.text() if len(ui.par5.text()) != 0 else None
            if headers:
                array = np.asarray(headers.split(','))
                dict_ = {}
                for header in array:
                    dict_[header.split(':')[0]] = header.split(':')[1]
                headers = dict_
            callback = callbacks.RemoteMonitor(root=root, send_as_json=ui.bool_check1.isCheck(),
                                                 path=path, field=field, headers=headers)
            return True, callback

        elif ui.list.currentText() == "TensorBoard":
            dir_ = ui.par1.text() if len(ui.par1.text()) != 0 else "logs"
            histogram = ui.par5.text() if len(ui.par5.text()) != 0 else 0
            update = ui.par6.text() if len(ui.par6.text()) != 0 else "epoch"
            profile = ui.par7.text() if len(ui.par7.text()) != 0 else 2
            freq = ui.par8.text() if len(ui.par8.text()) != 0 else 0
            metadata = ui.par9.text() if len(ui.par9.text()) != 0 else None
            if metadata:
                array = np.asarray(metadata.split(','))
                dict_ = {}
                for header in array:
                    dict_[header.split(':')[0]] = header.split(':')[1]
                metadata = dict_
            callback = callbacks.TensorBoard(log_dir=dir_, histogram_freq=int(histogram),
                                             write_graph=ui.bool_check1.isCheck(),
                                             write_images=ui.bool_check2.isCheck(),
                                             write_steps_per_second=ui.bool_check3.isCheck(),
                                             update_freq=update, profile_batch=int(profile),
                                             embeddings_freq=int(freq), 
                                             embeddings_metadata=metadata)
            return True, callback

    def choice_fun_file(self, obj):
    	#открываем окно поиска файла с функцией
        path = QtWidgets.QFileDialog.getOpenFileName(self.parent,
                                                     filter="Python files(*.py)")
        #если файл выбрали
        if len(path[0]) != 0:
            obj.path = path[0]
            self.fun_path = path[0]

    def make_array(self, array_text):
        array = array_text.split(',')
        return np.asarray(array)
    
