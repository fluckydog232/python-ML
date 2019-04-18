#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:51:29 2018

@author: apple
"""

from sklearn import preprocessing

#
#label encoding 
le=preprocessing.LabelEncoder()
city=["paris","paris","tokoyo","berlin"]
le.fit(city)
list(le.classes_)
after=le.transform(city)
print (after)

