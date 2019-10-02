# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:02:26 2018

@author: acer
"""
#import libraries
import pandas as pd
import pyodbc 
from sqlalchemy import create_engine

#input file
fileAddress='D:/ClosingStockMetaData2.xlsx'
sheetN='sheetName'
indexCol='indexCol'
#destination table name
TblName='TblName'
df = pd.read_excel(fileAddress,sheetname=sheetN)
engine = create_engine("mssql+pyodbc://USER:PWD@SERVER:PORT3(1433)/DBName?driver=SQL Server")
        
df=df.set_index(indexCol)
df.to_sql(TblName, engine,if_exists='append')





