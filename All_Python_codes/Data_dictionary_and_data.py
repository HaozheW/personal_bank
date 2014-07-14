from __future__ import unicode_literals

import re
import os, re, string, gzip, fnmatch, io
from array import *
import pandas as pd

r = re.compile(ur'[\x0c]{0,1}(\w+)[\s\t]*(\d{1,2})[\s\t]*(.*?)[\s\t]*\(*(\d+)\s*-\s*(\d+)\)*[\s]*$')

f = open(ur'C:/Users/William/Documents/Ontidia/Ontodia/CPS/jan2013.txt')

infolder = 'C:/Users/William/Documents/Ontidia/Ontodia/CPS/CPS_raw'
outfolder = 'C:/Users/William/Documents/Ontidia/Ontodia/CPS/CPS_out'

matches = []
for line in f:
    line = line.decode('utf-8')
    line = re.sub(ur'\u2013', '-', line)
    line = re.sub(ur'\u2026', '_', line)
    #print line
    m = r.match(line)
    #m = r.search(line)
    #print m
    if m:
        matches.append(m.groups())
#print matches

with open(ur'C:/Users/William/Documents/Ontidia/Ontodia/CPS/jan13_dd_parsed.txt', 'wt') as f:
    for line in matches:
        #print line
        f.write(','.join(x for x in line) + '\n')
    print('Wrote the parsed file.')

parsed_file=open(ur'C:/Users/William/Documents/Ontidia/Ontodia/CPS/jan13_dd_parsed.txt')
col_widths=[]
col_name=[]
for row in parsed_file.readlines():
    row = re.sub(ur', ', '_', row)
    Data = string.split(row,',')
    widths=Data[1]
    name=Data[2]
    col_name.append(name)
    col_widths.append(widths)
#print col_name
#print len(col_name)


#col_widths = [15, 2, 4, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2, 2, 2, 5, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 5, 3, 1, 1, 1, 1, 3, 3, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 1, 2, 8, 1, 4, 8, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 10, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15]

for filename in os.listdir(infolder):
    #print len(col_widths)
    print filename
    if filename.split(".")[1]=="dat":
        print filename        
        infilename = os.path.join(infolder,filename)
        col_widths = map(int, col_widths)
        infile = filename.split(".")[0]

        data_file = pd.read_fwf(infilename, widths = col_widths, quoting = 1, header = None, names = col_name)
        #data_file = pd.read_fwf(infilename, widths = col_widths, quoting = 1, header = None)
        #print len(data_file[0])
        #print data_file[:2]
        outfile_name = os.path.join(outfolder,infile+".csv")
        print outfile_name
        #outfile_name = os.path.join(outfolder,filename) 
        export = data_file.to_csv(outfile_name, header = True, index = False)
