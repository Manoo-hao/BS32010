#Assignment 2

###PFAM dataset files

Contains the dataset downloaded from PFAM (PF01924), processed according 
to the instructions on the assignment 2 handout.

###parsemultialign.py

Parser that takes a pairwise sequence alignment file from amps and 
returns a tab delimited table of various alignment characteristics and 
parameters. The parser was annotated.

###parser_output_file

The tab delimted table that was created by running the parser over the 
serprot_pairs.out file.

###replace_id

A small annotated python script that removes the identifier >P1; from 
the output files of multiple alignments, and replaces it with the 
identifier >. This is required to load the alignment into jalview 
successfully. A suggestion for improvement is included in the 
annotations.

###time

a text file that contains a list of times required to run a different 
amount of randomisations on an alignment. This was achieved by prefixing 
the command 'time' to the command that executed amps.
