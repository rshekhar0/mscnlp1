# Write a program using python to find synonym and antonym of word "active" using Wordnet.
from nltk.corpus import wordnet 
from tabulate import tabulate 
# Finding synsets for the word 'active' 
active_synsets = wordnet.synsets("active") 
# Prepare data for synsets and their definitions 
synset_data = [] 
for synset in active_synsets: 
    synset_data.append([synset.name(), synset.definition()]) 
# Finding antonyms of the lemma 'active.a.01.active' 
active_lemma = wordnet.lemma('active.a.01.active') 
antonyms = active_lemma.antonyms() 
antonym_names = ', '.join([antonym.name() for antonym in antonyms]) 
# Format output in table 
print("Synsets for 'active':") 
print(tabulate(synset_data, headers=['Synset', 'Definition'], tablefmt='pretty')) 
# Print Antonyms in a table format 
print("\nAntonyms:") 
print(tabulate([[antonym_names]], headers=['Antonyms'], tablefmt='pretty'))