import os
import pandas as pd
os.chdir("E:\pandas")
data_xlsx=pd.read_excel('annual.csv')
data_xlsx=pd.read_excel('annual.csv',index_col=0,na_values=['AA'])