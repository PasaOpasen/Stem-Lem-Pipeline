# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:08:35 2021

@author: qtckp
"""

import sys
sys.path.append('..')

from StemLemPipe import split_by_words, phrases2lower, phrases_transform, phrases_without_excess_symbols



some_text = "this IS some #### text with many !!!! 12 345& ? , symbols to ____prepare. Okay"

# split to phrases 
splitted = split_by_words(some_text, words = ['with', '?'])
print(splitted)
# ['this IS some #### text', 'many !!!! 12 345&', ', symbols to ____prepare. Okay']

lower_text = phrases2lower(splitted)
print(lower_text)
# ['this is some #### text', 'many !!!! 12 345&', ', symbols to ____prepare. okay']

# remove bad symbols
print(phrases_without_excess_symbols(lower_text, include_alpha= True, include_numbers= True, include_also='.,'))
# ['this is some text', 'many 12 345', ', symbols to prepare. okay']

good_text = phrases_without_excess_symbols(lower_text, include_alpha= True, include_numbers= False)
print(good_text)
# ['this is some text', 'many', 'symbols to prepare okay']


# use my own function

print(phrases_transform(good_text, lambda text: text[::-1]))
# ['txet emos si siht', 'ynam', 'yako eraperp ot slobmys']

