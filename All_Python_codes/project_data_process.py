###########################################################
#This code should add the matching PROJECTID to all ResNum#
###########################################################
import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter
import csv
from dateutil.parser import parse
from datetime import datetime
pd.set_option('display.max_columns', 100)#this allowed 80 columns to be shown in ipython notebook

#all the file names are renamed for coding convieneince
audit = pd.read_csv('audit.csv')
project = pd.read_csv('project.csv', parse_dates = ['COMPLETEDT'])
r2p = pd.read_csv('R2P.csv')


#the audit and project file with by merged with key file first; the dupicates will be joined afterwards
missing_audit = []
merge_audit = pd.merge(audit, r2p, left_on = 'ResNum', right_on = 'RESNUM', how = 'left')
merge_audit = pd.DataFrame(merge_audit)
del merge_audit['RESNUM']
drop_dup_audit = merge_audit.drop_duplicates('ResNum')#using ResNum will result in more records, 321 to 299
#drop_dup_audit = drop_dup_audit[drop_dup_audit.PROJECTID is None]
drop_dup_audit = drop_dup_audit[pd.notnull(drop_dup_audit['PROJECTID'])]
#drop_dup_audit.dropna(subset = [46])  


merge_project = pd.merge(project, r2p, on = 'PROJECTID', how= 'left')
merge_project = pd.DataFrame(merge_project)
drop_dup_project = merge_project.drop_duplicates('PROJECTID')
drop_dup_project_NN = drop_dup_project[pd.notnull(drop_dup_project['RESNUM'])]#successful merges
drop_dup_project_IN = drop_dup_project[pd.isnull(drop_dup_project['RESNUM'])]#unsuccessful merges
#set the complete date as the datetime index
#drop_dup_project_NN.set_index('COMPLETEDT', drop = False)
print len(drop_dup_project_NN)
#sort index to get the datetime in order
drop_dup_project_NN['COMPLETEDT'] = pd.to_datetime(drop_dup_project_NN['COMPLETEDT'])
drop_dup_project_NN.sort_index(by = 'COMPLETEDT')
#keep the projects compeleted after 10/15/2011
#print drop_dup_project_NN['COMPLETEDT']
drop_dup_project_NN = drop_dup_project_NN.ix['20101015':]

print len(drop_dup_project_NN)
drop_dup_project_NN = drop_dup_project_NN[(drop_dup_project_NN.COMPLETEDT >= "2010-11-15")]

print len(drop_dup_project_NN)



#joined_file = pd.merge(drop_dup_audit, drop_dup_project, on= 'PROJECTID', how= 'outer')#the audit should be on the left of the join in real data
joined_file = pd.merge(drop_dup_project, audit, left_on = 'RESNUM', right_on = 'ResNum', how= 'outer')
joined_file = pd.DataFrame(joined_file)
drop_dup_joined = joined_file.drop_duplicates('PROJECTID')#can't join by RESNUM, duplicates occur in RESNUM
#drop_dup_joined = drop_dup_joined[drop_dup_joined.PROJECTID is None]
#print len(drop_dup_joined)

drop_dup_audit.to_csv('audit_apprended.csv', index = False)
drop_dup_project_NN.to_csv('project_NN_appended.csv', index=False)
drop_dup_project_IN.to_csv('project_IN_appended.csv', index=False)
drop_dup_joined.to_csv('joined_audit_project2.csv', index=False)

#for further research, find top 10 contractors
contractor_count = Counter(list(drop_dup_joined['Audit Contractor']))
top_ten = contractor_count.most_common(10)
print top_ten

