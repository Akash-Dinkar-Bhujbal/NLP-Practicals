import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize,sent_tokenize
#sents = nltk.sent_tokenize(nltk.corpus)
sents = 'Akash is good boy'
print("The number of sentences is", str(sents))
#words = nltk.word_tokenize(nltk.corpus)
words = nltk.word_tokenize(sents)
print("The number of tokens is", str(words))
average_tokens = round(len(words)/len(sents))
print("The average number of tokens per sentence is",average_tokens)
unique_tokens = set(words)
print("The number of unique tokens are", str(unique_tokens))
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
final_tokens = []
for each in words:
    if each not in stop_words:ArithmeticError
    final_tokens.append(each)
    print("The number of total tokens after removing stopwords are", str((final_tokens)))