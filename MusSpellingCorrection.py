import pickle
import re
import csv

with open('/content/drive/MyDrive/Colab Notebooks/ShortFormMelayu.p', 'rb') as fp:
    sf_Dict = pickle.load(fp)
    sf_Dict = {v: k for v, k in sf_Dict.items()}

def pembetulEjaan(text):
  for word in sf_Dict:
    text = re.sub(r'\b'+word+'', sf_Dict[word], text)
  return text