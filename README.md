### **NLP Lab Manual - University of Mumbai**

**Practical No. 1:**
**Objective:** Introduction to NLTK and basic text-to-speech and speech-to-text conversion.

**Tasks:**
a) Install NLTK  
b) Convert the given text to speech.  
c) Convert audio file Speech to Text.

**Practical No. 2:**
**Objective:** Understanding corpus, conditional frequency distributions, tagged corpora, and word properties.

**Tasks:**
a. Study various Corpus: Brown, Inaugural, Reuters, udhr with methods like filelds, raw, words, sents, categories.  
b. Create and use your own corpora (plaintext, categorical).  
c. Study Conditional frequency distributions.  
d. Study tagged corpora with methods like tagged_sents, tagged_words.  
e. Write a program to find the most frequent noun tags.  
f. Map Words to Properties Using Python Dictionaries.  
g. Study DefaultTagger, Regular expression tagger, UnigramTagger.  
h. Find different words from a given plain text without any space by comparing this text with a given corpus of words. Also, find the score of words.

**Practical No. 3:**
**Objective:** Introduction to WordNet Dictionary and handling stopwords.

**Tasks:**
a. Study Wordnet Dictionary with methods like synsets, definitions, examples, antonyms.  
b. Study lemmas, hyponyms, hypernyms.  
c. Write a program using Python to find synonym and antonym of word "active" using Wordnet.  
d. Compare two nouns.  
e. Handling stopwords:
    i) Using NLTK Adding or Removing Stop Words in NLTK's Default Stop Word List.  
    ii) Using Gensim Adding and Removing Stop Words in Default Gensim Stop Words List.  
    iii) Using Spacy Adding and Removing Stop Words in Default Spacy Stop Words List.

**Practical No. 4:**
**Objective:** Understanding text tokenization using various libraries.

**Tasks:**
a-f. Tokenization using Python’s split() function, Regular Expressions (RegEx), NLTK, spaCy library, Keras, and Gensim.

**Practical No. 5:**
**Objective:** Importing NLP Libraries for Indian Languages and performing basic tasks.

**Tasks:**
a) Word tokenization in Hindi.  
b) Generate similar sentences from a given Hindi text input.  
c) Identify the Indian language of a text.

**Practical No. 6:**
**Objective:** Illustrate part-of-speech tagging (POS) and named entity recognition (NER).

**Tasks:**
a. Part-of-speech Tagging and chunking of user-defined text.  
b. Named Entity recognition of user-defined text.  
c. Named Entity recognition with diagram using NLTK corpus – treebank.

**Practical No. 7:**
**Objective:** Introduction to Finite State Automata.

**Tasks:**
a) Define grammar using NLTK. Analyze a sentence using the same.  
b) Accept the input string with Regular expression of Finite Automaton: 101+.  
c) Accept the input string with Regular expression of FA: (a+b)*bba.  
d) Implementation of Deductive Chart Parsing using context-free grammar.

**Practical No. 8:**
**Objective:** Study stemming and lemmatization.

**Tasks:**
Study PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer, WordNetLemmatizer.

**Practical No. 9:**
**Objective:** Implement Naive Bayes classifier.

**Practical No. 10:**
**Objective:** Introduction to speech tagging and statistical parsing.

**Tasks:**
a. Speech tagging using Spacy and NLTK.  
b. Statistical parsing: Usage of Give and Gave in the Penn Treebank sample, probabilistic parser.  
c. Malt parsing: Parse a sentence and draw a tree using malt parsing.

**Note:**
1. Java should be installed.  
2. Maltparser-1.7.2 zip file should be copied in C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39 folder and extracted in the same folder.  
3. Engmalt.linear-1.7.mco file should be copied to C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39 folder.

**Readme Format for GitHub:**
The lab manual provides a structured approach to learning Natural Language Processing (NLP) techniques. Each practical introduces fundamental concepts and provides hands-on exercises using Python and relevant libraries such as NLTK, spaCy, and Gensim. The manual covers tasks ranging from basic text processing to advanced topics like part-of-speech tagging, named entity recognition, and finite state automata. It also includes instructions for setting up the environment, including necessary installations and configurations.

# Required Libraries Installation Guide

1. **Update pip:**
    ```
    pip install --upgrade pip
    ```

2. **NLTK Installation:**
    ```
    pip install --user -U nltk
    ```

3. **NumPy Installation:**
    ```
    pip install --user -U numpy
    ```

4. **Speech Recognition Installation:**
    ```
    pip3 install SpeechRecognition pydub
    ```

5. **Gensim Installation:**
    ```
    pip install gensim
    ```

6. **spaCy Installation:**
    ```
    pip install spacy
    ```
    ```
    python -m spacy download en_core_web_sm
    ```
    ```
    python -m spacy download en
    ```

7. **Keras Installation:**
    ```
    pip install keras
    ```

8. **TensorFlow Installation:**
    ```
    pip install tensorflow
    ```

9. **PyTorch Installation:**
    ```
    pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
    ```

10. **Indian Language Toolkit (INltk) Installation:**
    ```
    pip install inltk
    ```

11. **Tornado Installation:**
    ```
    pip install tornado==4.5.3
    ```

12. **Pandas Installation:**
    ```
    pip install pandas
    ```

13. **Scikit-learn Installation:**
    ```
    pip install sklearn
    ```

