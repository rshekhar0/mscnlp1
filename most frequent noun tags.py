# Write a program to find the most frequent noun tags.
import nltk 
from collections import defaultdict 
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger') 
# Tokenize the text 
text = nltk.word_tokenize("Shivam likes to play football. Shivam does not like to play cricket.") 
# POS tagging 
tagged = nltk.pos_tag(text) 
print(tagged) 
# Check if the word is a noun and collect noun words 
addNounWords = [] 
for word, tag in tagged: 
    if tag in ('NN', 'NNS', 'NNPS', 'NNP'): 
        addNounWords.append(word) 
        print(addNounWords) 
# Memoize the count of each noun 
    temp = defaultdict(int) 
for noun in addNounWords: 
    temp[noun] += 1 
# Get the word with maximum frequency 
res = max(temp, key=temp.get) 
# Print the result
print("Word with maximum frequency : " + str(res))