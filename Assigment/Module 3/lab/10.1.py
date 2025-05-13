import re

text = "Python is awesome"
pattern = "Python"

if re.match(pattern, text):
    print("Match found!")
else:
    print("No match!")
