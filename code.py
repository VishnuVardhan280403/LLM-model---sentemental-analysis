!pip install transformers
!pip install torch
from transformers import pipeline
sentiment_pipeline= pipeline("sentiment-analysis")
import re
def clean_text(text):
  #text=re.sub(r'[a-zA-Z0-9]','',text)
  text=re.sub(r'<@#$&*>','',text)
  text=re.sub(r' ','',text)
  return text

def preprocess_text(text):
  text=clean_text(text)
  return text
def analyse_sentiment(text):
  text=preprocess_text(text)
  result=sentiment_pipeline(text)
  return result
sample_texts = [
    "I love this product! It's amazing.",
    "This is the worst service I've ever used.",
    "I'm not sure how I feel about this."
]

for text in sample_texts:
    print(f"Text: {text}")
    print(f"Sentiment: {analyse_sentiment(text)}\n")
def analyse_text_input():
  user_input=input("engter the text")
  result= analyse_sentiment(user_input)
  print(f"Sentiment: {result[0]['label']}, Confidence: {result[0]['score']}")

while True:
  analyse_text_input()

