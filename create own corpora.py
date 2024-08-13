# Create and use your own corpora (plaintext, categorical)

import nltk # Importing the NLTK library
from nltk.corpus import PlaintextCorpusReader # Importing PlaintextCorpusReader from NLTK
nltk.download('punkt')
# Define the path to the directory containing the corpus files
corpus_root = 'C:\\Users\\DELL\\Desktop\\STUDIES\\NLP\\sample_data'
# Create a PlaintextCorpusReader object to access the corpus files
filelist = PlaintextCorpusReader(corpus_root, '.*')
# Display the file list
print('\n File list: \n')
print(filelist.fileids()) # Printing the file identifiers
print(filelist.root) # Printing the root directory of the corpus
# Display statistics for each text in the corpus
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')
# Loop over all file identifiers in the corpus
for fileid in filelist.fileids():
# Counting the number of characters, words, sentences, and vocabulary size for each text
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
# Computing average word length, average sentence length, and average word frequency for each
text
avg_word_len = int(num_chars / num_words)
avg_sent_len = int(num_words / num_sents)
avg_word_freq = int(num_words / num_vocab)
# Printing the statistics for each text
print(avg_word_len, '\t\t\t', avg_sent_len, '\t\t\t', avg_word_freq, '\t\t', fileid)
