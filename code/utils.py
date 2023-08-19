# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:41:20 2021

@author: fhaou
"""
import json
import codecs
import gzip
import os
import pandas as pd
import glob
from json import loads
from requests import get
import requests
import re
import numpy as np

######################clean tweets######################################
def clean_tweets(text):
   if text is np.nan:
    return ""
   else:
    text = re.sub(r"http\S+", " ", text) # remove urls
    text = re.sub(r"RT ", " ", text) # remove rt
    text = re.sub(r"@[\w]*", " ", text) # remove handles
    text = re.sub(r"[\.\,\#_\|\:\?\?\/\=]", " ", text) # remove special characters
    text = re.sub(r'\t', ' ', text) # remove tabs
    text = re.sub(r'\n', ' ', text) # remove line jump
    text = re.sub(r"\s+", " ", text) # remove extra white space
    accents = re.compile(r'[\u064b-\u0652\u0640]') # harakaat and tatweel (kashida) to remove
     
    arabic_punc= re.compile(r'[\u0621-\u063A\u0641-\u064A\d+]+') # Keep only Arabic letters/do not remove numbers
    text=' '.join(arabic_punc.findall(accents.sub('',text)))
    text = text.strip()
    return text
  
######################clean text######################################
def clean_text(text):
    accents = re.compile(r'[\u064b-\u0652\u0640]') # harakaat and tatweel (kashida) to remove
    arabic_punc= re.compile(r'[\u0621-\u063A\u0641-\u064A\d+]+') # Keep only Arabic letters/do not remove numbers
    text=' '.join(arabic_punc.findall(accents.sub('',text)))
    text = text.strip()
    return text
  
#####################normalize tweets#################################
def normalize(text):
   if text is np.nan:
    return ""
   else:
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    return(text)
#######################################################################


