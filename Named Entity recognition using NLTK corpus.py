# Named Entity recognition with diagram using NLTK corpus – treebank.
import nltk 
nltk.download('treebank') 
from nltk.corpus import treebank_chunk 
treebank_chunk.tagged_sents()[0] 
treebank_chunk.chunked_sents()[0] 
treebank_chunk.chunked_sents()[0].draw() 
