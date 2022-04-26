# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:51:02 2022

@author: akash
"""

import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

text = "studies studying cries cry"

tokenization = nltk.word_tokenize(text)

for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))