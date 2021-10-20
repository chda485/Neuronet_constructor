#import net_classes
from keras.applications.densenet import DenseNet169
from keras.utils.vis_utils import plot_model

model = DenseNet169(include_top=True)
plot_model(model, to_file="model.png", show_shapes=True)
