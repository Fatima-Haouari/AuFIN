# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:41:20 2021

@author: fhaou
"""
import json
import codecs
import gzip
import os
from googletrans import Translator
import pandas as pd
import glob
from json import loads
from requests import get
import requests
import re
import numpy as np

######################clean text######################################
def clean(text):
   print(text, type(text))
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
def translate(text):
    #source#https://github.com/ssut/py-googletrans/issues/268
    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=ar&q=" + text
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    try:
      request_result = requests.get(url, headers=headers).json()
    except:
     pass
    return request_result['alternative_translations'][0]['alternative'][0]['word_postproc']

