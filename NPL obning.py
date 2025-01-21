'''import nltk

# Download the 'punkt' tokenizer if it isn't already installed
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Importing word_tokenize after ensuring punkt is downloaded
from nltk.tokenize import word_tokenize

# Sample text
text = "today is Blue monday but the sun is shining and life's good"

# Tokenize the text
tokens = word_tokenize(text)

print(tokens)'''


import spacy 

# "sv_core_news_sm"
nlp = spacy.load("en_core_web_sm")

# Exempeltext
# doc = nlp("Google grundades av Larry Page och Sergey Brin i USA.")
doc = nlp("Google gwas created by Larry Page and Sergey Brin in USA.")

# Identifiera entiteter
for ent in doc.ents:
   print(ent.text, ent.label_)




'''
import textBlob


svTexts = [
   "Den här produkten är fantastisk!",
   "Jag är missnöjd med servicen.",
   "Helt okej upplevelse, inte mer."
]

enTexts = [
    "This product is amazing!",
    "I am dissatisfied with the service.",
    "Okay experience, nothing more."
]

texts = enTexts

for text in texts:
   analysis = TextBlob(text)
   print(f"Text: {text}")
   print(f"Polarity: {analysis.sentiment.polarity}")
   print(f"Subjectivity: {analysis.sentiment.subjectivity}\n")
'''