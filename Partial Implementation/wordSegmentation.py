listOfWords = ["a","an","the","for", "and", "nor", "but", "or", "yet", "so","of","is"]
sentence = "This is a demo sentence for testing so for the purpose of tesing but also for fun"
sentence = sentence.split(" ")
newSentence = ""
for word in sentence:
  if word in listOfWords:
    newSentence+=""
  else:
    newSentence+=word + " "
print(newSentence)


#sentiment analysis and then find video similar to it in database
# make a dataset of commonly used words and their synonyms; train a model to then predict the relatable class for particular input and also it will be reponsible to avoid articles and other unwanted words.