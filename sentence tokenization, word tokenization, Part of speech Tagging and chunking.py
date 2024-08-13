# sentence tokenization, word tokenization, Part of speech Tagging and chunking of user defined text.
import nltk 
from nltk import tokenize, tag, chunk 
from tabulate import tabulate 
# Download necessary NLTK resources 
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger') 
nltk.download('maxent_ne_chunker') 
nltk.download('words') 
# Input paragraph 
para = "Hello! My name is Jack Reacher. Today you'll be learning NLTK." 
# Sentence tokenization 
sents = tokenize.sent_tokenize(para) 
# Word tokenization and POS Tagging 
tokenized_words = [] 
pos_tags = [] 
for sent in sents: 
    words = tokenize.word_tokenize(sent) 
    tokenized_words.append(words) 
    pos_tags.append(tag.pos_tag(words)) 
# Chunking 
chunked_trees = [] 
for tags in pos_tags: 
    chunked_trees.append(chunk.ne_chunk(tags)) 
# Format outputs into tables 
print("\nSentence Tokenization\n===================") 
print(tabulate([[sent] for sent in sents], headers=['Sentences'])) 
print("\nWord Tokenization\n===================") 
for i, words in enumerate(tokenized_words): 
    print(f"Sentence {i + 1}:") 
    print(tabulate([words], headers=['Words'])) 
print("\nPOS Tagging\n===========") 
for i, tags in enumerate(pos_tags): 
    print(f"POS Tags for Sentence {i + 1}:") 
    print(tabulate(tags, headers=['Word', 'POS Tag'])) 
print("\nChunking\n========") 
for i, tree in enumerate(chunked_trees): 
    print(f"Chunking for Sentence {i + 1}:") 
    print(tree) 
    print() 