#Data Mining for business analytics
#Author: Haozhe Wang

import csv

#with open('small.csv', 'rb') as inputfile:
#    reader = csv.reader(inputfile, delimiter=",")

inputfile = open('Air_time_1.csv', 'r')
"""
header_list = []
header = inputfile.readline()
headers = header.split(',')
header_list.append(header + '\n')
#print header_list

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()
#print input_lines[1]

AA_list = []
for i in range(0,len(input_lines)):
    if (input_lines[i].split(',')[4]) == 'AA':
    	AA_list.append(input_lines[i])
#print AA_list
"""

data_csv = csv.DictReader(inputfile)
new_header = data_csv.fieldnames
print "Loaded header:", new_header

#data_csv = list(data_csv)
aa_data = []

	

for line in data_csv:
	line['ORIGIN_CITY_NAME'] = line['ORIGIN_CITY_NAME'].replace(',','')
	line['DEST_CITY_NAME'] = line['DEST_CITY_NAME'].replace(',','')
	if line['UNIQUE_CARRIER'] == 'AA':
		aa_data.append(line)

print "Filtered by AA"

#full_list = header_list+AA_list
#print full_list
with open("AA2013_2.csv",'w+') as resultFile:
	"""
 	wr = csv.writer(resultFile, delimiter = ',', lineterminator = '\n', quotechar = '"')
 	for val in full_list:
 		wr.writerow(val.split(','))
 	"""
 	wr = csv.DictWriter(resultFile, new_header, lineterminator = '\n', quotechar = '"')
 	wr.writeheader()
 	print "Output file started"
 	wr.writerows(aa_data)