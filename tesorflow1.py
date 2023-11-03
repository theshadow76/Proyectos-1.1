import tensorflow as tf
from tensorflow import keras 
import numpy as np 
import matplotlib.pyplot as plt
import random as r

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
for t in range(1):
    ai1 = plt.imshow(train_images[8], cmap=plt.cm.binary)
    plt.show()
print(ai1)