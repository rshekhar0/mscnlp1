# Multiword Expressions in NLP
import nltk 
from nltk.tokenize import MWETokenizer 
from nltk import sent_tokenize, word_tokenize 
# Define the input text 
s = '''Good cake cost Rs.1500/kg in Mumbai. Please buy me one of them.\n\nThanks.''' 
# Define the MWE tokenizer with multi-word expressions 
mwe = MWETokenizer([('New', 'York'), ('Hong', 'Kong')], separator='_') 
# Tokenize the text into sentences and then tokenize each sentence 
print("Tokenized Output:") 
for sent in sent_tokenize(s): 
# Tokenize the sentence into words and then apply the MWE tokenizer 
    tokens = word_tokenize(sent) 
    mwe_tokens = mwe.tokenize(tokens) 
    print(mwe_tokens) 
