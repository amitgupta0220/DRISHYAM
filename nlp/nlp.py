import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle


with open("nlp/intents.json") as file:
    data = json.load(file)

# print(data["intents"])

try:
  with open("nlp/data.pickle","rb") as f:
      words, labels, training, output = pickle.load(f)
except:
  words = []
  labels = []
  docs_x = []
  docs_y = []

  for intent in data["intents"]:
      for pattern in intent["patterns"]:
          word = nltk.word_tokenize(pattern)
          words.extend(word)
          docs_x.append(word)
          docs_y.append(intent["tag"])

      if intent["tag"] not in labels:
          labels.append(intent["tag"])
  words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
  words = sorted(list(set(words)))

  labels = sorted(labels)

  training = []
  output = []

  out_empty = [0 for _ in range(len(labels))]

  for x, doc in enumerate(docs_x):
    bag = []

    word = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in word:
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)
  training = np.array(training)
  output = np.array(output)

  with open("nlp/data.pickle","wb") as f:
      pickle.dump((words, labels, training, output),f)


#Training the model here

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
  model.load("nlp/model.tflearn")
except:
  model = tflearn.DNN(net)
  model.fit(training, output, n_epoch=1000, batch_size=10, show_metric=True)
  model.save("nlp/model.tflearn")


def bag_of_words(s, words):
  bag = [0 for _ in range(len(words))]
  s_words = nltk.word_tokenize(s)
  s_words = [stemmer.stem(word.lower()) for word in s_words]

  for se in s_words:
      for i,w in enumerate(words):
          if w == se:
              bag[i] = 1
  return np.array(bag)


def chat(query):
  result = model.predict([bag_of_words(query, words)])

  result_index = np.argmax(result)

  tag = labels[result_index]

  responses = ""

  for tg in data["intents"]:
      if tg["tag"] == tag:
          responses = tg['responses']
  if responses=="":
    print("it is an article")
  else:
    print("Not an article")

chat('This is a demo sentence for testing so for the purpose of tesing but also for fun')