# load the trained model and use it for predictions
import random
import json
import pickle
import numpy as np

import nltk
# sometimes nltk.download() is needed to download the packages
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("src/intents.json").read())

words = pickle.load(open("src/words.pkl", "rb"))
classes = pickle.load(open("src/classes.pkl", "rb"))
model = load_model('src/chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

print("GO, Bot is running!")
def chat(text):
    while True:
        #text = input(" ")
        print("you: ", text)
        ints = predict_class(text, model)
        print("ints: ", ints)
        try:
            res = get_response(ints, intents)
            print("valiantlynx_bot: ", res)
            return res
        except IndexError:
            res = "I don't understand. Please try again."
            print(res)
            return res
