# Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms.
import nltk
from nltk.corpus import wordnet

# Ensure the required NLTK data is downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')

# Print synsets (collections of synonym words or lemmas) for the word 'car' 
print("Synsets for 'car':") 
print(wordnet.synsets("car")) 
# Print definition of the word 'car' in its first synset 
print("\nDefinition of 'car':") 
print(wordnet.synset("car.n.01").definition()) 
# Print examples of the word 'car' in its first synset 
print("\nExamples of 'car':") 
print("Examples:", wordnet.synset("car.n.01").examples()) 
# Get antonyms of the word 'buy' in its first lemma 
print("\nAntonyms of 'buy':") 
print(wordnet.lemma('buy.v.01.buy').antonyms()) 