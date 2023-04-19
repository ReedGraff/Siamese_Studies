import tensorflow as tf
from tensorflow import image_dataset_from_directory

def BasicNN():
    # Create a basic model instance
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    return model

def initial_generator(batch_size, ):
    # placeholder
    yield 0

def main():
    model = BasicNN()
    model.fit(image_dataset_from_directory("../Data"), epochs=1)




if __name__ == "__main__":
    main()