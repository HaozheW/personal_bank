#author: Haozhe Wang
#cd C:\Skydrive\2014 Ontodia\National\National\Assisted housing\AHS_2011_PUF_v1.3_CSV

import pandas as pd
import numpy as np

housing = pd.read_csv('housing_file.csv')
counter = housing['CONTROL'].groupby([housing['STATE'],housing['COUNTY']]).count()
counter.to_csv('counted_housing.csv')


#concat_state_county = pd.concat(['STATE'],['COUNTY'])
#concat_state_county.to_csv('concat_state_county.csv')
