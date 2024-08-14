import re

def custom_tokenize(text):
    # Split on spaces and punctuation
    return re.findall(r'\S+', text)

# Sample Hindi text
text = "मैं आज स्कूल जा रहा हूँ"

# Tokenize text
tokens = custom_tokenize(text)
print(tokens)


