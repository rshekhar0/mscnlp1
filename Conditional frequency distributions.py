# Study Conditional frequency distributions.
import nltk 
from nltk.corpus import brown, inaugural, udhr 
# Download required NLTK data 
nltk.download('brown') 
nltk.download('inaugural') 
nltk.download('udhr') 
# Process a sequence of pairs 
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...] 
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...] 
# Construct a Conditional Frequency Distribution 
fd = nltk.ConditionalFreqDist( 
    (genre, word) 
    for genre in brown.categories() 
    for word in brown.words(categories=genre) 
)
# Create a list of genre-word pairs 
genre_word = [ 
    (genre, word) 
    for genre in ['news', 'romance'] 
    for word in brown.words(categories=genre) 
] 
# Print the length and sample pairs from genre_word 
print(len(genre_word)) 
print(genre_word[:4]) 
print(genre_word[-4:]) 
# Create and print the Conditional Frequency Distribution 
cfd = nltk.ConditionalFreqDist(genre_word) 
print(cfd) 
print(cfd.conditions()) 
print(cfd['news']) 
print(cfd['romance']) 
print(list(cfd['romance'])) 
# Create a CFD for inaugural corpus 
cfd = nltk.ConditionalFreqDist( 
    (target, fileid[:4]) 
    for fileid in inaugural.fileids() 
    for w in inaugural.words(fileid) 
    for target in ['america', 'citizen'] 
    if w.lower().startswith(target) 
) 
# Define languages for udhr corpus 
languages = ['Chickasaw', 'English', 'German_Deutsch', 
        'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik'] 
# Create and tabulate CFD for udhr corpus 
cfd = nltk.ConditionalFreqDist( 
    (lang, len(word)) 
    for lang in languages 
    for word in udhr.words(lang + '-Latin1') 
) 
cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True) 