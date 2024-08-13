# Speech tagging using nktl
import nltk 
from nltk.corpus import state_union 
from nltk.tokenize import PunktSentenceTokenizer 
# Download required NLTK data files 
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger') 
nltk.download('state_union') 
# Create our training and testing data
train_text = state_union.raw("2005-GWBush.txt") 
sample_text = state_union.raw("2006-GWBush.txt") 
 
# Train the Punkt tokenizer 
custom_sent_tokenizer = PunktSentenceTokenizer(train_text) 
 
# Tokenize the sample text 
tokenized = custom_sent_tokenizer.tokenize(sample_text) 
 
def process_content(): 
    try: 
        for i in tokenized[:2]:  # Process only the first 2 sentences 
            words = nltk.word_tokenize(i) 
            tagged = nltk.pos_tag(words) 
            print("\nTokenized Sentence:") 
            print(i) 
            print("\nPOS Tags:") 
            print(tagged) 
    except Exception as e: 
        print(str(e)) 
 
# Process and display the content 
process_content() 
