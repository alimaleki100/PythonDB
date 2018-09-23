# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:02:26 2018

@author: acer
"""

import pandas as pd
df = pd.read_excel('file Address')
#df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://user:PWD@SERVERNAME:Port#(5432)/DBName')

df.to_sql("TBLName", engine,if_exists='append')


