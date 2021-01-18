# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:37:29 2021

@author: qtckp
"""

import sys
sys.path.append('..')

from StemLemPipe import get_ngrams, words_to_ngrams_list


text = "word1 word2 word3 ... word10"

# returns generator
gen = get_ngrams(text.split(), n = 3)
# just list of lists
print(list(gen))
# [['word1', 'word2', 'word3'], ['word2', 'word3', '...'], ['word3', '...', 'word10']]


# words in n-gram are combined, it's list of strings
print(words_to_ngrams_list(text.split(), n_min = 1, n_max = 3))
# ['word1', 'word2', 'word3', '...', 'word10', 'word1 word2', 'word2 word3', 'word3 ...', '... word10', 'word1 word2 word3', 'word2 word3 ...', 'word3 ... word10']

