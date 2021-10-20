import keras.callbacks.LambdaCallback as LC

def create_lambda():
    callback = LC(on_epoch_begin=(parameter1), on_epoch_end=(parameter2),
                  on_batch_begin=(parameter3), on_batch_end=(parameter4),
                  on_train_begin=(parameter5), on_train_end=(parameter6))
    return callback
