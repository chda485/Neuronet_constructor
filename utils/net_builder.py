#from keras import backend as K
import os, cv2, helper
import numpy as np
import keras
from sklearn.preprocessing import LabelBinarizer

class NetBuilder():
    def __init__(self):
        self.classes = None
    
    def preprocess_data(self, file, shape):
        return cv2.resize(file, shape[:-1])
    
    def prepare_data(self, path, needed_shape=(224, 224, 3)):
        X_train = []
        Y_train = []
        X_test = []
        Y_test = []
        X_val = []
        Y_val = []
        train = os.path.join(path, "train")
        validation = os.path.join(path, "validation")
        test = os.path.join(path, "test")
        dir_tuple = (train, validation, test)
        X_tuple = (X_train, X_val, X_test)
        Y_tuple = (Y_train, Y_val, Y_test)
        for element in zip(dir_tuple, X_tuple, Y_tuple):
            self.classes = os.listdir(element[0])
            print(element)
            for classes in os.listdir(element[0]):
                print(classes)
                for files in os.listdir(os.path.join(element[0], classes)):
                    file = cv2.imread(os.path.join(element[0], classes, files))
                    if file.shape != needed_shape:
                        file = self.preprocess_data(file, needed_shape)
                    element[1].append(file)
                    element[2].append(classes)
        X_train = np.asarray(X_train)
        lb = LabelBinarizer()
        Y_train = np.asarray(Y_train)
        Y_train = lb.fit_transform(Y_train)

        X_val = np.asarray(X_val)
        lb = LabelBinarizer()
        Y_val = np.asarray(Y_val)
        Y_val = lb.fit_transform(Y_val)

        X_test = np.asarray(X_test)
        lb = LabelBinarizer()
        Y_test = np.asarray(Y_test)
        Y_test = lb.fit_transform(Y_test)
        return (X_train, X_val, X_test), (Y_train, Y_val, Y_test)
        
    def build_model(self, model_name, inputShape, dataset=None):
        model_class = helper.LISTS_NEURONETS[model_name]
        if type(inputShape) is str:
            shape = inputShape.split(',')
            new_shape = []
            for s in shape:
                new_shape.append(int(s))
        else:
            new_shape = inputShape
        if dataset:
            dir_ = os.listdir(dataset)[0]
            classes = len(os.listdir(os.path.join(dataset, dir_)))
            return model_class.build(new_shape, classes)
        else: return model_class.build(new_shape)
        
    def rebuild_last_layer(self, model, dataset):
        if model.layers[-1].output_shape[-1] == 1:
            return model
        else:
            num_classes = len(os.listdir(os.path.join(dataset, os.listdir(dataset)[0])))
            new_layer = keras.layers.Dense(num_classes, activation="sigmoid")(
                model.layers[-2].output)
            new_model = keras.Model(inputs=model.input, outputs=new_layer)
            return new_model

    def model_train(self, model, opt, loss_fun, metric,
                    epochs, dataset_path, batch_size=32, detail_result=False,
                    from_disk=False):
        if from_disk:
            X, Y = self.prepare_data(dataset_path, model.layers[0].input_shape[0][1:])
        else:
            X, Y = self.prepare_data(dataset_path, model.layers[0].input_shape[1:])
        if type(opt) == str:
            optimizer = opt.lower()
        else: 
            optimizer = opt
        if type(metric) == str:
            metric = helper.LIST_METRICS[metric]
        else:
            metric = metric
        if type(loss_fun) == str:
            loss = helper.LIST_LOSSES[loss_fun]
        else:
            loss = loss_fun

        model.compile(loss=loss, optimizer=optimizer, metrics=[metric])
        
        #СДЕЛАТЬ БЛОКИРОВКУ ВЫВОДА В КОНСОЛЬ, ЕСЛИ НЕ ВЫБРАН ПОДРОБНЫЙ ОТЧЕТ О ХОДЕ ОБУЧЕНИЯ
        H = model.fit(X[0], Y[0], validation_data=(X[1], Y[1]),
                      batch_size=batch_size, epochs=int(epochs))
        #ЕСЛИ ДЕЛАЛИ БЛОКИРОВКУ, ЗДЕСЬ СНЯТЬ ЕЁ
        
        if detail_result:           
            detail = helper.print_predictions(model, self.classes, batch_size,
                                              X[2], Y[2])
        else: detail = None
        return H, model, detail
    
