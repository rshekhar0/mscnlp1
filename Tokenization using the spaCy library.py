import spacy

# Load the English blank model
nlp = spacy.blank("en")

# Create a string input
input_str = "I love to study Natural Language Processing in Python"

# Process the text with the NLP pipeline
doc = nlp(input_str)

# Extract tokens from the processed document
words = [token.text for token in doc]

# Print the list of tokens
print("Tokens:")
print("=======")
print(words)
