#UnigramTagger
from nltk.tag import UnigramTagger 
from nltk.corpus import treebank 
# Load the first 10 tagged sentences of the treebank corpus as training data 
train_sents = treebank.tagged_sents()[:10] 
# Initialize the UnigramTagger with the training sentences 
tagger = UnigramTagger(train_sents) 
# Print the first sentence of the treebank corpus as a list of words 
print("First sentence of the treebank corpus:") 
print(treebank.sents()[0]) 
# Tag the first sentence using the trained UnigramTagger 
print("\nTagged sentence:") 
print(tagger.tag(treebank.sents()[0])) 
# Override the context model with a specific mapping 
tagger = UnigramTagger(model={'Pierre': 'NN'}) 
# Tag the first sentence again with the overridden context model 
print("\nTagged sentence with overridden model:") 
print(tagger.tag(treebank.sents()[0]))