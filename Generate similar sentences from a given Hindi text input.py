# Install required packages
#!pip install torch==1.3.1
#!pip install inltk
#!pip install tornado==4.5.3

# Import required functions
from inltk.inltk import setup, get_similar_sentences

# Setup the Hindi language model
setup('hi')

# Get similar sentences to the given input in Hindi
input_text = 'मैं आज बहुत खुश हूं'
output = get_similar_sentences(input_text, 5, 'hi')

# Print the output
print("Similar Sentences:")
for sentence in output:
    print(sentence)

print("\nSample Sentences:")
print("मैं आज बहुत खुश हूं")
print("मैं बहुत खुश हूं")
print("मैं बहुत खुश हूँ")
print("मैं आज खुश हूं")
print("मैं आज बहुत खुश हूँ")
