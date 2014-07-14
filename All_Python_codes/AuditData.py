###########################################################
#This code should add the matching PROJECTID to all ResNum#
###########################################################


# In[11]:

import pandas as pd
import numpy as np
import scipy as sp
pd.set_option('display.max_columns', 80)


# In[4]:

audit = pd.read_csv('Audit.csv')
project = pd.read_csv('Project.csv')
r2p = pd.read_csv('R2P.csv')
#frame = audit.set_index(['Audit Contractor','County'])
#print audit[:10]
#print r2p[:1]


# In[32]:

merge_audit = pd.merge(audit, r2p, left_on = 'ResNum', right_on = 'RESNUM', how = 'left')
merge_project = pd.merge(project, r2p, on = 'PROJECTID', how= 'left')
#print merge_audit[:10]


# In[39]:

merge_audit = pd.DataFrame(merge_audit)
merge_project = pd.DataFrame(merge_project)
drop_dup_audit = merge_audit.drop_duplicates('RESNUM')#using ResNum will result in more records, 321 to 299
drop_dup_project = merge_project.drop_duplicates('PROJECTID')

drop_dup_audit.to_csv('audit_apprended2.csv', index = False)
drop_dup_project.to_csv('project_appended.csv', index=False)


# In[ ]:



