#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:53:15 2015

@author: dmamartin
"""
import sys #import module sys

if len(sys.argv)!=3: #if the length of the command line arguments passed to python is not 3, print the following statement, then exit the script
    print """Run this parser with the following arguments:
    parsemultalign.py multalign_file output_file
    """
    exit(0)

infile=sys.argv[1] #assign to variable 'infile' the command line argument at position 1 (second position) not sure, one scriptname is passed to the python interpreter
outfile=sys.argv[2] #assign to variable 'outfile' the command line argument at position 2 (third position) not sure, one scriptname is passed to the python interpreter

#print Parsing input file + name of file specified as input file, + writing results to name of specified output file.
print("Parsing input file %s, writing results to %s"%(infile, outfile))

ifh=open(infile) #open the file with the name 'infile' and store the file object in the variable called 'ifh'. Not specifying a second argument the file is opened in mode 'read'.
ofh=open(outfile, "w") #open the file with the name 'outfile' and store the file object in the variable called 'ofh'. Specifying second argument as 'w' opens the file in mode 'write'

line=ifh.readline() #read line from 'ifh' and store it in the variable named 'line'

identifiers=[] #define the empty list called 'identifiers'

while line[1:6] != 'Index': #initiate a while-loop: While characters 1-6 (starting from second character, counting up to but not including the sixth character) do not match the string 'Index'
    line=ifh.readline() #read line from 'ifh' and store it in the variable named 'line'
    
for line in ifh.readlines(): #initiate for-loop
    if line[9]=='>': #initiate if-statement: If then 10th character of a line (from infile) is the 'greater than' character...
        identifiers.append(line[13:32].strip()) #...append (add to) the list 'identifiers' the characters 14 up to but not including the thirty-second characters of this line, while removing the terminal whitespace character.
    else: #If then 10th character of a line (from infile) is not the 'greater than' character...
        if line[5]== 'I': #...and the sixth character of a line is the character 'I'...
            headers=line.strip().split() #...remove terminal whitespaces in the line, split line at all remaining whitespaces. Then store the result in the variable 'headers'.
            headers.append('PWMATCH') #Add to the variable 'headers' PWMATCH
            ofh.write("\t".join(headers)+"\n") #write into variable 'ofh' (which specifies the file 'outfile') the headers separated by a tab, and end with a newline.
            continue #go back to the beginning of the for-loop
        if line[1:6]=='Times': #initiate if-statement: While characters 1-6 (starting from second character, counting up to but not including the sixth character) do not match the string 'Times'
            break #Exit the loop
        fields=[x.strip() for x in (line[0:6], line[6:11],line[11:16],line[16:21], #populate fields under headers with content of lines first to up to but not including the sixth character, and all other specified character-sets while stripping terminal whitespaces from all of them.
                line[21:31],line[31:38], line[38:45],line[45:52], line[52:62],
                line[62:72], line[72:82],line[82:89], line[89:99], line[99:109],
                line[109:119], line[119:126])]
        fields[0]=identifiers[int(fields[0])-1]
        fields[1]=identifiers[int(fields[1])-1]
        ofh.write("\t".join(fields)+"\n") #write into variable 'ofh' (which specifies the file 'outfile') the headers separated by a tab, and end with a newline.

ofh.close()
ifh.close()
