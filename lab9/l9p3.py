from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from PIL import Image

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

predictions = model.predict(test_images)

shirt=Image.open("newshirt.PNG")
dress=Image.open("newdress.PNG")
coat=Image.open("newcoat.PNG")
npshirt=np.array(shirt)/255.0
npdress=np.array(dress)/255.0
npcoat=np.array(coat)/255.0
tests=np.array([npshirt,npdress,npcoat])
predictions = model.predict(tests)
print("Supposed shirt prediction:")
print(predictions[0])
print("\nprediction: ")
print(class_names[np.argmax(predictions[0])])
print("\nSupposed dress prediction:")
print(predictions[1])
print("\nprediction: ")
print(class_names[np.argmax(predictions[1])])
print("\nSupposed coat prediction:")
print(predictions[2])
print("\nprediction: ")
print(class_names[np.argmax(predictions[2])])