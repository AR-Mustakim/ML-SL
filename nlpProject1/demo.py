import numpy as np
from textblob import TextBlob

randNum = np.random.randint(100)
print(randNum)


def getPol(text):
    polarity = TextBlob(text).sentiment.polarity
    return polarity



print("The polarity score is: "+str(getPol("😊")))