import pandas as pd
#sample = pd.read_csv('C:/Users/William/OneDrive/air_data/')
import os

name_list  = []

for file in os.listdir('C:/SkyDrive/2014 Ontodia/National/County/States/csv/'):
    if file.endswith(".csv"):
        name_list.append(file)


pieces = []
for state in name_list:
    path = 'C:/SkyDrive/2014 Ontodia/National/County/States/csv/' + state
    frame = pd.read_csv(path)
    pieces.append(frame)
all_states = pd.concat(pieces, ignore_index=True)
all_states.to_csv('states.csv', ingore_index=True)
