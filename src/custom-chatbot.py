'''
this might be part of the final report. im thinking of making the same ai without using the ai library. for now it is not working. i will try to make it work later.
'''

import numpy as np
import nltk
import string
import random

f=open('./src/chatbot.txt', 'r', errors='ignore')
raw_doc=f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt') #punkt tokenizer
nltk.download('wordnet') # wordnet Dictionary
sent_tokens =  nltk.sent_tokenize(raw_doc) # cornverts raw doc to list of sentences
word_tokens = nltk.word_tokenize(raw_doc) #cornverts doc to list of words

#text preprocessing
lemmer = nltk.stem.WordNetLemmatizer()
#wordnet is a english dictionary included in NLTK
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punkt_dict = dict((ord(punkt), None) for punkt in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punkt_dict)))


GREET_INPUTS = ("hello", "hey", "greeting", "sup", "what's up", "hey")
GREET_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are taking to me"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)
        

question = "sup"
print(greet(question))


from sklearn.feature_extraction.text import TfidfVectorizer #Tfidf. tf-term frequency - is how many a term appears. idf-inverde document frequency - metric that attaches a component of how rare the word is 
from sklearn.metrics.pairwise import cosine_similarity 

def response(user_response):
    robo1_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    Tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(Tfidf[-1], Tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo1_response= robo1_response+"I am sorry!, I donæt understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sent_tokens[idx]
        return robo1_response
    
flag=True
print("BOT: My name is sheep. Let's have a conversation! Also if you want to exit anytime, just type Bye!")
while(flag==True):
    user_response = input()
    user_response= user_response.lower()
    if(user_response!="bye"):
        if(user_response=="thanks" or user_response=='thank you'):
            flag=False
            print("Bot: You are welcome...")
        else: 
            if(greet(user_response)!=None):
                print("Bot: "+greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("BOT: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("BOt: bye bye")