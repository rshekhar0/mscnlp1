# Regular expression tagger
from nltk.corpus import brown 
from nltk.tag import RegexpTagger 
# Load a sample sentence from the Brown corpus under 'news' category 
test_sent = brown.sents(categories='news')[0] 
# Define a RegexpTagger with regular expression patterns and corresponding tags 
regexp_tagger = RegexpTagger([ 
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers 
    (r'(The|the|A|a|An|an)$', 'AT'),   # articles 
    (r'.*able$', 'JJ'),               
# adjectives
    (r'.*ness$', 'NN'),              
    (r'.*ly$', 'RB'),                 
    (r'.*s$', 'NNS'),                 
    (r'.*ing$', 'VBG'),              
    (r'.*ed$', 'VBD'),               
    (r'.*', 'NN')                     
]) 
print("RegexpTagger object:") 
print(regexp_tagger) 
# Tag the sample sentence using the RegexpTagger 
tagged_sentence = regexp_tagger.tag(test_sent) 
# Print the tagged sentence 
print("\nTagged sentence:") 
print(tagged_sentence) 