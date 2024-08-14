# corpus_creation.py

import os
import re
import requests
import pandas as pd
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize


nltk.download('punkt')

def scrape_articles(url):
    """Scrape articles from a given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    articles = [p.text for p in soup.find_all('p')]
    return articles

def load_data(csv_path):
    """Load categorical data from a CSV file."""
    df = pd.read_csv(csv_path)
    return df

def clean_text(text):
    """Clean and normalize text data."""
    
    text = re.sub(r'<.*?>', '', text)
    
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)
    return text

def clean_categorical_data(df):
    """Handle missing values and encode categorical variables."""
    
    df = df.fillna(method='ffill')

    df = pd.get_dummies(df, columns=['category_column'])
    return df

def save_articles(articles, directory):
    """Save cleaned articles to text files."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i, article in enumerate(articles):
        with open(os.path.join(directory, f'article_{i}.txt'), 'w') as file:
            file.write(article)

def save_categorical_data(df, csv_path):
    """Save cleaned dataframe to a CSV file."""
    df.to_csv(csv_path, index=False)

def analyze_corpus(articles):
    """Tokenize and perform frequency analysis on the corpus."""
    tokens = [word_tokenize(article) for article in articles]
    flat_tokens = [token for sublist in tokens for token in sublist]
    freq_dist = nltk.FreqDist(flat_tokens)
    return freq_dist

def visualize_data(df):
    """Visualize categorical data."""
    sns.countplot(x='category_column', data=df)
    plt.show()



# 1. Plaintext Corpus
url = "https://example.com/articles"
articles = scrape_articles(url)
cleaned_articles = [clean_text(article) for article in articles]
save_articles(cleaned_articles, 'cleaned_articles')

# Perform analysis
freq_dist = analyze_corpus(cleaned_articles)
freq_dist.plot(30, cumulative=False)

# 2. Categorical Corpus
csv_path = 'data.csv'
df = load_data(csv_path)
cleaned_df = clean_categorical_data(df)
save_categorical_data(cleaned_df, 'cleaned_data.csv')

# Visualize data
visualize_data(cleaned_df)
