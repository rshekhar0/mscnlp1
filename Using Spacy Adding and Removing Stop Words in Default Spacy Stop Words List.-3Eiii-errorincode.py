#pip install spacy
#python -m spacy download en_core_web_sm
import spacy
from nltk.tokenize import word_tokenize
from tabulate import tabulate

# Load English language model in Spacy
sp = spacy.load('en_core_web_sm')

# Get Spacy's default stopwords
all_stopwords = sp.Defaults.stop_words

# Add 'play' to Spacy's default stopwords
all_stopwords.add("play")

# Define the text to process
text = "Sara likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

# Remove stopwords including 'play' from tokenized text
tokens_without_sw1 = [word for word in text_tokens if not word in all_stopwords]

# Check if 'not' is in stop word collection before removing it
if 'not' in all_stopwords:
    all_stopwords.remove('not')

# Remove stopwords excluding 'not' from tokenized text
tokens_without_sw2 = [word for word in text_tokens if not word in all_stopwords]

# Prepare data for table
data = [
    ["1. Remove stopwords including 'play' from Spacy's default stop words list:", tokens_without_sw1],
    ["2. Remove stopwords excluding 'not' from Spacy's default stop words list:", tokens_without_sw2],
    ["Explanation:", "Using Spacy: Adding and Removing Stop Words in Default Spacy Stop Words List"]
]

# Print table
print(tabulate(data, headers=['Output Section', 'Content'], tablefmt='grid'))
