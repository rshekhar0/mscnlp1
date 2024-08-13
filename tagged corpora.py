import nltk 
from nltk import tokenize 
# Download necessary NLTK data 
nltk.download('punkt') 
nltk.download('words') 
nltk.download('averaged_perceptron_tagger') 
# Paragraph for tokenization 
para = "Hello! My name is Pikachu. Today you'll be learning NLTK." 
# Sentence tokenization 
sents = tokenize.sent_tokenize(para) 
print("\nSentence Tokenization\n===================\n", sents) 
# Word tokenization and POS tagging 
print("\nWord Tokenization and POS Tagging\n===================\n") 
tagged_sents = [] 
tagged_words = [] 
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index]) 
    tagged = nltk.pos_tag(words) 
    tagged_sents.append(tagged) 
    tagged_words.extend(tagged) 
    print(words) 
    print(tagged)
# Display tagged sentences and tagged words 
print("\nTagged Sentences\n===================\n", tagged_sents) 
print("\nTagged Words\n===================\n", tagged_words) 
# Explanation of POS Tags: 
# NN: Noun, singular or mass 
# PRP$: Possessive pronoun 
# VBZ: Verb, 3rd person singular present 
# NNP: Proper noun, singular 
# PRP: Personal pronoun 
# MD: Modal verb 
# VB: Verb, base form 
# VBG: Verb, gerund or present participle 
# .: Punctuation
