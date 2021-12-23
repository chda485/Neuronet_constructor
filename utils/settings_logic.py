from PyQt5 import QtWidgets
from keras import optimizers, metrics, losses, callbacks
import keras.applications as ready_nets
import helper, os
import numpy as np
import csv


class SettingsLogic():
    def __init__(self, win_type, parent):
        self.win_type = win_type
        self.fun_path = None
        self.truth_labels = []
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(False)
            ui.par3.setVisible(False)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(False)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(False)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(False)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(False)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(False)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(False)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(True)
            ui.par9.setVisible(False)
            ui.par10.setVisible(False)
        elif number == 9:
            ui.par1_label.setVisible(True)
            ui.par2_label.setVisible(True)
            ui.par3_label.setVisible(True)
            ui.par4_label.setVisible(True)
            ui.par5_label.setVisible(True)
            ui.par6_label.setVisible(True)
            ui.par7_label.setVisible(True)
            ui.par8_label.setVisible(True)
            ui.par9_label.setVisible(True)
            ui.par10_label.setVisible(False)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(True)
            ui.par9.setVisible(True)
            ui.par10.setVisible(False)
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
            ui.par10_label.setVisible(True)
            ui.par1.setVisible(True)
            ui.par2.setVisible(True)
            ui.par3.setVisible(True)
            ui.par4.setVisible(True)
            ui.par5.setVisible(True)
            ui.par6.setVisible(True)
            ui.par7.setVisible(True)
            ui.par8.setVisible(True)
            ui.par9.setVisible(True)
            ui.par10.setVisible(True)
            
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
        lr = float(ui.par1.text()) if len(ui.par1.text()) != 0 else 0.01
        if ui.list.currentText() == "SGD":
            momentum = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.0
            opt = optimizers.SGD(learning_rate=lr, momentum=momentum, 
                                 nesterov=ui.bool_check1.isChecked())
            return opt
        
        elif ui.list.currentText() == "RMSprop":
            epsilon = ui.par5.text() if len(ui.par5.text()) != 0 else 1e-7
            momentum = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.0
            rho = float(ui.par4.text()) if len(ui.par4.text()) != 0 else 0.9
            opt = optimizers.RMSprop(learning_rate=lr, epsilon=epsilon,
                                     momentum=momentum,
                                     centered=ui.bool_check1.isChecked())
            return opt
        
        elif ui.list.currentText() == "Adam":
            beta1 = float(ui.par4.text()) if len(ui.par4.text()) != 0 else 0.9
            beta2 = float(ui.par5.text()) if len(ui.par5.text()) != 0 else 0.999
            epsilon = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 1e-7
            opt = optimizers.Adam(learning_rate=lr, beta_1=beta1,
                                  beta_2=beta2, epsilon=epsilon,
                                  amsgrad=ui.bool_check1.isChecked())
            return opt
        
        elif ui.list.currentText() == "Adadelta":
            epsilon = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 1e-7
            rho = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 0.95
            opt = optimizers.Adadelta(learning_rate=lr, rho=rho,
                                      epsilon=epsilon)
            return opt
        
        elif ui.list.currentText() == "Nadam":
            beta1 = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.9
            beta2 = float(ui.par4.text()) if len(ui.par4.text()) != 0 else 0.999
            epsilon = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Nadam(learning_rate=lr, beta_1=beta1,
                                   beta_2=beta2, epsilon=epsilon)
            return opt
        
        elif ui.list.currentText() == "Adagrad":
            in_acc_val = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.1
            epsilon = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Adagrad(learning_rate=lr,
                                     initial_accumulator_value=in_acc_val,
                                     epsilon=epsilon)
            return opt
        
        elif ui.list.currentText() == "Adamax":
            beta1 = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.9
            beta2 = float(ui.par4.text()) if len(ui.par4.text()) != 0 else 0.999
            epsilon = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 1e-7
            opt = optimizers.Adamax(learning_rate=lr, beta_1=beta1,
                                   beta_2=beta2, epsilon=epsilon)
            return opt
        
        elif ui.list.currentText() == "Ftrl":
            lr_power = float(ui.par7.text()) if len(ui.par7.text()) != 0 else -0.5
            in_acc_val = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 0.1
            l1_reg_str = float(ui.par3.text()) if len(ui.par3.text()) != 0 else 0.0
            l2_reg_str = float(ui.par4.text()) if len(ui.par4.text()) != 0 else 0.0
            l2_shrin = float(ui.par5.text()) if len(ui.par5.text()) != 0 else 0.0
            beta = float(ui.par6.text()) if len(ui.par6.text()) != 0 else 0.0
            opt = optimizers.Ftrl(learning_rate=lr, learning_rate_power=lr_power,
                                  initial_accumulator_value=in_acc_val,
                                  l1_regularization_strength=l1_reg_str,
                                  l2_regularization_strength=l2_reg_str,
                                  l2_shrinkage_regularization_strength=l2_shrin,
                                  beta=beta)
            return opt

    def pass_loss_settings(self, ui):
        reduction = ui.par1.text() if len(ui.par1.text()) != 0 else "auto"
        if ui.list.currentText() == "BinaryCrossentropy":
            label_smoothing = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 0
            loss = losses.BinaryCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                            label_smoothing=label_smoothing,
                                            reduction=reduction)
            return loss

        elif ui.list.currentText() == "CategoricalCrossentropy":
            label_smoothing = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 0
            loss = losses.CategoricalCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                            label_smoothing=label_smoothing,
                                            reduction=reduction)
            return loss

        elif ui.list.currentText() == "SparseCategorical":
            loss = losses.SparseCategoricalCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                                        reduction=reduction)
            return loss

        elif (ui.list.currentText() == "Poisson") or (ui.list.currentText() == "MSE") or (
            ui.list.currentText() == "MAE") or (ui.list.currentText() == "MAEPercentage") or (
            ui.list.currentText() == "MSEPLogarithmic") or (ui.list.currentText() == "Hinge") or (
            ui.list.currentText() == "SquaredHinge") or (ui.list.currentText() == "CategoricalHinge") or (
            ui.list.currentText() == "LogCosh") or (ui.list.currentText() == "KLDivergence"):           
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
            elif ui.list.currentText() == "KLDivergence":
                loss = losses.KLDivergence(reduction=reduction)
            return loss

        elif ui.list.currentText() == "CosineSimilarity":
            axis = int(ui.par2.text()) if len(ui.par2.text()) != 0 else -1
            loss = losses.CosineSimilarity(axis=axis, reduction=reduction)
            return loss

        elif ui.list.currentText() == "Huber":
            delta = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 1.0
            loss = losses.Huber(delta=delta, reduction=reduction)
            return loss

    def pass_metric_settings(self, ui):
        dtype = ui.par1.text() if len(ui.par1.text()) != 0 else None
        if (ui.list.currentText() == "Accuracy") or (ui.list.currentText() == "CategoricalAccuracy") or (
            ui.list.currentText() == "SparseCategorical") or (
            ui.list.currentText() == "Hinge") or (ui.list.currentText() == "SquaredHinge") or (
            ui.list.currentText() == "CategoricalHinge") or (
            ui.list.currentText() == "KLDivergence") or (ui.list.currentText() == "Poisson") or (
            ui.list.currentText() == "MSE") or (ui.list.currentText() == "RootMSE") or (
            ui.list.currentText() == "MAE") or (ui.list.currentText() == "MAEPercentage") or (
            ui.list.currentText() == "MSELogarithmic") or (ui.list.currentText() == "LogCoshError"):
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
            return metric

        elif ui.list.currentText() == "TopKCategorical":
            k = int(ui.par2.text()) if len(ui.par2.text()) != 0 else 5
            metric = metrics.TopKCategoricalAccuracy(k=k, dtype=dtype)
            return metric

        elif ui.list.currentText() == "SparseTopKCategorical":
            k = int(ui.par2.text()) if len(ui.par2.text()) != 0 else 5
            metric = metrics.SparseTopKCategoricalAccuracy(k=k, dtype=dtype)
            return metric
        
        elif ui.list.currentText() == "BinaryAccuracy":
            threshold = float(ui.par2.text()) if len(ui.par2.text()) != 0 else 0.5
            metric = metrics.BinaryAccuracy(threshold=threshold, dtype=dtype)
            return metric

        elif ui.list.currentText() == "AUC":
            num_thresholds = int(ui.par4.text()) if len(ui.par4.text()) != 0 else 200
            curve = ui.par5.text() if len(ui.par5.text()) != 0 else "ROC"
            summation = ui.par6.text() if len(ui.par6.text()) != 0 else "interpolation"
            thresholds = float(ui.par7.text()) if len(ui.par7.text()) != 0 else None
            label_weights = ui.par8.text() if len(ui.par8.text()) != 0 else None
            if label_weights:
                label_weights = self.make_array(label_weights)
            metric = metrics.AUC(num_thresholds=num_thresholds, curve=curve,
                                 summation_method=summation, dtype=dtype,
                                 thresholds=thresholds, multi_label=ui.bool_check1.isChecked(),
                                 label_weights=label_weights)
            return metric

        elif ui.list.currentText() == "Precision":
            thresholds = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            topK = int(ui.par3.text()) if len(ui.par3.text()) != 0 else None
            classID = int(ui.par4.text()) if len(ui.par4.text()) != 0 else None
            metric = metrics.Precision(thresholds=thresholds, top_k=topK,
                                       class_id=classID, dtype=dtype)
            return metric

        elif ui.list.currentText() == "Recall":
            thresholds = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            topK = int(ui.par3.text()) if len(ui.par3.text()) != 0 else None
            classID = int(ui.par4.text()) if len(ui.par4.text()) != 0 else None
            metric = metrics.Recall(thresholds=thresholds, top_k=topK,
                                       class_id=classID, dtype=dtype)
            return metric

        elif (ui.list.currentText() == "TruePositives") or (ui.list.currentText() == "TrueNegatives") or (
            ui.list.currentText() == "FalsePositives") or (ui.list.currentText() == "FalseNegatives"):
            thresholds = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            if ui.list.currentText() == "TruePositives":
                metric = metrics.TruePositives(dtype=dtype, thresholds=thresholds)
            elif ui.list.currentText() == "TrueNegatives":
                metric = metrics.TrueNegatives(dtype=dtype, thresholds=thresholds)
            elif ui.list.currentText() == "FalsePositives":
                metric = metrics.FalsePositives(dtype=dtype, thresholds=thresholds)
            elif ui.list.currentText() == "FalseNegatives":
                metric = metrics.FalseNegatives(dtype=dtype, thresholds=thresholds)
            return metric

        elif (ui.list.currentText() == "PrecisionAtRecall") or (
              ui.list.currentText() == "SensitivityAtSpecificity") or (
              ui.list.currentText() == "SpecificityAtSensitivity"):
            if ui.list.currentText() == "PrecisionAtRecall":
                recall = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            elif ui.list.currentText() == "SensitivityAtSpecificity":
                specificity = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            elif ui.list.currentText() == "SpecificityAtSensitivity":
                sensitivity = float(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            num_thresholds = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 200
            if ui.list.currentText() == "PrecisionAtRecall":
                metric = metrics.PrecisionAtRecall(num_thresholds=num_thresholds, recall=recall,
                                                   dtype=dtype)
            elif ui.list.currentText() == "SensitivityAtSpecificity":
                metric = metrics.SensitivityAtSpecificity(num_thresholds=num_thresholds,
                                                   specificity=specificity,
                                                   dtype=dtype)
            elif ui.list.currentText() == "SpecificityAtSensitivity":
                metric = metrics.SpecificityAtSensitivity(num_thresholds=num_thresholds,
                                                          sensitivity=sensitivity,
                                                          dtype=dtype)
            return metric

        elif ui.list.currentText() == "MeanIoU":
            classes = int(ui.par2.text()) if len(ui.par2.text()) != 0 else None
            metric = metrics.MeanIoU(num_classes=classes, dtype=dtype)
            return metric

        elif ui.list.currentText() == "BinaryCrossentropy":
            label_smoothing = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 0
            metric = metrics.BinaryCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                            label_smoothing=label_smoothing,
                                            dtype=dtype)
            return metric

        elif ui.list.currentText() == "CategoricalCrossentropy":
            label_smoothing = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 0
            metric = metrics.CategoricalCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                            label_smoothing=label_smoothing,
                                            dtype=dtype)
            return metric

        elif ui.list.currentText() == "SparseCategorical" or (
             ui.list.currentText() == "CosineSimilarity"):
            axis = int(ui.par3.text()) if len(ui.par3.text()) != 0 else -1
            if ui.list.currentText() == "SparseCategorical":
                metric = metrics.SparseCategoricalCrossentropy(from_logits=ui.bool_check1.isChecked(),
                                                            axis=axis, dtype=dtype)
            else:
                metric = metrics.CosineSimilarity(axis=axis, dtype=dtype)
            return metric

    def pass_callbacks_settings(self, ui):
        if ui.list.currentText() == "BackupAndRestore":
            dir_ = ui.par1.text() if len(ui.par1.text()) != 0 else None
            callback = callbacks.BackupAndRestore(backup_dir=dir_)
            return callback

        elif ui.list.currentText() == "CSVLogger":
            file = ui.par1.text() if len(ui.par1.text()) != 0 else None
            sep = ui.par3.text() if len(ui.par3.text()) != 0 else ","
            callback = callbacks.CSVLogger(filename=file, separator=sep,
                                           append=ui.bool_check1.isChecked())
            return callback

        elif ui.list.currentText() == "EarlyStopping":
            monitor = ui.par1.text() if len(ui.par1.text()) != 0 else "val_loss"
            delta = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 0
            patience = int(ui.par4.text()) if len(ui.par4.text()) != 0 else 0
            verbose = int(ui.par5.text()) if len(ui.par5.text()) != 0 else 0
            mode = ui.par6.text() if len(ui.par6.text()) != 0 else "auto"
            baseline = float(ui.par7.text()) if len(ui.par7.text()) != 0 else None
            callback = callbacks.EarlyStopping(monitor=monitor, restore_best_weights=ui.bool_check1.isChecked(),
                                               min_delta=delta, patience=patience,
                                               verbose=verbose, mode=mode,
                                               baseline=baseline)
            return callback

        elif ui.list.currentText() == "LambdaCallback":
            on_epoch_begin = ui.par1.text() if len(ui.par1.text()) != 0 else None
            on_epoch_end = ui.par2.text() if len(ui.par2.text()) != 0 else None
            on_batch_begin = ui.par3.text() if len(ui.par3.text()) != 0 else None
            on_batch_end = ui.par4.text() if len(ui.par4.text()) != 0 else None
            on_train_begin = ui.par5.text() if len(ui.par5.text()) != 0 else None
            on_train_end = ui.par6.text() if len(ui.par6.text()) != 0 else None

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
            return callback

        elif ui.list.currentText() == "LearningRateSchedular":
            if self.fun_path:
                fun = helper.include_function(self.fun_path, os.getcwd())
            else:
                fun = None
            verbose = int(ui.par2.text()) if len(ui.par2.text()) != 0 else 0
            callback = callbacks.LearningRateScheduler(schedule=fun, verbose=verbose)
            return callback

        elif ui.list.currentText() == "ModelCheckpoint":
            file = ui.par1.text() if len(ui.par1.text()) != 0 else None
            monitor = ui.par4.text() if len(ui.par4.text()) != 0 else "val_loss"
            verbose = int(ui.par5.text()) if len(ui.par5.text()) != 0 else 0
            mode = ui.par6.text() if len(ui.par6.text()) != 0 else "auto"
            save_freq = ui.par7.text() if len(ui.par7.text()) != 0 else "epoch"
            callback = callbacks.ModelCheckpoint(filepath=file, save_best_only=ui.bool_check1.isChecked(),
                                                 save_weights_only=ui.bool_check2.isChecked(),
                                                 verbose=verbose, mode=mode,
                                                 monitor=monitor, save_freq=save_freq)
            return callback

        elif ui.list.currentText() == "ProgbarLogger":
            mode = ui.par1.text() if len(ui.par1.text()) != 0 else "samples"
            stateful = ui.par2.text() if len(ui.par2.text()) != 0 else None
            if stateful:
                stateful = self.make_array(stateful)
            callback = callbacks.ProgbarLogger(count_mode=mode, stateful_metrics=stateful)
            return callback

        elif ui.list.currentText() == "ReduceLROnPlateau":
            monitor = ui.par1.text() if len(ui.par1.text()) != 0 else "val_loss"
            factor = int(ui.par2.text()) if len(ui.par2.text()) != 0 else 0.1
            patience = int(ui.par3.text()) if len(ui.par3.text()) != 0 else 10
            verbose = int(ui.par4.text()) if len(ui.par4.text()) != 0 else 0
            mode = ui.par5.text() if len(ui.par5.text()) != 0 else "auto"
            delta = float(ui.par6.text()) if len(ui.par6.text()) != 0 else 0.0001
            cooldown = int(ui.par7.text()) if len(ui.par7.text()) != 0 else 0
            min_lr = int(ui.par8.text()) if len(ui.par8.text()) != 0 else 0
            callback = callbacks.ReduceLROnPlateau(factor=factor, patience=patience,
                                                 verbose=verbose, mode=mode,
                                                 monitor=monitor, min_delta=delta,
                                                 cooldown=cooldown, min_lr=min_lr)
            return callback

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
            callback = callbacks.RemoteMonitor(root=root, send_as_json=ui.bool_check1.isChecked(),
                                                 path=path, field=field, headers=headers)
            return callback

        elif ui.list.currentText() == "TensorBoard":
            dir_ = ui.par1.text() if len(ui.par1.text()) != 0 else "logs"
            histogram = ui.par5.text() if len(ui.par5.text()) != 0 else 0
            update = ui.par6.text() if len(ui.par6.text()) != 0 else "epoch"
            profile = int(ui.par7.text()) if len(ui.par7.text()) != 0 else 2
            freq = int(ui.par8.text()) if len(ui.par8.text()) != 0 else 0
            metadata = ui.par9.text() if len(ui.par9.text()) != 0 else None
            if metadata:
                array = np.asarray(metadata.split(','))
                dict_ = {}
                for header in array:
                    dict_[header.split(':')[0]] = header.split(':')[1]
                metadata = dict_
            callback = callbacks.TensorBoard(log_dir=dir_, histogram_freq=int(histogram),
                                             write_graph=ui.bool_check1.isChecked(),
                                             write_images=ui.bool_check2.isChecked(),
                                             write_steps_per_second=ui.bool_check3.isChecked(),
                                             update_freq=update, profile_batch=profile,
                                             embeddings_freq=freq, 
                                             embeddings_metadata=metadata)
            return callback
        
    def pass_net_settings(self, ui):
        weights = ui.par1.text() if len(ui.par1.text()) != 0 else "imagenet"
        input_tensor = ui.par3.text() if len(ui.par3.text()) != 0 else None
        input_shape = ui.par4.text() if len(ui.par4.text()) != 0 else None
        pooling = ui.par5.text() if len(ui.par5.text()) != 0 else None
        classes = int(ui.par6.text()) if len(ui.par6.text()) != 0 else 1000
        if ui.list.currentText() == "Xception" or ui.list.currentText() == "InceptionResNetV2" or (
           ui.list.currentText() == "InceptionV3") or ui.list.currentText() == "ResNet50" or (
           ui.list.currentText() == "ResNet101") or ui.list.currentText() == "ResNet152" or (
           ui.list.currentText() == "ResNet50V2") or ui.list.currentText() == "VGG16" or (
           ui.list.currentText() == "VGG19") or ui.list.currentText() == "ResNet101V2" or (
           ui.list.currentText() == "ResNet152V2"):
            activation = ui.par7.text() if len(ui.par7.text()) != 0 else "softmax"
            if ui.list.currentText() == "Xception":
                net = ready_nets.Xception(include_top=ui.bool_check1.isChecked(),
                                          weights=weights, input_tensor=input_tensor,
                                          input_shape=input_shape, classes=classes,
                                          pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "InceptionResNetV2":
                net = ready_nets.InceptionResNetV2(include_top=ui.bool_check1.isChecked(),
                                          weights=weights, input_tensor=input_tensor,
                                          input_shape=input_shape, classes=classes,
                                          pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet50":
                net = ready_nets.ResNet50(include_top=ui.bool_check1.isChecked(),
                                          weights=weights, input_tensor=input_tensor,
                                          input_shape=input_shape, classes=classes,
                                          pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet101":
                net = ready_nets.ResNet101(include_top=ui.bool_check1.isChecked(),
                                           weights=weights, input_tensor=input_tensor,
                                           input_shape=input_shape, classes=classes,
                                           pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "InceptionV3":
                net = ready_nets.InceptionV3(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet152":
                net = ready_nets.ResNet152(include_top=ui.bool_check1.isChecked(),
                                           weights=weights, input_tensor=input_tensor,
                                           input_shape=input_shape, classes=classes,
                                           pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet50V2":
                net = ready_nets.ResNet50V2(include_top=ui.bool_check1.isChecked(),
                                            weights=weights, input_tensor=input_tensor,
                                            input_shape=input_shape, classes=classes,
                                            pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet101V2":
                net = ready_nets.ResNet101V2(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "ResNet152V2":
                net = ready_nets.ResNet152V2(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "VGG16":
                net = ready_nets.VGG16(include_top=ui.bool_check1.isChecked(),
                                       weights=weights, input_tensor=input_tensor,
                                       input_shape=input_shape, classes=classes,
                                       pooling=pooling, classifier_activation=activation)
                return net
            
            elif ui.list.currentText() == "VGG19":
                net = ready_nets.VGG19(include_top=ui.bool_check1.isChecked(),
                                       weights=weights, input_tensor=input_tensor,
                                       input_shape=input_shape, classes=classes,
                                       pooling=pooling, classifier_activation=activation)
                return net
        
        elif ui.list.currentText() == "MobileNet":
            activation = ui.par7.text() if len(ui.par7.text()) != 0 else "softmax"
            alpha = float(ui.par8.text()) if len(ui.par8.text()) != 0 else 1.0
            multi = int(ui.par9.text()) if len(ui.par9.text()) != 0 else 1
            dropout = float(ui.par10.text()) if len(ui.par10.text()) != 0 else 0.001
            net = ready_nets.MobileNet(include_top=ui.bool_check1.isChecked(),
                                       weights=weights, input_tensor=input_tensor,
                                       input_shape=input_shape, classes=classes,
                                       pooling=pooling, classifier_activation=activation,
                                       alpha=alpha, depth_multiplier=multi,
                                       dropout=dropout)
            return net
        
        elif ui.list.currentText() == "MobileNetV2":
            activation = ui.par7.text() if len(ui.par7.text()) != 0 else "softmax"
            alpha = float(ui.par8.text()) if len(ui.par8.text()) != 0 else 1.0
            net = ready_nets.MobileNetv2(include_top=ui.bool_check1.isChecked(),
                                         weights=weights, input_tensor=input_tensor,
                                         input_shape=input_shape, classes=classes,
                                         pooling=pooling, classifier_activation=activation,
                                         alpha=alpha)
            return net
        
        elif ui.list.currentText() == "DenseNet121" or ui.list.currentText() == "DenseNet169" or (
           ui.list.currentText() == "DenseNet201"):
            if ui.list.currentText() == "DenseNet121":
                net = ready_nets.DenseNet121(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling)
                return net
            
            elif ui.list.currentText() == "DenseNet169":
                net = ready_nets.DenseNet169(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling)
                return net
            
            elif ui.list.currentText() == "DenseNet201":
                net = ready_nets.DenseNet201(include_top=ui.bool_check1.isChecked(),
                                             weights=weights, input_tensor=input_tensor,
                                             input_shape=input_shape, classes=classes,
                                             pooling=pooling)
                return net

    def pass_check_metric_settings(self, ui):
        results = ""
        results += "true_lables|" + ui.par1.text() + ";" if len (
            ui.par1.text()) != 0 else ""
        results += "sample_weight|" + ui.par2.text() + ";" if len(
            ui.par2.text()) != 0 else ""
        if ui.list.currentText() == "F1" or ui.list.currentText() == "Precision" or (
           ui.list.currentText() == "Recall") or ui.list.currentText() == "Jaccard":
               results += "labels|" + ui.par3.text() + ";" if len(
                   ui.par3.text()) != 0 else ""
               results += "pos_label|" + ui.par4.text() + ";" if len(
                   ui.par4.text()) != 0 else ""
               results += "average|" + ui.par5.text() + ";" if len(
                   ui.par5.text()) != 0 else ""
               results += "zero_division|" + ui.par6.text() if len(
                   ui.par6.text()) != 0 else ""

        elif ui.list.currentText() == "Accuracy":
            results += "normalize|" + str(ui.bool_check2.isChecked())

        elif ui.list.currentText() == "Balanced_accuracy":
            results += "adjusted|" + str(ui.bool_check2.isChecked())

        elif ui.list.currentText() == "Top_K_accuracy":
            results += "normalize|" + str(ui.bool_check2.isChecked()) + ";"
            results += "k:" + ui.par4.text() + ";" if len(
                ui.par4.text()) != 0 else ""
            results += "labels|" + ui.par5.text() if len(
                ui.par5.text()) != 0 else ""

        elif ui.list.currentText() == "Average_precision":
            results += "pos_label|" + ui.par3.text() + ";" if len(
                ui.par3.text()) != 0 else ""
            results += "average|" + ui.par4.text() if len(
                ui.par4.text()) != 0 else ""

        elif ui.list.currentText() == "Neg_brief":
            results += "pos_label|" + ui.par3.text() if len(
                ui.par3.text()) != 0 else ""

        elif ui.list.currentText() == "Neg_log":
            results += "normalize|" + str(ui.bool_check2.isChecked()) + ";"
            results += "eps:" + ui.par4.text() + ";" if len(
                ui.par4.text()) != 0 else ""
            results += "labels|" + ui.par5.text() if len(
                ui.par5.text()) != 0 else ""

        elif ui.list.currentText() == "ROC_AUC":
            results += "average|" + ui.par3.text() + ";" if len(
                ui.par3.text()) != 0 else ""
            results += "max_fpr|" + ui.par4.text() + ";" if len(
                ui.par4.text()) != 0 else ""
            results += "multi_class|" + ui.par5.text() + ";" if len(
                ui.par5.text()) != 0 else ""
            results += "labels|" + ui.par6.text() if len(
                ui.par6.text()) != 0 else ""           

        #убираем последнее ; если есть
        if results[-1] == ';':
            results = results[:-1]
        return results

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
    
    def read_true_label(self, obj):
        #открываем окно поиска файла с метками
        path = QtWidgets.QFileDialog.getOpenFileName(self.parent,
                                                     filter="CSV files(*.csv)")
        #если файл выбрали
        if len(path[0]) != 0:
            f = open(path[0], 'r')
            csv_reader = csv.reader(f)
            for label in csv_reader:
                self.truth_label.append(label)
            obj.truth_labels = np.asarray(self.truth_labels)
