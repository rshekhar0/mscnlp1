#!pip install -U spacy
#!python -m spacy download en_core_web_sm
import spacy
from tabulate import tabulate
# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")
# Input text
text = ("When Sebastian Thrun started working on self-driving cars at "
"Google in 2007, few people outside of the company took him "
"seriously. “I can tell you very senior CEOs of major American "
"car companies would shake my hand and turn away because I wasn’t "
"worth talking to,” said Thrun, in an interview with Recode earlier "
"this week.")
# Process the text with the loaded NLP pipeline
doc = nlp(text)
# Extract noun phrases and verbs
noun_phrases = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
# Format outputs into two columns
noun_phrases_table = [[f"Noun Phrase {i+1}", phrase] for i, phrase in enumerate(noun_phrases)]
verbs_table = [[f"Verb {i+1}", verb] for i, verb in enumerate(verbs)]
# Print outputs using tabulate for formatted display
print("Noun phrases and Verbs:")
print(tabulate(noun_phrases_table + verbs_table, headers=["Type", "Text"], tablefmt="pretty"))