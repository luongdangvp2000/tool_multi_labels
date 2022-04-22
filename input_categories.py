from sre_parse import CATEGORIES

from apt import Cache
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
import os
import fcntl
import time

CATEGORIES = []
ID = 1
LOOP = True

while LOOP:
    input_categories = input()
    if input_categories == "end":
        LOOP = False
    CATEGORIES.append([input_categories, ID])
    ID += 1 

df = pd.DataFrame(CATEGORIES)
df.columns = ['Disease', 'ID']
df.to_csv('categories/categories.csv')