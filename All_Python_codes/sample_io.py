import os
import sys
import pandas as pd
import numpy as np

print "\n"
pathname = 'C:\Users\William\Documents\GitHub\urban_project_Haozhe'

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


# Read csv into pandas dataframe
df = read_data(pathname, 'Audits_0713update.csv')

# Formalize null values
df = df.replace('nan',np.nan)

# Find observations without COUNTY
# null_counties = []
# for i, COUNTY in enumerate(df['COUNTY']):
#   if str(COUNTY) == 'nan':
#     print(i, df['ResNum'][i],
#              df['City'][i],
#              df['Zip4'][i],
#              df['Zip5'][i])




# Fill in counties
df.iloc[:,8][56268] = 'JEFFERSON'
df.iloc[:,8][57001] = 'MONROE'
df.iloc[:,8][57213] = 'BROOME'
df.iloc[:,8][58476] = 'QUEENS'
df.iloc[:,8][58801] = 'TOMPKINS'
df.iloc[:,8][60860] = 'MONROE'
df.iloc[:,8][60922] = 'WARREN'
df.iloc[:,8][61085] = 'BROOME'
df.iloc[:,8][61679] = 'RICHMOND'
df.iloc[:,8][62082] = 'ERIE'
df.iloc[:,8][62145] = 'ROCKLAND'
df.iloc[:,8][62693] = 'ORANGE'
df.iloc[:,8][62958] = 'ONEIDA'
df.iloc[:,8][64102] = 'NASSAU'
df.iloc[:,8][64210] = 'ERIE'
df.iloc[:,8][66281] = 'MONROE'
df.iloc[:,8][66483] = 'CATTARAUGUS'
df.iloc[:,8][66500] = 'FRANKLIN'
df.iloc[:,8][66902] = 'ONEIDA'
df.iloc[:,8][68060] = 'ORANGE'
print "\n", "Null counties filled in."

# Remove row 63083; could not identify COUNTY
df = df.drop([63083])
print "\n", "Row 63083 removed. Couldn't find the city or the zip code anywhere in New York!"
df = df.reindex()

region_table = read_data(pathname, 'COUNTY_region.csv')
df = merge_df(df, region_table, 'COUNTY')


# Select attributes of interest
df = df[['COUNTY',
         'HOMETYPE',
         'SQFT',
         'INCOME',
         'PRIMARYFUELTYPE',
         'ANNUALELECTRICUSAGE',
         'ANNUALPRIMARYUSAGE',
         'CENTRALAIR',
         'OWNER',
         'AUDIT CONTRACTOR',
         'CLASS',
         'ELECTRICESTIMATED',
         'PRIMARYESTIMATED',
         'REGION']]
del df['COUNTY']
# Create Region COUNTY (arbitrarily matches the COUNTY column.)
#df['Region'] = df['COUNTY']
print "\n", "Attributes selected from the dataframe. Region column added."

# Assign region to each observation
#df = map_to_region(df,14)
#print "\n", "Counties successfully mapped to regions."
# Drop COUNTY column as we don't need it anymore
#df = df.drop('COUNTY',axis=1)

# Drop observations where electric, fuel is estimated
df = df[df['ELECTRICESTIMATED'] != 'Yes']
df = df[df['PRIMARYESTIMATED'] != 'Yes']
# Drop these two columns as we don't need them anymore
df = df.drop('ELECTRICESTIMATED',axis=1)
df = df.drop('PRIMARYESTIMATED',axis=1)

# Drop observations where INCOME = HEAP Eligible *
df = df[df['INCOME'] != 'HEAP Eligible *']
print "\n", "HEAP Eligible households removed from the sample."

# [ ] TO DO : drop observations with AuditContractor, PRIMARYFUELTYPE, and Region
# with <25 audits

# Drop observations with null values
df = df.dropna()
print "\n", "Null observations removed from the sample."

sample = df.to_csv("C:\Users\William\Documents\GitHub\urban_project_Haozhe\sample0723_HW.csv", index = False)
print "\n", "Sample written to csv. Process complete!"
