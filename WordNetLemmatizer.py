# Study PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer Study WordNetLemmatizer.
import nltk 
from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer 
from nltk.stem import WordNetLemmatizer 
# Ensure you have the required NLTK data files 
nltk.download('wordnet') 
# PorterStemmer 
word_stemmer = PorterStemmer() 
print("PorterStemmer: 'writing' ->", word_stemmer.stem('writing')) 
# LancasterStemmer 
Lanc_stemmer = LancasterStemmer() 
print("LancasterStemmer: 'writing' ->", Lanc_stemmer.stem('writing')) 
# RegexpStemmer 
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4) 
print("RegexpStemmer: 'writing' ->", Reg_stemmer.stem('writing')) 
# SnowballStemmer 
english_stemmer = SnowballStemmer('english') 
print("SnowballStemmer: 'writing' ->", english_stemmer.stem('writing')) 
# WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
print("\nWordNetLemmatizer:") 
print("word :\tlemma") 
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora")) 
# 'a' denotes adjective in "pos" 
print("better :", lemmatizer.lemmatize("better", pos="a"))
