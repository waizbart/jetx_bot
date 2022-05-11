import numpy as np
import csv
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def splitSequence(seq, n_steps):
    
    #Declare X and y as empty list
    X = []
    y = []
    
    for i in range(len(seq)):
        #get the last index
        lastIndex = i + n_steps
        
        #if lastIndex is greater than length of sequence then break
        if lastIndex > len(seq) - 1:
            break
            
        #Create input and output sequence
        seq_X, seq_y = seq[i:lastIndex], seq[lastIndex]
        
        #append seq_X, seq_y in X and y list
        X.append(seq_X)
        y.append(seq_y)
        pass
    #Convert X and y into numpy array
    X = np.array(X)
    y = np.array(y)
    
    return X,y 
    
    pass

data = [3.20, 1.18, 1.35, 1.58, 1.18, 2.80, 1.14, 2.70, 1.35, 1.28, 1.00, 11.91, 3.60, 4.66, 1.51, 7.60, 16.13, 1.34, 6.39, 3.12, 1.26, 2.49, 1.26, 1.39, 1.04, 2.77]

n_steps = 5
X, y = splitSequence(data, n_steps = 5)

n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))

model = tf.keras.Sequential()
model.add(layers.LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(layers.Dense(1))

model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

model.fit(X, y, epochs=200, verbose=1)

test_data = np.arange(1, 2, 0.01)
test_data = np.array(test_data)
test_data = test_data.reshape((1, n_steps, n_features))
predictNextNumber = model.predict(test_data, verbose=1)
print(predictNextNumber)

