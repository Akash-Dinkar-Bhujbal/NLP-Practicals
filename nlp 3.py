import re
from nltk.util import ngrams
s = "natural language processing (NLP) is an area of computer science " \
    "and aitificial intelligence concerned with the  interactions" \
    "between computer and human language."
s = s.lower()
s = re.sub(r'[^a-zA-z0-9\s]', '', s)
tokens = [token for  token in s.split(" ")if token != ""]
output = list(ngrams(tokens,3))
print (output)
    