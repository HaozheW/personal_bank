import pandas as pd
#sample = pd.read_csv('C:/Users/William/OneDrive/air_data/')
months  = [1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312]
pieces = []
for month in months:
    path = 'C:/Users/William/OneDrive/air_data/%d.csv' % month
    frame = pd.read_csv(path)
    pieces.append(frame)
all_air = pd.concat(pieces, ignore_index=True)
all_air.to_csv('Air_time_2013.csv', ingore_index=True)


