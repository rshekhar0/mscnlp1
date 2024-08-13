# Tokenization using Gensim
from gensim.utils import tokenize 
# Create a string input 
input_str = "I love to study Natural Language Processing in Python" 
# Tokenize the text using gensim's tokenize function 
tokens = list(tokenize(input_str)) 
# Print the tokens 
print("Tokens:") 
print("=======") 
for token in tokens: 
    print(token) 