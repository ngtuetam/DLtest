import tensorflow as tf

def setup_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(20, input_shape=input_shape),
        tf.keras.layers.Flatten()
    ])
    return model


base_model = setup_model()
base_model.load_weights(pretrained_weights)

# dense layers train with pruning
def apply_pruning_to_dense(layer):
    if isinstance(layer, tf.keras.layers.Dense):
        return tfmot.sparsity.keras.prune_low_magnitude(layer)
    return layer


model_for_pruning = tf.keras.models.clone_model(
    base_model,
    clone_function=apply_pruning_to_dense,
)

model_for_pruning.summary()