from typing import Union, Optional
from fastapi import FastAPI, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
origins = [
    "https://valiantlynx.github.io/htmx-chat/",
    "https://valiantlynx.github.io",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")
 
import debugpy
debugpy.listen(("0.0.0.0", 5678))

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

hist = model.fit(np.array(train_x), np.array(train_y), epochs=350, batch_size=5, verbose=1)
model.save('src/chatbotmodel.h5', hist)
print("Done training!")

















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

        
'''
def chatbot_response(text):
    ints = predict_class(text, model)
    print("ints: ", ints)
    res = get_response(ints, intents)
    return res

from tkinter import *

def send():
    msg = EntryBox.get('1.0', 'end-1c').strip()
    EntryBox.delete('0.0', END)
    if msg != '':
        Chatlog.config(state=NORMAL)
        Chatlog.insert(END, "You: " + msg + '\n\n')
        Chatlog.config(foreground="#442265", font=("Verdana", 12))
        res = chatbot_response(msg)
        Chatlog.insert(END, "Bot: " + str(res) + '\n\n')
        Chatlog.config(state=DISABLED)
        Chatlog.yview(END)

base = Tk()
base.title("Valiantlynx Bot")
base.geometry("400x500")
base.resizable(width=False, height=False)

Chatlog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
Chatlog.config(state=DISABLED)
scrollbar = Scrollbar(base, command=Chatlog.yview, cursor="heart")
Chatlog['yscrollcommand'] = scrollbar.set
SendButton = Button(base, font=("Verdana", 12, 'bold'), text='send', width="12", height=5, bd=0, bg="#31de97", activebackground = "#3b9d9b", fg='#000000', command=send)


EntryBox= Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
Chatlog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
base.mainloop()
'''

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

@app.get("/")
def read_root():
    return {"Hello": "World1 ass wiper"}

# Notice that you have to pass the request as part of the key-value pairs in the context for Jinja2. So, you also have to declare it in your path operation.
@app.get("/chat/{chat_id}", response_class=HTMLResponse)
async def read_item(request: Request, chat_id: int, q: Union[str, None] = None, hx_request: Optional[str] = Header(None)):
    res = chat(q)
    context = {"request": request, "chat_id": chat_id, "q": q, "res": res}
    if hx_request:
        return templates.TemplateResponse("bubble.html", context)
    
    return  {"chat_id": chat_id, "question": q, "response": res}

