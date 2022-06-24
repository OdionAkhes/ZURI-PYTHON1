# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        return f.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.lower()
    counted_text=Counter(text.split())
    print(counted_text)

count_words()