sentence = "This is a sample sentence for testin purpose."
listOfWords = sentence.split(sep=" ")
for word in listOfWords:
  #sentiment analysis and then find video similar to it in database
  # make a dataset of commonly used words and their synonyms; train a model to then predict the relatable class for particular input and also it will be reponsible to avoid articles and other unwanted words.
  print(word)