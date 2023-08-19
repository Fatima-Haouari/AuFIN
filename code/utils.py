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

######################clean text######################################
def clean_text(text):
    accents = re.compile(r'[\u064b-\u0652\u0640]') # harakaat and tatweel (kashida) to remove
    arabic_punc= re.compile(r'[\u0621-\u063A\u0641-\u064A\d+]+') # Keep only Arabic letters/do not remove number
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


