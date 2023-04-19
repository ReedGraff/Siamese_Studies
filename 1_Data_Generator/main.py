import tensorflow as tf
from tensorflow import image_dataset_from_directory
import matplotlib.pyplot as plt

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
    history = model.fit(image_dataset_from_directory("../Data"), epochs=1)

    # plot history
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['loss'], label = 'loss')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')
    plt.savefig("history.png")




if __name__ == "__main__":
    main()