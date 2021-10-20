import nets
#from keras import metrics
import os, cv2, shutil
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

"""
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

"""
LISTS_NEURONETS = [
    "LeNet", "AlexNet",
    "MiniVGGNet", "ShallowNet",
    "VGG16", "VGG19",
    "MobileNet", "SqueezeNet",
    "ResNet18", "ResNet34",
    "ResNet50", "ResNet101",
    "ResNet152", "InceptionV2",
    "InceptionV3", "InceptionV4",
    "Xception", "GoggleNet",
    "DenseNet"
    ]


LIST_LOSSES = {
    "BinaryCrossentropy": "binary_crossentropy", "CategoricalCrossentropy": "categorical_crossentropy",
    "SparseCategorical": "sparse_categorical_crossentropy", "Poisson": "poisson",
    "KLDivergence": "kl_divergence", "MAE": "mae", "MSE": "mse",
    "MAEPercentage": "mean_absolute_percentage_error", "MSEPLogarithmic": "mean_squared_logarithmic_error",
    "CosineSimilarity": "cosine_similarity", "Huber": "huber_class",
    "LogCosh": "log_cosh", "Hinge": "hinge", "SquaredHinge": "squared_hinge",
    "CategoricalHinge": "categorical_hinge"
    }

LIST_METRICS = [
    "Accuracy", "BinaryAccuracy",
    "CategoricalAccuracy", "TopKCategorical",
    "SparseTopKCategorical",
    "BinaryCrossentropy", "CategoricalCrossentropy",
    "SparseCategorical", "Poisson",
    "KLDivergence", "MAE", "MSE",
    "MAEPercentage", "MSELogarithmic",
    "CosineSimilarity", "RootMSE",
    "LogCoshError", "AUC", "Precision",
    "Recall", "TruePositives", "TrueNegatives",
    "FalsePositive", "FalseNegative",
    "PrecisionAtRecall", "SensitivityAtSpecificity",
    "SpecificityAtSensitivity", "MeanloU",
    "Hinge", "SquaredHinge", "CategoricalHinge"
    ]

LIST_OPTS = ["SGD", "RMSprop", "Adam", "Adadelta",
             "Nadam", "Adagrad", "Adamax", "Ftrl"]

LIST_CALLBACKS = ["ModelCheckpoint", "TensorBoard", "EarlyStopping",
                  "LearningRateSchedular", "ReduceLROnPlateau",
                  "RemoteMonitor", "LambdaCallback", "TerminateOnNaN",
                  "CSVLogger", "ProgbarLogger", "BackupAndRestore"]

LIST_LAYERS = ["Activation", "AveragePool2D", "Conv2D",
               "Conv2DTranspose", "Dense", "GlobalAveragePool2D",
               "GlobalMaxPool2D", "MaxPooling2D", "SeparableConv2D"]

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

def check_settings(settings, bools=(None,None), fun=None):
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
    #проверяем установку пути к функции
    if fun:
        answer = True
        return answer
    return answer
    
def include_function(path, current):#скорректировать current!!!!!!!
    #получаем путь к файлу
    base = os.path.basename(path)
    length = len(base) + 1
    folder_path = path[:-length]
    #путь к новому файлу функции
    new = os.path.join(current, "incl_fun.py")
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

def show_plot(H):
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0,100), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0,100), H.history["accuracy"], label="train_accuracy")
    plt.plot(np.arange(0,100), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0,100), H.history["val_accuracy"], label="val_accuracy")
    plt.title("Flowers17")
    plt.xlabel("Epoch")
    plt.ylabel("Loss/accuracy")
    plt.legend()
    plt.show()

def print_predictions(model, target_names, batch, testX, testY):
    predictions = model.predict(testX, batch_size=batch)
    print(classification_report(testY.argmax(axis=1),
                                predictions.argmax(axis=1),
                                target_names=target_names))
