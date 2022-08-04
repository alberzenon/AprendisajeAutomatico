#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:50:17 2021

@author: alberto
"""

import pandas as pd
import glob
import numpy as np

all_files = glob.glob("Aemet2019-*.xls")

file_list = []
for f in all_files:
    data = pd.read_excel(f,skiprows=4)
    data['source_file'] = f # nueva columna conteniendo el nombre del fichero leido
    file_list.append(data)
df = pd.concat(file_list)

df.shape
(24707, 13)

df.head()