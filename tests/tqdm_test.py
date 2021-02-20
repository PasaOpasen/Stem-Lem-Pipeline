# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:10:30 2021

@author: qtckp
"""

import sys
sys.path.append('..')

from StemLemPipe import split_by_words, phrases2lower, phrases_transform, phrases_without_excess_symbols



some_text = "this IS some #### text with many !!!! 12 345& ? , symbols to ____prepare. Okay "*100000

# split to phrases 
splitted = split_by_words(some_text, words = ['with', '?'])


good_text = phrases_without_excess_symbols(splitted, include_alpha= True, include_numbers= False)



# use my own function

phrases_transform(good_text, lambda text: text[::-1], progress_bar=True)
# ['txet emos si siht', 'ynam', 'yako eraperp ot slobmys']