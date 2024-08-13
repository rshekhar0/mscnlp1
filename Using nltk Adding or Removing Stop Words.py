# Using nltk Adding or Removing Stop Words in NLTK's Default Stop Word List.
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
# Download stopwords data 
nltk.download('stopwords') 
# Input text 
text = "Nobita enjoys playing football, but he isn't particularly fond of tennis." 
# Tokenize the text 
text_tokens = word_tokenize(text) 
# Remove stopwords from NLTK's stopwords list 
tokens_without_sw_default = [word for word in text_tokens if not word in 
stopwords.words('english')] 
# Print output with default stopwords list 
print("Using default NLTK stopwords:") 
print("Word Tokens:", text_tokens) 
print("Tokens without Stopwords:", tokens_without_sw_default) 
print() 
# Add 'play' to the NLTK stopwords collection 
all_stopwords = stopwords.words('english') 
all_stopwords.append('play') 
# Remove stopwords including 'play' 
tokens_without_sw_with_play = [word for word in text_tokens if not word in all_stopwords] 
# Print output with 'play' added to stopwords 
print("Adding 'play' to NLTK stopwords:") 
print("Word Tokens:", text_tokens) 
print("Tokens without Stopwords (including 'play'):", tokens_without_sw_with_play) 
print() 
# Remove 'not' from NLTK stopwords collection 
all_stopwords.remove('not') 
# Remove stopwords excluding 'not' 
tokens_without_sw_without_not = [word for word in text_tokens if not word in all_stopwords] 
# Print output after removing 'not' from stopwords 
print("Removing 'not' from NLTK stopwords:") 
print("Word Tokens:", text_tokens) 
print("Tokens without Stopwords (excluding 'not'):", tokens_without_sw_without_not)
