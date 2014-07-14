
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.max_columns', 100)#this allowed 80 columns to be shown in ipython notebook


# In[3]:

#all the file names are renamed for coding convieneince
master = pd.read_csv('master_contractor.csv')
print "total number of master:", len(master)

master = master.drop_duplicates('PROJECTID_y')
master['COMPLETEDT'] = pd.to_datetime(master['COMPLETEDT'])
master = master[(master.COMPLETEDT >= "2010-11-15")]
print "number of null value in TOTAL_HOI_AMT", len(master[pd.isnull(master['TOTAL_HOI_AMT'])])#0 null value
print "number of null value in TOTAL_CONTRACTOR_INCENT", len(master[pd.isnull(master['TOTAL_CONTRACTOR_INCENT'])])#18 null value
print "number of null value in HOI_GJGNY_AMT", len(master[pd.isnull(master['HOI_GJGNY_AMT'])])#0 null value


# In[4]:

master = master[pd.notnull(master['TOTAL_CONTRACTOR_INCENT'])]

master['total_incentives_paid'] = master['TOTAL_HOI_AMT']+master['TOTAL_CONTRACTOR_INCENT']+master['HOI_GJGNY_AMT']
master['saving_per_dollar'] = master['KWH']/master['total_incentives_paid']#the unit of this indicator is kWh per dollar
print "total number of master:", len(master)


# In[5]:

#Slice off the top and bottom 10% of the ROI
print "The new index name is", master.index.name
master = master.sort(columns = 'saving_per_dollar', ascending = True)
print "the length of the dataframe is:", len(master)
master = master[(len(master)/100):(len(master)-len(master)/100)]
print "the length of the dataframe is:", len(master)
master.reset_index()
print len(master[pd.isnull(master['total_incentives_paid'])])
master.to_csv('master_by_pro.csv', index = False)


# In[8]:

plot_col1 = master[['COMPANYNAME', 'saving_per_dollar']]
contractor_list = plot_col1.groupby('COMPANYNAME').mean()
df_list = pd.DataFrame(contractor_list)
sorted_list = df_list.sort(columns = 'saving_per_dollar', ascending = True)
print len(sorted_list)
tb_quantile1 = sorted_list.iloc[:28]#slicing the data set by top quantile
tb_quantile1.to_csv('first_quantile.csv')
tb_quantile4 = sorted_list.iloc[245:273]
tb_quantile4.to_csv('last_quantile.csv')


# In[50]:

fig, axes = plt.subplots(2,1)
plt.title('Average Energy Project Efficiency', fontsize = 30)
rcParams['figure.figsize'] = 40, 30
q4 = tb_quantile4.plot(kind= 'bar', ax = axes[0], grid = False, rot = 75);
axes[0].set_title('First Quantile Contractors Efficency', fontsize = 50);
axes[0].set_xlabel(' ', fontsize = 45);
axes[0].set_ylabel('kWh/Dollar', fontsize = 45)
q4.tick_params(axis='both', which='major', labelsize=25)


#rcParams['figure.figsize'] = 40, 24
q1 = tb_quantile1.plot(kind= 'bar', ax = axes[1], color = 'red', grid = False, rot = 75);
axes[1].set_title('Last Quantile Contractors Efficiency', fontsize = 50);
axes[1].set_xlabel('Contractors', fontsize = 45)
axes[1].set_ylabel('kWh/Dollar', fontsize = 45)
q1.tick_params(axis='both', which='major', labelsize=25)

plt.tight_layout()
savefig('quantile_contrac.png')


# In[31]:

rcParams['figure.figsize'] = 45, 18
plot_col = master[['COMPANYNAME', 'saving_per_dollar']]
fig = plot_col.groupby('COMPANYNAME').mean().plot(kind='bar', use_index ='COMPANYNAME', grid = False)
plt.title('Average Energy Project Efficiency Snapshot', fontsize = 50)
plt.ylabel('kWh/Dollar', fontsize = 40)
plt.xlabel('Contractor', fontsize = 40)
plt.tight_layout()
savefig('Efficency_ave.png')


# In[47]:

import matplotlib.cm as cm
rcParams['figure.figsize'] = 18,12
fig = plt.figure()
ax = fig.add_subplot(111)
plot_col2 = master[['COMPANYNAME', 'KWH', 'total_incentives_paid']]

scatter_list = plot_col2.groupby('COMPANYNAME').mean()
scatter_list = pd.DataFrame(scatter_list)
scatter_list.to_csv('scatter_list.csv', index = True)
"""
x = scatter_list['KWH']
ys = scatter_list['total_incentives_paid']
print len(x)
print len(ys)
colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))
for y in ys:
    plt.scatter(x, y, color=next(colors))"""
#print scatter_list.sort(columns = ('KWH','total_incentives_paid'), ascending = False)
plt.scatter(scatter_list.KWH, scatter_list.total_incentives_paid, color = 'green', s= 20)
#Annotate the bad example
#ax.annotate('Chuck Russo Heat\n & Air Conditioning LLC', xy=(-6232, 49700), xytext=(-5400, 55000), arrowprops=dict(facecolor='red', shrink=0.05),fontsize = 19)
ax.annotate('Van Hee Mechanical', xy=(-2122.5, 49033), xytext=(-1022, 53000),
            arrowprops=dict(facecolor='red', shrink=0.05),fontsize = 19
            )
ax.annotate('Gleason Geothermal', xy=(-1920.793103, 30861.151724), xytext=(-400, 37000),
            arrowprops=dict(facecolor='red', shrink=0.05),horizontalalignment='left', verticalalignment='top',fontsize = 19
            )
ax.annotate('Integrated Geothermal LLC', xy=(-1569.285714, 40100.485714), xytext=(-0, 45000),
            arrowprops=dict(facecolor='red', shrink=0.05),horizontalalignment='left', verticalalignment='top',fontsize = 19
            )
#Annotate the good examples
#ax.annotate('Chuck Russo Heating\n & Air Conditioning LLC', xy=(9870, 15790), xytext=(8100, 9600), arrowprops=dict(facecolor='blue', shrink=0.05),horizontalalignment='left', verticalalignment='top',fontsize = 18)
ax.annotate('Home Energy Saving\n Solutions Corporation', xy=(10560, 19725), xytext=(12000, 10000),
            arrowprops=dict(facecolor='blue', shrink=0.05),horizontalalignment='right', verticalalignment='top',fontsize = 18
            )
ax.annotate('Woltner-Summit\n Contracting LLC', xy=(6117, 13896), xytext=(5000, 7000),
            arrowprops=dict(facecolor='blue', shrink=0.05),horizontalalignment='left', verticalalignment='top',fontsize = 18
            )





plt.title('Averaged Contractor Performance:\n kWh Saving vs. Total Incentive Paid', fontsize= 30)
plt.xlabel('kWh Saving', fontsize = 25)
plt.ylabel('Total Incentive Paid', fontsize = 25)
ax.tick_params(axis='both', which='major', labelsize=18)
plt.tight_layout()
savefig('Average_scatter.png')
plt.show()


# In[ ]:



