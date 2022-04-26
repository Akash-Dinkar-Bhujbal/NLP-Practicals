import nltk
text = input('Enter text: ')
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
result.draw() 