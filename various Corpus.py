import nltk  # Importing the NLTK library 
from nltk.corpus import brown  # Importing the Brown corpus from NLTK 
nltk.download('brown') 
# Displaying the file identifiers of the Brown corpus 
print ('File ids of brown corpus\n', brown.fileids()) 
# Loading the words from the 'ca01' file of the Brown corpus 
ca01 = brown.words('ca01') 
# Displaying the first few words from the 'ca01' file 
print('\nca01 has following words:\n', ca01[:10])  # Displaying first 10 words 
# Counting the total number of words in the 'ca01' file 
print('\nca01 has', len(ca01), 'words') 
# Displaying the categories or files in the Brown corpus 
print ('\n\nCategories or file in brown corpus:\n') 
print (brown.categories()) 
# Displaying statistics for each text in the Brown corpus 
print ('\n\nStatistics for each text:\n') 
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\t\tFileName') 
# Looping over all file identifiers in the Brown corpus 
for fileid in brown.fileids(): 
    num_chars = len(brown.raw(fileid))  # Counting the number of characters 
    num_words = len(brown.words(fileid))  # Counting the number of words 
    num_sents = len(brown.sents(fileid))  # Counting the number of sentences 
    num_vocab = len(set([w.lower() for w in brown.words(fileid)]))  # Counting the vocabulary size 
    avg_word_len = int(num_chars / num_words) 
    avg_sent_len = int(num_words / num_sents) 
    avg_word_freq = int(num_words / num_vocab) 
# Printing the statistics for each text 
    print (avg_word_len, '\t\t\t', avg_sent_len, '\t\t\t', avg_word_freq, '\t\t\t', fileid)
