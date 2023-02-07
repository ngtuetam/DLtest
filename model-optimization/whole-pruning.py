# whole model pruning
import tensorflow as tf

def setup_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(20, input_shape=input_shape),
        tf.keras.layers.Flatten()
    ])
    return model

base_model = setup_model()

base_model.load_weights(pretrained_weights)

model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(base_model)
model_for_pruning.summary()