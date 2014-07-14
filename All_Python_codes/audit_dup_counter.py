
import collections
import pandas as pd
import numpy as np
from datetime import datetime
import os
pd.set_option('display.max_columns', 100)#this allowed 80 columns to be shown in ipython notebook

#all the file names are renamed for coding convieneince
pathname = "C:\Users\William\Documents\urban_project\Raw_data"


# read data into pandas dataframe and convert column names to upper case
def read_data(pname,fname):
	if fname.endswith('.csv'):
		df = pd.DataFrame.from_csv(os.path.join(pname,fname),index_col=None)
		df = df.rename(columns=lambda x: x.upper(),inplace=False)
		return df
	elif fname.endswith('.xlsx'):
		df = pd.io.excel.read_excel(os.path.join(pname,fname),sheetname=0,index_col=None)
		df = df.rename(columns=lambda x: x.upper(),inplace=False)
		return df
def merge_df(df,map,on):
    df = pd.DataFrame.merge(df,map,how='left',on=on)
    return df



# read data into pandas dataframes
audit = read_data(pathname,"audit.csv")
print "total number of audits:", len(audit)
merge_table = read_data(pathname,"R2P.csv")
print "Data read into dataframes"


audits_merge = merge_df(audit,merge_table,'RESNUM')
print "Merged on merge table"
audits_merge = audits_merge.sort('RESNUM')#sort No.1 to make sure the column is ordered


#print list(audits_merge.RESNUM)#to make sure the header is not converted to be part of the list
counter = collections.Counter(list(audits_merge.RESNUM))
dup_count = counter.values()



# remove duplicate audit for efficacy counting
print 'the size of audit file is', len(audits_merge)
audits_merge = audits_merge[audits_merge.DESCRIPTION != 'duplicate Entry']
audits_merge = audits_merge.drop_duplicates('RESNUM')
print 'the size of audit file after removing duplicates is', len(audits_merge)
#sort No.2 to make sure the order of the dataframe is the same as last sort. If the sort is not right, the insert function will mismatch the counts
audits_merge = audits_merge.sort('RESNUM')
audits_merge.insert( 0, 'DUP_COUNT', dup_count)#add the duplicate count to the first row, it works better at the beginning



audits_merge.to_csv('audit_with_dup_count.csv', index = False)#this doc does not have all the matching PROJECTIDs, but it should be good for efficacy counting


