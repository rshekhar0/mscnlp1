# Install required packages with specific versions
#!pip install torch==1.9.0
#!pip install inltk
#!pip install tornado==4.5.3

# Import necessary functions from inltk
from inltk.inltk import setup, identify_language

# Set up the language model for Gujarati
setup('gu')

# Identify the language of the given text
text_to_identify = 'બીના કાપડિયા'
language = identify_language(text_to_identify)

# Print the identified language
print("Identified Language:", language)
