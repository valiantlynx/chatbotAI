# the code below is for training the model. it is not needed for the code to run. 
import json
import pickle
import random

import nltk
# sometimes nltk.download() is needed to download the packages
nltk.download('punkt')
nltk.download('wordnet')
import numpy as np
from nltk.stem import WordNetLemmatizer
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
from keras.optimizers import SGD

def train():
    lemmatizer = WordNetLemmatizer()

    intents = json.loads(open("src/intents.json").read())

    words = []
    classes = []
    documents = []
    ignore_letter = ['?', '!', '.', ',', '...']

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letter]
    words = sorted(set(words))

    classes = sorted(set(classes))

    print(len(documents), "documents")

    print(len(classes), "classes", classes)

    print(len(words), "unique lemmatized words", words)
    pickle.dump(words, open('src/words.pkl', 'wb'))
    pickle.dump(classes, open('src/classes.pkl', 'wb'))

    training = []
    output_empty = [0] * len(classes)

    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)



    # find_different_lengths(training) # just for checking. not needed for the code to run
    training = np.array(training, dtype=object)

    train_x = list(training[ :, 0])
    train_y = list(training[:, 1])
    print("Training data created")

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(learning_rate=0.01, weight_decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=400, batch_size=5, verbose=1)
    model.save('src/chatbotmodel.h5', hist)
    print("Done training!")
    
    return model, words, classes

