# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:01:53 2021

@author: qtckp
"""


import sys
sys.path.append('..')


from StemLemPipe import remove_hook_words



text = 'a simple text with some hook words. u should delete each hook word and one word after them'

print(remove_hook_words(text, hook_words = ['u', 'hook', 'word']))


