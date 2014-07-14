#Data Mining for business analytics
#Author: Haozhe Wang

import csv

with open('small.csv', 'rb') as inputfile:
    reader = csv.reader(inputfile, delimiter=",")

inputfile = open('small.csv', 'r')

header_list = []

header = inputfile.readline()
headers = header.split(',')
header_list.append(header)
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

full_list = header_list+AA_list
#print full_list
with open("AA2013.csv",'w+') as resultFile:
 	wr = csv.writer(resultFile, delimiter= ",", lineterminator = '\n')
 	for val in full_list:
 		wr.writerow(val.split(','))
