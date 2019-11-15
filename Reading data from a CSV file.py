import os
import pandas as pd
os.chdir("E:\pandas")
data_csv=pd.read_csv('annual.csv')
data_csv=pd.read_csv('annual.csv',index_col=0,na_values=['AA'])