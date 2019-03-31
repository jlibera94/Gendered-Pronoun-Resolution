# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:30:44 2019

@author: jlibe
"""

import spacy.en
nlp = spacy.en.English()

for tok in nlp(u"You and I make us"):
    print (tok.string, tok.pos)
    