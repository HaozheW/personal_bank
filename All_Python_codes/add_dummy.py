
import pandas as pd
import numpy as np
all_air = pd.read_csv('small.csv')

all_air['Delay(0/1)']=np.nan
all_air['CARRIER_DELAY'].fillna('-1') #pandas will take NaN as 0 in calculation
print all_air['CARRIER_DELAY']


for n in all_air['CARRIER_DELAY']:
	#all_air['CARRIER_DELAY'].fillna('ND')
	#print n
	if n >=5.0:
		all_air['Delay(0/1)'] = 0
	else:
		all_air['Delay(0/1)'] = 1
all_air.to_csv('sample_small.csv')
