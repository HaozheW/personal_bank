
import collections
from datetime import datetime
import os
import time
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from collections import Counter

pd.set_option('display.max_columns', 100)#this allowed 100 columns to be shown in ipython notebook
filetime = time.strftime("%m%d%H%M")#adding time to file name later for version


#all the file names are renamed for coding convieneince
pathname = "C:\Users\William\Documents\Github\urban_project_Haozhe\Raw_data"

# read data into pandas dataframe and convert column names to upper case
def read_data(pname,fname):
	if fname.endswith('.csv'):
		df = pd.DataFrame.from_csv(os.path.join(pname,fname),index_col=None)
		df = df.rename(columns=lambda x: x.upper(),inplace=False)
		return df
	elif fname.endswith('.xlsx'):
		df = pd.io.excel.read_excel(os.path.join(pname,fname),sheetname=0,			index_col=None)
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
audits_merge = audits_merge.sort('RESNUM')


#print list(audits_merge.RESNUM)
#to make sure the header is not converted to be part of the list
counter = collections.Counter(list(audits_merge.RESNUM))
dup_count = counter.values()
dup_count[:] = [x - 1 for x in dup_count]
print len(dup_count)
# remove duplicate audit for efficacy counting
print 'the size of audit file is', len(audits_merge)
audits_merge = audits_merge.drop_duplicates('RESNUM')
audits_merge = audits_merge.sort('RESNUM')
#audits_merge.insert( 0, 'DUP_COUNT', dup_count)
audits_merge = audits_merge[audits_merge.DESCRIPTION != 'Duplicate Entry']
print 'the size of audit file after removing duplicates is', len(audits_merge)


#create the 0/1 dummy for coverted audits
audits_merge['CONVERT'] = np.nan#create new empty column
audits_merge.loc[audits_merge['PROJECTID'].isnull(), 'CONVERT'] = 0#assign 0 to PROJECTID if null
audits_merge.loc[audits_merge['PROJECTID'].notnull(), 'CONVERT'] = 1#assign 1 to PROJECTID if not null

#save file to csv
file_name = 'audit_logisticR_'+filetime+'.csv'
audits_merge.to_csv(file_name, index = False)

#check for number of audits done by each contractor
contractor_count = Counter(list(audits_merge['AUDIT CONTRACTOR']))
top_ten = contractor_count.most_common(320)
print top_ten
