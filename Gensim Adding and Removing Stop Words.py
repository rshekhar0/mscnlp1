# Using Gensim Adding and Removing Stop Words in Default Gensim Stop Words List.
import gensim 

import gensim 
from gensim.parsing.preprocessing import remove_stopwords 
from nltk.tokenize import word_tokenize 
from tabulate import tabulate 
# Original text 
text = "Ben likes to play football, however he is not too fond of tennis." 
# Remove stopwords using Gensim's default stopwords list 
filtered_sentence = remove_stopwords(text) 
# Get Gensim's default stopwords list 
all_stopwords = gensim.parsing.preprocessing.STOPWORDS 
# Add 'likes' and 'play' to Gensim's default stopwords list 
from gensim.parsing.preprocessing import STOPWORDS 
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play'])) 
# Tokenize text and remove stopwords including 'likes' and 'play' 
text_tokens = word_tokenize(text) 
tokens_without_sw1 = [word for word in text_tokens if not word in all_stopwords_gensim] 
# Remove 'not' from Gensim's default stopwords list 
all_stopwords_gensim = STOPWORDS.difference({"not"}) 
# Tokenize text and remove stopwords excluding 'not' 
text_tokens = word_tokenize(text) 
tokens_without_sw2 = [word for word in text_tokens if not word in all_stopwords_gensim] 
# Prepare data for table 
data = [ 
    ["1. Remove stopwords using Gensim's default stopwords list:", filtered_sentence], 
    ["2. Gensim's default stopwords list:", '\n'.join(all_stopwords)], 
    ["3. Remove 'likes' and 'play' from Gensim's default stopwords list:", tokens_without_sw1], 
    ["4. Remove 'not' from Gensim's default stopwords list:", tokens_without_sw2], 
    ["Explanation:", "Using Gensim: Adding and Removing Stop Words in Default Gensim Stop Words List"] 
] 
# Print table 
print(tabulate(data, headers=['Output Section', 'Content'], tablefmt='grid'))