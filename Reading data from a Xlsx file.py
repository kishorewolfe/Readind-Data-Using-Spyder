import os
import pandas as pd
os.chdir("E:\pandas")
data_xlsx=pd.read_excel('annual.xlsx')
data_xlsx=pd.read_excel('annual.xlsx',index_col=0,na_values=['AA'])