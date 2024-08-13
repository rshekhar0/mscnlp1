# Find different words from a given plain text without any space by comparing this text with a given corpus of words. Also find the score of words.
from __future__ import with_statement  # To use 'with' statement for file reading 
import re
words_file_content = """\ 
hello 
what 
is 
my 
name 
www 
com 
""" 
# Write the sample content to words.txt 
with open('words.txt', 'w') as f: 
    f.write(words_file_content) 
# Initialize variables 
words = []  # List to store corpus words 
testword = []  # List to store test words 
ans = []  # List to store matched words from corpus 
# Menu display and user input
print("MENU") 
print("-----------") 
print(" 1. Hash tag segmentation") 
print(" 2. URL segmentation") 
print("Enter the input choice for performing word segmentation:") 
choice = int(input()) 
 
# Perform segmentation based on user choice 
if choice == 1: 
    text = "#whatismyname"  # Example hash tag test data 
    print("Input with HashTag:", text) 
    pattern = re.compile("[^\w']") 
    a = pattern.sub('', text) 
elif choice == 2: 
    text = "www.whatismyname.com"  # Example URL test data 
    print("Input with URL:", text) 
    splitwords = ["www", "com"]  # Words to be removed from segmentation 
    a = re.split(r'\W+', text)  # Splitting based on non-word characters 
    a = " ".join([each for each in a if each not in splitwords]) 
else: 
    print("Wrong choice...try again") 
    exit() 
 
print("Segmented Output:", a) 
 
# Read the words from words.txt into the words list 
with open('words.txt', 'r') as f: 
    lines = f.readlines() 
    words = [e.strip() for e in lines] 
 
# Function to perform segmentation based on corpus words 
def Seg(a, length): 
    ans = [] 
    for k in range(0, length + 1): 
        if a[0:k] in words: 
            print(a[0:k], "- Appears in the corpus") 
            ans.append(a[0:k]) 
            break 
    if ans != []: 
        g = max(ans, key=len) 
        return g 
 
test_length = len(a)  # Length of the segmented test data 
test_total_iter = 0  # Initialize total iteration count 
answer = []  # List to store segmented words 
while test_total_iter < test_length: 
    ans_words = Seg(a, test_length) 
    if ans_words: 
        test_iter = len(ans_words) 
        answer.append(ans_words) 
        a = a[test_iter:test_length] 
        test_total_iter += test_iter 
        after_segmentation = " ".join(answer) 
        print("\nOutput") 
        print("---------") 
    print("After segmentation:", after_segmentation) 
# Calculate and print score 
N = len(words)  # Total number of words in the corpus (N = 7 based on the sample words.txt) 
C = len(answer)  # Number of words segmented 
score = C * N / N  # Calculate the score 
print("Score:", score)