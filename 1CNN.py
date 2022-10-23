import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
import random

# -- data
(trainChar, trainLabels), (testChar, testLabels) = keras.datasets.mnist.load_data()
names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
trainChar = trainChar / 255
testChar = testChar / 255

# -- architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(strides=(2,2)),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])

# -- compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# -- training
model.fit(trainChar, trainLabels, epochs=2)

# -- test
testLoss, testAcc = model.evaluate(testChar, testLabels, verbose=1)
print('Test accuracy: ', testAcc)

predicts = model.predict(testChar)

fig, ax = plt.subplots(5,5)
for i in range(5):
    for j in range(5):
        index = random.randint(0,10000)
        name = names[np.argmax(predicts[index])]
        ax[i,j].imshow(testChar[index])
        ax[i,j].grid(False)
        ax[i,j].set_ylabel('Predicts: ' + name)

plt.show()
