# Usage of Give and Gave in the Penn Treebank sample
import nltk 
 
# Ensure required NLTK data is downloaded 
nltk.download('treebank') 
 
# Define a function to find specific VP nodes in the tree 
def give(t): 
    return (t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' and  
        (t[2].label() == 'PP-DTV' or t[2].label() == 'NP') and  
        ('give' in t[0].leaves() or 'gave' in t[0].leaves())) 
# Define a function to create a sentence from tree leaves 
def sent(t): 
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0') 
# Define a function to print a node with specified width 
def print_node(t, width): 
    output = "%s %s: %s / %s: %s" % (sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2])) 
    if len(output) > width: 
        output = output[:width] + "..." 
        print(output) 
# Iterate through parsed sentences in the Penn Treebank and apply the functions 
print("Finding and printing VP nodes that match the criteria:\n") 
for tree in nltk.corpus.treebank.parsed_sents(): 
    for t in tree.subtrees(give): 
        print_node(t, 72) 
