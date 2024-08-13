# probabilistic parser
import nltk 
# Define the PCFG grammar 
grammar = nltk.PCFG.fromstring(''' 
NP -> NNS [0.5] | JJ NNS [0.3] | NP CC NP [0.2] 
NNS -> "men" [0.1] | "women" [0.2] | "children" [0.3] | NNS CC NNS [0.4] 
JJ -> "old" [0.4] | "young" [0.6] 
CC -> "and" [0.9] | "or" [0.1] 
''') 
# Print the grammar 
print("Grammar:") 
print(grammar) 
# Create a Viterbi parser using the grammar 
viterbi_parser = nltk.ViterbiParser(grammar) 
# Define a sentence to parse 
sentence = "old men and women".split() 
# Parse the sentence using the Viterbi parser 
print("\nParsing Output:") 
for tree in viterbi_parser.parse(sentence): 
    print(tree) 
