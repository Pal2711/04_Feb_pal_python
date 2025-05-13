import re

text = "Hello, welcome to Python programming!"
word = "Python"

if re.search(word, text):
    print("Word found!")
else:
    print("Word not found!")
