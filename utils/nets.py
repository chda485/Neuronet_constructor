from keras.models import Sequential, Model
from keras import layers, regularizers
from keras import backend as K

class LeNet:
    @staticmethod
    def build(inputShape, classes=None):
        model = Sequential()
        model.add(layers.Conv2D(20, (5,5), padding="same",
                         input_shape=inputShape, activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Conv2D(50, (5,5), padding="same", activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(500, activation="relu"))
        model.add(layers.Dense(classes, activation="softmax"))
        return model

class ShallowNet:
    @staticmethod
    def build(inputShape, classes=None):
        model = Sequential()
        model.add(layers.Conv2D(32, (3,3), padding="same",
                         input_shape=inputShape, activation="relu"))
        model.add(layers.Flatten())
        model.add(layers.Dense(classes, activation="softmax"))
        return model

class MiniVGGNet: 
    @staticmethod
    def build(inputShape, classes=None):
        if K.image_data_format() == "channel_first": chanDim = 1
        else: chanDim =- 1
        model = Sequential()
        model.add(layers.Conv2D(32, (3,3), padding="same",
                         input_shape=inputShape,  activation="relu"))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.Conv2D(32, (3,3), padding="same", activation="relu"))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.MaxPooling2D(pool_size=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(64, (3,3), padding="same", activation="relu"))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.Conv2D(64, (3,3), padding="same", activation="relu"))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.MaxPooling2D(pool_size=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation="relu"))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(classes, activation="softmax"))
        return model

class AlexNet: 
    @staticmethod
    def build(inputShape, classes=None):
        if K.image_data_format() == "channel_first": chanDim = 1
        else: chanDim =- 1
        model = Sequential()
        model.add(layers.Conv2D(96, (11,11), strides=(4,4),
                                padding="same", input_shape=inputShape,
                                activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(256, (5,5),
                                padding="same", activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(384, (3,3),
                                padding="same", activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.Conv2D(284, (3,3),
                                padding="same", activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization(axis=chanDim))
        model.add(layers.Conv2D(256, (3,3),
                                padding="same", activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(4096, activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(4096, activation="relu",
                                kernel_regularizer=regularizers.l2(0.002)))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(classes, activation="softmax",
                               kernel_regularizer=regularizers.l2(0.002)))
        return model

class VGG16:
    @staticmethod
    def build(inputShape, classes=None):
        model = Sequential()
        model.add(layers.Conv2D(64, (3,3), padding="same",
                                activation="relu", input_shape=inputShape))
        model.add(layers.Conv2D(64, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(128, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(128, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(4096, activation="relu"))
        model.add(layers.Dense(4096, activation="relu"))
        model.add(layers.Dense(classes, activation="softmax"))
        return model

class VGG19:
    @staticmethod
    def build(inputShape, classes=None):
        model = Sequential()
        model.add(layers.Conv2D(64, (3,3), padding="same",
                                activation="relu", input_shape=inputShape))
        model.add(layers.Conv2D(64, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(128, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(128, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(256, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.Conv2D(512, (3,3), padding="same",
                                activation="relu"))
        model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(4096, activation="relu"))
        model.add(layers.Dense(4096, activation="relu"))
        model.add(layers.Dense(classes, activation="softmax"))
        return model

class MobileNet:    
    @staticmethod
    def build(inputShape, classes=None):
        def mobile_block(model, filters, strides=1):
            model.add(layers.DepthwiseConv2D(3, strides=strides, padding="same",
                                             activation="relu"))
            model.add(layers.BatchNormalization())
            model.add(layers.Conv2D(filters, (1,1), strides=1, padding="same",
                                    activation="relu"))
            model.add(layers.BatchNormalization())
            return model
    
        model = Sequential()
        model.add(layers.Conv2D(32, (3,3), padding="same", strides=(2,2),
                                activation="relu", input_shape=inputShape))
        model.add(layers.BatchNormalization())
        model = mobile_block(model, 64)
        model = mobile_block(model, 128, 2)
        model = mobile_block(model, 128)
        model = mobile_block(model, 256, 2)
        model = mobile_block(model, 256)
        model = mobile_block(model, 512, 2)
        for _ in range(5):
            model = mobile_block(model, 512)
        model = mobile_block(model, 1024, 2)
        model = mobile_block(model, 1024)
        model.add(layers.GlobalAvgPool2D())
        model.add(layers.Dense(classes, activation="softmax"))
        return model


class SqueezeNet:
    @staticmethod
    def build(inputShape, classes=None):
        def fire_module(input_l, filters_s, filters_e):
            s = layers.Conv2D(filters_s, (1,1), activation="relu")(input_l)
            e1 = layers.Conv2D(filters_e, (1,1), activation="relu")(s)
            e3 = layers.Conv2D(filters_e, (3,3), padding="same", activation="relu")(s)
            out = layers.Concatenate()([e1,e3])
            return out
    
        input_m = layers.Input(inputShape)
        x = layers.Conv2D(96, (7,7), strides=(2,2), activation="relu",
                               padding="same")(input_m)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = fire_module(x, 16, 64)
        x = fire_module(x, 16, 64)
        x = fire_module(x, 32, 128)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = fire_module(x, 32, 128)
        x = fire_module(x, 48, 192)
        x = fire_module(x, 48, 192)
        x = fire_module(x, 64, 256)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = fire_module(x, 64, 256)
        x = layers.Conv2D(classes, (1,1))(x)
        x = layers.GlobalAvgPool2D()(x)
        x = layers.Activation("softmax")(x)
        model = Model(input_m, x)
        return model

class ResNet18_34:
    def __init__(self, model_number=18):
        self.model_number = model_number
        
    def build(self, inputShape, classes=None):
        model_dict_params = {18: [2,2,2,2],
                             34: [3,4,6,3]} 
        def conv_block(input_l, f):
            x = layers.Conv2D(f, (3,3), activation="relu",
                              padding="same")(input_l)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f, (3,3), activation="relu",
                              padding="same")(x)
            x = layers.BatchNormalization()(x)
            y = layers.Conv2D(f, (1,1), activation="relu",
                              padding="same")(input_l)
            y = layers.BatchNormalization()(y)
            out = layers.Concatenate()([x,y])
            return out
    
        def identity_block(input_l, f):
            x = layers.Conv2D(f, (3,3), activation="relu",
                              padding="same")(input_l)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f, (3,3), activation="relu",
                              padding="same")(x)
            x = layers.BatchNormalization()(x)
            x = layers.Concatenate()([input_l,x])
            return x
    
        input_m = layers.Input(inputShape)
        x = layers.Conv2D(64, (7,7), strides=(2,2), activation="relu",
                          padding="same")(input_m)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        model_dict = model_dict_params[self.model_number]
        for _ in range(model_dict[0]):
            x = conv_block(x, 64)
            x = identity_block(x, 64)
        for _ in range(model_dict[1]):
            x = conv_block(x, 128)
            x = identity_block(x, 128)
        for _ in range(model_dict[2]):
            x = conv_block(x, 256)
            x = identity_block(x, 256)
        for _ in range(model_dict[3]):
            x = conv_block(x, 512)
            x = identity_block(x, 512)
        x = layers.GlobalAvgPool2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model
            
class ResNet50_152:
    def __init__(self, model_number=50):
        self.model_number = model_number

    def build(self, inputShape, classes=None):
        model_dict_params = {50: [2,3,5,2],
                             101: [2,3,22,2],
                             152: [2,7,35,2]}
        def conv_block(input_l, f1, f2):
            x = layers.Conv2D(f1, (1,1), activation="relu",
                              padding="same", strides=(2,2))(input_l)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f1, (3,3), activation="relu",
                              padding="same")(x)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f2, (3,3), activation="relu",
                              padding="same")(x)
            x = layers.BatchNormalization()(x)
            y = layers.Conv2D(f2, (1,1), activation="relu",
                              padding="same", strides=(2,2))(input_l)
            y = layers.BatchNormalization()(y)
            out = layers.Concatenate()([x,y])
            return out
        def identity_block(input_l, f1, f2):
            x = layers.Conv2D(f1, (1,1), activation="relu",
                              padding="same")(input_l)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f1, (3,3), activation="relu",
                              padding="same")(x)
            x = layers.BatchNormalization()(x)
            x = layers.Conv2D(f2, (1,1), activation="relu",
                              padding="same")(input_l)
            x = layers.BatchNormalization()(x)
            x = layers.Concatenate()([input_l,x])
            return x

        input_m = layers.Input(inputShape)
        x = layers.Conv2D(64, (7,7), strides=(2,2), activation="relu",
                          padding="same")(input_m)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        model_dict = model_dict_params[self.model_number]
        x = conv_block(x, 64, 256)
        for _ in range(model_dict[0]):
            x = identity_block(x, 64, 256)
        x = conv_block(x, 128, 512)
        for _ in range(model_dict[1]):
            x = identity_block(x, 128, 512)
        x = conv_block(x, 256, 1024)
        for _ in range(model_dict[2]):
            x = identity_block(x, 256, 1024)
        x = conv_block(x, 512, 2048)
        for _ in range(model_dict[3]):
            x = identity_block(x, 512, 2048)
        x = layers.GlobalAvgPool2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model
    
class InceptionV2:
    @staticmethod
    def build(inputShape, classes=None):
        def mixed_block1(input_l, filters):
            branch_1 = layers.Conv2D(filters[0], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(filters[1], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[2], (3,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(filters[3], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (3,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (3,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), 
                                               padding="same")(input_l)
            branch_4 = layers.Conv2D(filters[5], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out

        def mixed_block2(input_l, filters):
            branch_1 = layers.Conv2D(filters[0], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_1 = layers.Conv2D(filters[1], (3,3), activation="relu",
                                     strides=(2,2), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(filters[2], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[3], (3,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[3], (3,3), activation="relu",
                                     padding="same", strides=(2,2))(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="same")(input_l)
            out = layers.Concatenate()([branch_1, branch_2, branch_3])
            return out
        input_l = layers.Input(inputShape)
        x = layers.Conv2D(64, (7,7), strides=(2,2), activation="relu",
                          padding="same")(input_l)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = layers.Conv2D(64, (1,1), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(192, (3,3), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = mixed_block1(x, [64, 64, 64, 64, 96, 32])
        x = mixed_block1(x, [64, 64, 96, 64, 96, 64])
        x = mixed_block2(x, [128, 160, 64, 96])
        x = mixed_block1(x, [224, 64, 96, 96, 128, 128])
        x = mixed_block1(x, [192, 96, 128, 96, 128, 128])
        x = mixed_block1(x, [160, 128, 160, 128, 160, 96])
        x = mixed_block1(x, [96, 128, 192, 160, 192, 96])
        x = mixed_block2(x, [128, 192, 192, 256])
        x = mixed_block1(x, [352, 192, 320, 160, 224, 128])
        x = mixed_block1(x, [352, 192, 320, 192, 224, 128])
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_l, x)
        return model
    
class InceptionV3:
    @staticmethod
    def build(inputShape, classes=None):
        def mixed_block1(input_l, filters):
            branch_1 = layers.Conv2D(filters[0], (1,1), activation="relu",
                                    padding = "same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(filters[1], (1,1), activation="relu",
                                    padding = "same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[2], (5,6), activation="relu",
                                    padding = "same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(filters[3], (1,1), activation="relu",
                                    padding = "same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (3,3), activation="relu",
                                    padding = "same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (3,3), activation="relu",
                                    padding = "same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(input_l)
            branch_4 = layers.Conv2D(filters[5], (1,1), activation="relu",
                                    padding = "same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out

        def mixed_block2(input_l, filters):
            branch_1 = layers.Conv2D(filters[0], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(filters[1], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[1], (1,7), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[2], (7,1), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(filters[3], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[3], (7,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[3], (1,7), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[3], (7,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (1,7), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(input_l)
            branch_4 = layers.Conv2D(filters[4], (1,1), activation="relu",
                                     padding="same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out
        input_l = layers.Input(inputShape)
        x = layers.Conv2D(32, (3,3), strides=(2,2), activation="relu",
                          padding="same")(input_l)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(32, (3,3), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(64, (3,3), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = layers.Conv2D(80, (1,1), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(192, (3,3), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = mixed_block1(x, [64, 48, 64, 64, 96, 32])
        for _ in range(2):
            x = mixed_block1(x, [64, 48, 64, 64, 96, 64])
        
        branch_1 = layers.Conv2D(384, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(x)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.Conv2D(64, (1,1), activation="relu",
                                 padding="same")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(96, (3,3), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(96, (3,3), strides=(2,2), activation="relu",
                                 padding="valid")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_3 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        x = layers.Concatenate()([branch_1, branch_2, branch_3])
        
        x = mixed_block2(x, [192, 128, 192, 128, 192])
        for _ in range(2):
            x = mixed_block2(x, [192, 160, 192, 160, 192])
        x = mixed_block2(x, [192, 192, 192, 192, 192])

        branch_1 = layers.Conv2D(192, (1,1), activation="relu",
                          padding="same")(x)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_1 = layers.Conv2D(320, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(branch_1)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.Conv2D(192, (1,1), activation="relu",
                                 padding="same")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(192, (1,7), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(192, (7,1), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(192, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_3 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        x = layers.Concatenate()([branch_1, branch_2, branch_3])

        for _ in range(2):
            branch_1 = layers.Conv2D(320, (1,1), activation="relu",
                          padding="same")(x)
            branch_1 = layers.BatchNormalization()(x)
            branch_2 = layers.Conv2D(384, (1,1), activation="relu",
                              padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(x)
            branch_2_1 = layers.Conv2D(384, (1,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2_1 = layers.BatchNormalization()(branch_2_1)
            branch_2_2 = layers.Conv2D(384, (3,1), activation="relu",
                                     padding="same")(branch_2)
            branch_2_2 = layers.BatchNormalization()(branch_2_2)
            branch_2 = layers.Concatenate()([branch_2_1, branch_2_2])
            branch_3 = layers.Conv2D(448, (1,1), activation="relu",
                                     padding="same")(x)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(384, (3,3), activation="relu",
                              padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3_1 = layers.Conv2D(384, (1,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3_1 = layers.BatchNormalization()(branch_3_1)
            branch_3_2 = layers.Conv2D(384, (3,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3_2 = layers.BatchNormalization()(branch_3_2)
            branch_3 = layers.Concatenate()([branch_3_1, branch_3_2])
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(x)
            branch_4 = layers.Conv2D(192, (1,1), activation="relu",
                              padding="same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            x = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_l, x)
        return model

class InceptionV4:
    @staticmethod
    def build(inputShape, classes=None):
        def inception_a(input_l):
            branch_1 = layers.Conv2D(96, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(64, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(96, (3,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(64, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(96, (3,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(96, (3,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(input_l)
            branch_4 = layers.Conv2D(96, (1,1), activation="relu",
                                     padding="same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out
        def inception_b(input_l):
            branch_1 = layers.Conv2D(384, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(192, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(224, (1,7), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(256, (7,1), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(192, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(192, (1,7), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(224, (7,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(224, (1,7), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(256, (7,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(input_l)
            branch_4 = layers.Conv2D(128, (1,1), activation="relu",
                                     padding="same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out
        def inception_c(input_l):
            branch_1 = layers.Conv2D(256, (1,1), activation="relu",
                          padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(384, (1,1), activation="relu",
                              padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2_1 = layers.Conv2D(256, (1,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2_1 = layers.BatchNormalization()(branch_2_1)
            branch_2_2 = layers.Conv2D(256, (3,1), activation="relu",
                                     padding="same")(branch_2)
            branch_2_2 = layers.BatchNormalization()(branch_2_2)
            branch_2 = layers.Concatenate()([branch_2_1, branch_2_2])
            branch_3 = layers.Conv2D(384, (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(448, (1,3), activation="relu",
                              padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(512, (3,1), activation="relu",
                              padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3_1 = layers.Conv2D(256, (1,3), activation="relu",
                                     padding="same")(branch_3)
            branch_3_1 = layers.BatchNormalization()(branch_3_1)
            branch_3_2 = layers.Conv2D(256, (3,1), activation="relu",
                                     padding="same")(branch_3)
            branch_3_2 = layers.BatchNormalization()(branch_3_2)
            branch_3 = layers.Concatenate()([branch_3_1, branch_3_2])
            branch_4 = layers.AveragePooling2D(pool_size=(3,3), strides=(1,1), padding="same")(input_l)
            branch_4 = layers.Conv2D(256, (1,1), activation="relu",
                              padding="same")(branch_4)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out

        input_m = layers.Input(inputShape)
        x = layers.Conv2D(32, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(input_m)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(32, (3,3), activation="relu",
                          padding="valid")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Conv2D(64, (3,3), activation="relu",
                          padding="same")(x)
        x = layers.BatchNormalization()(x)
        
        branch_1 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        branch_2 = layers.Conv2D(96, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        x = layers.Concatenate()([branch_1, branch_2])
        
        branch_1 = layers.Conv2D(64, (1,1), activation="relu",
                          padding="same")(x)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_1 = layers.Conv2D(96, (3,3), activation="relu",
                          padding="valid")(branch_1)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.Conv2D(64, (1,1), activation="relu",
                          padding="same")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(64, (1,7), activation="relu",
                          padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(64, (7,1), activation="relu",
                          padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(96, (3,3), activation="relu",
                          padding="valid")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        x = layers.Concatenate()([branch_1, branch_2])
        
        branch_1 = layers.Conv2D(192, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(x)
        branch_2 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        x = layers.Concatenate()([branch_1, branch_2])    
        
        for _ in range(4):
            x = inception_a(x)
        
        branch_1 = layers.Conv2D(384, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(x)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.Conv2D(192, (1,1), activation="relu",
                                 padding="same")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(224, (3,3), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(256, (3,3), strides=(2,2), activation="relu",
                                 padding="valid")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_3 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        x = layers.Concatenate()([branch_1, branch_2, branch_3])
        
        for _ in range(7):
            x = inception_b(x)
        
        branch_1 = layers.Conv2D(192, (1,1), activation="relu",
                                 padding="same")(x)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_1 = layers.Conv2D(192, (3,3), strides=(2,2), activation="relu",
                          padding="valid")(branch_1)
        branch_1 = layers.BatchNormalization()(branch_1)
        branch_2 = layers.Conv2D(256, (1,1), activation="relu",
                                 padding="same")(x)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(256, (1,7), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(320, (7,1), activation="relu",
                                 padding="same")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_2 = layers.Conv2D(320, (3,3), strides=(2,2), activation="relu",
                                 padding="valid")(branch_2)
        branch_2 = layers.BatchNormalization()(branch_2)
        branch_3 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="valid")(x)
        x = layers.Concatenate()([branch_1, branch_2, branch_3])
        
        for _ in range(3):
            x = inception_c(x)
        
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model

class Xception:
    @staticmethod
    def build(inputShape, classes=None):
        def entry(input_l, f):
            branch_1 = layers.Activation("relu")(input_l)
            branch_1 = layers.SeparableConv2D(f, (3,3), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization(branch_1)
            branch_1 = layers.Activation("relu")(input_l)
            branch_1 = layers.SeparableConv2D(f, (3,3), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization(branch_1)
            branch_1 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="same")(branch_1)
            branch_2 = layers.Conv2D(f, strides=(2,2), activation="relu",
                                     padding="same")(input_l)
            out = layers.Add()([branch_1, branch_2])
            return out
        def middle(input_l):
            branch_1 = layers.Activation("relu")(input_l)
            branch_1 = layers.SeparableConv2D(728, (3,3), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization(branch_1)
            branch_1 = layers.Activation("relu")(branch_1)
            branch_1 = layers.SeparableConv2D(728, (3,3), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization(branch_1)
            branch_1 = layers.Activation("relu")(branch_1)
            branch_1 = layers.SeparableConv2D(728, (3,3), padding="same")(branch_1)
            branch_1 = layers.BatchNormalization(branch_1)
            out = layers.Add()([input_l, branch_1])
            return out
        input_m = layers.Input(inputShape)
        x = layers.Conv2D(32, (3,3), strides=(2,2), activation="relu",
                          padding="same")(input_m)
        x = layers.BatchNormalization(x)
        x = layers.Conv2D(32, (3,3), padding="same")(x)
        x = layers.BatchNormalization(x)
        x = entry(x, 128)
        x = entry(x, 256)
        x = entry(x, 728)
        for _ in range(8):
            x = middle(x)
        branch_1 = layers.Activation("relu")(x)
        branch_1 = layers.SeparableConv2D(728, (3,3), padding="same")(branch_1)
        branch_1 = layers.BatchNormalization(branch_1)
        branch_1 = layers.Activation("relu")(x)
        branch_1 = layers.SeparableConv2D(1024, (3,3), padding="same")(branch_1)
        branch_1 = layers.BatchNormalization(branch_1)
        branch_1 = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2), padding="same")(branch_1)
        branch_2 = layers.Conv2D(728, (1,1), strides=(2,2), activation="relu",
                                 padding="same")(x)
        x = layers.Add()([branch_1, branch_2])
        x = layers.SeparableConv2D(1536, (3,3), activation="relu", padding="same")(x)
        x = layers.BatchNormalization(x)
        x = layers.SeparableConv2D(2048, (3,3), activation="relu", padding="same")(x)
        x = layers.BatchNormalization(x)
        x = layers.GlobalAveragePooling()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model

class GoogleNet:
    @staticmethod
    def build(inputShape, classes=None):
        def inception_block(input_l, filters):
            branch_1 = layers.Conv2D(filters[0], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_1 = layers.BatchNormalization()(branch_1)
            branch_2 = layers.Conv2D(filters[1], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_2 = layers.Conv2D(filters[2], (3,3), activation="relu",
                                     padding="same")(branch_2)
            branch_2 = layers.BatchNormalization()(branch_2)
            branch_3 = layers.Conv2D(filters[3], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_3 = layers.Conv2D(filters[4], (5,5), activation="relu",
                                     padding="same")(branch_3)
            branch_3 = layers.BatchNormalization()(branch_3)
            branch_4 = layers.MaxPooling2D(pool_size=(3,3), strides=(1,1), 
                                               padding="same")(input_l)
            branch_4 = layers.Conv2D(filters[5], (1,1), activation="relu",
                                     padding="same")(input_l)
            branch_4 = layers.BatchNormalization()(branch_4)
            out = layers.Concatenate()([branch_1, branch_2, branch_3, branch_4])
            return out
        input_m = layers.Input(inputShape)
        x = layers.Conv2D(64, (7,7), strides=(2,2), activation="relu",
                          padding="same")(input_m)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = layers.Conv2D(192, (3,3), activation="relu",
                          padding="same")(input_m)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = inception_block(x, [64, 96, 128, 16, 32, 32])
        x = inception_block(x, [128, 128, 192, 32, 96, 64])
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = inception_block(x, [192, 96, 208, 16, 48, 64])
        x = inception_block(x, [160, 112, 224, 24, 64, 64])
        x = inception_block(x, [128, 128, 256, 24, 64, 64])
        x = inception_block(x, [112, 144, 288, 32, 64, 64])
        x = inception_block(x, [256, 160, 320, 32, 128, 128])
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        x = inception_block(x, [256, 160, 320, 32, 128, 128])
        x = inception_block(x, [384, 192, 384, 48, 128, 128])
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model

class DenseNet:
    @staticmethod
    def build(inputShape, classes=None):    
        def dense_block(input_l, ran):
            pred_outs = []
            for _ in range(ran):
                if len(pred_outs) > 0:
                    x = layers.BatchNormalization()(pred_outs[-1])
                else: x = layers.BatchNormalization()(input_l)
                x = layers.Conv2D(128, (1,1), activation="relu",
                                  padding="same")(x)
                x = layers.BatchNormalization()(x)
                x = layers.Conv2D(32, (3,3), activation="relu",
                                  padding="same")(x)               
                pred_outs.append(x)
                x = layers.Concatenate()([x, input_l])
                if len(pred_outs) > 1:
                    for out in pred_outs[:-1]:
                        x = layers.Concatenate()([x, out])
            return x
        def transition_block(input_l):
            x = layers.Conv2D(128, (1,1), activation="relu",
                              padding="same")(input_l)
            x = layers.AveragePooling2D(pool_size=(2,2), strides=(2,2))(x)
            return x
        range_list = [6, 12, 24, 16]
        input_m = layers.Input(inputShape)
        x = layers.Conv2D(64, (7,7), strides=(2,2), activation="relu",
                          padding="same")(input_m)
        x = layers.MaxPooling2D(pool_size=(3,3), strides=(2,2))(x)
        for r in range_list:
            x = dense_block(x, r)
            x = transition_block(x)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(classes, activation="softmax")(x)
        model = Model(input_m, x)
        return model
    
                
            
        
