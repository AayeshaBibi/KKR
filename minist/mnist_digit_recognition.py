import numpy as np
import tensorflow as tf
from keras import layers, models
from keras.datasets import mnist
from keras.utils import to_categorical

def main():
    # Load the MNIST dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(f"Training samples: {x_train.shape[0]}, Test samples: {x_test.shape[0]}")

    # Preprocessing data
    x_train = x_train.reshape(-1, 784).astype('float32') / 255
    x_test = x_test.reshape(-1, 784).astype('float32') / 255

    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    # Building ANN model
    model = models.Sequential([
        layers.Dense(512, activation='relu', input_shape=(784,)),
        layers.Dropout(0.2),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax')
    ])

    # Compiling model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Training the model
    model.fit(x_train, y_train,
              epochs=10,
              batch_size=128,
              validation_split=0.1)

    # Evaluating model
    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    # Save the trained model
    model.save("mnist_ann_model.keras")

if __name__ == "__main__":
    main()