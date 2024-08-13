# DefaultTagger
import nltk 
from nltk.tag import DefaultTagger 
from nltk.corpus import treebank 
nltk.download('treebank') 
# Create a default tagger that tags everything as 'NN' (noun) 
exptagger = DefaultTagger('NN') 
# Evaluate the tagger on a subset of the Treebank corpus 
testsentences = treebank.tagged_sents()[1000:] 
evaluation_score = exptagger.evaluate(testsentences) 
# Print the evaluation score 
print("Evaluation score of the default tagger on test sentences:") 
print(evaluation_score) 
# Tagging a list of sentences using the default tagger 
tagged_sentences = exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']]) 
# Print the tagged sentences 
print("\nTagged sentences:") 
print(tagged_sentences) 