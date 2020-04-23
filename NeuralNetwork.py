import pickle

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from dictfunctions import LangDistro
from globalVariables import NO_ALFACHARACTERS, LANGS
from keras.optimizers import Adam

print("Starting...")

x_train = []
y_train = []
x_test = []
y_test = []

print("Opening Files")
with open("testdata\\NewTrainX.txt", "r", encoding='utf-8') as testf:
    x_train = testf.readlines()

with open("testdata\\NewTrainY.txt", "r", encoding='utf-8') as testf:
    y_train = testf.readlines()

with open("testdata\\NewTestX.txt", "r", encoding='utf-8') as testf:
    x_test = testf.readlines()

with open("testdata\\NewTestY.txt", "r", encoding='utf-8') as testf:
    y_test = testf.readlines()

print("Prepare Trains data")
x_new_train = []
for line in x_train:
    textline = ""
    for c in line:
        if c not in NO_ALFACHARACTERS:
            textline = textline + ' ' + c
    x_new_train.append(textline)

y_new_train = []
for line in y_train:
    y_new_train.append(LANGS.index(line[:-1]))

print("Prepare Test data")
x_new_test = []
for line in x_test:
    textline = ""
    for c in line:
        if c not in NO_ALFACHARACTERS:
            textline = textline + ' ' + c
    x_new_test.append(textline)

y_new_test = []
for line in y_test:
    y_new_test.append(LANGS.index(line[:-1]))

print("Inicializing Tokenizer and padding results")
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(x_new_train)
word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(x_new_train)
training_padded = pad_sequences(training_sequences, maxlen=1200)

testing_sequences = tokenizer.texts_to_sequences(x_new_test)
testing_padded = pad_sequences(testing_sequences, maxlen=1200)

import numpy as np

training_padded = np.array(training_padded)
training_labels = np.array(y_new_train)
testing_padded = np.array(testing_padded)
testing_labels = np.array(y_new_test)

print("Inicializing Model")
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(word_index) + 1, 64, input_length=1200),
    #tf.keras.layers.GlobalAveragePooling1D(),
    #tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.GRU(32, return_sequences=True),
    tf.keras.layers.GRU(32),
    tf.keras.layers.Dense(len(LANGS), activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

num_epochs = 60
history = model.fit(training_padded, training_labels, epochs=num_epochs,
                    validation_data=(testing_padded, testing_labels), verbose=2)


import pandas as pd

pd.DataFrame.from_dict(history.history).to_csv('history.csv', index=False)

model.save('GRU.h5')



classifications = model.predict(testing_padded)
classifications = classifications.tolist()

sumtests = LangDistro()  # ile testow z danego jezyka bylo
sumfails = LangDistro()  # ile testow nasz algorytm zawalil
# Testujemy!
print("Runing tests...")
counter = 0
for x in range(len(testing_labels)):

    # Zwiekszamy ilosc testow o 1
    sumtests.appenddist(LANGS[testing_labels[x]])
    # Przygotowywujemy licznik do testow oblanych z akrutalnego jezyka
    if LANGS[testing_labels[x]] not in sumfails:
        sumfails[LANGS[testing_labels[x]]] = 0

    result = classifications[counter].index(max(classifications[counter]))

    # Jezeli zly jezyk zwiekszamy liczne porazek
    if LANGS[result] != LANGS[testing_labels[x]]:
        sumfails.appenddist(LANGS[testing_labels[x]])
        #if LANGS[testing_labels[x]] ==  "eng":
        #    print("Example:")
        #    print(x)
        #    print(x_test[counter])
        #    for i in range(len(LANGS)):
        #        print(LANGS[i] + ": " + str(classifications[counter][i]))
        #    print("Real: " + str(y_test[counter]))
    counter += 1

    #print(f'Tested {counter}/{len(testing_labels)}')

# Wypisujemy statysyki
print("Printing Stats...")
avg = []
for x in sumtests.keys():
    avg.append(((sumtests[x] - sumfails[x]) / sumtests[x]) * 100)
    print("Lang: \"{0}\" Failed: {1} Tested: {2} Accuracy: {3:0.3f}%".format(x, sumfails[x], sumtests[x],
                                                                             ((sumtests[x] - sumfails[x])
                                                                              / sumtests[x]) * 100))
print("Avg:")
print(np.mean(avg))

print("Example:")
print(x_test[6])
for i in range(len(LANGS)):
    print(LANGS[i] + ": " + str(classifications[6][i]))
print("Real: " + str(y_test[6]))
