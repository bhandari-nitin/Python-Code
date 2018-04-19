#################################################
########## Analyzing IMDB Data in Keras #########
#################################################

# Import statements for the code
import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt

np.random.seed(42)

# Loading the data
# 'num_words' parameter is used for how many words we want to look at
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=1000)
print x_train.shape
print x_test.shape

#Examining the data

#Notice that the data has been already pre-processed, where all the words have numbers, 
#and the reviews come in as a vector with the words that the review contains. 
#For example, if the word 'the' is the first one in our dictionary, and a review contains the word 'the', 
#then there is a 1 in the corresponding vector.
#The output comes as a vector of 1's and 0's, where 1 is a positive sentiment for the review, and 0 is negative.

print x_train[0]
print y_train[0]

# One-hot encoding the output
tokenizer = Tokenizer(1000)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(s_test, mode='binary')
print x_train[0]

y_train = keras.utils.to_categorical(y_train, num_classes=2)
y_test = keras.utils.to_categorical(y_test, num_classes=2)
print y_train.shape
print y_test.shape

# Building the model architecture

model = Sequential()
model.add(Dense(64, input_dim=1000))
model.add(Dropout(0.4))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('tanh'))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs= 10, batch_size=40, validation_set=(x_train, y_train), verbose=2)
score =model.evaluate(x_test, y_test, verbose=0)
print 'Accuracy:{}'.format(score[1])



