
# coding: utf-8

# In[1]:

cd /skydrive/dropbox/001GA files/cusp ga/haozhe/report raw


# In[2]:

import pylab
import pandas as pd
import csv
import matplotlib.pyplot as plt


# In[3]:

rawfile = pd.read_csv('raw25th.csv')
#print rawfile
AQ25thBC = rawfile[['a25thHour1','a25thHourlyBC']]
AQ25thPM = rawfile[['a25thHour1','a25thHourlyPM']]


# In[4]:

index1 = AQ25thBC.set_index('a25thHour1')
index2 = AQ25thPM.set_index('a25thHour1')
#print index2


# In[8]:

fig = plt.figure(figsize = (11,7))
ax = fig.add_subplot(111)
#fig,ax1 = plt.subplots()
plot1 = ax.plot(index1, 'co--', label = 'BC')
ax2 = ax.twinx()
plot2 = ax2.plot(index2, 'r^--', label = 'PM (right)')


plott = plot1+plot2
labs = [l.get_label() for l in plott]
ax.legend(plott,labs)#this allows two legend labels to show in the same legend box

ax.set_xlabel('Hour',fontsize = 14)
ax.set_xlim(6, 23)
ax.set_ylabel(r'BC($mg/m^{3}$)',fontsize = 14)#the dollar sign on both ends of the unit, allows square, cubic to show properly
ax2.set_ylabel(r'PM($mg/m^{3}$)',fontsize = 14)
#plt.axhline(y = 0.012, color = "k")#threshouldline for Good AQ
plt.axhline(y = 0.035, color = "k")#threshouldline for daily EPA AQ
#add annotations to the threshould lines
plt.annotate("EPA Daily PM2.5 Limit: 0.035$mg/m^{3}$",xy=(6,0.036),fontsize = 12)

ax.set_ylim(0.00,0.0050)
ax2.set_ylim(0.01,0.08)
ax.set_title('BC & PM2.5 averaged hourly 07/25/2013',fontsize = 16)
loc,labels = xticks()
xticks(arange(6,23), ('7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'
))
plt.tight_layout()
plt.savefig('BC and PM on July 25th Revised.jpg',dpi=300) 


# In[47]:




# In[44]:




# In[ ]:



