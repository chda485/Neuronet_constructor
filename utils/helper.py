import nets
from keras import metrics
import os, cv2, shutil
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from keras import applications as ready_net
import numpy as np

LISTS_NEURONETS = {
    "LeNet": nets.LeNet, "AlexNet": nets.AlexNet,
    "MiniVGGNet": nets.MiniVGGNet, "ShallowNet": nets.ShallowNet,
    "VGG16": nets.VGG16, "VGG19": nets.VGG19,
    "MobileNet": nets.MobileNet, "SqueezeNet": nets.SqueezeNet,
    "ResNet18": nets.ResNet18_34(18), "ResNet34": nets.ResNet18_34(34),
    "ResNet50": nets.ResNet50_152(50), "ResNet101": nets.ResNet50_152(101),
    "ResNet152": nets.ResNet50_152(152), "InceptionV2": nets.InceptionV2,
    "InceptionV3": nets.InceptionV3, "InceptionV4": nets.InceptionV4,
    "Xception": nets.Xception, "GoggleNet": nets.GoogleNet,
    "DenseNet": nets.DenseNet
    }


LIST_LOSSES = {
    "BinaryCrossentropy": "binary_crossentropy", "CategoricalCrossentropy": "categorical_crossentropy",
    "SparseCategorical": "sparse_categorical_crossentropy", "Poisson": "poisson",
    "KLDivergence": "kl_divergence", "MAE": "mae", "MSE": "mse",
    "MAEPercentage": "mean_absolute_percentage_error", "MSEPLogarithmic": "mean_squared_logarithmic_error",
    "CosineSimilarity": "cosine_similarity", "Huber": "huber_class",
    "LogCosh": "log_cosh", "Hinge": "hinge", "SquaredHinge": "squared_hinge",
    "CategoricalHinge": "categorical_hinge"
    }

LIST_METRICS = {
    "Accuracy": "accuracy", "BinaryAccuracy": "binary_accuracy",
    "CategoricalAccuracy": "categorical_accuracy", "TopKCategorical": "top_k_categorical_accuracy",
    "SparseTopKCategorical": "sparse_top_k_categorical_accuracy",
    "BinaryCrossentropy": "binary_crossentropy", 
    "CategoricalCrossentropy": "categorical_crossentropy",
    "SparseCategorical": "sparse_categorical_crossentropy", "Poisson": "poisson",
    "KLDivergence": "kullback_leibler_divergence", "MAE": "mae", "MSE": "mse",
    "MAEPercentage": "mean_absolute_percentage_error", "MSEPLogarithmic": "mean_squared_logarithmic_error",
    "CosineSimilarity": "cosine_similarity", "RootMSE": metrics.RootMeanSquaredError(), 
    "LogCoshError": "logcosh", "AUC": metrics.AUC(), "Precision": "precision",
    "Recall": "recall", "TruePositives": metrics.TruePositives(), 
    "TrueNegatives": metrics.TrueNegatives(),
    "FalsePositives": metrics.FalsePositives(), "FalseNegatives": metrics.FalseNegatives(),
    "PrecisionAtRecall": "precision_at_recall", 
    "SensitivityAtSpecificity": "sensitivity_at_specificity",
    "SpecificityAtSensitivity": "specificity_at_sensitivity", 
    "MeanIoU": "mean_io_u", "Hinge": "hinge", "SquaredHinge": "squared_hinge", "CategoricalHinge": "categorical_hinge"
}

LIST_ADJUST_ONLY_METRICS = [
    "PrecisionAtRecall", "SensitivityAtSpecificity",
    "SpecificityAtSensitivity", "MeanIoU"
]

LIST_WITH_CLASS_METRICS = {
    "AUC": "auc_1", "RootMSE": "root_mean_squared_error",
    "TruePositives": "true_positives_1", "TrueNegatives": "true_negatives_1",
    "FalsePositives": "false_positives_1", "FalseNegatives": "false_negatives_1"
}

LIST_OPTS = ["SGD", "RMSprop", "Adam", "Adadelta",
             "Nadam", "Adagrad", "Adamax", "Ftrl"]

LIST_CALLBACKS = ["ModelCheckpoint", "TensorBoard", "EarlyStopping",
                  "LearningRateSchedular", "ReduceLROnPlateau",
                  "RemoteMonitor", "LambdaCallback", "TerminateOnNaN",
                  "CSVLogger", "ProgbarLogger", "BackupAndRestore"]

LIST_LAYERS = ["Activation", "AveragePool2D", "Conv2D",
               "Conv2DTranspose", "Dense", "GlobalAveragePool2D",
               "GlobalMaxPool2D", "MaxPooling2D", "SeparableConv2D"]

"""
LIST_READY_NETS = {
    "Xception": ready_net.xception.Xception(), "VGG16": ready_net.vgg16.VGG16(),
    "VGG19": ready_net.vgg19.VGG19(), "ResNet50": ready_net.ResNet50(),
    "ResNet101": ready_net.ResNet101(), "ResNet152": ready_net.ResNet152(),
    "ResNet50V2": ready_net.ResNet50V2(), "ResNet101V2": ready_net.ResNet101V2(),
    "ResNet152V2": ready_net.ResNet152V2(), "InceptionV3": ready_net.InceptionV3(),
    "InceptionResNetV2": ready_net.InceptionResNetV2(), "MobileNet": ready_net.MobileNet(),
    "MobileNetV2": ready_net.MobileNetV2(), "DenseNet121": ready_net.DenseNet121(),
    "DenseNet169": ready_net.DenseNet169(), "DenseNet201": ready_net.DenseNet201()
}
"""

LIST_READY_NETS = [
    "Xception", "VGG16",
    "VGG19", "ResNet50",
    "ResNet101", "ResNet152",
    "ResNet50V2", "ResNet101V2",
    "ResNet152V2", "InceptionV3",
    "InceptionResNetV2", "MobileNet",
    "MobileNetV2", "DenseNet121",
    "DenseNet169", "DenseNet201"
]

LIST_CHECK_METRIC = [
    "Accuracy", "Balanced_accuracy", 
    "Top_K_accuracy", "Average_precision", 
    "Neg_brief", "F1", "Neg_log", "ROC_AUC",
    "Precision", "Recall", "Jaccard"
]

def check_all_choised(dataset_path, epochs):
    if len(dataset_path) == 0:
        return "The dataset is not choiced"
    elif len(epochs) == 0:
        return "Epochs are not maintained"
    else:
        return None

def construct_shape(path):
    #3 папки
    temp = os.listdir(path)
    #путь с train
    P = os.path.join(path, temp[0])
    #папки с классми
    temp2 = os.listdir(P)
    P2 = os.path.join(P, temp2[0])
    #папка с файлами первого класса
    temp3 = os.listdir(P2)
    P3 = os.path.join(P2, temp3[0])
    try:
        file = cv2.imread(P3)
    except: 
        return None
    return file.shape

def check_input(shape):
    #проверяем что длина формы больше 1 и содержит измерения данных
    if len(shape) <= 1 or ',' not in shape:
        return False
    #проверяем, нет ли букв
    for c in shape:
        if c.isalpha():
            return False
    return True

def check_settings(settings, bools=(None,None), buttons_par=(None,)):
    answer = False
    #проверяем установку обычных параметров
    for set_ in settings:
        if len(set_) == 0:
            continue
        else:
            answer = True
            return answer
    #проверяем выбор логических параметров
    for bool_ in bools:
        if not bool_:
            continue
        else:
            answer = True
            return answer
    #проверяем установку параметров-кнопок
    for par in buttons_par:
        if par is not None:
            answer = True
            return answer
    return answer
    
def include_function(path, current):#
    #получаем путь к файлу
    base = os.path.basename(path)
    length = len(base) + 1
    folder_path = path[:-length]
    #путь к новому файлу функции
    new = os.path.join(folder_path, "incl_fun.py")
    #копируем файл в новое расположение
    shutil.copyfile(path, new)
    #читаем содержимое исходного файла
    f = open(path)
    content = f.read()
    f.close()
    num = 0
    #ищем название исходной функции
    for i in range(len(content)):
        if content[i:i+3] == 'def':
            num = i + 4
            break
    num2 = 0
    for i in range(num, len(content)):
        if content[i+1] == '(':
            num2 = i+1
            break
    #меняем название для удобства импорта
    new_content = content.replace(content[num:num2], "fun")
    #перезаписываем файл
    f = open(new, 'w')
    f.write(new_content)
    f.close()
    #импортируем и возвращаем функцию
    import incl_fun
    return incl_fun.fun

def show_plot(metric, H, epochs, path=None, save_plots=False):
    plt.style.use("ggplot")
    plt.figure()
    if type(LIST_METRICS[metric]) is str:
        train = LIST_METRICS[metric]
    else:
        train = LIST_WITH_CLASS_METRICS[metric]
    plt.plot(np.arange(0, epochs), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), H.history[train], label="train_" + train)
    plt.plot(np.arange(0, epochs), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), H.history["val_"  + train], label="val_" + train)
    plt.title("Training plots")
    plt.xlabel("Epoch")
    plt.ylabel("Loss/accuracy")
    plt.legend()
    if path is not None:
        plt.savefig(path)
        if save_plots:
            plt.show()
    else:
        plt.show()
        print("hello")

def print_predictions(model, target_names, batch, testX, testY):
    predictions = model.predict(testX, batch_size=batch)
    return classification_report(testY.argmax(axis=1),
                                predictions.argmax(axis=1),
                                target_names=target_names)

def construct_tuple(str_):
    s = np.asarray(str_.split(','))
    if len(s) == 2:
        return (int(s[0]),)
    else:
        pass
    
def construct_array(str_):
    arr = str_.split(',')[0]
    if arr.isdigit():
        return np.asarray([int(i) for i in str_.split(',')])
    else:
        return np.asarray([i for i in str_.split(',')])
    
def rank5_accuracy(preds, labels):
    rank1 = 0
    rank5 = 0

    for (p, gt) in zip(preds, labels): 
        p = np.argsort(p)[::-1]
        if gt in p[:5]:
            rank5 += 1

        if gt == p[0]:
            rank1 += 1

    rank1 /= float(len(labels))
    rank5 /= float(len(labels))

    return (rank1, rank5)

