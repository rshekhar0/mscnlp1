#Tokenization using Regular Expressions (RegEx)
import nltk 
from nltk.tokenize import RegexpTokenizer 
# Create a reference variable for Class RegexpTokenizer 
tokenizer = RegexpTokenizer('\s+', gaps=True) 
# Create a string input 
input_str = "I love to study Natural Language Processing in Python" 
# Tokenize the input string 
tokens = tokenizer.tokenize(input_str) 
# Print tokens 
print("Tokenized Output:") 
print("=================") 
print(tokens)