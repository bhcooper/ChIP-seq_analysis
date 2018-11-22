#!/usr/bin/env python

import sys
import os

forward  = {
    "A":"A",
    "C":"C",
    "G":"G",
    "T":"T",
    "R":"[AG]",
    "Y":"[CT]",
    "K":"[GT]",
    "M":"[AC]",
    "S":"[CG]",
    "W":"[AT]",
    "B":"[CGT]",
    "D":"[AGT]",
    "H":"[ACT]",
    "V":"[ACG]",
    "N":"[ACGT]"
    }

reverse =  {
    "A":"T",
    "C":"G",
    "G":"C",
    "T":"A",
    "R":"[CT]",
    "Y":"[AG]",
    "K":"[AC]",
    "M":"[GT]",
    "S":"[CG]",
    "W":"[AT]",
    "B":"[ACG]",
    "D":"[ACT]",
    "H":"[AGT]",
    "V":"[CGT]",
    "N":"[ACGT]"
    }
    
input = sys.argv[2].upper()
mismatches = "0"
if(len(sys.argv) > 3):
    mismatches = sys.argv[3]
outfile = open("alignToIUPAC.tsv", "w")

cmd = 'agrep -nis --show-position "'
for c in input:
    cmd += forward[c]
output = os.popen(cmd + '" -D ' + str(int(mismatches) + 1) + ' -I ' + str(int(mismatches) + 1) + ' -E ' + mismatches + ' ' + sys.argv[1]).read()
output = output.splitlines()
   
i = 0
if(len(output) >= i + 1):
    find, score, range, match = output[i].split(":")
    range = list(map(int,range.split("-")))
    match = match[range[0]:range[1]]
    for j, line in enumerate(open(sys.argv[1], 'r')):
        while(j == int(find)-2):
            outfile.write(line.strip() + "\t" + match.upper() + "\t" + score + "\n")
            i += 1
            if(len(output) >= i + 1):
                find, score, range, match = output[i].split(":")
                range = list(map(int,range.split("-")))
                match = match[range[0]:range[1]]
            else:
                break
            
revcmd = 'agrep -nis --show-position "'
for c in input[::-1]:
    revcmd += reverse[c]
if(revcmd != cmd):
    output = os.popen(revcmd + '" -D ' + str(int(mismatches) + 1) + ' -I ' + str(int(mismatches) + 1) + ' -E ' + mismatches + ' ' + sys.argv[1]).read()
    output = output.splitlines()
    i = 0
    if(len(output) >= i + 1):
        find, score, range, match = output[i].split(":")
        range = list(map(int,range.split("-")))
        match = match[range[0]:range[1]]
        for j, line in enumerate(open(sys.argv[1], 'r')):
            while(j == int(find)-2):
                outfile.write(line.strip() + "\t")
                for c in match.upper():
                    outfile.write(reverse[c])
                outfile.write("\t" + score + "\n")
                i += 1
                if(len(output) >= i + 1):
                    find, score, range, match = output[i].split(":")
                    range = list(map(int,range.split("-")))
                    match = match[range[0]:range[1]]
                else:
                    break
                    
outfile.close()