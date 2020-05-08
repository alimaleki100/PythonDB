# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:02:26 2018

@author: alimaleki100
"""
## Write dataframe to postgres table
import pandas as pd
df = pd.read_excel('file Address')

from sqlalchemy import create_engine
engine = create_engine('postgresql://user:PWD@SERVERNAME/DBName')
df.to_sql("TBLName", engine,if_exists='append')




