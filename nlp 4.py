import nltk
from nltk.corpus import treebank

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

s = input('Enter Sentence: ')
tokens = nltk.word_tokenize(s)
#hello world this is akash and I'm using python rightnow
print(tokens)

tags = nltk.pos_tag(tokens)
print("POS Tags\n", tags)

#nltk.tree
entities = nltk.chunk.ne_chunk(tags)
print('Entities\n')
print(entities)