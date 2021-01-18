# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:43:50 2021

@author: qtckp
"""

import sys
sys.path.append('..')

from StemLemPipe import text2sentences, split_by_words, sentence_split, stopwords

text = "We should split this text. It has several sentences e. g. this"


# splitting by some words
print(split_by_words(text, ['split', 'has']))
# ['We should', 'this text. It', 'several sentences e. g. this']


# splitting to sentences
sentences = text2sentences(text)
print(sentences)
# ['We should split this text', 'It has several sentences e. g. this']


# split sentence by symbols and words
phrases = sentence_split(sentences[1], separators='.', stop_words=stopwords('en'))
print(phrases)
# ['It', 'several sentences e', 'g']

