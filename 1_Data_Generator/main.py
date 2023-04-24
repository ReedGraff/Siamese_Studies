import tensorflow as tf
import matplotlib.pyplot as plt

def get_basic_model():
    # increase input size...
    model = tf.keras.Sequential([
        tf.keras.layers.Resizing(28, 28),

        tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 3)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.25),
    
        tf.keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.25),
    
        tf.keras.layers.Conv2D(256, (2, 2), padding='same', activation='relu'),
        tf.keras.layers.Conv2D(256, (2, 2), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.25),
    
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(5)
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
    model = get_basic_model()
    history = model.fit(tf.keras.utils.image_dataset_from_directory("../Data/Monkeys/Training Data", crop_to_aspect_ratio=True), epochs=128)

    # plot history
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['loss'], label = 'loss')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.savefig("history.png")




if __name__ == "__main__":
    main()
